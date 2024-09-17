import click
from github_api import get_repo_data, display_stats

@click.command()
@click.option('--repo', prompt='GitHub Repository', help= 'The full name of the GitHub repository (e.g., owener/repo)')
def get_stats(repo):
    """
    CLI to get  stats for a GitHub Repository
    """
    data = get_repo_data(repo)
    if data:
        display_stats(data)

if __name__ == "__main__":
    get_stats()