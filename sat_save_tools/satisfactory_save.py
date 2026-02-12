import json
import logging
import pathlib
import typing
import zlib

import pydantic

from sat_save_tools.exceptions import SatisfactorySaveParserError
from sat_save_tools.logger import set_struct_name
from sat_save_tools.models import LevelObjectType, SaveFileBody, SaveFileHeader
from sat_save_tools.progress import LogProgress
from sat_save_tools.serde import (
    U8,
    U32,
    U64,
    Deserializer,
    Function,
    Object,
    Raw,
    Serializer,
)
from sat_save_tools.utils import make_chunks, pydantic_eq

__all__ = ("SatisfactorySaveFile",)

logger = logging.getLogger()


@pydantic_eq
class SatisfactorySaveFile(pydantic.BaseModel):
    header: SaveFileHeader
    body: SaveFileBody
    file_tag: int
    magic: int
    maximum_chunk_size: int
    unknown: int



    def __serialize__(self, ser: "Serializer") -> None:
        ser.add(self.header)

        ns = ser.new().ctx_update(header=self.header)
        ns.add(self.body)

        for chunk in LogProgress.iter(
            make_chunks(memoryview(bytes(ns.content)), self.maximum_chunk_size),
            desc="serialize chunks",
        ):
            uncompressed_size = len(chunk)
            compressed_chunk = zlib.compress(chunk)
            compressed_size = len(compressed_chunk)

            ser.add_struct(
                U32(self.file_tag)
                | U32(self.magic)
                | U32(self.maximum_chunk_size)
                | U8(0)
                | U32(self.unknown)
                | U64(compressed_size)
                | U64(uncompressed_size)
                | U64(compressed_size)
                | U64(uncompressed_size)
                | Raw(len(compressed_chunk))(compressed_chunk),
            )

    @classmethod
    def __deserialize__(cls, des: "Deserializer") -> typing.Self:
        content = des.get_dict(
            Object(SaveFileHeader)("header")
            | U32("file_tag")
            | U32("magic")
            | U32("maximum_chunk_size")
            | U8("padding")
            | U32("unknown"),
        )
        des.offset -= 17
        des.ctx_update(header=content["header"])
        content |= des.get_dict(Function(cls.get_body)("body"))
        return cls.model_validate(content)

    @classmethod
    def _get_compressed_file_body(cls, des: "Deserializer") -> bytes:
        return des.get_raw(len(des.content) - des.offset)

    @classmethod
    def _get_compressed_file_body_deserializer(cls, des: "Deserializer") -> "Deserializer":
        return des.new(cls._get_compressed_file_body(des))

    @classmethod
    @set_struct_name("UncompressedBody")
    def get_body(cls, des: "Deserializer") -> "SaveFileBody":
        des = cls._get_compressed_file_body_deserializer(des)
        chunks: list[bytes] = []
        logger.info("Uncompressing save body")
        while des.offset < des.total:
            content = des.get_dict(
                U32("ue_package_signature")
                | U32("magic")
                | U32("maximum_chunk_size")
                | U8("padding")
                | U32("unknown")
                | U64("compressed_size")
                | U64("uncompressed_size")
                | U64("compressed_size_2")
                | U64("uncompressed_size_2"),
            )

            if content["compressed_size"] != content["compressed_size_2"]:
                raise SatisfactorySaveParserError(
                    "corrupt_data",
                    "Compressed size mismatch {} {}",
                    content["compressed_size"],
                    content["compressed_size_2"],
                )
            if content["uncompressed_size"] != content["uncompressed_size_2"]:
                raise SatisfactorySaveParserError(
                    "corrupt_data",
                    "Uncompressed size mismatch {} {}",
                    content["uncompressed_size"],
                    content["uncompressed_size_2"],
                )

            result = zlib.decompress(des.get_raw(content["compressed_size"]))

            if len(result) != content["uncompressed_size"]:
                raise SatisfactorySaveParserError("corrupt_data", "Uncompressed size mismatch")

            chunks.append(result)
        logger.info(
            "Uncompressing complete (%d chunks, %d bytes)",
            len(chunks),
            sum(len(c) for c in chunks),
        )
        result = des.new(b"".join(chunks)).get_struct(Object(SaveFileBody))
        return result[0]

    @classmethod
    def load_from_json(cls, filename: pathlib.Path) -> typing.Self:
        text = filename.read_text(encoding="utf-8")
        content = json.loads(text)
        return cls.model_validate(content)

    def save_to_json(self, filename: pathlib.Path) -> None:
        json_content = self.model_dump(mode="json")
        filename.write_text(json.dumps(json_content, ensure_ascii=False, indent=2), encoding="utf-8")

    @classmethod
    def load_from_sav(cls, filename: pathlib.Path) -> typing.Self:
        with filename.open("rb") as f:
            des = Deserializer(f.read())
        return des.get(cls)

    def save_to_sav(self, filename: pathlib.Path) -> None:
        ser = Serializer()
        ser.add(self)
        with filename.open("wb") as f:
            f.write(ser.content)

    def save_to_file(self, filename: pathlib.Path) -> None:
        if str(filename).endswith(".sav"):
            return self.save_to_sav(filename)
        if str(filename).endswith(".json"):
            return self.save_to_json(filename)
        raise SatisfactorySaveParserError("unknown_file_type", "File must ends with .sav or .json")

    @classmethod
    def load_from_file(cls, filename: pathlib.Path) -> typing.Self:
        if filename.suffix == ".sav":
            return cls.load_from_sav(filename)
        if filename.suffix == ".json":
            return cls.load_from_json(filename)
        raise SatisfactorySaveParserError("unknown_file_type", "Unknown file type: {}", filename.suffix)

    def get_objects_by_instance_name(self, instance_name: str) -> list["LevelObjectType"]:
        found = []
        for level in [self.body.persistent_level, *self.body.levels]:
            obj = level.objects.get(instance_name)
            if obj is not None:
                found.append(obj)
        return found
