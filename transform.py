# Open up your terminal. Go to the transform folder on the desktop
# Run as python3 transform.py >> output.csv
# That will write the results to a csv file

import csv

input_file = 'master-project.csv'
output = 'output.csv'
emails = {}

# Step 1: Make emails contain something like
# {
#     'email1': [site1, site2, site3, ...],
#     'email2': [site1]
# }
with open(input_file, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for (sd_owner, prod_url, _,_,_,_,_,) in reader:
        emails.setdefault(sd_owner, []).append(prod_url)

#This section doesn't seem to do anything. Does it need to?
# Step 2: Print
for (sd_owner, prod_url) in emails.items():
   print(", ".join([sd_owner] + sorted(prod_url)))
