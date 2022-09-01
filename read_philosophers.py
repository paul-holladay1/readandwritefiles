# This program reads and displays the contents
# of thee philosophers.txt file
def main():
    # Open a file names philosophers.txt
    infile = open('philosophers.txt', 'r')

    # Read the file's contents.
    #file_contents = infile.read()

    # Read the file's contents
    line1 = infile.readline().rstrip('\n')                                 #string created when reading
    line2 = infile.readline().rstrip('\n')  
    line3 = infile.readline().rstrip('\n')  

    # Print the data that was read into memory.
    #print(file_contents)

    print(line1)
    print(line2)
    print(line3)
# Call the main function.
main()