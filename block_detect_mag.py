import mcpi.minecraft as minecraft
import mcpi.block as block
from random import randint
from gpiozero import LED, Buzzer
from time import sleep
from math import sqrt

mc = minecraft.Minecraft.create()

mc.postToChat("Go find the block")

p = mc.player.getTilePos()
# x = p.x + randint(-20, 20)
# y = p.y + randint(-5, 5)
# z = p.z +randint(-20,20)

x = p.x + randint(0, 25)
y = p.y - 2
z = p.z + randint(0, 25)

mc.setBlock(x, y , z, block.GOLD_BLOCK.id)

led = LED(26)
buzz = Buzzer(24)

led.on()
sleep(1)
led.off()

dist = 0
gameover = False

while gameover == False:
    p = mc.player.getTilePos()

    xd = p.x - x
    yd = p.y - y
    zd = p.z - z

    #mc.postToChat(xd)
    #mc.postToChat(yd)
    #mc.postToChat(zd)

    dist_now = sqrt((xd*xd) + (zd*zd))

    mc.postToChat(dist_now)

    if dist_now < 5:
        led.on()
    else:
        led.off()
