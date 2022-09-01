def main():
    infile = open('clients.txt', 'r')
    
    counter = 1

    i = 0
    for line in infile:
        print(counter,". ", line.rstrip('\n'), sep='')

        counter += 1

main()
