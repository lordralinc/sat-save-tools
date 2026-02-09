import rich.console
import rich.panel

__all__ = ("AnswerManager",)

console = rich.console.Console()


class AnswerManager:
    @classmethod
    def success(cls, title: str, message: rich.console.RenderableType) -> None:
        console.print(
            rich.panel.Panel(
                message,
                title=f"[bold white]{title}[/]",
                border_style="green",
                expand=False,
            ),
        )

    @classmethod
    def error(cls, title: str, message: rich.console.RenderableType) -> None:
        console.print(
            rich.panel.Panel(
                message,
                title=f"[bold white]{title}[/]",
                border_style="red",
                expand=False,
            ),
        )
