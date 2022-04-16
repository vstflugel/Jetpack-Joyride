import os
from colorama import init, Fore,Back
init()
class Dragon_ball:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
        self.__ball=True

    def print(self,board):
        self.__prv=board[self.__y][self.__x]
        board[self.__y][self.__x]=Fore.RED + "*" + '\x1b[0m'
        return board

    def ball_move(self,x,y,board):
        if self.__ball==True:
            board[self.__y][self.__x]=" "
            columns,rows=os.get_terminal_size()

            if self.__x < x:
                self.__x +=1
            elif self.__x > x:
                self.__x -=1

            if self.__y < y:
                self.__y +=1
            elif self.__y > y:
                self.__y -=1

            if (board[self.__y][self.__x] !=" " and board[self.__y][self.__x] !=Fore.RED+ "\\" + '\x1b[0m' and board[self.__y][self.__x] !=Fore.RED+ "/" + '\x1b[0m')or board[self.__y][self.__x+1] == Fore.RED + ">" + '\x1b[0m' or board[self.__y][self.__x+2] ==Fore.RED + ">" + '\x1b[0m' or board[self.__y][self.__x+3] ==Fore.RED + ">" + '\x1b[0m' or board[self.__y][self.__x+4] ==Fore.RED + ">" + '\x1b[0m':
                self.__ball=False
                #board[self.__y][self.__x]=" "
                return -1,board
            else:
                board[self.__y][self.__x]=Fore.RED + "*" + '\x1b[0m'
                return 0,board

            

        