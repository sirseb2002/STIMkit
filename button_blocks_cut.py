import mcpi.minecraft as minecraft
import mcpi.block as block
from random import randint
from gpiozero import LED
from gpiozero import Button
from time import sleep
from math import sqrt

mc= minecraft.Minecraft.create()

led_target = LED(26)
led1= LED(19)
led2= LED(13)
led3= LED(6)
led4= LED(5)
led5= LED(22)
led6= LED(27)
led7= LED(17)
led8= LED(16)
led9= LED(20)
led10= LED(21)

button1 = Button(18)
button2 = Button(23)
button3 = Button(24)
button4 = Button(25)

var_block1 = 0
var_block2 = 0
var_block3 = 0

run_once = 0

#Ceci dit au LED la distance entre le joueur et le bloc
def distance_now():
    global gameover
    global var_block1
    global var_block2
    global var_block3
    global run_once
    gameover = False
    print("Un bloc est enfoui")
    while gameover == False:
        p = mc.player.getTilePos()

        xd = p.x - x
        yd = p.y - y
        zd = p.z - z

        dist_now = sqrt((xd*xd) + (zd*zd))
        
        if dist_now < 19:
            led1.on()
            if dist_now < 17:
                led2.on()
                if dist_now < 15:
                    led3.on()
                    if dist_now < 13:
                        led4.on()
                        if dist_now < 11:
                            led5.on()
                            if dist_now < 9:
                                led6.on()
                                if dist_now < 7:
                                    led7.on()
                                    if dist_now < 5:
                                        led8.on()
                                        if dist_now < 3:
                                            led9.on()
                                            if dist_now < 1:
                                                led10.on()
                                            else:
                                                led10.off()
                                        else:
                                            led9.off()
                                    else:
                                        led8.off()
                                else:
                                    led7.off()
                            else:
                                led6.off()
                        else:
                            led5.off()
                    else:
                        led4.off()
                else:
                    led3.off()
            else:
                led2.off()
        else:
            led1.off()
        
        if (dist_now == 0) and (yd == 1):
            led_target.on()
            #Ceci dit d'appuyer sur le boutton 4 quand le joueur est sur le bloc
            if run_once == 0:
                message()
                run_once = 1
            if button4.is_pressed:
                print("Bouton 4 est appuye")
                gameover = True
        else:
            led_target.off()
            run_once = 0
      
#MAIN

#Ceci place le joueur sur la coordonnée 1, 0, 1
mc.player.setPos(1, 0, 1)

#Ceci place une clôture sur la coordonée 0, 0, 0
mc.setBlock(0, 0, 0, block.FENCE.id)



