from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
import requests,os

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



def make_request(url):
    """"
    Make a GET request to the specified URL and return the JSON response
    """
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        console.print(f"[bold red] Failed to fetch data: {response.status_code} - {response.get('message', 'unknown error')}[/bold red]")
    

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