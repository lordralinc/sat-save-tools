import collections
import collections.abc
import logging
import time

from sat_save_tools.env import SF_PROGRESS_LOG_EVERY, SF_PROGRESS_USE_RICH

__all__ = ("LogProgress",)

logger = logging.getLogger(__name__)


class LogProgress:
    if SF_PROGRESS_USE_RICH:
        from rich.progress import (  # noqa: PLC0415
            BarColumn,
            MofNCompleteColumn,
            Progress,
            SpinnerColumn,
            TaskProgressColumn,
            TextColumn,
            TimeElapsedColumn,
            TimeRemainingColumn,
        )

        progress = Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            MofNCompleteColumn(),
            TaskProgressColumn(),
            TimeElapsedColumn(),
            TimeRemainingColumn(),
            refresh_per_second=5,
        )

        @classmethod
        def iter[T](  # type: ignore
            cls,
            iterable: collections.abc.Iterable[T],
            total: int | None = None,
            desc: str = "",
        ) -> collections.abc.Iterable[T]:
            if total is not None and total < SF_PROGRESS_LOG_EVERY * 3:
                yield from iterable
            else:
                with cls.progress:
                    task = cls.progress.add_task(desc, total=total)
                    for item in iterable:
                        yield item
                        cls.progress.advance(task)
                    cls.progress.remove_task(task)

    else:

        @classmethod
        def iter[T](
            cls,
            iterable: collections.abc.Iterable[T],
            total: int | None = None,
            desc: str = "",
        ) -> collections.abc.Iterable[T]:
            if total is not None and total < SF_PROGRESS_LOG_EVERY * 3:
                yield from iterable
            else:
                start = time.monotonic()
                last_log = 0

                for i, item in enumerate(iterable, 1):
                    yield item

                    if i - last_log >= SF_PROGRESS_LOG_EVERY or i == total:
                        last_log = i
                        elapsed = time.monotonic() - start
                        rate = i / elapsed if elapsed > 0 else 0.0
                        if total is not None:
                            logger.info(
                                f"{desc}: {i}/{total} ({i / total:.1%}) {rate:.1f} it/s",
                            )
                        else:
                            logger.info(f"{desc}: {i} it/s {rate:.1f} it/s")
                if total is not None:
                    logger.info(f"{desc}: {total}/{total} (100.0%) Completed")
                else:
                    logger.info(f"{desc}: Completed")

    @classmethod
    def iter_list[T](
        cls,
        iterable: collections.abc.Iterable[T],
        *,
        total: int | None = None,
        desc: str = "",
    ) -> list[T]:
        return list(cls.iter(iterable, total=total, desc=desc))
