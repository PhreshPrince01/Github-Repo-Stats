from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
import requests,os, click

console = Console()
TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {"Authorization":f"token {TOKEN}"}

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


def prompt_confirmation(command, repo):
    """Prompt for confirmation before proceeding."""
    return click.confirm(f"Are you sure you want to fetch {command} for {repo}?", default=True)


def print_error_msg():
    console.print("[bold red]Failed to fetch repository data. Please check the repository name and try again.[/bold red]")


def make_request(url):
    """
    Make a GET request to the GitHub API and handle errors gracefully.
    """
    headers = {"Authorization": f"token {TOKEN}"}
    try:
        response = requests.get(url, headers=headers)
        
        
        # Handle common HTTP error status codes
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            console.print("[bold red]Unauthorized. Please check your GitHub token.[/bold red]")
        elif response.status_code == 403:
            console.print("[bold red]Forbidden request. You might not have access to this resource.[/bold red]")
        elif response.status_code == 404:
            console.print(f"[bold red]Repository: {url} not found. Please check the repository name.[/bold red]")
        else:
            console.print(f"[bold red]An error occurred: {response.status_code} - {response.reason}[/bold red]")
        
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]An error occurred while making the request: {str(e)}[/bold red]")
    return None


def display_table(title, columns, rows):
    """
    Display a table with given title, columns, and rows.
    """
    table = Table(title=title)
    for col in columns:
        table.add_column(col['name'], justify=col.get('jusitify','left'), style=col.get('style','white'), no_wrap=col.get('no_wrap', False))
    
    for row in rows:
        table.add_row(*row)
    
    console.print(table)