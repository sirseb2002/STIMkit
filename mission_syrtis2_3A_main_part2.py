#Ceci dit au joueur d'appuyer sur le boutton 2
#Quand le boutton 2 est appuyé, cela fait apparaître le deuxième bloc au hazard
#Ensuite ceci dit au joueur d'aller trouver le bloc
if (var_block1 == 1) and (var_block2 == 0):
    mc.postToChat("Veuillez appuyer sur le bouton 2")
    button2.wait_for_press()
    print("Bouton2 est appuye")
    p = mc.player.getTilePos()
    x = p.x + randint(0, 25)
    y = p.y - 2
    z = p.z + randint(0, 25)
    mc.setBlock(x, y, z, block.GOLD_BLOCK.id)
    mc.postToChat("Allez trouver le 2e bloc")
    distance_now()
    end2()

#Ceci dit au joueur d'appuyer sur le boutton 3
#Quand le boutton 3 est appuyé, cela fait apparaître le troisième bloc au hazard
#Ensuite ceci dit au joueur d'aller trouver le bloc
if (var_block1 == 1) and (var_block2 == 1) and (var_block3 == 0):
    mc.postToChat("Veuillez appuyer sur le bouton 3")
    button3.wait_for_press()
    print("Bouton3 est appuye")
    p = mc.player.getTilePos()
    x = p.x + randint(0, 25)
    y = p.y - 2
    z = p.z + randint(0, 25)
    mc.setBlock(x, y, z, block.IRON_BLOCK.id)
    mc.postToChat("Allez trouver le 3e bloc")
    distance_now()
    end3()