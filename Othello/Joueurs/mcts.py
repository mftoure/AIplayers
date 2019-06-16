#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game
import math
import random









def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    
    global moi
    moi = game.getJoueur(jeu)
    global adv
    adv = moi%2 + 1
   
    
    return recherche(jeu)


def recherche(jeu):

	i=0
	
	etat = MonteCarlo()
	etat.state = jeu
	
	while (i<100):
		
		result = MonteCarlo.traverse(etat,etat.state)
		MonteCarlo.backpropagation(etat,result)
		
		print(etat.s)
		
		i+=1



	return meill_state(etat)

	
def meill_state(etat):
	
	meill_state=None
	
	for el in etat.children:
		
		N= float('-inf')
		if N < el.n:
			N=el.n
			meill_state = el.state

	
	return meill_coup(meill_state,etat)



def meill_coup(meill_state,etat):
	
	for cp in game.getCoupsValides(etat.state):
		copie =game.getCopieJeu(etat.state)
		game.joueCoup(copie,cp)
		if (copie == meill_state):
			return cp

		

	

class MonteCarlo:

	def __init__(self,parent=None):
		self.state = []
		self.n=0
		self.s=0
		self.children=[]
		self.parent = parent
		

	
	def traverse(self,state):
	
		
		
		
		
	
		
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
					
		
		
		
			
		if self.n==0:
			
			
			return self.rollout()

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
			
		


			







	def rollout(self):
		
		copie= game.getCopieJeu(self.state)

		while (True):
			
			if (game.finJeu(copie)):
				
				
				
				return self.resultat(copie)			
			
			a = random.choice(game.getCoupsValides(copie))
			
			

			
			game.joueCoup(copie,a)
			
			
			

	


	def backpropagation(self,resultat):
		self.n +=1
		self.s+=resultat
		if self.parent is not None:
			self.parent.backpropagation(result)





	def estUneFeuille(self):

		if len(self.children)== 0:
			return True
		return False


	def resultat(self,state):

		if game.getGagnant(state) == moi:
			return 1
		elif game.getGagnant(state) == adv:
			return -1
		else:
			return 0


