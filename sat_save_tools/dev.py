from sat_save_tools.env import SF_DUMP_UNPARSED_SAVE, SF_DUMP_UNPARSED_SAVE_FOLDER

__all__ = ("dev_dump_unparsed_chunk",)


def dev_dump_unparsed_chunk(*paths: str, content: bytes | memoryview[bytes]):
    if not SF_DUMP_UNPARSED_SAVE:
        return

    target_file = SF_DUMP_UNPARSED_SAVE_FOLDER

    for path in paths:
        target_file /= path.replace("/", "_").replace(":", "_")

    target_file = target_file.with_suffix(".bin")
    target_file.parent.mkdir(exist_ok=True, parents=True)
    target_file.write_bytes(bytes(content))
