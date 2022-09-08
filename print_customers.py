import csv

infile = open('customers.csv', 'r')

csvfile = csv.reader(infile, delimiter=',')

next(csvfile)                                       #this will skip the first row

for record in csvfile:
    print(format('ID: ', '10') + record[0])
    print(format('FName: ', '10') + record[1])
    print(format('LName: ', '10') + record[2])
    print(format('City: ', '10') + record[3])
    print(format('Country: ', '10') + record[4])
    print(format('Phone: ', '10') + record[5])
    print()
    input()
    


