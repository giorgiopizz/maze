#maze escaper script with walls as cells


import numpy as np
from random import randint
import matplotlib.pyplot as plt
import os.path
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

def move(x,y,direction,win,m):
    direction=right_direction(direction)
    nx,ny=next_cell(x,y,direction)
    cell=m[nx,ny]
    print(x, y, nx, ny, cell)
    if cell==4:
        win=True
        return x,y,direction,win
    elif cell==0:
        #can move here
        nnx,nny=next_cell(nx,ny,direction)
        m[x,y]=1
        m[nnx, nny] = 2
        x,y=nnx,nny
        return x,y,direction,win
    else:
        i=0
        while(i<3):
            direction =left_direction(direction)
            nx, ny = next_cell(x, y, direction)
            cell = m[nx, ny]
            #print(x, y, nx, ny, cell)
            if cell==4:
                win=True
                return x, y, direction, win
            elif cell == 0:
                # can move here
                nnx,nny=next_cell(nx,ny,direction)
                m[x, y] = 1
                m[nnx, nny] = 2
                x, y = nnx, nny
                return x,y,direction,win
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
    m=np.loadtxt("maze2.txt")
    #search for start
    found=False
    i,j=0,0
    for i in [0,m.shape[0]-1]:
        for j in range(1,m.shape[0]-1):
            #looking at first row i=0 and j from 1 to size-2 or last row
            cell = m[i, j]
            if cell == 3:
                x = i
                y = j
                found=True
                break
    if not found:
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

    nx, ny = next_cell(x, y, direction)
    m[nx, ny] = 2
    x, y = nx, ny
    return size,x,y,direction,m


def solve_maze(folder):
    win=False
    #get maze
    size,x,y,direction,m=get_maze()
    print(m)
    indice=0
    while(not win):
        #try to move to the next cell
        x,y,direction,win=move(x,y,direction,win,m)
        indice+=1
        #now m, position and direction are changed
    print(indice*2)

    plt.figure(figsize=(30, 30))
    plt.imshow(m, cmap=plt.cm.binary, interpolation='nearest')
    plt.xticks([]), plt.yticks([])
    base_name="maze"
    number=0
    ext_name=".png"
    while(os.path.exists(folder+base_name+str(number)+ext_name)):
        number+=1
    plt.savefig(folder+base_name+str(number)+ext_name)
    return indice*2

if __name__=="__main__":
    solve_maze("primo/")