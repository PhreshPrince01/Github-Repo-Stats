import click
from github_api import *
from utils import print_welcome_message

@click.group()
def cli():
    """
    CLI tool for interacting with GitHub repositories.
    
    Example Usage: python3 cli.py get-stats --repo octocat/Hello-World
            Help Example Usage: python3 cli.py get-contributors --help
    """
    

@cli.command(help="Fetch and display contributors for a GitHub repository.\n\nExample: python3 cli.py get-contributors --repo owner/repo")
@click.option('--repo', prompt='GitHub Repository', help='The full name of the GitHub repository (e.g., owner/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_contributors(repo, confirm):
    """Fetch and display contributors for a GitHub repository."""
    if confirm and not prompt_confirmation("contributors", repo):
        click.echo("Operation cancelled.")
        return
    contributors = get_contributors_stats(repo)
    if contributors:
        display_contributors_stats(contributors)
        

@cli.command(help="Fetch and display general stats for a GitHub repository.\n\nExample: python3 cli.py get-stats --repo owner/repo")
@click.option('--repo', prompt='GitHub Repository', help='The full name of the GitHub repository (e.g., owner/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_stats(repo, confirm):
    """Fetch and display general stats for a GitHub repository."""
    if confirm and not prompt_confirmation("stats", repo):
        click.echo("Operation cancelled.")
        return
    
    show_progress("Fetching Repo Stats...",total=100)
    data = get_repo_data(repo)
    if data:
        show_status("Repository stats fetched successfully.")
        display_stats(data)
    else:
        show_status("Failed to fetch repository stats.", success=False)


@cli.command(help="Fetch and display commits for a GitHub repository.\n\nExample: python3 cli.py get-commits --repo owner/repo")
@click.option('--repo', prompt='GitHub Repository', help='The full name of the GitHub repository (e.g., owner/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_commits(repo, confirm):
    """Fetch and display commits for a GitHub repository."""
    if confirm and not prompt_confirmation("commits", repo):
        click.echo("Operation cancelled.")
        return
    data = get_commits_data(repo)
    if data:
        show_status("Commits fetched successfully.")
        display_commits_stats(data, repo)
    else:
        show_status("Failed to fetch commits.", success=False)


@cli.command(help="Fetch and display issues for a GitHub repository.\n\nExample: python3 cli.py get-issues --repo owner/repo")
@click.option('--repo', prompt='GitHub Repository', help='The full name of the GitHub repository (e.g., owner/repo)')
@click.option('--state', type=click.Choice(['open', 'closed', 'all'], case_sensitive=False), default='all', help='Filter issues by state (open/closed).')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_issues(repo, state, confirm):
    """
    CLI to get issues for a GitHub Repository
    """
    if confirm:
        click.confirm(f"Are you sure you want to fetch {state} issues for {repo}?", abort=True)
    data = get_issues_stats(repo, state)
    if data:
        show_status("Issues fetched successfully.")
        display_issues(data)

    else:
        show_status("Failed to fetch Issues.", success=False)


@cli.command(help="Fetch and display pull requests for a GitHub repository.\n\nExample: python3 cli.py get-pull-requests --repo owner/repo")
@click.option('--repo', prompt='GitHub Repository', help='The full name of the GitHub repository (e.g., owner/repo)')
@click.option('--state', type=click.Choice(['open', 'closed','all'], case_sensitive=False),default='all', help='Filter pull requests by state (open/closed).')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_pull_requests(repo, state, confirm):
    """Fetch and display pull requests for a GitHub repository."""
    if confirm and not prompt_confirmation("pull requests", repo):
        click.echo("Operation cancelled.")
        return
    data = get_pull_requests_stats(repo,state)
    if data:
        show_status("Pull requests fetched successfully.")
        display_pull_requests(data)
    else:
        show_status("Failed to fetch Pull requests.", success=False)


@cli.command(help="Fetch and display branches for a GitHub repository.\n\nExample: python3 cli.py get-branches --repo owner/repo")
@click.option('--repo', prompt='GitHub Repository', help='The full name of the GitHub repository (e.g., owner/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_branches(repo, confirm):
    """Fetch and display branches for a GitHub repository."""
    if confirm and not prompt_confirmation("branches", repo):
        click.echo("Operation cancelled.")
        return
    branches, default_branch = get_branches_stats(repo)
    if branches and default_branch:
        show_status("Branches fetched successfully.")
        display_branches(branches, default_branch)
    else:
        show_status("Failed to fetch Branches.", success=False)


@cli.command(help="Fetch and display releases for a GitHub repository.\n\nExample: python3 cli.py get-releases --repo owner/repo")
@click.option('--repo', prompt='GitHub Repository', help='The full name of the GitHub repository (e.g., owner/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_releases(repo, confirm):
    """Fetch and display releases for a GitHub repository."""
    if confirm and not prompt_confirmation("releases", repo):
        click.echo("Operation cancelled.")
        return
    data = get_release_stats(repo)
    if data:
        show_status("Releases fetched successfully.")
        display_releases(data)
    else:
       show_status("Failed to fetch Releases.", success=False)


@cli.command(help="Fetch and display tags for a GitHub repository.\n\nExample: python3 cli.py get-tags --repo owner/repo")
@click.option('--repo', prompt='GitHub Repository', help='The full name of the GitHub repository (e.g., owner/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_tags(repo, confirm):
    """Fetch and display tags for a GitHub repository."""
    if confirm and not prompt_confirmation("tags", repo):
        return
    data = get_tags_stats(repo)
    if data:
        show_status("Tags fetched successfully.")
        display_tags(data)
    else:
        show_status("Failed to fetch Tags.", success=False)


@cli.command(help="Fetch and display languages used in a GitHub repository.\n\nExample: python3 cli.py get-languages --repo owner/repo")
@click.option('--repo', prompt='GitHub Repository', help='The full name of the GitHub repository (e.g., owner/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_languages(repo, confirm):
    """Fetch and display languages used in a GitHub repository."""
    if confirm and not prompt_confirmation("languages", repo):
        click.echo("Operation cancelled.")
        return
    data = get_languages_stats(repo)
    if data:
        show_status("Languages fetched successfully.")
        display_languages(data)
    else:
        show_status("Failed to fetch Languages.", success=False)


@cli.command(help="Fetch and display forks for a GitHub repository.\n\nExample: python3 cli.py get-forks --repo owner/repo")
@click.option('--repo', prompt='GitHub Repository', help='The full name of the GitHub repository (e.g., owner/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_forks(repo, confirm):
    """Fetch and display forks for a GitHub repository."""
    if confirm and not prompt_confirmation("repo", repo):
        click.echo("Operation cancelled.")
        return
    data = get_forks_stats(repo)
    if data:
        show_status("Forks fetched successfully.")
        display_forks(data)
    else:
        show_status("Failed to fetch Forks", success=False)


@cli.command(help="Fetch and display traffic data for a GitHub repository.\n\nExample: python3 cli.py get-traffic --repo owner/repo")
@click.option('--repo', prompt='GitHub Repository', help='The full name of the GitHub repository (e.g., owner/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_traffic(repo, confirm):
    """Fetch and display traffic data for a GitHub repository."""
    if confirm and not prompt_confirmation("trafic", repo):
        click.echo("Operation cancelled.")
        return
    data = get_traffic_stats(repo)
    if data:
        show_status("Traffic fetched successfully.")
        display_traffic(data)
    else:
        show_status("Failed to fetch Traffic.", success=False)


if __name__ == "__main__":
    print_welcome_message()
    cli()