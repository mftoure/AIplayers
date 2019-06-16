#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game





def saisieCoup(jeu):
    
    global tour
    tour=game.getScores(jeu)[0]+game.getScores(jeu)[1]
    coups=game.getCoupsValides(jeu)
    print (tour)
    """ jeu -> coup
        Retourne un coup a jouer
    """
    


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
    global tour
    moi=jeu[1]%2+1
    
    if game.finJeu(jeu):
        return jeufini(jeu)
    else:
        
        
        res=(66-tour)*nombre_de_pions_coin(jeu,moi)+(-63+tour)*nombre_de_mauvaises_cases_X(jeu,moi)+(-60+tour)*nombre_de_mauvaises_cases_C(jeu,moi)
        
        if tour>=48:
            
            res=res+game.getScores(jeu)[moi-1]
            
        

        return res

def jeufini(jeu):
    moi= jeu[1]%2+1
    if game.getGagnant(jeu)== jeu[1]:
        return -1000
    elif game.getGagnant(jeu) == moi:
        return 1000    
    else:
        return 0

def nombre_de_pions_coin(jeu,joueur):
    plateau=jeu[0]
    res=0
    if plateau[0][0] == joueur :  
        res+=1
            
    if plateau[0][7] == joueur:   
        res+=1
        
    if plateau[7][0] == joueur:
        res+=1

    if plateau[7][7] == joueur:
        res+=1
    return res










def nombre_de_mauvaises_cases_X(jeu,joueur):
    plateau=jeu[0]
    res=0
    if plateau[1][1] == joueur and plateau[0][0]==0:
        res+=1
        
    if plateau[6][6] == joueur and plateau[7][7]==0:
        res+=1

    if plateau[1][6] == joueur and plateau[0][7]==0:
        res+=1
        
    if plateau[6][1] == joueur and plateau[7][0]==0:
        res+=1

    return res


def nombre_de_mauvaises_cases_C(jeu,joueur):
    plateau=jeu[0]
    res=0
    if  plateau[0][1] == joueur and plateau[0][0]==0:
        res+=1
        
    if plateau[1][0] == joueur and plateau[0][0]==0:
        res+=1

    if plateau[0][6] == joueur and plateau[0][7]==0:
        res+=1
        
    if plateau[1][7] == joueur and plateau[0][7]==0:
        res+=1
        
    if plateau[6][0] == joueur and plateau[7][0]==0:
        res+=1

    if plateau[7][1] == joueur and plateau[7][0]==0:
        res+=1
        
    if plateau[7][6] == joueur and plateau[7][7]==0:
        res+=1
        
    if plateau[6][7] == joueur and plateau[7][7]==0:
        res+=1

    return res

