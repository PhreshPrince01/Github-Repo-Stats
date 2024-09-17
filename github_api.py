import os, requests
from rich.console import Console
from rich.table import Table

GITHUB_API_URL = "https://api.github.com"
TOKEN = os.getenv("GITHUB_TOKEN")
console = Console()

HEADERS = {"Authorization":f"token {TOKEN}"}

def get_repo_data(repo_name):
    """
    Fetch data from a GitHub repository.
    """
    url = f"{GITHUB_API_URL}/repos/{repo_name}"
    
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        console.print(f"[bold red]Failed to fetch data: {response.status_code}[/bold red]")
        return None
    

def display_stats(data):
    """
    Display repository stats in a tabele.
    """

    table = Table(title="GitHub Repository Stats")
    table.add_column("Stat", justify="right", style="cyan")
    table.add_column("Value", justify="right", style="magenta")

    table.add_row("Stars", str(data["stargazers_count"]))
    table.add_row("Forks", str(data["forks_count"]))
    table.add_row("Open issues", str(data["open_issues_count"]))
    table.add_row("Watchers", str(data["watchers_count"]))

    console.print(table)



def get_commits_data(repo_name):
    """
    Fetch commit data for a Github Repo
    """

    url = f"{GITHUB_API_URL}/repos/{repo_name}/commits"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        console.print(f"[bold red]Failed to fetch commit data: {response.status_code} - {response.json().get('message'),'unkown error'}[/bold red]")
        return None
    

def display_commits_stats(data):
    table = Table(title="GitHub Commit Stats")
    table.add_column("Commit Message", justify="left", style="cyan")
    table.add_column("Author", justify="right", style="magenta")

    for commit in data:
        table.add_row(commit['commit']['message'], commit['commit']['author']['name'])

    console.print(table)