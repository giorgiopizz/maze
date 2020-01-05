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
    direction=right_direction(direction)
    nx,ny=next_cell(x,y,direction)
    cell=m[nx,ny]
    print(x, y, nx, ny, cell)
    if cell!=1:
        #can move here
        m[x,y]=0
        m[nx, ny] = 2
        x,y=nx,ny
        if (nx == size - 1 or nx == 0 or ny==size-1 or ny == 0):
            win=True
        return
    else:
        i=0
        while(i<3):
            direction =left_direction(direction)
            nx, ny = next_cell(x, y, direction)
            cell = m[nx, ny]
            print(x, y, nx, ny, cell)
            if cell != 1:
                # can move here
                m[x, y] = 0
                m[nx, ny] = 2
                x, y = nx, ny
                if (nx == size - 1 or nx == 0 or ny == size - 1 or ny == 0):
                    win = True
                return
            else:
                i+=1
        #no possible way, go back
        print("Error in looking next cell")
        exit()

def generate_spawn():
    #can spawn on perimeter of the maze
    #let's select randomly on which side of the maze we will spawn
    l=randint(1,4)
    if l==1:
        #up so the box will be on x=0, y=random
        x=0
        y=randint(0,size-1)
    elif l==2:
        #left side x=random y=0
        x=randint(0,size-1)
        y=0
    elif l==3:
        #down x=size-1 y=random
        x=size-1
        y=randint(0,size-1)
    elif l==4:
        x=randint(0,size-1)
        y=size-1
    else:
        print("Error in spawning")
    return

def get_maze():
    global size,x,y,direction
    m=np.loadtxt("maze.txt")
    #search for start
    i,j=0,0
    for i in [0,m.shape[0]-1]:
        for j in range(1,m.shape[0]-1):
            #looking at first row i=0 and j from 1 to size-2 or last row
            cell = m[i, j]
            if cell == 3:
                x = i
                y = j
                break
    i,j=0,0
    for j in [0,m.shape[0]-1]:
        for i in range(1,m.shape[0]-1):
            #looking at first col and last col
            cell = m[i, j]
            if cell == 3:
                x = i
                y = j
                break
    size=m.shape[0]
    #need to get direction
    if x==0:
        direction=3
    elif y==0:
        direction=4
    elif x==size-1:
        direction=1
    elif y==size-1:
        direction=2

    return m

win=False

size,x,y,direction=0,0,0,0

#get maze
m=get_maze()
print(m)

while(not win):
    #try to move to the next cell
    move()
    print(m)
    #now m, position and direction are changed
