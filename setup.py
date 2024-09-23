from setuptools import setup, find_packages

# Function to read requirements from requirements.txt
def parse_requirements(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()

setup(
    name='github-repo-stats-cli',
    version='1.0.0',
    description='A CLI tool for fetching GitHub repository statistics',
    author='Prince Melane',
    author_email='princemelane14@gmail.com',
    url='https://github.com/PhreshPrince01/Github-Repo-Stats/',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},  # Set the source directory
    install_requires=parse_requirements('requirements.txt'),
    entry_points={
        'console_scripts': [
            'github-stats=cli:cli',  # Pointing to the cli function in cli.py
        ],
    },
)
