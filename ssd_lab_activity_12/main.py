import sys
from math import *
from datetime import datetime

def helper(matrix, tarray):
    lfoot,rfoot,ileft,iright = (),(),(),()

    itime,ftime,dleft,dright = 0,0,0,0


    for (ir, row) in enumerate(matrix):
        for (ic, col) in enumerate(row):
            lenlfoot=len(lfoot)
            lenrfoot=len(rfoot)
            if lenlfoot == 0 and lenrfoot == 0 and len(row) != 0:
                lfoot,ileft = col,col
            
                itime = tarray[ir]
                break
        
        
            elif lenrfoot:
                if col[0] not in range(rfoot[0] - 3, rfoot[0] + 4):
                    myans0=(col[0] - lfoot[0])
                    myans0=myans0 ** 2
                    myans1=(col[1] - lfoot[1])
                    mans1=myans1 ** 2
                    myans2=sqrt(myans0 + myans1)
                    dleft =dleft+ myans2
                    lfoot = col
                    if ftime == 0:
                        ftime = tarray[ir]
                else:
                    rfoot = col
                break
            elif lenlfoot != 0 and lenrfoot == 0 and col[0] != lfoot[0]:
                rfoot,iright = col,col
            
                break
        
            elif lenlfoot:
                if col[0] not in range(lfoot[0] - 3, lfoot[0] + 4):
                    myans0=(col[0] - rfoot[0])
                    myans0=myans0 ** 2
                    myans1=(col[1] - rfoot[1])
                    myans1=myans1 ** 2
                    myans2=sqrt(myans0 + myans1)
                    dright =dright+ myans2
                    rfoot = col
                else:
                    lfoot = col
                break
            elif col[0] != 0:
                break
    

    format = '%H:%M:%S.%f'
    p1,p2 = datetime.strptime(ftime, format),datetime.strptime(itime, format)
    p3=(p1 - p2).total_seconds()
    print("Stride length is:", dleft)
    print("Stride velocity is:", dleft / p3, "units")
    print("Cadence is:", 120 / p3);


def inputReading(n):
    matrices,tarray,l = [],[],[]

    row,col,mcount =0,0,0

    f=open('input.txt', 'r')
    rown,row = 0,[]
    for myline in f:
        inter=len(myline)
        if  inter!= 1:
            myline = myline.strip()
            fs = myline.split('\t')
            fi = fs[0]
            fs = fs[1:]
            medianline=20
            for idx, val in enumerate(fs):
                if val != '0':
                    row.append((rown, idx))
                
            
            if(rown == medianline):
                 tarray.append(fi)
            
            rown =rown+ 1
        else:
            matrices.append(row)
            row,rown = [],0
    if n == 2:
        
        
        mymatrix=[]
        mymatrix.append(matrices[8])
        mymatrix.append(matrices[9])
        mymatrix.append(matrices[16])
        mytarray=[]
        mytarray.append(tarray[8])
        mytarray.append(tarray[9])
        mytarray.append(tarray[16])
        matrices=mymatrix
        tarray=mytarray
        
    
    f.close()
    return (matrices, tarray)
        
    

def processingArguments(arguments):
    matrix,tarray = [],[]
    qn = arguments[1]

    if qn == "q1":
        matrix, tarray = inputReading(1)
    elif qn == "q2":
        matrix, tarray = inputReading(2)
    else:
        print("Invalid question number")

    helper(matrix, tarray)

if __name__ == "__main__":
    
    if len(sys.argv)>=2:
        processingArguments(sys.argv)
    else:
        raise ValueError('Incorrect number of arguments')
    