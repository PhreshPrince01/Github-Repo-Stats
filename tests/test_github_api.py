import unittest
from unittest.mock import patch

from src.github_api import *


class utils_tests(unittest.TestCase):

    @patch('src.github_api.console.print')
    def test_display_stats_no_data(self, mock_print):
        # Call display_stats with None
        display_stats(None)
        
        # Check if the correct error message is printed
        mock_print.assert_called_once_with("[bold red]No data available to display. Please check the repository name and try again.[/bold red]")



    @patch('src.github_api.display_table')
    @patch('src.github_api.console.print')  # To mock console output
    def test_display_stats_success(self, mock_print, mock_display_table):
        # Sample data as it would be returned by get_repo_data
        data = {
            "repo": {"size": 12345, "stargazers_count": 10, "forks_count": 5, "open_issues_count": 3, "watchers_count": 15, "default_branch": "main", "created_at": "2023-01-01", "updated_at": "2023-01-10"},
            "pulls": [{"state": "open"}, {"state": "closed"}],
            "contributors": [{"login": "contributor1"}, {"login": "contributor2"}],
            "license": {"license": {"name": "MIT"}},
            "latest_release": {"name": "v1.0.0"}
        }

        # Call display_stats function
        display_stats(data)

        # Assert display_table was called
        self.assertTrue(mock_display_table.called)



    @patch('src.github_api.make_request')
    def test_get_repo_data_success(self, mock_make_request):
        # Mock API responses
        mock_make_request.side_effect = [
            {"size": 12345, "stargazers_count": 10, "forks_count": 5, "open_issues_count": 3, "watchers_count": 15, "default_branch": "main", "created_at": "2023-01-01", "updated_at": "2023-01-10"},
            [{"state": "open"}, {"state": "closed"}],  # pulls
            [{"login": "contributor1"}, {"login": "contributor2"}],  # contributors
            {"license": {"name": "MIT"}},  # license
            {"name": "v1.0.0"}  # latest release
        ]
        
        repo_name = "test-repo"
        result = get_repo_data(repo_name)
        
        # Check that the combined data is returned
        self.assertIsNotNone(result)
        self.assertIn("repo", result)
        self.assertIn("pulls", result)
        self.assertIn("contributors", result)
        self.assertIn("license", result)
        self.assertIn("latest_release", result)



    @patch('src.github_api.make_request')
    def test_get_repo_data_failure(self, mock_make_request):
        # Simulate API failure (all None responses)
        mock_make_request.side_effect = [None, None, None, None, None]
        
        repo_name = "invalid-repo"
        result = get_repo_data(repo_name)
        
        # Check that the result is None when all API calls fail
        self.assertIsNone(result)

    

    @patch('src.github_api.display_table')
    def test_display_commits_stats(self, mock_display_table):
        # Sample commit data
        data = [
            {
                "commit": {"message": "Initial commit", "author": {"name": "John Doe", "email": "john@example.com"}},
                "sha": "abc123"
            }
        ]
        repo_name = "test-repo"

        # Call display_commits_stats function
        display_commits_stats(data, repo_name)

        # Assert display_table was called with correct rows
        mock_display_table.assert_called_once()
        self.assertEqual(mock_display_table.call_args[0][2][0], 
            ["Initial commit", "John Doe", "john@example.com", "https://github.com/test-repo/commit/abc123"])



    @patch('src.github_api.make_request')
    def test_get_contributors_stats(self, mock_make_request):
        """Test fetching contributors data."""
        mock_make_request.return_value = [
            {'login': 'user1', 'contributions': 42},
            {'login': 'user2', 'contributions': 27}
        ]
        repo_name = 'test-repo'
        result = get_contributors_stats(repo_name)
        self.assertEqual(len(result), 2)
        mock_make_request.assert_called_once_with(f"https://api.github.com/repos/{repo_name}/contributors")



    @patch('src.github_api.display_table')
    def test_display_contributors_stats(self, mock_display_table):
        """Test displaying contributors stats."""
        contributors = [
            {'login': 'user1', 'contributions': 42},
            {'login': 'user2', 'contributions': 27}
        ]
        display_contributors_stats(contributors)
        mock_display_table.assert_called_once()
        args, _ = mock_display_table.call_args
        expected_rows = [['user1', '42'], ['user2', '27']]
        self.assertEqual(args[0], "GitHib Contributor Stats")
        self.assertEqual(args[2], expected_rows)



    @patch('src.github_api.make_request')
    def test_get_issues_stats(self, mock_make_request):
        """Test fetching issues data."""
        mock_make_request.return_value = [
            {'title': 'Issue 1', 'user': {'login': 'user1'}, 'state': 'open', 'created_at': '2023-01-01T00:00:00Z'},
            {'title': 'Issue 2', 'user': {'login': 'user2'}, 'state': 'closed', 'created_at': '2023-01-02T00:00:00Z'}
        ]
        repo_name = 'test-repo'
        result = get_issues_stats(repo_name)
        self.assertEqual(len(result), 2)
        mock_make_request.assert_called_once_with(f"{GITHUB_API_URL}/repos/{repo_name}/issues?state=all")



    @patch('src.github_api.display_table')
    def test_display_issues(self, mock_display_table):
        """Test displaying issues stats."""
        issues = [
            {'title': 'Issue 1', 'user': {'login': 'user1'}, 'state': 'open', 'created_at': '2023-01-01T00:00:00Z'},
            {'title': 'Issue 2', 'user': {'login': 'user2'}, 'state': 'closed', 'created_at': '2023-01-02T00:00:00Z'}
        ]
        display_issues(issues)
        mock_display_table.assert_called_once()
        args, _ = mock_display_table.call_args
        expected_rows = [
            ['Issue 1', 'user1', 'open', '2023-01-01'],
            ['Issue 2', 'user2', 'closed', '2023-01-02']
        ]
        self.assertEqual(args[0], "GitHub Issues Stats")
        self.assertEqual(args[2], expected_rows)



    @patch('src.github_api.make_request')
    def test_get_pull_requests_stats(self, mock_make_request):
        """Test fetching pull requests data."""
        mock_make_request.return_value = [
            {'title': 'PR 1', 'user': {'login': 'user1'}, 'state': 'open', 'created_at': '2023-01-03T00:00:00Z'},
            {'title': 'PR 2', 'user': {'login': 'user2'}, 'state': 'closed', 'created_at': '2023-01-04T00:00:00Z'}
        ]
        repo_name = 'test-repo'
        result = get_pull_requests_stats(repo_name)
        self.assertEqual(len(result), 2)
        mock_make_request.assert_called_once_with(f"{GITHUB_API_URL}/repos/{repo_name}/pulls?state=all")



    @patch('src.github_api.display_table')
    def test_display_pull_requests(self, mock_display_table):
        """Test displaying pull requests stats."""
        prs = [
            {'title': 'PR 1', 'user': {'login': 'user1'}, 'state': 'open', 'created_at': '2023-01-03T00:00:00Z'},
            {'title': 'PR 2', 'user': {'login': 'user2'}, 'state': 'closed', 'created_at': '2023-01-04T00:00:00Z'}
        ]
        display_pull_requests(prs)
        mock_display_table.assert_called_once()
        args, _ = mock_display_table.call_args
        expected_rows = [
            ['PR 1', 'user1', 'open', '2023-01-03'],
            ['PR 2', 'user2', 'closed', '2023-01-04']
        ]
        self.assertEqual(args[0], "GitHib Pull Requests Stats")
        self.assertEqual(args[2], expected_rows)



    @patch('src.github_api.make_request')
    def test_get_branches_stats(self, mock_make_request):
        """Test fetching branches data."""
        def side_effect(url):
            if 'branches' in url:
                return [
                    {'name': 'main', 'protected': True},
                    {'name': 'develop', 'protected': False}
                ]
            else:
                return {'default_branch': 'main'}
        mock_make_request.side_effect = side_effect
        repo_name = 'test-repo'
        branches, default_branch = get_branches_stats(repo_name)
        self.assertEqual(default_branch, 'main')
        self.assertEqual(len(branches), 2)



    @patch('src.github_api.display_table')
    def test_display_branches(self, mock_display_table):
        """Test displaying branches stats."""
        branches = [
            {'name': 'main', 'protected': True},
            {'name': 'develop', 'protected': False}
        ]
        default_branch = 'main'
        display_branches(branches, default_branch)
        mock_display_table.assert_called_once()
        args, _ = mock_display_table.call_args
        expected_rows = [
            ['[bold yellow]main (default)[/bold yellow]', 'Yes'],
            ['develop', 'No']
        ]
        self.assertEqual(args[0], "GitHub Branches Stats")
        self.assertEqual(args[2], expected_rows)



    @patch('src.github_api.make_request')
    def test_get_release_stats(self, mock_make_request):
        """Test fetching release data."""
        mock_make_request.return_value = [
            {'tag_name': 'v1.0', 'name': 'First Release', 'published_at': '2023-01-05T00:00:00Z'}
        ]
        repo_name = 'test-repo'
        releases = get_release_stats(repo_name)
        self.assertEqual(len(releases), 1)
        mock_make_request.assert_called_once_with(f"{GITHUB_API_URL}/repos/{repo_name}/releases")



    @patch('src.github_api.display_table')
    def test_display_releases(self, mock_display_table):
        """Test displaying releases stats."""
        releases = [
            {'tag_name': 'v1.0', 'name': 'First Release', 'published_at': '2023-01-05T00:00:00Z'}
        ]
        display_releases(releases)
        mock_display_table.assert_called_once()
        args, _ = mock_display_table.call_args
        expected_rows = [
            ['v1.0', 'First Release', '2023-01-05']
        ]
        self.assertEqual(args[0], "GitHib Releses Stats")
        self.assertEqual(args[2], expected_rows)



    @patch('src.github_api.make_request')
    def test_get_tags_stats(self, mock_make_request):
        """Test fetching tags data."""
        mock_make_request.return_value = [
            {'name': 'v1.0', 'commit': {'sha': 'abc123'}}
        ]
        repo_name = 'test-repo'
        tags = get_tags_stats(repo_name)
        self.assertEqual(len(tags), 1)
        mock_make_request.assert_called_once_with(f"{GITHUB_API_URL}/repos/{repo_name}/tags")



    @patch('src.github_api.display_table')
    def test_display_tags(self, mock_display_table):
        """Test displaying tags."""
        tags = [
            {'name': 'v1.0', 'commit': {'sha': 'abc123'}}
        ]
        display_tags(tags)
        mock_display_table.assert_called_once()
        args, _ = mock_display_table.call_args
        expected_rows = [
            ['v1.0', 'abc123']
        ]
        self.assertEqual(args[0], "GitHub Tags")
        self.assertEqual(args[2], expected_rows)



    @patch('src.github_api.make_request')
    def test_get_languages_stats(self, mock_make_request):
        """Test fetching languages data."""
        mock_make_request.return_value = {'Python': 15000, 'JavaScript': 5000}
        repo_name = 'test-repo'
        languages = get_languages_stats(repo_name)
        self.assertEqual(languages['Python'], 15000)
        mock_make_request.assert_called_once_with(f"{GITHUB_API_URL}/repos/{repo_name}/languages")



    @patch('src.github_api.display_table')
    def test_display_languages(self, mock_display_table):
        """Test displaying languages stats."""
        languages = {'Python': 15000, 'JavaScript': 5000}
        display_languages(languages)
        mock_display_table.assert_called_once()
        args, _ = mock_display_table.call_args
        expected_rows = [
            ['Python', '75.00%'],
            ['JavaScript', '25.00%']
        ]
        self.assertEqual(args[0], "GitHub Repository Languages")
        self.assertEqual(args[2], expected_rows)



    @patch('src.github_api.make_request')
    def test_get_forks_stats(self, mock_make_request):
        """Test fetching forks data."""
        mock_make_request.return_value = [
            {'full_name': 'user1/test-repo', 'owner': {'login': 'user1'}, 'stargazers_count': 10}
        ]
        repo_name = 'test-repo'
        forks = get_forks_stats(repo_name)
        self.assertEqual(len(forks), 1)
        mock_make_request.assert_called_once_with(f"{GITHUB_API_URL}/repos/{repo_name}/forks")



    @patch('src.github_api.display_table')
    def test_display_forks(self, mock_display_table):
        """Test displaying forks stats."""
        forks = [
            {'full_name': 'user1/test-repo', 'owner': {'login': 'user1'}, 'stargazers_count': 10}
        ]
        display_forks(forks)
        mock_display_table.assert_called_once()
        args, _ = mock_display_table.call_args
        expected_rows = [
            ['user1/test-repo', 'user1', '10']
        ]
        self.assertEqual(args[0], "GitHub Repository Forks")
        self.assertEqual(args[2], expected_rows)



    @patch('src.github_api.make_request')
    def test_get_traffic_stats(self, mock_make_request):
        """Test fetching traffic data."""
        def side_effect(url):
            if 'views' in url:
                return {'views': [{'timestamp': '2023-01-06T00:00:00Z', 'uniques': 100, 'count': 200}]}
            elif 'clones' in url:
                return {'clones': [{'timestamp': '2023-01-06T00:00:00Z', 'uniques': 50, 'count': 80}]}
            else:
                return None
        mock_make_request.side_effect = side_effect
        repo_name = 'test-repo'
        traffic = get_traffic_stats(repo_name)
        self.assertIsNotNone(traffic)
        self.assertIn('views', traffic)
        self.assertIn('clones', traffic)



    @patch('src.github_api.display_table')
    def test_display_traffic(self, mock_display_table):
        """Test displaying traffic data."""
        traffic_data = {
            'views': {
                'views': [
                    {'timestamp': '2023-01-06T00:00:00Z', 'uniques': 100, 'count': 200}
                ]
            },
            'clones': {
                'clones': [
                    {'timestamp': '2023-01-06T00:00:00Z', 'uniques': 50, 'count': 80}
                ]
            }
        }
        display_traffic(traffic_data)
        self.assertEqual(mock_display_table.call_count, 2)
        calls = mock_display_table.call_args_list

        # Check views table
        args, _ = calls[0]
        expected_views_rows = [
            ('2023-01-06', '100', '200')
        ]
        self.assertEqual(args[0], "GitHub Repository Traffic - Views")
        self.assertEqual(args[2], expected_views_rows)

        # Check clones table
        args, _ = calls[1]
        expected_clones_rows = [
            ('2023-01-06', '50', '80')
        ]
        self.assertEqual(args[0], "GitHub Repository Traffic - Clones")
        self.assertEqual(args[2], expected_clones_rows)