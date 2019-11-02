import numpy as np


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

def next_direction(direction):
    if direction==1:
        l=[2,4]
    elif direction==2:
        l=[3,1]
    elif direction==3:
        l=[4,2]
    elif direction==4:
        l=[1,3]
    else:
        print("Error in next direction")
        exit()
    return l

def move():
    global m,x,y,direction,win
    nx,ny=next_cell(x,y,direction)
    cell=m[nx,ny]
    print(x, y, nx, ny, cell)
    if cell==0:
        #can move here
        m[x,y]=0
        m[nx, ny] = 2
        x,y=nx,ny
        if (nx == size - 1 or nx == 0 or ny==size-1 or ny == 0):
            win=True
        return
    else:
        l = next_direction(direction)
        nx, ny = next_cell(x, y, l[0])
        cell = m[nx, ny]
        print(x, y, nx, ny, cell, l)
        if cell == 0:
            # can move here
            m[x, y] = 0
            m[nx, ny] = 2
            x, y = nx, ny
            direction = l[0]
            if (nx == size - 1 or nx == 0 or ny == size - 1 or ny == 0):
                win = True
            return
        else:
            nx, ny = next_cell(x, y, l[1])
            cell = m[nx, ny]
            print(x, y, nx, ny, cell, l)
            if cell == 0:
                # can move here
                m[x, y] = 0
                m[nx, ny] = 2
                x, y = nx, ny
                direction = l[1]
                if (nx == size - 1 or nx == 0 or ny == size - 1 or ny == 0):
                    win = True
                return
            else:
                #no possible way, go back
                print("Error in looking next cell")
                exit()

win=False
size=5
m=np.ones(shape=(size,size))
m[0,1]=0
m[1,1]=0
m[2,1]=0
#initial spawn at center, position is x and y
x=size//2
y=size//2
m[x,y]=2
print(m)
#direction can be up, left, down, right(1,2,3,4)
direction = 1
while(not win):
    #try to move to the next cell
    move()
    print(m)
    #now m, position and direction are changed