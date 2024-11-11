import csv

# Read CSV file
# CSV (Comma Seperated Values) is a simple file format used to store data tabular data, such as a spreadsheet

with open("example.csv", 'r') as file:
    csv_reader = csv.reader(file) # Generate a reader object [iterator]
    header = next(csv_reader) # Returns the next row of the reader's iterable object as a list
    for i in csv_reader: # Iterating through the reader object for the remaining rows
        print(i)

# Write CSV file
data = [
    ['name', 'age', 'city'],
    ['John Doe','45','New york'],
    ['Jane Doe','46', 'Chicago'],
    ['Tom Doe', '47', 'Los Angeles']
]

with open ("data.csv", 'w') as file:
    csv_writer = csv.writer(file) # Generates a writer object[Iterator]
    for row in data: # Iterating through the data list
        csv_writer.writerow(row) # Write each row to the csv file
