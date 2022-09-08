#Python program that reads the employeepay.csv file and prints out details of each employee

import csv

infile = open('employeepay.csv', 'r')

csvfile = csv.reader(infile, delimiter=',')

next(csvfile)    


for record in csvfile:
    EmpID = record[0]
    FName = record[1]
    LName = record[2]
    EmpSalary = record[3]
    EmpBonus = record[4]
    TotalPay = str(int(record[3]) + (int(record[3]) * float(record[4])))
    
    print(format('ID: ', '20') + EmpID)
    print(format('First Name: ', '20') + FName)
    print(format('Last Name: ', '20') + LName)
    print(format('Salary: ', '20') + '$' + format(int(EmpSalary), '.2f'))
    print(format('Bonus: ', '20') + '$'  + format(float(EmpBonus), '.2f'))
    print(format('Total Pay: ', '20') + '$'  + format(float(TotalPay), '.2f'))
    input()
