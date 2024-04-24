import csv

def manipulate_data():
    with open('data.csv', 'r') as file:
        for line in file:
            line = line.strip()
            columns = line.split(',')
            print(columns)

manipulate_data()
