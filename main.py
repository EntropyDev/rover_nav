#! Python3 - PEP8 Style Guide -tt
# Copyright 2017 - Vaibhav Chimalgi
""" A squad of robotic rovers are to be landed by NASA on a plateau on
Mars. This plateau, which is curiously rectangular, must be navigated
by the rovers so that their on-board cameras can get a complete view of
the surrounding terrain to send back to Earth.
This module finds final co-ordinates and heading for each rover. """


import sys
import re


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


def move(pos, toprightX, toprightY):
    try:
        if(pos[0] < 0 or pos[2] < 0 or
           pos[0] > toprightX or
           pos[2] > toprightY):
                raise ValueError('Rover co-ordinates on edge !!')
    except ValueError as err:  # Edge case exception handling
        print(err.args)
        sys.exit(1)
    else:
        # Change the coordinate according to the direction
        if(pos[4] == 'N'):
            pos[2] += 1
        elif(pos[4] == 'E'):
            pos[0] += 1
        elif(pos[4] == 'S'):
            pos[2] -= 1
        elif(pos[4] == 'W'):
            pos[0] -= 1


def rover(pos, nav_inst_list, toprightX, toprightY):
    # For each instruction call respective methods
    while(nav_inst_list):
        inst = nav_inst_list.pop(0)
        if(inst == 'L'):
            turnLeft(pos)
        elif(inst == 'R'):
            turnRight(pos)
        elif(inst == 'M'):
            move(pos, int(toprightX), int(toprightY))
    res = ''.join(str(e) for e in pos)
    print(res)  # Print the final coordinate


def main():
    # Get input from file
    filename = sys.argv[1]
    try:
        f = open(filename, 'rU')
    except FileNotFoundError:
        print('File not found Error.')
    else:
        # Setting the top-right coordinates
        toprightX = f.readline(1)
        toprightY = f.readline(2)
        try:
            m = re.match("(^\d\s\d)", toprightX+toprightY)
            if not m:
                raise ValueError('The top line should be coordinates')
        except ValueError as err:
            print(err.args)
        else:
            # Reading the rest of the lines
            for line in f:
                txt = f.read()
            f.close()
            all_inst = txt.split('\n')

            for i in range(0, len(all_inst), 2):
                # Converting strings into lists
                pos = list(all_inst[i])
                nav_inst_list = list(all_inst[i+1])
                try:
                    m = re.match("(^\d\d[N,E,S,W])", all_inst[i][0]
                                 + all_inst[i][2]
                                 + all_inst[i][4])
                    if not m:
                        raise ValueError('The initial co-ordinates'
                                         'error')
                except ValueError as err:
                    print(err.args)
                try:
                    m = re.match("(^[L,R,M]+)", all_inst[i+1])
                    if(m.group() != all_inst[i+1]):
                        raise ValueError('The instructions error')
                except ValueError as err:
                    print(err.args)
                else:
                    # Converting the coordinates in pos to integers
                    pos[0] = int(pos[0])
                    pos[2] = int(pos[2])
                    # Calling the rover for execution
                    rover(pos, nav_inst_list, toprightY, toprightY)

# Standard boilerplate to call the main() function to begin
# the program
if __name__ == '__main__':
    main()