from Board import Board
from Scenery import Scenery
from Mando import Mando
from Input import take_input
from Dragon import Dragon
from Dragon_ball import Dragon_ball
from Magnet import Magnet
from start import start
from end import end

from colorama import init, Fore,Back
init()

import random
import time
import os
import time
import signal 

# os.system('afplay ../../Super-Mario-master/music/theme.wav')
os.system('nohup mpg123 ./music/theme.mp3 2>&1 &')
start()

columns,rows=os.get_terminal_size()

status=0
obj_board=Board(rows,500)
obj_scenery=Scenery()
obj_mando=Mando(1,rows-4)
obj_board.matrix_set(obj_mando.place_mando(1,obj_board.matrix_get()))
obj_board.matrix_set(obj_scenery.create_ground(rows,500,obj_board.matrix_get()))
obj_board.matrix_set(obj_scenery.create_sky(rows,500,obj_board.matrix_get()))
obj_board.matrix_set(obj_scenery.create_clouds(obj_board.matrix_get()))
obj_board.matrix_set(obj_scenery.create_coins(rows,500,obj_board.matrix_get()))
obj_board.matrix_set(obj_scenery.create_powerup(rows,500,obj_board.matrix_get()))
obj_board.matrix_set(obj_scenery.create_obstacles(obj_board.matrix_get()))
obj_board.matrix_set(obj_scenery.create_deadwall(obj_board.matrix_get()))
obj_dragon=Dragon(rows,500)
obj_board.matrix_set(obj_dragon.place_dragon(rows,500,obj_board.matrix_get()))
y=random.randint(10,rows-15)
x=random.randint(60,300)
obj_magnet=Magnet(x,20)
obj_board.matrix_set(obj_magnet.print(obj_board.matrix_get()))
stage=-1
obj_dragon_ball=Dragon_ball(10,10)
obj_board.matrix_set(obj_dragon_ball.print(obj_board.matrix_get()))
game_time=100
game_strt_time=time.time()
power_time=0
mando_check_roar=0
boss_fight_start=time.time()
def mag_force(x,y,stage,board):
    dist=19
    mag_x,mag_y=obj_magnet.get_x_y()
    if x < mag_x and mag_x-x<dist and mag_y-y<dist and mag_y-y>-dist:
        obj_board.matrix_set(obj_mando.move_mando("right",1,stage,board))
    elif x > mag_x and x-mag_x<dist and mag_y-y<dist and mag_y-y>-dist:
        obj_board.matrix_set(obj_mando.move_mando("left",1,stage,board))

    if y < mag_y and mag_y-y<dist and mag_x-x<dist and mag_x-x>-dist:
        obj_board.matrix_set(obj_mando.move_mando("down",1,stage,board))
    elif y > mag_y and y-mag_y<dist and mag_x-x<dist and mag_x-x>-dist:
        obj_board.matrix_set(obj_mando.move_mando("up",2,stage,board))
        obj_mando.deactivate_gravity()

    if (y - mag_y < 4 and y-mag_y>-4) and (x - mag_x <= 5 and x-mag_x>=-5):
        end(0,str(obj_mando.tell_score()),"BEWARE OF MAGNETS IN JURASSIC WORLD")
def kbhit():
    inp=take_input()
    if obj_mando.get_power_state() == True:
        mg=2

    else:

        mg=0
    if inp=="w":
        obj_board.matrix_set(obj_mando.move_mando("up",2+mg,stage,obj_board.matrix_get()))
        obj_mando.deactivate_gravity()
    elif inp=="d":
        obj_board.matrix_set(obj_mando.move_mando("right",2+mg,stage,obj_board.matrix_get()))
        #obj_mando.deactivate_gravity()
    elif inp=="a":
        obj_board.matrix_set(obj_mando.move_mando("left",2+mg,stage,obj_board.matrix_get()))
        #obj_mando.deactivate_gravity()
    elif inp==" ":
        obj_board.matrix_set(obj_mando.shoot(stage,obj_board.matrix_get()))
        # obj_mando.move_mando("down",1,stage,obj_board.matrix)
    elif inp=="q":
        os.system('ps -ef | grep mpg | grep -v grep | awk \'{print $2}\' | xargs kill')
        exit(0)
    elif inp=="p":
        obj_board.matrix_set(obj_mando.activate_shield(obj_board.matrix_get()))
    elif inp=="t":
        obj_mando.transform()
    else:
        obj_mando.activate_gravity()

prev_dt = int(round(time.time() * 1000))
data=""
life=obj_mando.get_lives()



while True:

    os.system("clear")
    dt=int(round(time.time() * 1000))
    columns,rows=os.get_terminal_size()
    
    life=obj_mando.get_lives()
    if(life<=0):
        end(0,str(obj_mando.tell_score()),"BETTER TAKE CARE OF YOUR HEALTH !!")
    j=0
    for i in data:
        matrix=obj_board.matrix_get()
        matrix[3][j+5+stage-1]=" "
        obj_board.matrix_set(matrix)
        j+=1
    for i in range(5):
        matrix=obj_board.matrix_get()
        matrix[3][j+5+stage-1]=" "
        obj_board.matrix_set(matrix)
        j+=1

    data=""
    data+="     SCORE:"
    data+=obj_mando.tell_score()
    data+=obj_mando.shield_status()
    data+="         LIFE(S):"
    data+=str(life)
    data+="     TIME REMAININNG:"
    data+=str(int((100-(time.time()-game_strt_time))-(100-(time.time()-game_strt_time))%1))
    data+="s"
    data+="     DRAGON LIFE(S):"
    drg_life=obj_dragon.get_lives()
    data += str(drg_life)
    j=0
    for i in data:
        matrix=obj_board.matrix_get()
        matrix[3][j+5+stage]=i
        obj_board.matrix_set(matrix)
        j+=1
    obj_board.print_board(stage,columns)
    # print("\033[0;0H")

    # if life-obj_mando.get_lives()!=0:
    #     p,q=obj_mando.get_coordinates()
    #     for tmp in range(-10,10):
    #         for tmp2 in range(-10,10):
    #             if q+tmp < rows and q+tmp > 0 and p+tmp2 < 500 and p+tmp2 > 0 and obj_board.matrix[q+tmp][p+tmp2] == Fore.WHITE+Back.RED + "*" + '\x1b[0m':
    #                 obj_board.matrix[q+tmp][p+tmp2]=" "
                    
    
    # time.sleep(0.01)

    kbhit()
    if obj_mando.get_power_state() == True:
        power_time=100
    else:
        power_time=0
    if stage<500-columns and dt-prev_dt>=150-power_time:
        stage+=1
        prev_dt=dt
    x,y=obj_mando.get_coordinates()
    mag_force(x,y,stage,obj_board.matrix_get())

    obj_board.matrix_set(obj_mando.check_left_wall(stage,obj_board.matrix_get()))
    obj_board.matrix_set(obj_mando.check_shield_timer(obj_board.matrix_get()))
    obj_board.matrix_set(obj_mando.gravity(stage,obj_board.matrix_get()))
    x,y=obj_mando.get_coordinates()
    obj_board.matrix_set(obj_dragon.dragon_follow(y,rows,columns,obj_board.matrix_get()))
    obj_board.matrix_set(obj_mando.move_bullets(stage,obj_board.matrix_get()))
    obj_board.matrix_set(obj_mando.count_coin(2,obj_board.matrix_get()))
    
    hurray,brd=obj_scenery.check_obstacle_bullet_collision(obj_board.matrix_get())
    obj_board.matrix_set(brd)
    obj_mando.set_score(hurray)

    obj_board.matrix_set(obj_dragon.shoot(x,y,obj_board.matrix_get()))
    obj_board.matrix_set(obj_dragon.follow(x,y,obj_board.matrix_get()))
    obj_board.matrix_set(obj_scenery.create_deadwall(obj_board.matrix_get()))
    obj_dragon.check_hit(obj_board.matrix_get())
    
    if(x>500-columns and mando_check_roar==0):
        mando_check_roar=1
        boss_fight_start=time.time()
        os.system('ps -ef | grep mpg | grep -v grep | awk \'{print $2}\' | xargs kill')
        os.system('nohup mpg123 ./music/rex.mp3 2>&1 &')

    if(mando_check_roar==1 and time.time()-boss_fight_start >=3):
        mando_check_roar=2
        os.system('ps -ef | grep mpg | grep -v grep | awk \'{print $2}\' | xargs kill')
        os.system('nohup mpg123 ./music/boss.mp3 2>&1 &')

    if (x > 500 -27):
        end(status,str(obj_mando.tell_score()),"DARE NOT CROSS THE LINE NEXT TIME!!!")

    if (drg_life<=0):
        obj_mando.set_score(50)
        end(1,str(obj_mando.tell_score()),"")

    if time.time() -game_strt_time >=100:
        end(0,str(obj_mando.tell_score()),"BETTER HURRY NEXT TIME!!!")
