#python script to generate a maze with recursive backtracker with walls as cells

import numpy as np
from random import randint
import matplotlib.pyplot as plt
def next_cell(x,y, direction):
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
    return l
def right_direction(direction):
    if direction>1:
        return direction-1
    elif direction==1:
        return 4
    else:
        print("Error in right direction")
        exit()
    return

def generate_spawn():
    #can spawn on perimeter of the maze not in even positions
    #let's select randomly on which side of the maze we will spawn
    global x,y,direction
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
    return

def neighbours(x,y,direction):

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

def remove_wall(x,y,direction):
    global m
    nx,ny = next_cell(x,y,direction)
    m[nx,ny]=0
    return

def check_neighbours():
    global m,x,y,direction,unvisited,win
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
        remove_wall(x,y,choosen[2])
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
        return





win=False
size=27
m=np.ones(shape=(size,size))
for i in range(0,size+1,2):
    m[i,:]=8
for j in range(0,size+1,2):
    m[1:size-1,j]=9
print(m)
stack=[]
unvisited=(size//2)**2-1
#initial spawn at center, position is x and y
x=size//2
y=size//2
#direction can be up, left, down, right(1,2,3,4)
direction = 1
#first time generating spawn is used to generate the arrival point
generate_spawn()
m[x,y]=4
nx,ny=next_cell(x,y,direction)
m[nx,ny]=-1
ax,ay=x,y


generate_spawn()
nx,ny=next_cell(x,y,direction)
print(ax, x, ay, y,nx,ny)
while (ax==x and ay==y) or m[nx,ny]==-1:
    generate_spawn()
    nx, ny = next_cell(x, y, direction)
    print(ax, x, ay, y)
#1 is wall, 2 is current position, 3 is start, 4 arrival
m[x,y]=3
x,y=nx,ny
m[x,y]=2
print(m)

while(unvisited>0):
    #move to the next cell
    check_neighbours()
    print(m)
    #now m, position and direction are changed

m[x,y]=0
np.savetxt("maze2.txt",m)

plt.figure(figsize=(10, 5))
plt.imshow(m, cmap=plt.cm.binary, interpolation='nearest')
plt.xticks([]), plt.yticks([])
plt.show()