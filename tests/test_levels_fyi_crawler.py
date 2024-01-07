import unittest
from unittest.mock import patch
from levelsfyi_crawler import __name__ as script_name

class TestLevelsFYICrawler(unittest.TestCase):

    @patch('builtins.input', side_effect=['d', 'max_tc', 'exit'])
    @patch(f'{script_name}.open', create=True)
    def test_script_execution(self, mock_open, mock_input):
        try:
            # Your test logic here
            # Call the part of the script you want to test
            with open('levelsfyi_crawler.py') as script:
                exec(script.read())
        except SystemExit as e:
            # The script exited, you can print the exit code for debugging
            print(f'SystemExit: {e.code}')
            self.assertEqual(e.code, 0)
        except Exception as e:
            # An unexpected exception occurred
            print(f'Unexpected exception: {e}')
            raise

if __name__ == '__main__':
    unittest.main()