import mcpi.minecraft as minecraft
import mcpi.block as block
from random import randint
from gpiozero import LED
from time import sleep
from math import sqrt

mc = minecraft.Minecraft.create()

mc.postToChat("Go find the SECRET CODE !")
sleep(1)

mc.player.setPos(1,0,1)
sleep(0.5)

mc.setBlock(28, 0 , 28, block.IRON.id)
mc.setBlock(30, 0 , 30, block.SANDSTONE.id)
mc.setBlock(35, 0 , 35, block.GRAVEL.id)
mc.setBlock(40, 0 , 40, block.DIRT.id)

p = mc.player.getTilePos()
# x = p.x + randint(-20, 20)
# y = p.y + randint(-5, 5)
# z = p.z +randint(-20,20)
