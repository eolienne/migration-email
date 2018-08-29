# Open up your terminal. Go to the transform folder on the desktop
# Run as python3 transform.py >> output.csv
# That will write the results to a csv file

import csv

input_file = 'group.csv'
output = 'output.csv'
emails = {}

# Step 1: Make emails contain something like
# {
#     'email1': [site1, site2, site3, ...],
#     'email2': [site1]
# }
with open(input_file, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for (owner, site) in reader:
        emails.setdefault(owner, []).append(site)

# Step 2: Print
for (owner, site) in emails.items():
   print(", ".join([owner] + sorted(site)))
