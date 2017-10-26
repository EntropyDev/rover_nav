#!Python3 -tt 
#Copyright 2017 - Vaibhav Chimalgi 


import sys 


dir_ = ['N', 'E', 'S', 'W']

def turnLeft(pos):
	i = dir_.index(pos[4])
	pos[4] = dir_[i-1]

def turnRight(pos):
	i = dir_.index(pos[4])
	pos[4] = dir_[(i+1)%4]

def move(pos):
	if(pos[4] == 'N'):
		pos[2] += 1
	elif(pos[4] == 'E'):
		pos[0] += 1
	elif(pos[4] == 'S'):
		pos[2] -= 1
	elif(pos[4] == 'W'):
		pos[0] -= 1



def rover(pos,nav_inst_list):
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
    filename = sys.argv[1]
    f = open(filename, 'rU')
    toprightX = f.readline(1)
    toprightY = f.readline(2)
    for line in f:
    	txt = f.read()
    f.close()
    list_inst = txt.split('\n');
    for i in range(0,len(list_inst),2):
    	pos = list(list_inst[i])
    	nav_inst_list = list(list_inst[i+1])
    	pos[0] = int(pos[0])
    	pos[2] = int(pos[2])
    	rover(pos,nav_inst_list)

# Boilerplate call function
if __name__ == '__main__':
    main()
