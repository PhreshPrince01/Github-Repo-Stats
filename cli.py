import click
from github_api import get_repo_data, display_stats, get_commits_data, display_commits_stats
from utils import print_welcome_message


@click.group()
def cli():
    print_welcome_message()


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
        display_commits_stats(data)


if __name__ == "__main__":
    cli()