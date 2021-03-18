import mcpi.minecraft as minecraft
import mcpi.block as block
from random import randint
from gpiozero import LED
from time import sleep
from math import sqrt

led_target = LED(26)

led_target.on()
sleep(2)
led_target.off()

mc = minecraft.Minecraft.create()

mc.postToChat("Go find the SECRET CODE !")
sleep(1)

mc.player.setPos(1,0,1)
sleep(0.5)

p = mc.player.getTilePos()

IRx = p.x + randint(26, 100)
IRy = p.y - 2
IRz = p.z + randint(26, 100)

SSx = p.x + randint(26, 100)
SSy = p.y - 2
SSz = p.z + randint(26, 100)

GRx = p.x + randint(26, 100)
GRy = p.y - 2
GRz = p.z + randint(26, 100)

DTx = p.x + randint(26, 100)
DTy = p.y - 2
DTz = p.z + randint(26, 100)


mc.setBlock(IRx, IRy , IRz, block.IRON.id)
mc.setBlock(SSx, SSy , SSz, block.SANDSTONE.id)
mc.setBlock(GRx, GRy , GRz, block.GRAVEL.id)
mc.setBlock(DTx, DTy , DTz, block.DIRT.id)

dist = 0
gameover = False

while gameover == False:
    IRp = mc.player.getTilePos()
    # x = p.x + randint(-20, 20)
    # y = p.y + randint(-5, 5)
    # z = p.z +randint(-20,20)
