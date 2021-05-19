import RPi.GPIO as GPIO # Importer la librairie Raspberry Pi GPIO
from time import sleep # Importer la fonction SLEEP du module TIME

GPIO.setwarnings(False) # Ignorer les WARNINGS pour le moment
GPIO.setmode(GPIO.BOARD) # Utiliser le mode PLATEAU de test
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW) # Assigner la pin 26 pour être une sortie. Initialiser la sortie à OFF au départ

while True: # Boucle infinie
    GPIO.output(8, GPIO.HIGH) # mettre à ON
    sleep(1) # Attendre 1 seconde
    GPIO.output(8, GPIO.LOW) # mettre à OFF
    sleep(1) # attendre 1 second
    
    #recommencer la boucle. Presser STOP pour arrêter
 