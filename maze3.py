import numpy as np
from random import randint

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

def move():
    global m,x,y,direction,win
    nx,ny=next_cell(x,y,direction)
    cell=m[nx,ny]
    print(x, y, nx, ny, cell)
    #moving  here
    if(m[x,y]!=3):
        m[x,y]=0
    m[nx, ny] = 2
    x,y=nx,ny
    if (nx == size - 1 or nx == 0 or ny==size-1 or ny == 0):
        win=True
    return
    #no possible way, go back
    print("Error in moving to next cell")
    exit()

def generate_spawn():
    #can spawn on perimeter of the maze
    #let's select randomly on which side of the maze we will spawn
    global x,y,direction
    l=randint(1,4)
    if l==1:
        #up so the box will be on x=0, y=random
        x=0
        y=randint(1,size-2)
        direction=3
    elif l==2:
        #left side x=random y=0
        x=randint(1,size-2)
        y=0
        direction=4
    elif l==3:
        #down x=size-1 y=random
        x=size-1
        y=randint(1,size-2)
        direction=1
    elif l==4:
        x=randint(1,size-2)
        y=size-1
        direction=2
    else:
        print("Error in spawning")
    return


def random_walk():
    global m, x,y,direction
    move()
    l = randint(1, 3)
    if l == 1:
        direction = right_direction(direction)
    elif l == 2:
    # no change in direction, go forward
        direction=direction
    elif l == 3:
        direction = left_direction(direction)
    else:
        print("Error in generating direction")
        exit()
    return


win=False
size=10
m=np.ones(shape=(size,size))
#initial spawn at center, position is x and y
x=size//2
y=size//2
#direction can be up, left, down, right(1,2,3,4)
direction = 1
#first time generating spawn is used to generate the arrival point
generate_spawn()
m[x,y]=4
generate_spawn()
#1 is wall, 2 is current position, 3 is start, 4 arrival
m[x,y]=3
print(m)


while(not win):
    #move to the next cell
    random_walk()
    print(m)
    #now m, position and direction are changed
m[x,y]=4
print(m)
np.savetxt("maze.txt",m)