import os
from colorama import init, Fore,Back
init()
columns,rows=os.get_terminal_size()
def end(type,score,str):
    if type==1:
        f=open("./utilities/hitman","r")
        dino=[]
        for i in f:
            dino.append(i)
        f.close()
        f=open("./utilities/won","r")
        won=[]
        for i in f:
            won.append(i)
        f.close()

        matrix=[]

        for i in range (rows): #rows                              
            new = []                 
            for j in range (columns): #columns  
                new.append(Back.BLACK+" "+'\x1b[0m')      
            matrix.append(new)

        for i in range(39):
            for j in range(46):
                matrix[i][j+5]=Back.BLACK+dino[i][j]+'\x1b[0m'

        for i in range(5):
            for j in range(46):
                matrix[i+5][j+70]=Back.BLACK+won[i][j]+'\x1b[0m'

        data="YOU HITMAN OR SOMETHING ??!!"
        data+=",,SCORE:"
        data+=(score)
        data+=",,PRESS 'ENTER' TO CONTINUE"
        j=0
        x=0
        for i in data:
            if i==",":
                x+=2
                j=0
            else:
                matrix[20+x][j+90]=Back.BLACK+Fore.WHITE+i+'\x1b[0m'
                j+=1
        for i in range(rows):
                for j in range(columns):
                    print(matrix[i][j],end="")
                print()

        inp=input()
        os.system('ps -ef | grep mpg | grep -v grep | awk \'{print $2}\' | xargs kill')
        exit(0)
    else:
        matrix=[]

        for i in range (rows): #rows                              
            new = []                 
            for j in range (columns): #columns  
                new.append(Back.BLACK+" "+'\x1b[0m')      
            matrix.append(new)
        f=open("./utilities/lose","r")
        dino=[]
        for i in f:
            dino.append(i)
        f.close()
       
        f=open("./utilities/fun","r")
        fun=[]
        for i in f:
            fun.append(i)
        f.close()

        for i in range(5):
            for j in range(48):
                matrix[i+5][j+80]=Back.BLACK+Fore.RED+dino[i][j]+'\x1b[0m'

        for i in range(24):
            for j in range(79):
                matrix[i+10][j]=Back.BLACK+fun[i][j]+'\x1b[0m'
        data=""
        data+=str
        data+=",SCORE:"
        data+=score
        data+=",,,PRESS 'ENTER' TO CONTINUE"
        j=0
        x=0
        for i in data:
            if i==",":
                x+=2
                j=0
            else:
                matrix[20+x][j+82]=Back.BLACK+Fore.WHITE+i+'\x1b[0m'
                j+=1

        for i in range(rows):
            for j in range(columns):
                print(matrix[i][j],end="")
            print()
        inp=input()
        os.system('ps -ef | grep mpg | grep -v grep | awk \'{print $2}\' | xargs kill')
        exit(0)