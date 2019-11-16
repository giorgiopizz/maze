import sys
if len(sys.argv)<2:
    print("Bisogna passare un file")
else:
    M=0
    m=sys.maxsize
    file=open(sys.argv[1],"r")
    line=file.readline()
    while line:
        if(int(line)<m):
            m=int(line)
        if(int(line)>M):
            M=int(line)
        line=file.readline()

    file.close()
    print("Max e min: {}, {}".format(M,m))
