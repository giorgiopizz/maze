#python script to generate a maze with recursive backtracker with walls as cells

import numpy as np
from random import randint
import matplotlib.pyplot as plt

def next_cell(x,y, direction):
    """
    Given a position it outputs the next cell given the direction
    :return: position of the next cell
    """
    if direction==1:
        x-=1
    elif direction==2:
        y-=1
    elif direction==3:
        x+=1
    elif direction==4:
        y+=1
    else:
        print("Error in next cell direction")
        exit()
    return x,y

def left_direction(direction):
    if direction<4:
        return direction+1
    elif direction==4:
        return 1
    else:
        print("Error in left direction")
        exit()

def right_direction(direction):
    if direction>1:
        return direction-1
    elif direction==1:
        return 4
    else:
        print("Error in right direction")
        exit()

def generate_spawn(x,y,direction):
    """
    It generates a spawn point and an arrival point
    :return:
    """
    #can spawn on perimeter of the maze but not in even positions
    #let's select randomly on which side of the maze we will spawn
    l=randint(1,4)
    if l==1:
        #up so the box will be on x=0, y=random
        x=0
        # want to spawn on an odd position
        n = randint(0, size // 2 - 1)
        y = 2 * n + 1
        direction=3
    elif l==2:
        #left side x=random y=0
        n = randint(0, size // 2 - 1)
        x= 2 * n +1
        y=0
        direction=4
    elif l==3:
        #down x=size-1 y=random
        x=size-1
        n = randint(0, size // 2 - 1)
        y= 2*n+1
        direction=1
    elif l==4:
        n = randint(0, size // 2 - 1)
        x=2 * n +1
        y=size-1
        direction=2
    else:
        print("Error in spawning")
    return x,y,direction

def neighbours(x,y,direction):
    """
    It checks if there is a neighbour in a given direction or if it has reached the matrix bounds
    :return: bool
    """
    if x-2>0 and direction==1:
        #can go up
        return True
    elif y-2>0 and direction==2:
        #can go left
        return True
    elif x+2<size-1 and direction==3:
        #can go down
        return True
    elif y+2<size-1 and direction==4:
        #can go right
        return True
    else:
        return False

def remove_wall(x,y,direction,m):
    """
    It removes the wall that is between the current cell and the cell pointed by the direction
    :return:
    """
    nx,ny = next_cell(x,y,direction)
    m[nx,ny]=0
    return

def check_neighbours(x,y,unvisited,m):
    """
    This function is the core of the program.
    It checks in the four directions if there is an unvisited cell, if there are two or more
    it selects randomly one of these. If there are none it goes back popping from the stack
    the previous cells stopping when one of the cells have some unvisited neighbours.
    :return: the changed parameters
    """
    possible_cell=[]
    #found indicates wheter exist an unvisited neighbour
    found = False
    for i in range(1,5):
        #looping 3 times
        if neighbours(x,y,i):
            nx,ny=next_cell(x,y,i)
            nnx,nny= next_cell(nx,ny,i)
            cell=m[nnx,nny]
            if cell==1 or cell==-1:
                #is unvisited
                pos=[nnx,nny,i]
                possible_cell.append(pos)
                found = True
    if found:
        #choose random cell from possibles
        j=randint(0,len(possible_cell)-1)
        choosen= possible_cell[j]
        stack.append([x,y])
        #remove wall between the actual position and the choosen one
        remove_wall(x,y,choosen[2],m)
        #move to the cell
        m[x,y]=0
        unvisited-=1
        m[choosen[0],choosen[1]]=2
        x=choosen[0]
        y=choosen[1]

    else:
        #no neighbours have been found unvisited, will go back
        #let's check if the last cell has unvisited neighbours
        print("need to go back")
        found = False
        while(not found and len(stack)>0):
            last = stack.pop()
            for i in range(1, 5):
                # looping 4 times
                if neighbours(last[0], last[1], i):
                    nx, ny = next_cell(last[0], last[1], i)
                    nnx, nny = next_cell(nx, ny, i)
                    cell = m[nnx, nny]
                    if cell == 1 or cell==-1:
                        # is unvisited
                        found = True
                        break

        # move to the cell
        m[x, y] = 0
        m[last[0], last[1]] = 2
        x = last[0]
        y = last[1]

    return x, y, unvisited



def initialize(size):
    """
    This function creates and popolate the matrix of the maze
    :param size: size of the matrix(including walls and free cells)
    :return: x,y of the start position and m matrix
    """
    if size<5:
        print("Size must me greater than 5!")
        exit()
    elif size%2==0:
        print("Size must be odd!")
        exit()
    m = np.ones(shape=(size, size))
    for i in range(0, size + 1, 2):
        # orizonthal wall
        m[i, :] = 8
    for j in range(0, size + 1, 2):
        # vertical wall
        m[1:size - 1, j] = 9

    # initial spawn at center, position is x and y
    x = 0
    y = 0
    # direction can be up, left, down, right(1,2,3,4)
    direction = 0
    # first time generating spawn is used to generate the arrival point
    x, y, direction = generate_spawn(x, y, direction)
    # let's set the exit with 4
    m[x, y] = 4
    nx, ny = next_cell(x, y, direction)
    # and set the cell in front of the arrival point with -1
    m[nx, ny] = -1
    ax, ay = x, y
    # now the spawn point is generated
    x, y, direction = generate_spawn(x, y, direction)
    nx, ny = next_cell(x, y, direction)
    # check if arrival and start are the same or if the cell in front of arrival and start is the same
    while (ax == x and ay == y) or m[nx, ny] == -1:
        x, y, direction = generate_spawn(x, y, direction)
        nx, ny = next_cell(x, y, direction)
    # setting the start point
    m[x, y] = 3
    x, y = nx, ny
    # and the current position in front of the start point
    m[x, y] = 2
    return x,y,m

#8 and 9 are walls, 1 is unvisited, 2 is current position, 3 is start, 4 arrival
size=31
stack = []
x,y,m=initialize(size)
# although there are size**2 cells, only (size//2)^2 are usable and being spawned in a point means you
# start with already one cell visited
unvisited = (size // 2) ** 2 - 1

while(unvisited>0):
    #move to the next cell
    x,y,unvisited=check_neighbours(x,y,unvisited,m)
    print(m)
    #now x,y unvisited and m are changed

#it's useless to know the current position after the generation
m[x,y]=0

np.savetxt("maze2.txt",m)

# plt.figure(figsize=(10, 5))
# plt.imshow(m, cmap=plt.cm.binary, interpolation='nearest')
# plt.xticks([]), plt.yticks([])
# plt.show()