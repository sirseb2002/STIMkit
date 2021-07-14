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
    mc.postToChat("Allez maintenant verifier votre code au point de depart")

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