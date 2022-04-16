import os
from datetime import datetime
from colorama import init, Fore,Back,Style
from Bullet import Bullet
import time

init()

class Mando:
    def __init__(self,x_cord,y_cord):
        self.__x=x_cord
        self.__y=y_cord
        self.__shape1 = [ ["|", 'O', "|"], [" ", "|", " "], ["^", " ", "^"] ]
        self.__shape2 = [ ["|", "O", "|"], [" ", "|", " "], ["M", " ", "M"] ]
        self.__shape2[2][2] =  Back.RED +Fore.WHITE + "M"+ '\x1b[0m'
        self.__shape2[2][0] =  Back.RED +Fore.WHITE + "M"+ '\x1b[0m'
        self.__shape3 = [ [" ", 'O', Fore.RED+"|"+'\x1b[0m'], [" ", "|", Fore.RED+"|"+'\x1b[0m'], ["^", " ", Fore.RED+"|"+'\x1b[0m'] ]
        self.__shape4 = [ [" ", "O", Fore.RED+"|"+'\x1b[0m'], [" ", "|", Fore.RED+"|"+'\x1b[0m'], ["M", " ", Fore.RED+"|"+'\x1b[0m'] ]
        self.__shape4[2][0] =  Back.RED +Fore.WHITE + "M"+ '\x1b[0m'
        self.__shape5=[[" ",Back.YELLOW+" "+'\x1b[0m'," "],[Back.YELLOW+"*"+'\x1b[0m'," ",Back.RED+Fore.WHITE+"'"+'\x1b[0m'],[" "," "," "]]
        self.__shape6=[[Back.YELLOW+" "+'\x1b[0m'," "," "],[" ",Back.YELLOW+" "+'\x1b[0m'," "],[" "," ",Back.RED+Fore.WHITE+"'"+'\x1b[0m']]
        self.__shape7=[[" "," "," "],[Back.YELLOW+" "+'\x1b[0m'," ",Back.RED+Fore.WHITE+"'"+'\x1b[0m'],[" ",Back.YELLOW+" "+'\x1b[0m'," "]]
        self.__shape8=[[" "," ",Back.RED+Fore.WHITE+"'"+'\x1b[0m'],[" ",Back.YELLOW+" "+'\x1b[0m'," "],[Back.YELLOW+" "+'\x1b[0m'," "," "]]
        self.__bul=False
        self.__bul_arr=[]
        self.__score=0
        self.__shield=False
        self.__shield_timer=0
        self.__shield_start=time.time()
        self.__shoot_time=time.time()
        self.__gravity=False
        self.__gravity_mag=1
        self.__prev_stage=0
        self.__powerup=False
        self.__power_start_time=time.time()
        self.__lives=5
        self.__life_dec_time=time.time()
        self.__snake=0
        self.__snake_state=0

    def place_mando(self,shape,board):

        if self.__snake==0: 
            if self.__shield==False:
            
                if shape==1:
                    for i in range(-1,2):
                        for j in range(-1,2):
                            board[self.__y + i][self.__x + j]=self.__shape1[i+1][j+1]
                else:
                    for i in range(-1,2):
                        for j in range(-1,2):
                            board[self.__y + i][self.__x + j]=self.__shape2[i+1][j+1]
            else:
                if shape==1:
                    for i in range(-1,2):
                        for j in range(-1,2):
                            board[self.__y + i][self.__x + j]=self.__shape3[i+1][j+1]
                else:
                    for i in range(-1,2):
                        for j in range(-1,2):
                            board[self.__y + i][self.__x + j]=self.__shape4[i+1][j+1]

        else:
            if self.__snake_state %4==0:
                for i in range(-1,2):
                        for j in range(-1,2):
                            board[self.__y + i][self.__x + j]=self.__shape5[i+1][j+1]
            elif self.__snake_state %4==1:
                for i in range(-1,2):
                        for j in range(-1,2):
                            board[self.__y + i][self.__x + j]=self.__shape6[i+1][j+1]
            elif self.__snake_state %4==2:
                for i in range(-1,2):
                        for j in range(-1,2):
                            board[self.__y + i][self.__x + j]=self.__shape7[i+1][j+1]
            elif self.__snake_state %4==3:
                for i in range(-1,2):
                        for j in range(-1,2):
                            board[self.__y + i][self.__x + j]=self.__shape8[i+1][j+1]
            self.__snake_state+=1

        return board

    def transform(self):
        if self.__snake==0:
            self.__snake=1

        elif self.__snake==1:
            self.__snake=0


    def move_mando(self,dir,mag,stage,board):
        
        columns,rows=os.get_terminal_size()
           
        
        if dir=="left" and self.__x > mag+stage:
            for i in range(-1,2):
                for j in range(-1,2):
                    board[self.__y+i][self.__x+j]=" "
            self.__x-=mag
            board=self.count_coin(1,board)
            if self.__y < rows-4 :
                self.place_mando(2,board)
            else:
                self.place_mando(1,board)

        
        elif dir=="right" and self.__x < columns-mag+stage:
            for i in range(-1,2):
                for j in range(-1,2):
                    board[self.__y+i][self.__x+j]=" "
            self.__x+=mag
            board=self.count_coin(1,board)
            if self.__y < rows-4 :
                self.place_mando(2,board)
            else:
                self.place_mando(1,board)
        
        elif dir=="up" and self.__y>mag+6:
            for i in range(-1,2):
                for j in range(-1,2):
                    board[self.__y+i][self.__x+j]=" "
            self.__y-=mag
            board=self.count_coin(1,board)
            self.place_mando(2,board)

        elif dir=="down": 
            if self.__y<=len(board)-4-mag:
                for i in range(-1,2):
                    for j in range(-1,2):
                        board[self.__y+i][self.__x+j]=" "
                self.__y+=mag
                board=self.count_coin(mag,board)
                self.place_mando(1,board)
            else:
                for i in range(-1,2):
                    for j in range(-1,2):
                        board[self.__y+i][self.__x+j]=" "
                tmp=len(board)-4-self.__y
                self.__y+=tmp
                board=self.count_coin(mag,board)
                self.place_mando(1,board)

        return board

    def check_left_wall(self,stage,board):

        columns,rows=os.get_terminal_size()
        ret=board
        if self.__x==stage+1:
            ret = self.move_mando("right",1,stage,board)
        
        elif self.__y<=len(board)-4 and stage+columns<500 and self.__prev_stage < stage:
            ret = self.move_mando("right",1,stage,board)
            self.__prev_stage=stage

        if self.__powerup==True and time.time()-self.__power_start_time > 5:
            self.__powerup=False

        return ret

    
    def shoot(self,stage,board):
        ret =board
        if time.time()-self.__shoot_time >=1:
            obj_bullet=Bullet(self.__x,self.__y,stage)
            ret=obj_bullet.print(board)
            self.__bul_arr.append(obj_bullet)
            self.__shoot_time=time.time()
        
        return ret

    def move_bullets(self,stage,board):
        for i in self.__bul_arr:
            board,temp=i.bul_move(stage,board)
            if temp == -1:
                self.__bul_arr.remove(i)

        return board
    
    def count_coin(self,mag,board):
        columns,rows=os.get_terminal_size()
        for i in range(-1,1+mag):
            for j in range(-1,2):
                if self.__y+i < len(board) and self.__x+j < len(board[0]): 
                    if board[self.__y+i][self.__x+j]==Fore.LIGHTYELLOW_EX+ Style.BRIGHT +"$"+'\x1b[0m':
                        board[self.__y+i][self.__x+j]=" "
                        self.__score+=1 
                    elif board[self.__y+i][self.__x+j]==Fore.BLACK+Back.WHITE+"#"+'\x1b[0m':
                        board[self.__y+i][self.__x+j]=" "
                        self.__powerup=True
                        self.__power_start_time=time.time()
                    elif board[self.__y+i][self.__x+j]==Fore.WHITE+Back.RED+"*"+'\x1b[0m' and time.time()-self.__life_dec_time > 0.5 and self.__shield==False:
                        board[self.__y+i][self.__x+j]=" "
                        self.__lives-=1
                        self.__life_dec_time=time.time()
                        for k in range(-30,31):
                            for q in range(-30,31):
                                if self.__x + k > 0 and self.__x+k < 500 and self.__y+q > 0 and self.__y+q<rows and board[self.__y+q][self.__x+k] == Fore.WHITE+Back.RED+"*"+'\x1b[0m':
                                    board[self.__y+q][self.__x+k]=" "
                    elif board[self.__y+i][self.__x+j]==Fore.RED +"*"+ '\x1b[0m' and time.time()-self.__life_dec_time > 0.5 and self.__shield==False:
                        board[self.__y+i][self.__x+j]=" "
                        self.__lives-=1
                        self.__life_dec_time=time.time()
                    # elif board[self.__y+i][self.__x+j]==Back.RED +" "+ '\x1b[0m' or board[self.__y+i][self.__x+j]==Back.LIGHTBLACK_EX +" "+ '\x1b[0m':
                    #     self.__lives==0 

        return board
 
    def tell_score(self):
        return str(self.__score) 
    
    def set_score(self,inc):
        self.__score += inc

    def shield_status(self):
        if self.__shield == True:
            return "        SHIELD WILL DEACTIVATED IN " + str((5-self.__shield_timer)-(5-self.__shield_timer)%1) +"s"
        else:
            if 15-self.__shield_timer > 0:
                return "        SHIELD CAN BE ACTIVATED IN " + str((15-self.__shield_timer)-(15-self.__shield_timer)%1) + "s"
            else:
                return "        SHIELD CAN BE ACTIVATED "

    
    def activate_shield(self,board):
        ret=board
        if self.__shield==False and self.__shield_timer>=15:
            self.__shield=True
            ret=self.place_mando(1,board)
            self.__shield_timer=0
            self.__shield_start=time.time()
        
        return ret
    
    def check_shield_timer(self,board):
        self.__shield_timer=time.time()-self.__shield_start
        ret=board
        if self.__shield==True and self.__shield_timer >=5:
            self.__shield=False
            ret=self.place_mando(1,board)
            
        return ret

    def activate_gravity(self):
        self.__gravity=True
    
    def deactivate_gravity(self):
        self.__gravity=False
        self.__gravity_mag=1

    def gravity(self,stage,board):
        ret=board
        
        if(self.__gravity==True):
            if self.__y==len(board)-4:
                self.deactivate_gravity()
            else:
                ret=self.move_mando("down",self.__gravity_mag,stage,board)
                self.__gravity_mag+=1
        
        return ret
            
    def get_coordinates(self):
        return self.__x,self.__y

    def get_power_state(self):
        return self.__powerup

    def get_lives(self):
        return self.__lives


                
        


