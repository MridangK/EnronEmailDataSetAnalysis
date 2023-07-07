import os
import csv

def convert_to_csv(root_folder, output_csv):
    # Open the output CSV file in write mode
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Username', 'Email Type', 'Email Contents'])  # Write the header row

        # Iterate over the usernames in the root folder
        for username in os.listdir(root_folder):
            username_folder = os.path.join(root_folder, username)
            if not os.path.isdir(username_folder):
                continue

            # Iterate over the sent_items in the username folder
            email_type_folder = os.path.join(username_folder, 'sent_items')
            if not os.path.isdir(email_type_folder):
                continue

            # Iterate over the email files in the email type folder
            for email_file in os.listdir(email_type_folder):
                email_file_path = os.path.join(email_type_folder, email_file)
                if os.path.isdir(email_file_path):
                    continue

                # Open each email file and read its contents
                with open(email_file_path, 'r', encoding="ISO-8859-1") as email:
                    email_contents = email.read()

                # Write the username, email type, and email contents to the CSV file
                writer.writerow([username, 'sent_items', email_contents])

root_folder = '/home/mridang/Downloads/maildir'
output_csv = '/home/mridang/Downloads/finals/combinedemails.csv'

convert_to_csv(root_folder, output_csv)