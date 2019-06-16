#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game


coeffs=[5,-2,2,1,1]



# La fonction dot puisque numpy n'est pas disponible sur le seveur

def dot(L1,L2):
    return sum(x*y for x,y in zip(L1,L2))

def saisieCoup(jeu):
    """Jeu->Coup
       retourne le coup choisi par decision"""
    return decision(jeu)[0]

def decision(jeu):
    """Jeu->Coup
       retourne le coup ayant le plus haut score apres une iteration.
       hypothese : si tous les coups ont le meme score, on prend le premier coup valide"""



    global moi
    moi=game.getJoueur(jeu)
    global adv
    adv = moi % 2 +1
    
    listeCoups = game.getCoupsValides(jeu)
    res=listeCoups[0]
    maxres = estimation(jeu,res)
    
    sc=[]
    
    
    for c in listeCoups :
        score = estimation(jeu,c)
        if score > maxres :
            maxres=score
            res=c
    sc.append(res)
    sc.append(score)
    return sc

def estimation(jeu,coup):
    """Jeu*Coup->double
       retourne l'evaluation du coup passe en parametre"""
    
    return evaluation(jeu)

def evaluation(jeu):
    """Jeu*coup->double
       retourne le poids du coup passe en parametre a partir de la somme des coef
       et de differentes fonctions d'evaluation"""

    global moi
    
    if game.finJeu(jeu):
        return jeufini(jeu,moi) 
    
    else:
        
        score = [game.getScores(jeu)[moi-1],getCasesDes(jeu,moi),getCasesAv(jeu,moi),getNbGraines(jeu,moi),getPrises(jeu,moi)]


        return dot(coeffs,score)



def getCasesDes(jeu,joueur):
    """jeu*int->int
       retourne le max des cases successives valant 2 ou 3
       hypothese : comme avoir des cases faibles est desavantageux, ce coef sera negatif"""
    nb=0
    nbmax=0
    for i in range(6):
        case=jeu[0][joueur-1][i]
        if case==0 or case == 1 or case == 2:
            nb+=1
        else:
            nbmax=max(nb,nbmax)
            nb=0
    nbmax=max(nb,nbmax)
    return nbmax

def getCasesAv(jeu,joueur):
    """jeu*int->int
       retourne le max des cases successives de l'adversaire valant 2 ou 3
       hypothese : comme avoir des cases faibles est desavantageux pour l'adversaire, ce coef sera positif"""
    

    nb=0
    nbmax=0
    for i in range(6):
        case=jeu[0][joueur%2][i]
        if case==0 or case == 1 or case == 2:
            nb+=1
        else:
            nbmax=max(nb,nbmax)
            nb=0
    nbmax=max(nb,nbmax)
    return nbmax

def getNbGraines(jeu,joueur):
    """Jeu*int->int
       retourne la difference de graines entre le joueur et l'adversaire"""
    nb_joueur=0
    nb_adversaire=0

    adversaire = joueur%2 +1

    for i in range(6):
        nb_joueur+=jeu[0][joueur-1][i]
        nb_adversaire+=jeu[0][adversaire - 1][i]

    return nb_joueur-nb_adversaire

def getPrises(jeu,joueur):
    """Jeu*int->int
       retourne les differentes autres possibilites de prises"""
    # Cette fonction ne sert à rien

    cases=[0,0,0,0,0,0]

    for i in range(6) :
        valeur=jeu[0][joueur-1][i]
        nbG=((valeur//12)+valeur)%12
        if joueur-1 == 0 :
            nbG-=i
        else:
            nbG-=(5-i)
        if nbG>=0 and nbG<=6 :
            cases[nbG-1]+=1
    res = 0
    for e in cases :
        if e>0:
            res+=1
    return res



def jeufini(jeu,joueur):
    
    
    if game.getGagnant(jeu)== joueur%2+1:
        return -1000
    elif game.getGagnant(jeu) == joueur:
        return 1000    
    else:
        return 0

        
