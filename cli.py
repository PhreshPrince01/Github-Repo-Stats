import click
from github_api import *
from utils import print_welcome_message


@click.group()
def cli():
    print_welcome_message()


@cli.command()
@click.option('--repo', prompt='GitHub Repository', help= 'The full name of the GitHub repository (e.g., owener/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_contributors(repo, confirm):
    """
    CLI to get contributors for a GitHub repository
    """
    if confirm:
        click.confirm(f"Are you sure you want to fetch data stats for {repo}",abort=True)
    contributors = get_contributors_stats(repo)
    if contributors:
        display_contributors_stats(contributors)


@cli.command()
@click.option('--repo', prompt='GitHub Repository', help= 'The full name of the GitHub repository (e.g., owener/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_stats(repo, confirm):
    """
    CLI to get  stats for a GitHub Repository
    """
    if confirm:
        click.confirm(f"Are you sure you want to fetch data stats for {repo}",abort=True)
    data = get_repo_data(repo)
    if data:
        display_stats(data)



@cli.command()
@click.option('--repo', prompt='GitHub Repository', help= 'The full name of the GitHub repository (e.g., owener/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_commits(repo, confirm):
    """
    CLI to get commits for a GitHub Repository
    """
    if confirm:
        click.confirm(f"Are you sure you want to fetch commits for {repo}",abort=True)
    data = get_commits_data(repo)
    if data:
        display_commits_stats(data,repo)


@cli.command()
@click.option('--repo', prompt='GitHub Repository', help= 'The full name of the GitHub repository (e.g., owener/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_issues(repo, confirm):
    """
    CLI to get commits for a GitHub Repository
    """
    if confirm:
        click.confirm(f"Are you sure you want to fetch issues for {repo}",abort=True)
    data = get_issues_stats(repo)
    if data:
        display_issues(data)


@cli.command()
@click.option('--repo', prompt='GitHub Repository', help= 'The full name of the GitHub repository (e.g., owener/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_pull_requests(repo, confirm):
    """
    CLI to get commits for a GitHub Repository
    """
    if confirm:
        click.confirm(f"Are you sure you want to fetch pull requests for {repo}",abort=True)
    data = get_pull_requests_stats(repo)
    if data:
        display_pull_requests(data)


@cli.command()
@click.option('--repo', prompt='GitHub Repository', help= 'The full name of the GitHub repository (e.g., owener/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_branches(repo, confirm):
    """
    CLI to get branches for a GitHub Repository
    """
    if confirm:
        click.confirm(f"Are you sure you want to fetch branches for {repo}",abort=True)
    branches, default_branch = get_branches_stats(repo)
    if branches and default_branch:
        display_branches(branches, default_branch)



@cli.command()
@click.option('--repo', prompt='GitHub Repository', help= 'The full name of the GitHub repository (e.g., owener/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_releases(repo, confirm):
    """
    CLI to get branches for a GitHub Repository
    """
    if confirm:
        click.confirm(f"Are you sure you want to fetch releases for {repo}",abort=True)
    data = get_release_stats(repo)
    if data:
        display_releases(data)
    else:
        print(404)


@cli.command()
@click.option('--repo', prompt='GitHub Repository', help= 'The full name of the GitHub repository (e.g., owener/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_tags(repo, confirm):
    """
    CLI to get tags for a GitHub Repository
    """
    if confirm:
        click.confirm(f"Are you sure you want to fetch tags for {repo}",abort=True)
    data = get_tags_stats(repo)
    if data:
        display_tags(data)
    else:
        print(404)


@cli.command()
@click.option('--repo', prompt='GitHub Repository', help= 'The full name of the GitHub repository (e.g., owener/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_languages(repo, confirm):
    """
    CLI to get languages for a GitHub Repository
    """
    if confirm:
        click.confirm(f"Are you sure you want to fetch languages for {repo}",abort=True)
    data = get_languages_stats(repo)
    if data:
        display_languages(data)
    else:
        print(404)


@cli.command()
@click.option('--repo', prompt='GitHub Repository', help= 'The full name of the GitHub repository (e.g., owener/repo)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before fetching data.')
def get_forks(repo, confirm):
    """
    CLI to get forks for a GitHub Repository
    """
    if confirm:
        click.confirm(f"Are you sure you want to fetch forks for {repo}",abort=True)
    data = get_forks_stats(repo)
    if data:
        display_forks(data)
    else:
        print(404)

if __name__ == "__main__":
    cli()