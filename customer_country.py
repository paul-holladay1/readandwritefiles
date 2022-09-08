import csv
def main():
    infile = open('customers.csv', 'r')

    file_contents = csv.reader(infile)
    

    outfile = open('customer_country.csv', 'w')
    
    for line in file_contents:

        outfile.write(line[1] + ',')
        outfile.write(line[2] + ',')
        outfile.write((line[4]) + '\n')


    infile.close()
    outfile.close()


main()

    

