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

sleep(0.5)


mc.setBlock(0, 0 , 0, block.FENCE.id)

#Etape 4 Faisons en sorte qu'un message affiche les instructions dans le chat.
mc.postToChat("Teleportez vous !")
sleep(1)

#Etape 5 Écrivons les fonctions individuelles de vos DEL.
#Ici, nous indiquerons à nos DEL quand s'allumer ou s'éteindre.
#Nous obtiendrons également nos données de position actuelles.
gameover = False

while gameover == False:
    p = mc.player.getTilePos()
    
    if p.x > 35:
        led1.on()
        if p.x > 45:
            led2.on()
            if p.x > 55:
                led3.on()
            else:
                led3.off()
        else:
            led2.off()
    else:
        led1.off()
        
    if p.z > 35:
        led4.on()
        if p.z > 45:
            led5.on()
            if p.z > 55:
                led6.on()
            else:
                led6.off()
        else:
            led5.off()
    else:
        led4.off()
        