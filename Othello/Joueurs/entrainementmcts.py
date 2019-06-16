#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import othello
sys.path.append("../..")
import game
import math
import random
import pickle
import datetime




# programme pour l'entrainement du joueuer utilisant MCTS


game.game = othello


jeu = game.initialiseJeu()

moi = game.getJoueur(jeu)

adv = moi%2 + 1
   
 
# Définition de l'intervalle de temps pendant lequel le joueur
# sera entrainé

now = datetime.datetime.now()
end = now + datetime.timedelta(hours=1)  


def entrainement(jeu):

	
	
	etat = MonteCarlo()
	etat.state = jeu
	
	while (datetime.datetime.now()<end):
	
		result = MonteCarlo.traverse(etat,etat.state)
		MonteCarlo.backpropagation(etat,result)
		
		
		


	# sauvegarde de l'arbre final obtenu avec les valeurs des noeuds.
	with open('modeleOthello', 'wb') as f:
		pickle.dump(etat,f)
	


	

		

	



class MonteCarlo:

	# constructeur pour l'initialisation d'un noeud
	def __init__(self,parent=None):
		self.state = []
		self.n=0
		self.s=0
		self.children=[]
		self.parent = parent
		

	

	# permet d'aller 
	def traverse(self,state):
	
		
		
		# Tant que le noeud n'est pas une feuille, on choisit de faire une simulation sur le noeud fils qui
		# a la plus grande valeur UCB1
		


		while(not self.estUneFeuille()):
			
			
			maxval=float('-inf')
			
			coups = game.getCoupsValides(state)
			
			for cp in coups:
		
				

				copie=game.getCopieJeu(state)
				
				
				game.joueCoup(copie,cp)

				
				child = MonteCarlo()
				child.parent = self
				child.state=copie
				
				self.children.append(child)
				
				
				if child.n == 0:
					self = self.children[0]
				else:
					val= (child.s/child.n) + 2 * math.sqrt(math.log(child.parent.n)/child.n)

					if maxval<val:
						maxval = val	
						self= child
					
		
		
		
		# si le noeud n'a jamais été visité, on fait une simulation
		if self.n==0:
			
			
			return self.rollout()

		# sinon on ajoute les fils du noeud et on fait une simulation sur le premier noeud fils
		else:
			coups = game.getCoupsValides(state)
			for cp in coups:
				
				copie= game.getCopieJeu(state)
				
				
				game.joueCoup(copie,cp)

				child = MonteCarlo()
				child.parent =self
				
				child.state=copie
				
				self.children.append(child)
					
			

			
			return self.children[0].rollout()
			
		


			






	# simulation de jeu à partir du noeud jusqu'à la fin de partie
	def rollout(self):
		
		copie= game.getCopieJeu(self.state)

		while (True):
			
			if (game.finJeu(copie)):
				
				
				
				return self.resultat(copie)			
			
			
			#choix d'un coup aléatoire  parmi les coups valides
			a = random.choice(game.getCoupsValides(copie))
			
			

			
			game.joueCoup(copie,a)
			
			
			

	

	# mise à jour après la simulation des noeuds parcourus
	def backpropagation(self,resultat):
		self.n +=1
		self.s+=resultat
		if self.parent is not None:
			self.parent.backpropagation(result)




	# vérifie si le noeud est une feuille, ie si le noeud n'a pas de fils
	def estUneFeuille(self):

		if len(self.children)== 0:
			return True
		return False


	


	# retourne le résultat (victoire ou défaite ou match nul) à la fin du jeu
	
	def resultat(self,state):

		if game.getGagnant(state) == moi:
			return 1
		elif game.getGagnant(state) == adv:
			return -1
		else:
			return 0







entrainement(jeu)