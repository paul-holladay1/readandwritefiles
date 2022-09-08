# avg_steps.py - using the file steps.csv, calculate the average steps taken each month. 
# Each row represents one day. Output should have the name of the month and the corresponding 
# average steps for that month (such as 'January, 5246.19')


# I would probably make a variable for each month outside of the for 
# loop, and in the for loop you can use an if statement like:
# If record[0] ==1:
#   January +=record[1]

import csv

def main():
    infile = open('steps.csv', 'r')

    file_contents = csv.reader(infile)
    
    outfile = open('avg_steps.csv', 'w')

    next(file_contents)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    i = '1'
    total = 0
    count = 0
   
    for line in file_contents:
        if line[0] == i:
            total += int(line[1])
            count += 1
        else:
            total = total/count
            outfile.write(str(months[int(i)-1]) + ',' + (str(total)) + '\n')
            i = line[0]

    total = total/count
    outfile.write(str(months[int(i)-1]) + ',' + (str(total)) + '\n') 

            

        

        
main()
