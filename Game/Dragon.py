from Dragon_ball import Dragon_ball
import time
import os
from colorama import init, Fore,Back,Style
class Dragon:
    def __init__(self,rows,columns):
        self.__shape=[]
        with open("./utilities/dragon") as dragon:
            for line in dragon:
                self.__shape.append(line.strip("\n"))
        # f=open("utilities/dragon","r")
        # for i in f:
        #     self.__shape.append(i)
        self.__x=columns-26 
        self.__y=rows-20 
        self.__strt=time.time()
        self.__bal_arr=[]
        self.__lives=10
        self.__last_hit=time.time()
    
    def place_dragon(self,rows,columns,board):
        for i in range(0,25):
            for j in range(0,15):
                board[self.__y+j][self.__x+i]=self.__shape[j][i]

        return board

    def move_dragon(self,dir,rows,columns,board):

        for i in range(0,25):
            for j in range(0,15):
                board[self.__y+j][self.__x+i]=" "

        if dir=="up" and self.__y>5:    
            self.__y-=1
        elif dir=="down" and self.__y < rows-17:
            self.__y+=1

        for i in range(0,25):
            for j in range(0,15):
                board[self.__y+j][self.__x+i]=self.__shape[j][i]

        return board

    
    def dragon_follow(self,y,rows,columns,board):
        ret =board
        if y - self.__y > 8:
            ret=self.move_dragon("down",rows,columns,board)
        elif self.__y-y > 0:
            ret=self.move_dragon("up",rows,columns,board)

        return ret

    def shoot(self,x,y,board):
        columns,rows=os.get_terminal_size()
        if x > 500 - columns +3 and time.time()-self.__strt>2:
            obj=Dragon_ball(self.__x,self.__y+8)
            board=obj.print(board)
            self.__bal_arr.append(obj)
            self.__strt=time.time()

        return board

    def follow(self,x,y,board):
        for i in self.__bal_arr:
            tmp,board = i.ball_move(x,y,board)
            if  tmp== -1:
                self.__bal_arr.remove(i)

        return board

        

    def check_hit(self,board):
        for i in range(0,25):
            for j in range(0,15):
                if board[self.__y+j][self.__x+i]==Fore.RED + ">" + '\x1b[0m' and time.time() - self.__last_hit > 0.5:
                    self.__lives-=1
                    self.__last_hit=time.time()

    def get_lives(self):
        return self.__lives
