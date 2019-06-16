#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game


pmax = 2




def saisieCoup(jeu):
    global moi
    moi=game.getJoueur(jeu)
    global adv
    adv = moi % 2 +1

    global tour
    tour=game.getScores(jeu)[0]+game.getScores(jeu)[1]+1
    coups=game.getCoupsValides(jeu)
    print (tour)
    """ jeu -> coup
        Retourne un coup a jouer
    """
    


    return decision(jeu,coups)[0]







def evaluation(jeu):
    global tour
    
    global moi
    
    
    if game.finJeu(jeu):
        return jeufini(jeu)
    else:
        
        
        res=(66-tour)*nombre_de_cases_coin(jeu)+(-60+tour)*nombre_de_mauvaises_cases_X(jeu)+(-63+tour)*nombre_de_mauvaises_cases_C(jeu)
        
        if tour>=44:
            
            res=res+game.getScores(jeu)[moi-1]
            
        

        return res

def jeufini(jeu):
    
    global moi
    global adv
    if game.getGagnant(jeu)== adv:
        return -1000
    elif game.getGagnant(jeu) == moi:
        return 1000    
    else:
        return 0

def nombre_de_cases_coin(jeu):
    global moi

    plateau=jeu[0]
    res=0
    if plateau[0][0] == moi :  
        res+=1
            
    if plateau[0][7] == moi:   
        res+=1
        
    if plateau[7][0] == moi:
        res+=1

    if plateau[7][7] == moi:
        res+=1
    return res




def nombre_de_mauvaises_cases_X(jeu):
	global moi
	plateau=jeu[0]
	res=0
	if plateau[1][1] == moi and plateau[0][0]==0:
		res+=1
	if plateau[6][6] == moi and plateau[7][7]==0:
		res+=1
	if plateau[1][6] == moi and plateau[0][7]==0:
		res+=1
	if plateau[6][1] == moi and plateau[7][0]==0:
		res+=1
	return res




def nombre_de_mauvaises_cases_C(jeu):
    plateau=jeu[0]
    res=0
    
    global moi

    if  plateau[0][1] == moi and plateau[0][0]==0:
        res+=1
        
    if plateau[1][0] == moi and plateau[0][0]==0:
        res+=1

    if plateau[0][6] == moi and plateau[0][7]==0:
        res+=1
        
    if plateau[1][7] == moi and plateau[0][7]==0:
        res+=1
        
    if plateau[6][0] == moi and plateau[7][0]==0:
        res+=1

    if plateau[7][1] == moi and plateau[7][0]==0:
        res+=1
        
    if plateau[7][6] == moi and plateau[7][7]==0:
        res+=1
        
    if plateau[6][7] == moi and plateau[7][7]==0:
        res+=1

    return res



def decision(jeu,coups):
    """ jeu*coups-> [coup, scoremax]
        retourne le coup et le score qui donne un plus grand score
    """
    
    
    #copie=game.getCopieJeu(jeu)
    
    #game.joueCoup(copie,coups[0])
    meill_coup=coups[0]
    
    scoremax =  float('-inf')
    for cp in coups:
        copie=game.getCopieJeu(jeu)
        game.joueCoup(copie,cp)
        s = estimation(copie,False)
        
        if ( s > scoremax):
        	scoremax = s
        	meill_coup=cp
    res=[]
    res.append(meill_coup)
    res.append(scoremax)
    
    return res




def estimation(jeu,me,p=1):

    global pmax
    
    

    if p==pmax or game.finJeu(jeu):
    	return evaluation(jeu)
    
    vmax = None
  
    	
    coups= game.getCoupsValides(jeu)
    for cp in coups:
    	copie=game.getCopieJeu(jeu)
    	game.joueCoup(copie,cp)
    	
    	if me:
    	
    		v = estimation(copie,False,p+1)

    		if vmax is None:
    			
    			vmax =v
    		
    		
    			
    		if (vmax<v):
    			vmax =v
    			
    	else:
    		
    		v = estimation(copie,True,p+1) 
    		
    		if vmax is None:
    			
    			vmax = v
    		
    	
    	
    		if (vmax>v):
    			
    			vmax=v
    			
    
    return vmax




