import os
import csvkit

directory = os.getcwd()
for file in os.listdir(directory):
    if file.endswith(".csv"):
        with open(file, 'r', encoding='latin-1') as csvfile:
            reader = csvkit.py3.CSVKitDictReader(csvfile)
            fieldnames = reader.fieldnames
            nebFile = open('nebraska.csv', 'a')
            writer = csvkit.py3.CSVKitDictWriter(nebFile, fieldnames = fieldnames)
            #writer.writeheader()
            #break
            for row in reader:
                if row['STATE'] == 'NEBRASKA':
                    writer.writerow(row)
