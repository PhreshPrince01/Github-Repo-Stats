import click
from github_api import *
from utils import print_welcome_message

@click.group()
def cli():
    """
    CLI tool for interacting with GitHub repositories.
    
    Example Usage: python3 cli.py --repo get-stats ooctocat/Hello-World
            Help Example Usage: python3 cli.py get-contributors --help
    """
    

@cli.command(help="Fetch and display contributors for a GitHub repository.\n\nExample: python3 cli.py get-contributors --repo owner/repo")
@click.option('--repo', prompt='GitHub Repository', help='The full name of the GitHub repository (e.g., owner/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_contributors(repo, confirm):
    """Fetch and display contributors for a GitHub repository."""
    if confirm and not click.confirm(f"Are you sure you want to fetch contributors for {repo}?", default=True):
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
    if confirm and not click.confirm(f"Are you sure you want to fetch stats for {repo}?", default=True):
        click.echo("Operation cancelled.")
        return
    data = get_repo_data(repo)
    if data:
        display_stats(data)


@cli.command(help="Fetch and display commits for a GitHub repository.\n\nExample: python3 cli.py get-commits --repo owner/repo")
@click.option('--repo', prompt='GitHub Repository', help='The full name of the GitHub repository (e.g., owner/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_commits(repo, confirm):
    """Fetch and display commits for a GitHub repository."""
    if confirm and not click.confirm(f"Are you sure you want to fetch commits for {repo}?", default=True):
        click.echo("Operation cancelled.")
        return
    data = get_commits_data(repo)
    if data:
        display_commits_stats(data, repo)


@cli.command(help="Fetch and display issues for a GitHub repository.\n\nExample: python3 cli.py get-issues --repo owner/repo")
@click.option('--repo', prompt='GitHub Repository', help='The full name of the GitHub repository (e.g., owner/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_issues(repo, confirm):
    """Fetch and display issues for a GitHub repository."""
    if confirm and not click.confirm(f"Are you sure you want to fetch issues for {repo}?", default=True):
        click.echo("Operation cancelled.")
        return
    data = get_issues_stats(repo)
    if data:
        display_issues(data)


@cli.command(help="Fetch and display pull requests for a GitHub repository.\n\nExample: python3 cli.py get-pull-requests --repo owner/repo")
@click.option('--repo', prompt='GitHub Repository', help='The full name of the GitHub repository (e.g., owner/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_pull_requests(repo, confirm):
    """Fetch and display pull requests for a GitHub repository."""
    if confirm and not click.confirm(f"Are you sure you want to fetch pull requests for {repo}?", default=True):
        click.echo("Operation cancelled.")
        return
    data = get_pull_requests_stats(repo)
    if data:
        display_pull_requests(data)


@cli.command(help="Fetch and display branches for a GitHub repository.\n\nExample: python3 cli.py get-branches --repo owner/repo")
@click.option('--repo', prompt='GitHub Repository', help='The full name of the GitHub repository (e.g., owner/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_branches(repo, confirm):
    """Fetch and display branches for a GitHub repository."""
    if confirm and not click.confirm(f"Are you sure you want to fetch branches for {repo}?", default=True):
        click.echo("Operation cancelled.")
        return
    branches, default_branch = get_branches_stats(repo)
    if branches and default_branch:
        display_branches(branches, default_branch)


@cli.command(help="Fetch and display releases for a GitHub repository.\n\nExample: python3 cli.py get-releases --repo owner/repo")
@click.option('--repo', prompt='GitHub Repository', help='The full name of the GitHub repository (e.g., owner/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_releases(repo, confirm):
    """Fetch and display releases for a GitHub repository."""
    if confirm and not click.confirm(f"Are you sure you want to fetch releases for {repo}?", default=True):
        click.echo("Operation cancelled.")
        return
    data = get_release_stats(repo)
    if data:
        display_releases(data)


@cli.command(help="Fetch and display tags for a GitHub repository.\n\nExample: python3 cli.py get-tags --repo owner/repo")
@click.option('--repo', prompt='GitHub Repository', help='The full name of the GitHub repository (e.g., owner/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_tags(repo, confirm):
    """Fetch and display tags for a GitHub repository."""
    if confirm and not click.confirm(f"Are you sure you want to fetch tags for {repo}?", default=True):
        click.echo("Operation cancelled.")
        return
    data = get_tags_stats(repo)
    if data:
        display_tags(data)


@cli.command(help="Fetch and display languages used in a GitHub repository.\n\nExample: python3 cli.py get-languages --repo owner/repo")
@click.option('--repo', prompt='GitHub Repository', help='The full name of the GitHub repository (e.g., owner/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_languages(repo, confirm):
    """Fetch and display languages used in a GitHub repository."""
    if confirm and not click.confirm(f"Are you sure you want to fetch languages for {repo}?", default=True):
        click.echo("Operation cancelled.")
        return
    data = get_languages_stats(repo)
    if data:
        display_languages(data)


@cli.command(help="Fetch and display forks for a GitHub repository.\n\nExample: python3 cli.py get-forks --repo owner/repo")
@click.option('--repo', prompt='GitHub Repository', help='The full name of the GitHub repository (e.g., owner/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_forks(repo, confirm):
    """Fetch and display forks for a GitHub repository."""
    if confirm and not click.confirm(f"Are you sure you want to fetch forks for {repo}?", default=True):
        click.echo("Operation cancelled.")
        return
    data = get_forks_stats(repo)
    if data:
        display_forks(data)


@cli.command(help="Fetch and display traffic data for a GitHub repository.\n\nExample: python3 cli.py get-traffic --repo owner/repo")
@click.option('--repo', prompt='GitHub Repository', help='The full name of the GitHub repository (e.g., owner/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_traffic(repo, confirm):
    """Fetch and display traffic data for a GitHub repository."""
    if confirm and not click.confirm(f"Are you sure you want to fetch traffic data for {repo}?", default=True):
        click.echo("Operation cancelled.")
        return
    data = get_traffic_stats(repo)
    if data:
        display_traffic(data)

if __name__ == "__main__":
    print_welcome_message()
    cli()
