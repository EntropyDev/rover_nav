# rover_nav

A squad of robotic rovers are to be landed by NASA on a plateau on
Mars. This plateau, which is curiously rectangular, must be navigated
by the rovers so that their on-board cameras can get a complete view of
the surrounding terrain to send back to Earth.  
 *This module finds final co-ordinates and heading for each rover.* 

## Getting Started


### Prerequisites

You need to have Python3 installed.

### How to run

1. Move to `rover_nav` directory.
2. Create a text file named `input.txt` with input in following format. 

*The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0, 0.*  

*The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover's position, and the second line is a series of instructions telling the rover how to explore the plateau.*  

 *The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover's orientation.*  
 
 *Each rover will be finished sequentially, which means that the second rover won't start to move until the first one has finished moving.*
```
5 8
1 2 N
LMLMLMLLLLLLLLLLLLLMM
3 3 E
MMRMMRMRRMRRRRRRRRRRRR
```
3. Open terminal in the directory and run the `main.py`

```
> python main.py input.txt  
 1 3 N
 5 1 E
```

## Running the tests

Run the tests for the module from the `test.py` using `nose`

```
> pip install nose  
> nosetests -v  
 test_move (test.TestCaseMove) ... ok
 test_move_off_edge (test.TestCaseMove) ... ok
 test_turning_left (test.TestCaseTurn) ... ok
 test_turning_right (test.TestCaseTurn) ... ok
 test_filename (test.TestMain) ... ok
 test_main_input (test.TestMain) ... ok
 test_rover (test.TestRover) ... ok
 test_rover_inst (test.TestRover) ... ok
 ----------------------------------------------------------------------
 Ran 8 tests in 0.022s

 OK

```

### And coding style tests

Test the files for coding style with PEP8 Style Guidelines using `pycodestyle`

```
> pip install pycodestyle  

> pycodestyle main.py

> pycodestyle test.py
```

## Built With

* Python3

## Authors

* **Vaibhav Chimalgi** - [EntropyDev](https://github.com/EntropyDev)
