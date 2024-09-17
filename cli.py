from rich.text import Text
import click
from github_api import get_repo_data, display_stats
from rich.console import Console
from rich.panel import Panel

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
                      padding=(1,2),)
    console.print(panel)
    # console.print("[bold cyan] Welcome to the GitHub Repo Stats CLI Tool![/bold cyan]")
    # console.print("Fetch and display various statistics for GitHub repository with ease.")


@click.group()
def cli():
    print_welcome_message()


@cli.command()
@click.option('--repo', prompt='GitHub Repository', help= 'The full name of the GitHub repository (e.g., owener/repo)')
def get_stats(repo):
    """
    CLI to get  stats for a GitHub Repository
    """
    data = get_repo_data(repo)
    if data:
        display_stats(data)


if __name__ == "__main__":
    cli()