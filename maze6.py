#this files creates multiple maze and memorize the number of moves requested to solve it
from time import sleep
from maze4 import *
from maze5 import *
import os

if __name__=="__main__":
    n=100000
    sum=0
    percorso="primo"
    if not os.path.exists(percorso):
        os.mkdir(percorso)
    for i in range(5,7,2):
        vec=[]
        for l in range(n):
            #creating n maze and solving them
            create_maze(i)
            j=solve_maze(percorso+"/",str(i))
            vec.append(j)
            if(l%1000==0):
                sleep(5)
        #saving the n moves
        file=open("dati-"+str(i)+".txt","a")
        for j in vec:
            file.write(str(j)+"\n")
        file.close()
