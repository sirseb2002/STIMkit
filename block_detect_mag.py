import mcpi.minecraft as minecraft
import mcpi.block as block
from random import randint
from gpiozero import LED
from time import sleep
from math import sqrt

mc = minecraft.Minecraft.create()

mc.postToChat("Go find the block")
sleep(1)

mc.player.setPos(1,0,1)
sleep(0.5)

mc.setBlock(0, 0 , 0, block.FENCE.id)

p = mc.player.getTilePos()
# x = p.x + randint(-20, 20)
# y = p.y + randint(-5, 5)
# z = p.z +randint(-20,20)

x = p.x + randint(0, 25)
y = p.y - 2
z = p.z + randint(0, 25)

mc.setBlock(x, y , z, block.GOLD_BLOCK.id)

led_target = LED(26)
led1= LED(17)
led2= LED(27)
led3= LED(22)
led4= LED(5)
led5= LED(6)
led6= LED(13)
led7= LED(19)
led8= LED(16)
led9= LED(20)
led10= LED(21)

led_target.on()
sleep(2)
led_target.off()

dist = 0
gameover = False

while gameover == False:
    p = mc.player.getTilePos()

    xd = p.x - x
    yd = p.y - y
    zd = p.z - z

    dist_now = sqrt((xd*xd) + (zd*zd))

    #mc.postToChat(dist_now)

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


    if dist_now == 0:
        led_target.on()
    else:
        led_target.off()
