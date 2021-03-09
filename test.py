#ETAPE 1  **************************
#importer les librairies utiles dans la centrale

import mcpi.minecraft as minecraft
import time


#ETAPE 2  **************************
#Nommer un robot libraire capable de gérer la librairie pour vous
#Appelons-le "mc" 
#Assignons lui la tache de gerer la librairie MINECRAFT

mc = minecraft.Minecraft.create()


#ETAPE 3  **************************
#Donnons nous du temps pour effectuer nos taches quand on lance un programme
#Ici, l'on se donne 5 secondes

time.sleep(5)


#ETAPE 4  **************************
#Demandons au robot libraire d'afficher un message sur la console Minecraft

mc.postToChat("BONJOUR AGENCE SPATIALE !!!")
