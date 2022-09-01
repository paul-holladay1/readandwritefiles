import csv

infile = open('customers.csv', 'r')

csvfile = csv.reader(infile, delimiter=',')

next(csvfile)                                       #this will skip the first row

for record in csvfile:
    print('ID: ' + record[0])
    print('FName: ' + record[1])
    print('LName: ' + record[2])
    print('City: ' + record[3])
    print('Country: ' + record[4])
    print('Phone: ' + record[5])
    print()
    input()
    


