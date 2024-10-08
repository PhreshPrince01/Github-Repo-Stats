from src.utils import *

GITHUB_API_URL = "https://api.github.com"

def get_repo_data(repo_name):
    """
    Fetch data from a GitHub repository, including pull requests, contributors, and other details.
    """
    repo_url = f"{GITHUB_API_URL}/repos/{repo_name}"
    pulls_url = f"{GITHUB_API_URL}/repos/{repo_name}/pulls?state=all"
    contributors_url = f"{GITHUB_API_URL}/repos/{repo_name}/contributors"
    license_url = f"{GITHUB_API_URL}/repos/{repo_name}/license"
    releases_url = f"{GITHUB_API_URL}/repos/{repo_name}/releases/latest"
    
    repo_data = make_request(repo_url)
    pulls_data = make_request(pulls_url)
    contributors_data = make_request(contributors_url)
    license_data = make_request(license_url)
    latest_release = make_request(releases_url)
   
    if repo_data == None and pulls_data == None and contributors_data == None and license_data == None and latest_release == None:
        return None
    
    # Return combined data
    return {
        "repo": repo_data,
        "pulls": pulls_data,
        "contributors": contributors_data,
        "license": license_data,
        "latest_release": latest_release
    }

    

def display_stats(data):
    """
    Display repository stats in a table with formatted numbers and repository size in MB.
    """
    if data is None:
        console.print("[bold red]No data available to display. Please check the repository name and try again.[/bold red]")
        return

    repo = data["repo"]
    pulls = data["pulls"]
    contributors = data["contributors"]
    license_info = data["license"]
    latest_release = data["latest_release"]
  

    open_pulls = len([pr for pr in pulls if pr["state"] == "open"])
    closed_pulls = len([pr for pr in pulls if pr["state"] == "closed"])

    # Convert repository size from KB to MB and format to 2 decimal places
    repo_size_mb = f"{repo['size'] / 1024:.2f} MB"


     # Check if latest_release is not None before accessing its attributes
    latest_release_name = latest_release.get("name") if latest_release else "No releases"


    columns = [
        {"name": "Stat", "justify": "right", "style": "cyan"},
        {"name": "Value", "justify": "right", "style": "magenta"}
    ]

    rows = [
        ["Stars", f"{repo['stargazers_count']:,}"],
        ["Forks", f"{repo['forks_count']:,}"],
        ["Open Issues", f"{repo['open_issues_count']:,}"],
        ["Watchers", f"{repo['watchers_count']:,}"],
        ["Open Pull Requests", f"{open_pulls:,}"],
        ["Closed Pull Requests", f"{closed_pulls:,}"],
        ["Contributors", f"{len(contributors):,}"],
        ["License", license_info.get("license", {}).get("name", "No license")],
        ["Latest Release", latest_release_name],
        ["Default Branch", repo["default_branch"]],
        ["Repository Size", repo_size_mb],
        ["Creation Date", repo["created_at"][:10]],
        ["Last Updated", repo["updated_at"][:10]]
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


def get_issues_stats(repo_name, state='all'):
    """
    Fetch issues data
    """
    url = f"{GITHUB_API_URL}/repos/{repo_name}/issues?state={state}"
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
        [issue['title'], issue['user']['login'], issue['state'], issue['created_at'][:10]]
        for issue in issues
    ]
    display_table("GitHub Issues Stats", columns, rows)


def get_pull_requests_stats(repo_name, state="all"):
    """
    Fetch issues data
    """
    url = f"{GITHUB_API_URL}/repos/{repo_name}/pulls?state={state}"
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
        [pr['title'],pr['user']['login'],pr['state'],pr['created_at'][:10]]
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

