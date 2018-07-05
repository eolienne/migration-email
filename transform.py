# Open up your terminal. Go to the transform folder on the desktop
# Run as python3 transform.py >> output.csv
# That will write the results to a csv file

import csv

input_file = 'sendy.csv'
output = 'output.csv'
emails = {}

# Step 1: Make emails contain something like
# {
#     'email1': [site1, site2, site3, ...],
#     'email2': [site1]
# }
with open(input_file, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for (email, site, _,_,_,_) in reader:
        emails.setdefault(email, []).append(site)

# Step 2: Print
for (email, sites) in emails.items():
    print(", ".join([email] + sorted(sites)))
