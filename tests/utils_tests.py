import unittest
from unittest.mock import patch, MagicMock


from src.utils import print_welcome_message, show_status,prompt_confirmation,print_error_msg, make_request, display_table

class utils_tests(unittest.TestCase):

    @patch("src.utils.console.print")
    def test_print_welcome_message(self, mock_console_print):
        print_welcome_message()
        # Check that console.print was called once
        self.assertEqual(mock_console_print.call_count, 1)

    
    @patch("src.utils.click.confirm")
    def test_prompt_confirmation(self, mock_confirm):
        mock_confirm.return_value = True
        response = prompt_confirmation("stats", "my-repo")
        self.assertTrue(response)
        mock_confirm.assert_called_with("Are you sure you want to fetch stats for my-repo?", default=True)



    @patch("src.utils.console.print")
    def test_show_status_success(self, mock_console_print):
        show_status("Operation completed")
        mock_console_print.assert_called_once()

    
    @patch("src.utils.console.print")
    def test_show_status_error(self, mock_console_print):
        show_status("Operation failed", success=False)
        mock_console_print.assert_called_once()

    
    @patch("src.utils.requests.get")
    @patch("src.utils.console.print")
    def test_make_request_404_error(self, mock_console_print, mock_get):
        # Mock a 404 error response
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.reason = "Not Found"
        mock_get.return_value = mock_response

        result = make_request("https://api.github.com/repos/non-existent-repo")
        self.assertIsNone(result)
        mock_console_print.assert_called_with("[bold red]Repository: https://api.github.com/repos/non-existent-repo not found. Please check the repository name.[/bold red]")


    @patch("src.utils.console.print")
    def test_display_table(self, mock_console_print):
        columns = [{"name": "Stat"}, {"name": "Value"}]
        rows = [["Stars", "100"], ["Forks", "50"]]
        display_table("Test Table", columns, rows)
        mock_console_print.assert_called_once()



    @patch('src.utils.console.print')
    def test_print_error_msg(self, mock_print):
        """Test that the error message is printed correctly."""
        
        # Call the function
        print_error_msg()
        
        # Check if console.print was called with the correct error message
        mock_print.assert_called_once_with("[bold red]Failed to fetch repository data. Please check the repository name and try again.[/bold red]")
