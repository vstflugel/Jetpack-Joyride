import os
from colorama import init, Fore,Back
init()
def start():
    f=open("./utilities/dinasaur","r")
    dino=[]
    for i in f:
        dino.append(i)
    f.close()
    f=open("./utilities/banner","r")

    banner=[]
    for i in f:
        banner.append(i)
    f.close

    columns,rows=os.get_terminal_size()
    matrix=[]

    for i in range (rows): #rows                              
        new = []                 
        for j in range (columns): #columns  
            new.append(Back.BLACK+" "+'\x1b[0m')      
        matrix.append(new)

    for i in range(29):
        for j in range(75):
            matrix[i+5][j+65]=Back.BLACK+dino[i][j]+'\x1b[0m'

    for i in range(11):
        for j in range(48):
            matrix[i+5][j+10]=Back.BLACK+Fore.RED+banner[i][j]+'\x1b[0m'
    data=""
    data+="W:GOING UP ,A:LEFT ,D:RIGHT ,SPACE:SHOOT ,P:SHIELD ,Q:QUIT ,T:TRANSFORM ,,,PRESS 'ENTER' TO CONTINUE"

    j=0
    x=0
    for i in data:
        if i==",":
            x+=2
            j=0
        else:
            matrix[20+x][j+12]=Back.BLACK+Fore.WHITE+i+'\x1b[0m'
            j+=1

    for i in range(rows):
        for j in range(columns):
            print(matrix[i][j],end="")
        print()

    inp=input()