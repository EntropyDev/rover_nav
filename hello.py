#!Python3 -tt 
#Copyright 2017 - Vaibhav Chimalgi 

import sys 

    
     

def main():
    filename = sys.argv[1]
    f = open(filename, 'rU')
    for line in f:
        print(line,end="")
    f.close()

# Boilerplate call function
if __name__ == '__main__':
    main()
