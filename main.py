#! Python3 - PEP8 Style Guide -tt
# Copyright 2017 - Vaibhav Chimalgi
""" A squad of robotic rovers are to be landed by NASA on a plateau on
Mars. This plateau, which is curiously rectangular, must be navigated
by the rovers so that their on-board cameras can get a complete view of
the surrounding terrain to send back to Earth.
This module finds final co-ordinates and heading for each rover. """


import sys


# A list of directions in clockwise order
dir_ = ['N', 'E', 'S', 'W']


def turnLeft(pos):
    # Find the position of current direction from dir_
    i = dir_.index(pos[4])
    pos[4] = dir_[i-1]  # Change the direction after a left turn


def turnRight(pos):
    # Find the position of current direction from dir_
    i = dir_.index(pos[4])
    pos[4] = dir_[(i+1) % 4]  # Change the direction after a right turn


def move(pos):
    # Change the coordinate according to the direction
    if(pos[4] == 'N'):
        pos[2] += 1
    elif(pos[4] == 'E'):
        pos[0] += 1
    elif(pos[4] == 'S'):
        pos[2] -= 1
    elif(pos[4] == 'W'):
        pos[0] -= 1


def rover(pos, nav_inst_list):
    while(nav_inst_list):
        inst = nav_inst_list.pop(0)
        if(inst == 'L'):
            turnLeft(pos)
        elif(inst == 'R'):
            turnRight(pos)
        elif(inst == 'M'):
            move(pos)
    res = ''.join(str(e) for e in pos)
    print(res)


def main():
    # Get input from file
    filename = sys.argv[1]
    f = open(filename, 'rU')
    # Setting the top-right coordinates
    toprightX = f.readline(1)
    toprightY = f.readline(2)
    # Reading the rest of the lines
    for line in f:
        txt = f.read()
    f.close()
    all_inst = txt.split('\n')
    for i in range(0, len(all_inst), 2):
        # Converting strings into lists
        pos = list(all_inst[i])
        nav_inst_list = list(all_inst[i+1])
        # Converting the coordinates in pos to integers
        pos[0] = int(pos[0])
        pos[2] = int(pos[2])
        rover(pos, nav_inst_list)  # Calling the rover for execution


# Standard boilerplate to call the main() function to begin
# the program
if __name__ == '__main__':
    main()
