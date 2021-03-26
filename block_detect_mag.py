# Programme mission 2

#Etape 1
#importez les librairies utiles à la mission 2
import mcpi.minecraft as minecraft
import mcpi.block as block
from random import randint
from gpiozero import LED
from time import sleep
from math import sqrt


#Etape 2
#Nommez votre librairie
#nous le nommons ici "mc"
mc = minecraft.Minecraft.create()


#Etape 3
#Demandons au libraire d'afficher un message sur l'écran
mc.postToChat("Allez trouver le bloc d'or")
#Donnons-nous du temps pour le voir
sleep(1)


#Etape 4
#Designons les sorties du RaspBerry Pi qui iront vers les DEL
led_target = LED(26)  #Green LED

#Bargraph designation
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



#Etape 5
#Placons notre travailleur à une position connue dans Minecraft
mc.player.setPos(1, 0, 1)
#Donnons-nous du temps avant de passer a la prochaine etape
sleep(0.5)

#Deposons un une barriere derriere nous qui nous servira de repere
mc.setBlock(0, 0 , 0, block.FENCE.id)


#Etape 6 UN PEU DE MATHEMATIQUE !
#
p = mc.player.getTilePos()

x = p.x + randint(0, 25)
y = p.y - 2
z = p.z + randint(0, 25)


#Etape 7 Demandons au libraire de cacher un bloc d or

mc.setBlock(x, y , z, block.GOLD_BLOCK.id)


#Etape 8 Validons que les DEL fonctionnent
led_target.on()
sleep(3)
led_target.off()


#Etape 9 Partons a la chasse d'un bloc d or!

gameover = False

while gameover == False:
    p = mc.player.getTilePos()

    xd = p.x - x
    yd = p.y - y
    zd = p.z - z

    dist_now = sqrt((xd*xd) + (zd*zd))

    #mc.postToChat(dist_now)

#Etape 10 Affichons notre proximite avec le bloc d or!
    if dist_now < 20:
        led1.on()
        if dist_now < 18:
            led2.on()
            if dist_now < 16:
                led3.on()
                if dist_now < 14:
                    led4.on()
                    if dist_now < 12:
                        led5.on()
                        if dist_now < 10:
                            led6.on()
                            if dist_now < 8:
                                led7.on()
                                if dist_now < 6:
                                    led8.on()
                                    if dist_now < 4:
                                        led9.on()
                                        if dist_now < 2:
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

#Etape 11 Allumons la DEL VERTE quand on est direct sur le bloc d or!
    if dist_now == 0:
        led_target.on()
    else:
        led_target.off()
