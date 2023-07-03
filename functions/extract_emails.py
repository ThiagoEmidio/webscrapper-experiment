import re

def extract_emails(string):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    emails = re.findall(pattern, string)
    if len(emails)==1:
        return emails[0]
    return emails
