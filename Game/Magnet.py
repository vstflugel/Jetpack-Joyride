from colorama import init, Fore,Back
init()
class Magnet:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
        self.__shape=[[Back.RED+" "+'\x1b[0m',Back.RED+" "+'\x1b[0m',Back.RED+" "+'\x1b[0m',Back.RED+" "+'\x1b[0m',Back.RED+" "+'\x1b[0m'],[Back.RED+" "+'\x1b[0m'," "," "," ",Back.RED+" "+'\x1b[0m'],[Back.LIGHTBLACK_EX+" "+'\x1b[0m'," "," "," ",Back.LIGHTBLACK_EX+" "+'\x1b[0m']]
        
    def print(self,board):
        for i in range(-2,3):
            for j in range(-1,2):
                board[self.__y+j][self.__x+i]=self.__shape[j+1][i+2]

        return board

    def get_x_y(self):
        return self.__x,self.__y
        