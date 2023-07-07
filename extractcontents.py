import pandas as pd
import email
from email.header import decode_header
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

# Read the CSV file into a DataFrame
df = pd.read_csv('combinedemails.csv')

# Create new DataFrame to store extracted data
output_df = pd.DataFrame(columns=['Username', 'Email Body'])

# Iterate over the rows of the input DataFrame
for index, row in df.iterrows():
    raw_message = row['Email Contents']
    lines = raw_message.split('\n')
    # Parse email contents and extract the body
    body = ''
    for line in lines:
        if ':' not in line:
            body+= line.strip()

    # Append the extracted body and username to the output DataFrame
    output_df = output_df.append({'Username': row['Username'], 'Email Body': body}, ignore_index=True)

# Save the output DataFrame to a new CSV file
output_df.to_csv('cleancombinedemails.csv', index=False)
