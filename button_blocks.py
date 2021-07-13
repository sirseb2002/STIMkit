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

#Ceci dit d'appuyer sur le boutton 4 quand on est directement sur le bloc
def message():
    mc.postToChat("Veuillez appuyer sur le boutton 4")

#Ceci fait que le bloc 1 ne peut plus apparaître et fait que le bloc suivant peut apparaître
def end1():
    global var_block1
    global run_once
    print("end1")
    clear_led()
    if var_block1 == 0:
        code1()
        var_block1 = 1
    if run_once == 1:
        run_once = 0

#Ceci fait que le bloc 2 ne peut plus apparaître et fait que le bloc suivant peut apparaître
def end2():
    global var_block1
    global var_block2
    global run_once
    print("end2")
    clear_led()
    if (var_block1 == 1) and (var_block2 == 0):
        code2()
        var_block2 = 1
    if run_once == 1:
        run_once = 0

#Ceci fait que le bloc 3 ne peut plus apparaître et fait que le jeu finisse
def end3():
    global var_block1
    global var_block2
    global var_block3
    print("end3")
    clear_led()
    mc.postToChat("Bravo!!!")
    if (var_block1 == 1) and (var_block2 == 1) and (var_block3 ==0):
        code3()
        var_block3 = 1
    sleep(1)
    mc.postToChat("Allez maintenant verifier votre code a coter de la cloture")

#Ceci fait que le premier chiffre du code apparaisse
def code1():
    print("code1")
    mc.setBlock(5, 10, 0, block.WOOL.id)
    mc.setBlock(7, 10, 0, block.WOOL.id)
    mc.setBlock(9, 10, 0, block.WOOL.id)
    mc.setBlock(11, 10, 0, block.WOOL.id)

#Ceci fait que le deuxième chiffre du code apparaisse
def code2():
    print("code2")
    mc.setBlock(5, 7, 0, block.WOOL.id)

#Ceci fait que le deuxième chiffre du code apparaisse
def code3():
    print("code3")
    mc.setBlock(5, 4, 0, block.WOOL.id)
    mc.setBlock(7, 4, 0, block.WOOL.id)
    mc.setBlock(9, 4, 0, block.WOOL.id)

#Ceci éteint tous les LED 
def clear_led():
    print("led off")
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    led5.off()
    led6.off()
    led7.off()
    led8.off()
    led9.off()
    led10.off()
    led_target.off()

#Ceci dit au LED la distance entre le joueur et le bloc
def distance_now():
    global gameover
    global var_block1
    global var_block2
    global var_block3
    global run_once
    gameover = False
    print("Block is placed")
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
                print("Button4 is pressed")
                gameover = True
        else:
            led_target.off()
            run_once = 0
      
#MAIN

#Ceci place le joueur sur la coordonnée 1, 0, 1
mc.player.setPos(1, 0, 1)

#Ceci place une clôture sur la coordonée 0, 0, 0
mc.setBlock(0, 0, 0, block.FENCE.id)

#Ceci dit au joueur d'appuyer sur le boutton 1
#Quand le boutton 1 est appuyé, cela fait apparaître le premier bloc au hazard
#Ensuite ceci dit au joueur d'aller trouver le bloc
if var_block1 == 0:
    mc.postToChat("Veuillez appuyer sur le boutton 1")
    button1.wait_for_press()
    print("Button1 is pressed")
    p = mc.player.getTilePos()
    x = p.x + randint(0, 25)
    y = p.y - 2
    z = p.z + randint(0, 25)
    mc.setBlock(x, y, z, block.DIAMOND_BLOCK.id)
    mc.postToChat("Allez trouver le 1er bloc")
    distance_now()
    end1()

#Ceci dit au joueur d'appuyer sur le boutton 2
#Quand le boutton 2 est appuyé, cela fait apparaître le deuxième bloc au hazard
#Ensuite ceci dit au joueur d'aller trouver le bloc
if (var_block1 == 1) and (var_block2 == 0):
    mc.postToChat("Veuillez appuyer sur le boutton 2")
    button2.wait_for_press()
    print("Button2 is pressed")
    p = mc.player.getTilePos()
    x = p.x + randint(0, 25)
    y = p.y - 2
    z = p.z + randint(0, 25)
    mc.setBlock(x, y, z, block.GOLD_BLOCK.id)
    mc.postToChat("Allez trouver le 2e bloc")
    distance_now()
    end2()

#Ceci dit au joueur d'appuyer sur le boutton 3
#Quand le boutton 3 est appuyé, cela fait apparaître le troisième bloc au hazard
#Ensuite ceci dit au joueur d'aller trouver le bloc
if (var_block1 == 1) and (var_block2 == 1) and (var_block3 == 0):
    mc.postToChat("Veuillez appuyer sur le boutton 3")
    button3.wait_for_press()
    print("Button3 is pressed")
    p = mc.player.getTilePos()
    x = p.x + randint(0, 25)
    y = p.y - 2
    z = p.z + randint(0, 25)
    mc.setBlock(x, y, z, block.IRON_BLOCK.id)
    mc.postToChat("Allez trouver le 3e bloc")
    distance_now()
    end3()