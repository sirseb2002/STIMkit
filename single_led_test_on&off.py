#Test de fonctionnement d'une seule DEL.
#Etape 1 Importons nos bibliothèques.
import mcpi.minecraft as minecraft
import mcpi.block as block
from gpiozero import LED
from time import sleep
from math import sqrt

#Etape 2 Donnons une désignation à notre DEL
led1= LED(18)


#Etape 3 Définissons notre position et créons notre point de référence.
mc = minecraft.Minecraft.create()


mc.player.setPos(1, 0, 1)

sleep(0.5)


mc.setBlock(0, 0 , 0, block.FENCE.id)

#Etape 4 Faisons en sorte qu'un message affiche les instructions dans le chat.
mc.postToChat("Teleportez vous !")
sleep(1)


#Etape 5 Décrivez ce que fera la LED jusqu'à ce qu'elle soit éteinte.
#Nous obtiendrons également nos données de position actuelles.

gameover = False

while gameover == False:
    p = mc.player.getTilePos()
    
    if p.x > 35:
        led1.on()
    else:
        led1.off()