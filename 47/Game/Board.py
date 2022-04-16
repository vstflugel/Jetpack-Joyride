import numpy as np
from colorama import init, Fore,Back
init()
class Board:

    def __init__(self,rows,columns):
        self.__rows=rows
        self.__columns = columns
        self.__matrix = []
        self.str=""
        for i in range (self.__rows): #rows                              
            self.__new = []                 
            for j in range (self.__columns): #columns  
                self.__new.append(" ")      
            self.__matrix.append(self.__new)


    def print_board(self,start_pos,screen_width):
        if start_pos+screen_width<500:      
            for i in range(self.__rows):
                for j in range(start_pos , start_pos + screen_width):
                    # print(self.matrix[i][j] , end="")
                    self.str+=self.__matrix[i][j]
                # print()
                #self.str+="\n"
                print(self.str)
                self.str=""
        else:
            for i in range(self.__rows):
                for j in range(500-screen_width , 500):
                    # print(self.matrix[i][j] , end="")
                    self.str+=self.__matrix[i][j]
                # print()
                print(self.str)
                self.str=""

    def matrix_get(self):
        return self.__matrix
    
    def matrix_set(self,matrix):
        self.__matrix=matrix
