#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game


coeffs=[66,-63,-60]



# La fonction dot puisque numpy n'est pas disponible sur le seveur

def dot(L1,L2):
    return sum(x*y for x,y in zip(L1,L2))






def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    
    global moi
    moi = game.getJoueur(jeu)
    
    coups=game.getCoupsValides(jeu)
    
    return decision(jeu,coups)[0]








def decision(jeu,coups):
    """ jeu*coups-> [coup, scoremax]
        retourne le coup et le score qui donne un plus grand score
    """
    
    
    copie=game.getCopieJeu(jeu)
    
    game.joueCoup(copie,coups[0])
    maxi=coups[0]
    scoremax =  evaluation (copie)
    for el in coups:
        copie=game.getCopieJeu(jeu)
        game.joueCoup(copie,el)
        s = evaluation(copie)
        if (scoremax < s):
            scoremax = s
            maxi = el
    res=[]
    res.append(maxi)
    res.append(scoremax)
    
    return res



def evaluation(jeu):
    

    if game.finJeu(jeu):
        return jeufini(jeu)
    else:
        
        score  = [nombres_de_cases_coins(jeu),nombre_de_mauvaises_cases_X(jeu),nombre_de_mauvaises_cases_C(jeu)]
        
        return  dot(coeffs,score)
       





def nombres_de_cases_coins(jeu):

    # nombres de pions sur les coins
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
    
    # renvoie le nombre de pions qui se trouvent sur des cases qui sont adjacentes diagonalement aux coins

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
    
    # renvoie le nombre de pions qui se trouvent sur des cases qui sont adjacentes diagonalement aux coins

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






def jeufini(jeu):
    

    # est appelé si le jeu est fini et renvoie en fonction de l'éventualité un score

    adv= jeu[1]%2+1
    if game.getGagnant(jeu) == jeu[1]:
        return 1000
    if game.getGagnant(jeu) == adv:
        return -1000
    else:
       return 0










