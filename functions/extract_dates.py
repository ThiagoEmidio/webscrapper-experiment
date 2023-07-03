import re

def extract_dates(string):
    pattern = r'\d{2}/\d{2}/\d{4}'  # Regular expression pattern for date in DD/MM/YYYY format
    dates = re.findall(pattern, string)
    return dates
