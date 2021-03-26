# Programme mission 2

#Étape 1
#importez les librairies utiles à la mission 2
import mcpi.minecraft as minecraft
import mcpi.block as block
from random import randint
from gpiozero import LED
from time import sleep
from math import sqrt


#Étape 2
#Nommez votre librairie
#nous le nomons ici "mc"
mc = minecraft.Minecraft.create()


#Étape 3
#Demandons au libraire d'afficher un message sur l'écran
mc.postToChat("Allez trouver le bloc d'or")
#Donnons-nous du temps pour le voir
sleep(1)


#Étape 4
#Désignons les sorties du RaspBerry Pi qui iront vers les DEL
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



#Étape 5
#Plaçons notre travailleur à une position connue dans Minecraft
mc.player.setPos(1, 0, 1)
#Donnons-nous du temps avant de passer à la prochaine étape
sleep(0.5)

#Déposons un une barrière derrière nous qui nous servira de repère
mc.setBlock(0, 0 , 0, block.FENCE.id)


#Étape 6 UN PEU DE MATHÉMATIQUE !
#
p = mc.player.getTilePos()

x = p.x + randint(0, 25)
y = p.y - 2
z = p.z + randint(0, 25)


#Étape 7 Demandons au libraire de cacher un bloc d'or

mc.setBlock(x, y , z, block.GOLD_BLOCK.id)


#Étape 8 Validons que les DEL fonctionnent
led_target.on()
sleep(3)
led_target.off()


#Étape 9 Partons à la chasse d'un bloc d'or!

gameover = False

while gameover == False:
    p = mc.player.getTilePos()

    xd = p.x - x
    yd = p.y - y
    zd = p.z - z

    dist_now = sqrt((xd*xd) + (zd*zd))

    #mc.postToChat(dist_now)

#Étape 10 Affichons notre proximité avec le bloc, d'or!
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

#Étape 11 Allumons la DEL VERTE quand on est direct sur le bloc d'or!
    if dist_now == 0:
        led_target.on()
    else:
        led_target.off()
