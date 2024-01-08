import pytest
from unittest.mock import patch
from io import StringIO
from levelsfyi_crawler import query

def test_query_company():
    levels_data = [
        {
            'Company': 'Google',
            'Location': 'Sunnyvale, CA',
            'Date': '2024-01-07', 
            'Level Name': 'L4',
            'Tag': 'Software',
            'YearOfExperience': '5 years',
            'Total/AtCompany': '0',  
            'TotalCompensation': '$170,000',
            'Base': '$120,000',
            'Stock(yr)': '$40,000',
            'Bonus': '$10,000'
        },
        {
            'Company': 'Facebook',
            'Location': 'Menlo Park, CA',
            'Date': '2024-01-07',
            'Level Name': 'E4',
            'Tag': 'Software',
            'YearOfExperience': '5 years',
            'Total/AtCompany': '0',
            'TotalCompensation': '$200,000',
            'Base': '$120,000',
            'Stock(yr)': '$60,000',
            'Bonus': '$20,000'
        }
    ]
    
    with patch('builtins.input', side_effect=['company Google', 'exit']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            query(levels_data)
            assert "[v] google total compensation" in mock_stdout.getvalue() \
                    and "Company: Google" in mock_stdout.getvalue() \
                    and not "Company: Facebook" in mock_stdout.getvalue()