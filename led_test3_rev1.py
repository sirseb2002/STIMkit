#DEL_Test 3: Test de position Minecraft avec plusieurs DEL.
#Etape 1 Importons nos bibliothèques.
import mcpi.minecraft as minecraft
import mcpi.block as block
from gpiozero import LED
from time import sleep
from math import sqrt

#Etape 2 Donnons les désignations de nos DEL's.
led1= LED(13)
led2= LED(19)
led3= LED(26)
led4= LED(16)
led5= LED(20)
led6= LED(21)


#Etape 3 Définissons notre position et créons notre point de référence.
mc = minecraft.Minecraft.create()


mc.player.setPos(1, 0, 1)

#Donnons-nous du temps.
sleep(0.5)


mc.setBlock(0, 0 , 0, block.FENCE.id)

#Etape 4 Faisons en sorte qu'un message affiche les instructions dans le chat.
mc.postToChat("Teleportez vous !")
sleep(1)

#Etape 5 Écrivons les fonctions individuelles de vos DEL.
#Ici, nous indiquerons à nos DEL quand s'allumer ou s'éteindre.
#Nous obtiendrons également nos données de position actuelles.
gameover = False  #Définissons les paramètres et les conditions de notre programme en boucle avec des declartions vrai et faux.

while gameover == False:   #Ici, nous créons une condition, qui continuera à répéter cette boucle de verifications.
    p = mc.player.getTilePos()   #Disons à notre programme de continuer à lire notre position actuelle dans Minecraft.

#Nous commencons par définir les conditions pour que notre programme véerifie si lesdites déclarations sont vraies ou fausses.
    if p.x > 34 and p.x < 64:  #Nous indiquons ici quels sont les paramètres d'une condition vraie (TRUE) en validant  la position actuelle de notre joueur le long de l'axe X.
        led1.on()        #Ici, nous disons à notre programme ce qu'il doit faire si les conditions sont remplies et sont vraies (TRUE).
        if p.x > 44 and p.x < 64:
            led2.on()
            if p.x > 54 and p.x < 64:
                led3.on()
                if p.x > 64:    #Ici, nous n'avons qu'une seule condition à vérifier car ce sera notre frontière finale.
                    led3.off()
                    led2.off()
                    led1.off()
            else:      #Maintenant, disons à notre programme ce qu'il doit faire si les déclarations sont fausses (FALSE).
                led3.off()
        else:
            led2.off()
            led3.off()
    else:
        led1.off()
        led2.off()
        led3.off()


#Maintenant que nous avons la moitié de notre programme qui est entièrement axé sur la position actuelle du joueur le long de l'axe X.
#Faisons l'autre moitié qui sera pour notre ax Z.
#N'oubliez pas qu'il est important de conserver les indentations!

#Encore une fois, nous définirons d'abord nos vraies (TRUE) conditions.
    if p.z > 34 and p.z < 64:     #Cependant, cette fois, nous vérifierons la position de notre joueur le long de 2 coordonnées sur l'axe Z.
        led4.on()
        if p.z > 44 and p.z < 64:
            led5.on()
            if p.z > 54 and p.z < 64:
                led6.on()
                if p.z > 64:      #Ici, nous n'avons qu'une seule condition à vérifier car ce sera notre frontière finale.
                    led6.off()
                    led5.off()
                    led4.off()
            else:        #Et n'oublions pas d'ajouter les action pour nos fausses (FALSE) déclarations.
                led6.off()
        else:
            led5.off()
            led6.off()
    else:
        led4.off()
        led5.off()
        led6.off()
        