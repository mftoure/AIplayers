#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
tmp= time.time()




import othello
import sys
sys.path.append("..")
import game
game.game=othello
sys.path.append("./Joueurs")


import joueur_aleatoire
import joueur_premier_coup_valide

import joueur_horizon1_statique
import joueur_horizon1_dynamique

import minimax_statique
import minimax_dynamique

import alpha_beta_statique
import alpha_beta_dynamique

import negamax
import negascout


#import entrainementmcts
#import mcts1



game.joueur1= alpha_beta_statique
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