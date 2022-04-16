import os
from colorama import init, Fore,Back
init()
class Bullet:

    def __init__(self,x,y,stage):
        self.__bul_x = x+1
        self.__bul_y = y
        self.__bul=True

    def print(self,board):
        self.__prv=board[self.__bul_y][self.__bul_x+1]
        board[self.__bul_y][self.__bul_x]=Fore.RED + ">" + '\x1b[0m'
        return board

    def bul_move(self,stage,board):
        
        columns,rows=os.get_terminal_size()
        ret=0
        if self.__bul==True:
            if self.__bul_x + 4 >= columns+stage or board[self.__bul_y][self.__bul_x+4]==Fore.WHITE+Back.RED+"*"+'\x1b[0m' or board[self.__bul_y][self.__bul_x + 1]==Fore.WHITE+Back.RED+"*"+'\x1b[0m' or board[self.__bul_y][self.__bul_x + 2]==Fore.WHITE+Back.RED+"*"+'\x1b[0m' or board[self.__bul_y][self.__bul_x + 3]==Fore.WHITE+Back.RED+"*"+'\x1b[0m' or self.__bul_x > 500 -28 and board[self.__bul_y][self.__bul_x+3]!=" ": #or board[self.__bul_y][self.__bul_x + 4]==Fore.WHITE+Back.RED+"*"+'\x1b[0m':
                self.__bul = False

            else:
                board[self.__bul_y][self.__bul_x]=self.__prv
                self.__bul_x+=4
                if board[self.__bul_y][self.__bul_x] != Fore.WHITE+Back.RED+"*"+'\x1b[0m' and board[self.__bul_y][self.__bul_x] != Fore.RED+"*"+'\x1b[0m':
                    self.__prv=board[self.__bul_y][self.__bul_x]
                else:
                    self.__prv=" "

                board[self.__bul_y][self.__bul_x]=Fore.RED + ">" + '\x1b[0m'

        else:
            board[self.__bul_y][self.__bul_x]=self.__prv
            ret=-1
        
        return board,ret
        


# board[self.__bul_y][self.__bul_x] == Fore.WHITE+Back.RED+"*"+'\x1b[0m'or board[self.__bul_y][self.__bul_x+1] == Fore.WHITE+Back.RED+"*"+'\x1b[0m'or board[self.__bul_y][self.__bul_x+2] == Fore.WHITE+Back.RED+"*"+'\x1b[0m'or board[self.__bul_y][self.__bul_x-1] == Fore.WHITE+Back.RED+"*"+'\x1b[0m'or board[self.__bul_y][self.__bul_x -2] == Fore.WHITE+Back.RED+"*"+'\x1b[0m'
    