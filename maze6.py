#this files creates multiple maze and memorize the number of moves requested to solve it

from maze4 import *
from maze5 import *
import os

if __name__=="__main__":
    vec=[]
    n=3
    sum=0
    percorso="primo"
    if not os.path.exists(percorso):
        os.mkdir(percorso)
    for i in range(5,11,2):
        for _ in range(n):
            create_maze(i)
            j=solve_maze(percorso+"/")
            sum+=j
        elm=[i,sum/n]
        vec.append(elm)
    file=open("dati.txt","a")
    for elm in vec:
        file.write(str(elm[0])+", "+str(elm[1])+"\n")
    file.close()
