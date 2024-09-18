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
    


def display_pull_requests(prs):
    """
    Display pull requests stats in a table
    """

    table = Table(title="GitHib Pull Requests Stats")
    table.add_column("Tittle", justify="left", style="cyan", no_wrap=True)
    table.add_column("Author", justify="left", style="magenta")
    table.add_column("State", justify="center", style="green")
    table.add_column("Created At", justify="left", style="yellow")


    
    for pr in prs:
        table.add_row(
            pr['title'],
            pr['user']['login'],
            pr['state'],
            pr['created_at']
        )
    console.print(table)



def get_branches_stats(repo_name):
    """
    Fetch branches data
    """
    branch_url = f"{GITHUB_API_URL}/repos/{repo_name}/branches"
    repo_url =  f"{GITHUB_API_URL}/repos/{repo_name}"

    branches_response = requests.get(branch_url, headers=HEADERS)
    repo_response = requests.get(repo_url,headers=HEADERS)


    if branches_response.status_code == 200 and repo_response.status_code == 200:
            branches = branches_response.json()
            default_branch = repo_response.json()['default_branch']
            return branches, default_branch
    else:
        console.print(f"[bold red]Failed to fetch branches data: {branches_response.status_code} - {branches_response.json().get('message'),'unkown error'}[/bold red]")
        return None, None
    

def display_branches(branches, defalut_branch):
    """
    display branches data
    """
    table = Table(title="GitHib Pull Requests Stats")
    table.add_column("Branch Name", justify="left", style="cyan", no_wrap=True)
    table.add_column("Protected", justify="center", style="green")

    for branch in branches:
        protected_status = "yes" if branch['protected'] else "No"
        branch_name = branch['name']

        if branch_name == defalut_branch:
            table.add_row(f"[bold yellow]{branch_name} (default)[/bold yellow]", protected_status)
        else:
            table.add_row(branch['name'],protected_status)
    
    console.print(table)


def get_release_stats(repo_name):
    """
    Fetch release data
    """
    url = f"{GITHUB_API_URL}/repos/{repo_name}/releases"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        console.print(f"[bold red]Failed to fetch release data: {response.status_code} - {response.json().get('message'),'unkown error'}[/bold red]")
        return None
    


def display_releases(releases):
    """
    Display pull releases stats in a table
    """

    table = Table(title="GitHib Releses Stats")
    table.add_column("Release Tag", justify="left", style="cyan", no_wrap=True)
    table.add_column("Release Name", justify="left", style="magenta")
    table.add_column("Published Date", justify="center", style="green")
    table.add_column("Notes", justify="left", style="yellow")

    for release in releases:
        tag_name = releases['tag_name']
        release_name = release.get('name')
        published_at = release['published_at']
        notes = release.get('body', 'No release notes')[:200]
        table.add_row(tag_name,release_name,published_at,notes)

        console.print(table)


    