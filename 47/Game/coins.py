from colorama import init, Fore,Back,Style
import random
import os
init()
class coins():
    
    def __init__(self,x,y):
        self.__x=x
        self.__y=y

    def print(self,board):
        for i in range(5):
            for j in range(self.__y,self.__y+5):
                board[self.__x][j]= Fore.LIGHTYELLOW_EX+ Style.BRIGHT +"$"+'\x1b[0m'