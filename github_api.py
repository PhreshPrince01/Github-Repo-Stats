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
    

def display_commits_stats(data, repo_name):
    table = Table(title="GitHub Commit Stats")
    table.add_column("Commit Message", justify="left", style="cyan")
    table.add_column("Author", justify="left", style="magenta")
    table.add_column("Email", justify="left", style="yellow")
    table.add_column("Commit URL", justify="left", style="purple")

    base_url = f"https://github.com/{repo_name}/commit/"

    for commit in data:
        commit_msg = commit['commit']['message']
        author_name = commit['commit']['author']['name']
        author_email = commit['commit']['author']['email']
        commit_sha = commit['sha']
        commit_url = f"{base_url}{commit_sha}"

        table.add_row(commit_msg, author_name, author_email,commit_url)
        
    console.print(table)



def get_contributors_stats(repo_name):
    """
    Fetch contributors data for a GitHub repository.
    """
    url = f"https://api.github.com/repos/{repo_name}/contributors"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.json()
    else:
        console.print(f"[bold red]Failed to fetch contributors data: {response.status_code} - {response.json().get('message'),'unkown error'}[/bold red]")
        return None
    


def display_contributors_stats(contributors):
    """
    Display contributor stats in a table
    """

    table = Table(title="GitHib Contributor Stats")
    table.add_column("Contributor", justify="left", style="cyan")
    table.add_column("Contributions", justify="right", style="magenta")

    for contributor in contributors:
        table.add_row(contributor['login'], str(contributor['contributions']))

    console.print(table)



def get_issues_stats(repo_name):
    """
    Fetch issues data
    """
    url = f"{GITHUB_API_URL}/repos/{repo_name}/issues?state=all"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        console.print(f"[bold red]Failed to fetch issues data: {response.status_code} - {response.json().get('message'),'unkown error'}[/bold red]")
        return None



def display_issues(issues):
    """
    Display issues stats in a table
    """

    table = Table(title="GitHib Issues Stats")
    table.add_column("Tittle", justify="left", style="cyan")
    table.add_column("Author", justify="left", style="magenta")
    table.add_column("Date", justify="center", style="green")
    table.add_column("Created At", justify="left", style="yellow")


    
    for issue in issues:
        table.add_row(
            issue['title'],
            issue['user']['login'],
            issue['state'],
            issue['created_at']
        )
    console.print(table)


def get_pull_requests_stats(repo_name):
    """
    Fetch issues data
    """
    url = f"{GITHUB_API_URL}/repos/{repo_name}/pulls?state=all"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        console.print(f"[bold red]Failed to fetch pull requests data: {response.status_code} - {response.json().get('message'),'unkown error'}[/bold red]")
        return None
    

