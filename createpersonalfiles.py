import os
import re

# Create the output directory if it doesn't exist
output_dir = "cleanedemails"
os.makedirs(output_dir, exist_ok=True)

with open('part-00000', 'r') as file:
    for line in file:
        line = line.strip()
        username, text = line.split('\t', 1)  # Split by the first tab character
        
        # Extract words using regex and remove unwanted characters
        words = re.findall(r'\b\w+\b', text.replace('"', '').replace('-', ''))
        
        # Create a separate file for each username in the output directory
        filename = f"{username}.txt"
        output_path = os.path.join(output_dir, filename)
        with open(output_path, 'w') as output_file:
            for word in words:
                output_file.write(word + ' ')
