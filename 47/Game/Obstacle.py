from colorama import init, Fore,Back
init()
class Obstacle_horizontal:
    def __init__(self,x,y):
        self._xi=x
        self._yi=y
        self._x=[]
        self._y=[]
        self._state=True
    
    def generate(self):    
        for i in range(self._xi,self._xi+6):
            self._x.append(i)
        for j in range(5):
            self._y.append(self._yi)
        

    def check_bullet(self,board):
        ret =0 
        ret2=0
        if self._state==True:
            for (i,j) in zip (self._x,self._y):
                for k in range(-4,0):
                    if board[j][i+k]==Fore.RED + ">" + '\x1b[0m':
                        self._state=False
                        ret=5
            
        else:
            board=self.delete(board)
            ret2=-1
        return ret,board,ret2

    def delete(self,board):
        for (t,q) in zip(self._x ,self._y):
            board[q][t]=" "
        return board

    def print(self,board):
        for (j,i) in zip(self._x ,self._y):
            board[i][j]=Fore.WHITE+Back.RED+"*"+'\x1b[0m'


class Obstacle_slant_2(Obstacle_horizontal):
    def __init__(self,x,y):
        self._xi=x
        self._yi=y
        self._x=[]
        self._y=[]
        self._state=True
        
    def generate(self):    
        for i in range(self._xi,self._xi+6):
            self._x.append(i)
        for j in range(self._yi,self._yi-6,-1):
            self._y.append(j)

class Obstacle_vertical(Obstacle_horizontal):
    def __init__(self,x,y):
        self._xi=x
        self._yi=y
        self._x=[]
        self._y=[]
        self._state=True

    def generate(self):
        for i in range(5):
            self._x.append(self._xi)
        for j in range(self._yi,self._yi+6):
            self._y.append(j)

class Obstacle_slant_1(Obstacle_horizontal):
    def __init__(self,x,y):
        self._xi=x
        self._yi=y
        self._x=[]
        self._y=[]
        self._state=True
        
    def generate(self):    
        for i in range(self._xi,self._xi+6):
            self._x.append(i)
        for j in range(self._yi,self._yi+6):
            self._y.append(j)