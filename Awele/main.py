#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
tmp= time.time()

import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_humain
import joueur_aleatoire
import alpha_beta
import MinMax
import joueur_horizon1


game.joueur1= joueur_horizon1
game.joueur2= joueur_aleatoire





S1=0
S2=0
for i in  range(100):

	jeu = game.initialiseJeu()


	while(not game.finJeu(jeu)):
		game.affiche(jeu)
		coup=game.saisieCoup(jeu)
		
		game.joueCoup(jeu,coup)

	game.affiche(jeu)	

	print ("Gagnant :",game.getGagnant(jeu))

	if game.getGagnant(jeu)==1:
		S1+=1
	if game.getGagnant(jeu)==2:
		S2+=1
print("joueur 1:",S1, " joueur 2:",S2)


tmp2 = time.time() - tmp

print("Temps d'exécution = ", tmp2)