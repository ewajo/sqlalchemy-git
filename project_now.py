
import csv


with open ("clean_stations.csv", newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(', '.join(row))

with open('plik.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['John', 'Doe', 'john.doe@example.com'])

