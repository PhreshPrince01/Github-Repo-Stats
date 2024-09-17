from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def print_welcome_message():
    """
    Print a welcome message to the user.
    """
    text = Text("Welcome to the GitHub Repo Stats CLI Tool!", justify="center", style="bold yellow")
    description_text = Text("Fetch and display various statistics for GitHub repository with ease.",
                            justify="center", style="green")
    panel = Panel.fit(text + "\n\n" + description_text,
                      title="GitHub Stats CLI",
                      border_style="bright_blue",
                      padding=(0,1),)
    console.print(panel)