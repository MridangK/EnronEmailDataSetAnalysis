#!/usr/bin/env python3
import sys

# Initialize variables
current_user = None
email_contents = []

# Read input from the mapper
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Parse the input from the mapper
    user, content = line.split('\t',1)

    # Check if the user has changed
    if current_user != user:
        # Output the result for the previous user
        if current_user is not None:
            # Write the email contents to a separate file for the current user
            print(current_user,'\t',email_contents)

        # Update the current user and clear email contents
        current_user = user
        email_contents = []

    # Add the content to the email contents list
    email_contents.append(content)

# Output the result for the last user
if current_user is not None:
    print(current_user,'\t',email_contents)