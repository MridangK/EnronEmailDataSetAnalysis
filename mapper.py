#!/usr/bin/env python3
'''mapper.py'''

import sys


# Read input from standard input (stdin) line by line
for line in sys.stdin:
    # Remove leading and trailing whitespace from the input line
    line = line.strip()
    
    # Split the line into username and email_body using a comma as the delimiter
    username, email_body = line.split(',',1)
    
    # Skip the header line
    if email_body == 'Email Body':
        continue

    print(username,'\t',email_body)
