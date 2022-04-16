
from colorama import init, Fore,Back
import random
import os
class power_up:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y

    def print(self,board):
        for j in range(2):
            for k in range(2):
                board[self.__x+j][self.__y+k]=Fore.BLACK+Back.WHITE+"#"+'\x1b[0m'