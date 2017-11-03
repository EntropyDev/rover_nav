#! Python3 - PEP8 Style Guide -tt
""" A squad of robotic rovers are to be landed by NASA on a plateau on
Mars. This plateau, which is curiously rectangular, must be navigated
by the rovers so that their on-board cameras can get a complete view of
the surrounding terrain to send back to Earth.

This module finds final co-ordinates and heading for each rover.

Author : Vaibhav Chimalgi
Created : October 2017 """


import sys
import re
import os


# A list of directions in clockwise order
dir_ = ['N', 'E', 'S', 'W']


def turnLeft(cur_dir):
    # Find the position of current direction from dir_
    i = dir_.index(cur_dir)
    return dir_[i-1]  # Return the direction after a left turn


def turnRight(cur_dir):
    # Find the position of current direction from dir_
    i = dir_.index(cur_dir)
    return dir_[(i+1) % 4]  # Return the direction after a right turn


def move(pos, toprightX, toprightY):
    # Change the coordinate according to the direction
    if(pos[4] == 'N' and pos[2] < toprightY):
        pos[2] += 1
        return pos[2]
    elif(pos[4] == 'E' and pos[0] < toprightX):
        pos[0] += 1
        return pos[0]
    elif(pos[4] == 'S' and pos[2] > 0):
        pos[2] -= 1
        return pos[2]
    elif(pos[4] == 'W' and pos[0] > 0):
        pos[0] -= 1
        return pos[0]
    else:
        raise ValueError('Rover co-ordinates are on the '
                         'edge !!. Cannot move off the edge')


def rover(pos, nav_inst_list, toprightX, toprightY):
    # For each instruction call respective methods
    while(nav_inst_list):
        try:
            inst = nav_inst_list.pop(0)
            if(inst == 'L'):
                pos[4] = turnLeft(pos[4])
            elif(inst == 'R'):
                pos[4] = turnRight(pos[4])
            elif(inst == 'M'):
                move(pos, int(toprightX), int(toprightY))
        except ValueError as err:
            print(err.args)
            return
    res = ''.join(str(e) for e in pos)
    return res  # return the final co-ordinates


def main(filename):
    # Get input from file
    try:
        f = open(os.getcwd()+"/"+filename, 'rU')
    except FileNotFoundError:
        print('File not found Error.')
    else:
        # Setting the top-right co-ordinates
        toprightX = f.readline(1)
        toprightY = f.readline(2)
        # Checking for input format - Top Right Co-ordinates
        try:
            m = re.match("(^\d\s\d)", toprightX + toprightY)
            if not m:
                raise ValueError('The top line should have '
                                 'integer coordinates')
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
                # Checking for input format - Starting Co-ordinate
                try:
                    m = re.match("(^\d\d[N,E,S,W])", all_inst[i][0]
                                 + all_inst[i][2]
                                 + all_inst[i][4])
                    if not m:
                        raise ValueError('The start co-ordinates '
                                         'of the rover must be '
                                         'in the format 2 3 E')
                except ValueError as err:
                    print(err.args)
                # Checking for input format - Rover Instructions
                try:
                    m = re.match("(^[L,R,M]+)", all_inst[i+1])
                    if(m.group() != all_inst[i+1]):
                        raise ValueError('The instructions must '
                                         'contain only one of these '
                                         'characters (L,R,M)')
                except ValueError as err:
                    print(err.args)
                else:
                    # Converting the co-ordinates in pos to integers
                    pos[0] = int(pos[0])
                    pos[2] = int(pos[2])
                    # Calling the rover method for execution
                    res = rover(pos, nav_inst_list,
                                toprightY, toprightY)
                    print(res)


# Standard boilerplate to call the main() function to begin
# the program
if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
