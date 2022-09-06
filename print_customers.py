import csv

infile = open('customers.csv', 'r')

csvfile = csv.reader(infile, delimiter=',')

next(csvfile)                                       #this will skip the first row

for record in csvfile:
    print('ID: ' '\t' + record[0])
    print('FName: ' '\t' + record[1])
    print('LName: ' '\t' + record[2])
    print('City: ' '\t' + record[3])
    print('Country: ' + record[4])
    print('Phone: ' '\t' + record[5])
    print()
    input()
    


