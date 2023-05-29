import csv
import requests
import json
import time
filename = 'paidlist.csv'

url = 'http://example.com/api/user'

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        # The second column is at index 1 (0-based indexing)
        print(f'https://mindkraft.org/api/data/{row[2]}')
        response = requests.get(f'https://mindkraft.org/api/data/{row[2]}')
        time.sleep(3)
        