import pytest
from unittest.mock import patch
from io import StringIO
from levelsfyi_crawler import query

def test_query_exit():
    with patch('builtins.input', return_value='exit'):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            query([])
            assert "[*] Setting levels.fyi query" in mock_stdout.getvalue()
            assert "[>] Query> " in mock_stdout.getvalue()

def test_query_invalid_command():
    with patch('builtins.input', side_effect=['invalid_command', 'exit']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            query([])
            assert "[!] invalid_command is not a valid command" in mock_stdout.getvalue()

def test_query_max_tc():
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
    
    with patch('builtins.input', side_effect=['max_tc', 'exit']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            query(levels_data)
            assert "[v] Max total compensation" in mock_stdout.getvalue() \
                    and "Company: Facebook" in mock_stdout.getvalue() \
                    and "Location: Menlo Park, CA" in mock_stdout.getvalue() \
                    and "Date: 2024-01-07" in mock_stdout.getvalue() \
                    and "Level Name: E4" in mock_stdout.getvalue() \
                    and "Tag: Software" in mock_stdout.getvalue() \
                    and "Year of Experience: 5 years" in mock_stdout.getvalue() \
                    and "Total/At Company: 0" in mock_stdout.getvalue() \
                    and "Total Compensation: $200,000" in mock_stdout.getvalue() \
                    and "Base: $120,000" in mock_stdout.getvalue() \
                    and "Stock(yr): $60,000" in mock_stdout.getvalue() \
                    and "Bonus: $20,000" in mock_stdout.getvalue() \
                    and "Company: Google" not in mock_stdout.getvalue()

def test_query_min_tc():
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
    
    with patch('builtins.input', side_effect=['min_tc', 'exit']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            query(levels_data)
            assert "[v] Min total compensation" in mock_stdout.getvalue() \
                    and "Company: Google" in mock_stdout.getvalue() \
                    and "Location: Sunnyvale, CA" in mock_stdout.getvalue() \
                    and "Date: 2024-01-07" in mock_stdout.getvalue() \
                    and "Level Name: L4" in mock_stdout.getvalue() \
                    and "Tag: Software" in mock_stdout.getvalue() \
                    and "Year of Experience: 5 years" in mock_stdout.getvalue() \
                    and "Total/At Company: 0" in mock_stdout.getvalue() \
                    and "Total Compensation: $170,000" in mock_stdout.getvalue() \
                    and "Base: $120,000" in mock_stdout.getvalue() \
                    and "Stock(yr): $40,000" in mock_stdout.getvalue() \
                    and "Bonus: $10,000" in mock_stdout.getvalue() \
                    and "Company: Facebook" not in mock_stdout.getvalue()

def test_query_median_tc():
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
            'Company': 'Netflix',
            'Location': 'Los Gatos, CA',
            'Date': '2024-01-07',
            'Level Name': 'L5',
            'Tag': 'AI/ML',
            'YearOfExperience': '5 years',
            'Total/AtCompany': '0',
            'TotalCompensation': '$300,000',
            'Base': '$200,000',
            'Stock(yr)': '$80,000',
            'Bonus': '$20,000'
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
    with patch('builtins.input', side_effect=['median_tc', 'exit']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            query(levels_data)
            assert "[v] Median total compensation" in mock_stdout.getvalue() \
                    and "200000" in mock_stdout.getvalue()

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

def test_query_location():
    levels_data = [
        {
            'Company': 'Google',
            'Location': 'New York, NY',
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
    
    with patch('builtins.input', side_effect=['location CA', 'exit']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            query(levels_data)
            assert "[v] Location: CA" in mock_stdout.getvalue() \
                    and "Company: Facebook" in mock_stdout.getvalue() \
                    and not "Company: Google" in mock_stdout.getvalue()
            
def test_query_level():
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
    
    with patch('builtins.input', side_effect=['level l4', 'exit']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            query(levels_data)
            assert "[v] Level: l4" in mock_stdout.getvalue() \
                    and "[v] Average year of experience" in mock_stdout.getvalue() \
                    and "Company: Google" in mock_stdout.getvalue() \
                    and not "Company: Facebook" in mock_stdout.getvalue()

def test_query_tag():
    levels_data = [
        {
            'Company': 'Google',
            'Location': 'Sunnyvale, CA',
            'Date': '2024-01-07', 
            'Level Name': 'L4',
            'Tag': 'Networking',
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
    
    with patch('builtins.input', side_effect=['tag Networking', 'exit']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            query(levels_data)
            assert "[v] Tag: Networking" in mock_stdout.getvalue() \
                    and "Company: Google" in mock_stdout.getvalue() \
                    and not "Company: Facebook" in mock_stdout.getvalue()

def test_query_yoe():
    levels_data = [
        {
            'Company': 'Google',
            'Location': 'Sunnyvale, CA',
            'Date': '2024-01-07', 
            'Level Name': 'L4',
            'Tag': 'Software',
            'YearOfExperience': '3 years',
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
    
    with patch('builtins.input', side_effect=['yoe 5', 'exit']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            query(levels_data)
            assert "[v] YOE: 5" in mock_stdout.getvalue() \
                    and "Company: Facebook" in mock_stdout.getvalue() \
                    and not "Company: Google" in mock_stdout.getvalue()

# filter location CA company google
def test_query_filter1():
    levels_data = [
        {
            'Company': 'Google',
            'Location': 'Sunnyvale, CA',
            'Date': '2024-01-07', 
            'Level Name': 'L4',
            'Tag': 'Software',
            'YearOfExperience': '3 years',
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
    
    with patch('builtins.input', side_effect=['filter location CA company google', 'exit']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            query(levels_data)
            assert  "Company: Google" in mock_stdout.getvalue() \
                    and not "Company: Facebook" in mock_stdout.getvalue()
    
# filter company google level l3 location CA
def test_query_filter2():
    levels_data = [
        {
            'Company': 'Google',
            'Location': 'Sunnyvale, CA',
            'Date': '2024-01-07', 
            'Level Name': 'L3',
            'Tag': 'Software',
            'YearOfExperience': '3 years',
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
    
    with patch('builtins.input', side_effect=['filter company google level l3 location CA', 'exit']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            query(levels_data)
            assert  "Company: Google" in mock_stdout.getvalue() \
                    and not "Company: Facebook" in mock_stdout.getvalue()


