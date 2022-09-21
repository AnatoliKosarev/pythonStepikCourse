import csv
from datetime import datetime
from collections import Counter

crime_list = []

with open('Crimes.csv') as file:
    reader = csv.DictReader(file)

    for line in reader:
        date = datetime.strptime(line['Date'], '%m/%d/%Y %H:%M:%S %p')

        if date.year == 2015:
            crime_list.append(line['Primary Type'])

    result_dict = dict(Counter(crime_list))
    print(max(result_dict, key=result_dict.get))
