from utils import *

GITHUB_API_URL = "https://api.github.com"

def get_repo_data(repo_name):
    """
    Fetch data from a GitHub repository.
    """
    url = f"{GITHUB_API_URL}/repos/{repo_name}"
    return make_request(url)
    

def display_stats(data):
    """
    Display repository stats in a tabele.
    """
    columns = [
        {"name": "Stat", "justify": "right", "style": "cyan"},
        {"name": "Value", "justify": "right", "style": "magenta"}
    ]

    rows = [
        ["Stars", str(data["stargazers_count"])],
        ["Forks", str(data["forks_count"])],
        ["Open issues", str(data["open_issues_count"])],
        ["Watchers", str(data["watchers_count"])]
    ]
    display_table("GitHub Repository Stats", columns, rows)


def get_commits_data(repo_name):
    """
    Fetch commit data for a Github Repo
    """
    url = f"{GITHUB_API_URL}/repos/{repo_name}/commits"
    return make_request(url)


def display_commits_stats(data, repo_name):
    columns = [
        {"name":"Commit Message", "justify": "left", "style":"cyan"},
        {"name": "Author", "justify":"left", "style":"magenta"},
        {"name": "Email", "justify":"left", "style":"yellow"},
        {"name": "Commit URL", "justify":"left", "style":"purple"}
    ]

    rows = [
        [commit['commit']['message'], commit['commit']['author']['name'],
         commit['commit']['author']['email'],f"https://github.com/{repo_name}/commit/{commit['sha']}"]
         for commit in data
    ]
    display_table("GitHub Commit Stats", columns, rows)


def get_contributors_stats(repo_name):
    """
    Fetch contributors data for a GitHub repository.
    """
    url = f"https://api.github.com/repos/{repo_name}/contributors"
    return make_request(url)
    

def display_contributors_stats(contributors):
    """
    Display contributor stats in a table
    """
    columns = [
        {"name": "Contributor", "justify":"left", "style":"cyan"},
        {"name": "Contributions", "justify":"right", "style":"magenta"}
    ]

    rows = [
        [contributor['login'],str(contributor['contributions'])]
        for contributor in contributors
    ]
    display_table("GitHib Contributor Stats", columns, rows)


def get_issues_stats(repo_name):
    """
    Fetch issues data
    """
    url = f"{GITHUB_API_URL}/repos/{repo_name}/issues?state=all"
    return make_request(url)


def display_issues(issues):
    """
    Display issues stats in a table
    """
    columns = [
        {"name": "Tittle", "justify" : "left", "style" : "cyan"},
        {"name": "Author", "justify" : "left", "style" : "magenta"},
        {"name": "State", "justify": "center", "style": "green"},
        {"name": "Created At", "justify": "left", "style": "yellow"}
    ]

    rows = [
        [issue['title'], issue['user']['login'], issue['state'], issue['created_at']]
        for issue in issues
    ]
    display_table("GitHub Issues Stats", columns, rows)


def get_pull_requests_stats(repo_name):
    """
    Fetch issues data
    """
    url = f"{GITHUB_API_URL}/repos/{repo_name}/pulls?state=all"
    return make_request(url)


def display_pull_requests(prs):
    """
    Display pull requests stats in a table
    """
    columns = [
        {"name": "Tittle", "justify" : "left", "style" : "cyan", "no_wrap":True},
        {"name": "Author", "justify" : "left", "style" : "magenta"},
        {"name": "State", "justify" : "center", "style" : "green"},
        {"name": "Created At", "justify" : "left", "style" : "yellow"}
    ]

    rows = [
        [pr['title'],pr['user']['login'],pr['state'],pr['created_at']]
        for pr in prs
    ]
    display_table("GitHib Pull Requests Stats", columns, rows)


def get_branches_stats(repo_name):
    """
    Fetch branches data and the default branch for a GitHub repository.
    """
    branches_url = f"{GITHUB_API_URL}/repos/{repo_name}/branches"
    repo_url = f"{GITHUB_API_URL}/repos/{repo_name}"

    # Fetch branches and repository data
    branches = make_request(branches_url)
    repo_data = make_request(repo_url)

    if branches and repo_data:
        default_branch = repo_data['default_branch']
        return branches, default_branch
    

def display_branches(branches, default_branch):
    """
    Display branches data in a table.
    """
    columns = [
        {"name": "Branch Name", "justify": "left", "style": "cyan", "no_wrap": True},
        {"name": "Protected", "justify": "center", "style": "green"}
    ]
    
    rows = [
        [f"[bold yellow]{branch['name']} (default)[/bold yellow]" 
        if branch['name'] == default_branch else branch['name'], 
        "Yes" if branch['protected'] else "No"]
        for branch in branches
    ]
    display_table("GitHub Branches Stats", columns, rows)


def get_release_stats(repo_name):
    """
    Fetch release data
    """
    url = f"{GITHUB_API_URL}/repos/{repo_name}/releases"
    return make_request(url)
    


def display_releases(releases):
    """
    Display pull releases stats in a table
    """
    columns = [
        {"name": "Release Tag", "justify":"left", "style":"cyan", "no_wrap":True},
        {"name": "Release Name", "justify":"left", "style":"magenta"},
        {"name": "Published Date", "justify":"center", "style":"green"}
    ]

    rows = [
        [release['tag_name'],release.get('name'),release['published_at'][:10]]
        for release in releases
    ]
    display_table("GitHib Releses Stats", columns, rows)


def get_tags_stats(repo_name):
    """
    Fetch tags data
    """
    url = f"{GITHUB_API_URL}/repos/{repo_name}/tags"
    return make_request(url)


def display_tags(tags):
    """
    Display tags in a table.
    """
    columns = [
        {"name": "Tag Name", "justify":"left", "style":"cyan"},
        {"name": "Commit SHA", "justify":"left", "style":"green"}
    ]

    rows = [
        [tag['name'], tag['commit']['sha']]
        for tag in tags
    ]
    display_table("GitHub Tags", columns, rows)


def get_languages_stats(repo_name):
    """
    Fetch programming languages used in a GitHub repository.
    """
    url = f"{GITHUB_API_URL}/repos/{repo_name}/languages"
    return make_request(url)


def display_languages(languages):
    """Display programming languages and their byte count in a table."""
    
    
    columns = [
        {"name": "Language", "justify":"left", "style":"cyan"},
        {"name": "Percentage", "justify":"right", "style":"green"}
    ]

    total_bytes = sum(languages.values())
    rows = [
        [language, f"{(bytes_of_code / total_bytes * 100):.2f}%"]
        for language, bytes_of_code in languages.items()
    ]
    display_table("GitHub Repository Languages", columns, rows)


def get_forks_stats(repo_name):
    """Fetch forks for a GitHub repository."""
    url = f"{GITHUB_API_URL}/repos/{repo_name}/forks"
    return make_request(url)


def display_forks(forks):
    """Display forks in a table."""
    columns = [
        {"name": "Fork Name", "justify":"left", "style":"cyan"},
        {"name": "Owner", "justify":"left", "style":"green"},
        {"name":"Stars", "justify":"right", "style":"magenta"}
    ]

    rows = [
        [fork['full_name'],fork['owner']['login'], str(fork['stargazers_count'])]
        for fork in forks
    ]

    display_table("GitHub Repository Forks",columns, rows)
import requests
from rich.console import Console

console = Console()

def get_traffic_stats(repo_name):
    """Fetch traffic data for a GitHub repository (views and clones)."""
    views_url = f"https://api.github.com/repos/{repo_name}/traffic/views"
    clones_url = f"https://api.github.com/repos/{repo_name}/traffic/clones"
    
    views_data = make_request(views_url)
    clones_data = make_request(clones_url)
    
    if views_data is not None and clones_data is not None:
        return {
            "views": views_data,
            "clones": clones_data
        }
    else:
        return None


def display_traffic(traffic_data):
    """Display traffic data (views and clones) in tables."""
    views = traffic_data['views']
    clones = traffic_data['clones']
    
    # Prepare data for Views Table
    view_columns = [
        {'name': "Date", 'justify': 'left', 'style': 'cyan'},
        {'name': "Unique Views", 'justify': 'right', 'style': 'green'},
        {'name': "Total Views", 'justify': 'right', 'style': 'magenta'}
    ]
    views_rows = [
        (view['timestamp'][:10], str(view['uniques']), str(view['count'])) 
        for view in views['views']]
    
    # Display Views Table
    display_table("GitHub Repository Traffic - Views", view_columns, views_rows)
    
    # Prepare data for Clones Table
    clones_columns = [
        {'name': "Date", 'justify': 'left', 'style': 'cyan'},
        {'name': "Unique Clones", 'justify': 'right', 'style': 'green'},
        {'name': "Total Clones", 'justify': 'right', 'style': 'magenta'}
    ]
    clones_rows = [
        (clone['timestamp'][:10], str(clone['uniques']), str(clone['count'])) 
        for clone in clones['clones']]
    
    # Display Clones Table
    display_table("GitHub Repository Traffic - Clones", clones_columns, clones_rows)

