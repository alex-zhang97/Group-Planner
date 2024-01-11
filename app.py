import csv

# Specify the path to your CSV file
file_path = input("Please enter the path to your CSV file: ")
rankings = {}
indicies = {}

# Open the CSV file in read mode
with open(file_path, 'r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Each row is a list representing the columns in that row
        rankings[row[0]] = row[1:]
        # print(row)

    
# print(rankings)