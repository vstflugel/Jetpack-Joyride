from Obstacle import Obstacle_horizontal
from Obstacle import Obstacle_vertical
from Obstacle import Obstacle_slant_1
from Obstacle import Obstacle_slant_2
from coins import coins
from Power_up import power_up

from colorama import init, Fore,Back,Style
import random
import os
init()
class Scenery:
    def __init__(self):
        self.__ground_atom=Back.GREEN + Fore.BLACK + " " + '\x1b[0m'
        self.__cloud=[]
        self.__obs=[]
        self.__num=6
    
    def create_ground(self,rows,columns,board):
        for i in range(columns):
            board[rows-2][i]=Fore.GREEN+Style.BRIGHT+"V"+'\x1b[0m'
            board[rows-1][i]= self.__ground_atom #Fore.RED + "_" + '\x1b[0m'

        return board

    def create_sky(self,rows,columns,board):
        for i in range(columns):
            board[5][i]=Fore.CYAN + Style.BRIGHT + "X" + '\x1b[0m'

        return board
   
    def create_clouds(self,board):
        f=open("./utilities/clouds","r")
        for i in f:
            self.__cloud.append(i)
        for k in range(0,500,50):    
            for i in range(4):
                for j in range(16):
                    board[6+i][k+j] = Style.BRIGHT + self.__cloud[i][j] + '\x1b[0m'

        return board
    
    def create_coins(self,rows,columns,board):
        num=10
        for i in range(num):
            tmp=int((columns-10)/num)
            y=random.randint(tmp*i+3,(tmp*(i+1))-2)
            x=random.randint(15,rows-15)
            obj=coins(x,y)
            obj.print(board)

        return board

    def create_powerup(self,rows,columns,board):
       
        num=2 
        for i in range(num):
            tmp=int((columns-10)/num)
            y=random.randint(tmp*i+3,(tmp*(i+1))-2)
            x=random.randint(15,rows-15)
            obj=power_up(x,y)
            obj.print(board)

        return board

    def create_obstacles(self,board):
        columns,rows=os.get_terminal_size()
        for i in range(self.__num+4):
            tmp=int(460/(self.__num+4))
            y=random.randint(tmp*i+5,tmp*(i+1)-3)
            x=random.randint(rows-9,rows-7)
            obj_obs=Obstacle_vertical(y,x)
            obj_obs.generate()
            self.__obs.append(obj_obs)
        
        for i in range(20,450,50):
            # y=random.randint(tmp*i+5,tmp*(i+1)-3)
            x=random.randint(6,8)
            obj_obs=Obstacle_vertical(i,x)
            obj_obs.generate()
            self.__obs.append(obj_obs)
        
        for i in range(self.__num):
            tmp=int(460/self.__num)
            y=random.randint(tmp*i+3,tmp*(i+1)-3)
            x=random.randint(9,rows-9)
            obj_obs=Obstacle_horizontal(y,x)
            obj_obs.generate()
            self.__obs.append(obj_obs)
        
        for i in range(self.__num-2):
            tmp=int(460/self.__num-2)
            y=random.randint(tmp*i+3,tmp*(i+1)-3)
            x=random.randint(9,rows-16)
            obj_obs=Obstacle_slant_1(y,x)
            obj_obs.generate()
            self.__obs.append(obj_obs)
        
        for i in range(self.__num-2):
            tmp=int(460/self.__num-2)
            y=random.randint(tmp*i+3,tmp*(i+1)-3)
            x=random.randint(15,rows-8)
            obj_obs=Obstacle_slant_2(y,x)
            obj_obs.generate()
            self.__obs.append(obj_obs)

        for i in self.__obs:
            i.print(board)

        return board

    def check_obstacle_bullet_collision(self,board):
        score=0
        for f in self.__obs:
           tmp,board,tmpo= f.check_bullet(board)
           score+=tmp
           if tmpo == -1:
               self.__obs.remove(f)
        return score,board

    def create_deadwall(self,board):
        columns,rows=os.get_terminal_size()
        chk=1
        for i in range(6,rows):
            if chk==1:
                board[i][500-28]= Fore.RED+ "\\" + '\x1b[0m'
                chk=2
            else:
                board[i][500-28]= Fore.RED + "/" + '\x1b[0m'
                chk=1

        return board