import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('cleancombinedemails.csv')

# Drop rows with null values in 'Username' or 'Email Body'
df.dropna(subset=['Username', 'Email Body'], inplace=True)

# Convert values to lowercase
df['Username'] = df['Username'].str.lower()
df['Email Body'] = df['Email Body'].str.lower()

# Save the modified DataFrame as a CSV file
df.to_csv('finalcleaned.csv', index=False)
