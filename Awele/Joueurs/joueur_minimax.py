#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 10:55:50 2019

@author: 3680558
"""

import sys
sys.path.append("../..")
import game
import math
global pmax
pmax=5
tour=0

coefs=[5,-2,2,0,0,100]


def maxValue(jeu,p):
    if p==pmax :
        return evaluation(jeu)
    vmax=-math.inf
    coups=game.getCoupsValides(jeu)
    for cp in coups :
        copie=game.getCopieJeu(jeu)
        game.joueCoup(copie,cp)
        v=min(vmax,minValue(jeu,p+1))
    return v
    
    
def minValue(jeu,p):
    if p==pmax :
        return evaluation(jeu)
    vmax=math.inf
    coups=game.getCoupsValides(jeu)
    for cp in coups :
        copie=game.getCopieJeu(jeu)
        game.joueCoup(copie,cp)
        v=max(vmax,maxValue(jeu,p+1))
    return v
        
    
def saisieCoup(jeu):
    """Jeu->Coup
       retourne le coup choisi par decision"""
    return minmaxdecision(jeu)[0]

def minmaxdecision(jeu):
    """Jeu->Coup
       retourne le coup ayant le plus haut score apres une iteration.
       hypothese : si tous les coups ont le meme score, on prend le premier coup valide"""

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

def estimation(jeu,p=1):
    """Jeu*Coup->double
       retourne l'evaluation du coup passe en parametre"""
    if p==pmax :
        return evaluation(jeu)
    vmax=None
    coups=game.getCoupsValides(jeu)
    for cp in coups :
        copie=game.getCopieJeu(jeu)
        game.joueCoup(copie,cp)
        v=estimation(copie,p+1)
        if vmax is None :
            vmax=v
        return vmax


def evaluation(jeu):
    """Jeu*coup->double
       retourne le poids du coup passe en parametre a partir de la somme des coef
       et de differentes fonctions d'evaluation"""

    joueurActif = jeu[1]
    return coefs[0]*(getScore(jeu,joueurActif)-jeu[4][joueurActif-1]) +\
           coefs[1]*getCasesDes(jeu,joueurActif) +\
           coefs[2]*getCasesAv(jeu,joueurActif) +\
           coefs[3]*getNbGraines(jeu,joueurActif) +\
           coefs[4]*getPlusDePossibilites(jeu,joueurActif) +\
           coefs[5]*getFinDePartie(jeu,joueurActif)

def getScore(jeu,joueur):
    """Jeu*int->int
       retourne le score d'un joueur"""
    return jeu[4][joueur-1]

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

    adversaire = joueur%2

    for i in range(6):
        nb_joueur+=jeu[0][joueur-1][i]
        nb_adversaire+=jeu[0][adversaire][i]

    return nb_joueur-nb_adversaire

def getPlusDePossibilites(jeu,joueur):
    """Jeu*int->int
       retourne les differentes autres possibilites de prises"""
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


def getFinDePartie(jeu,joueur):
    """Jeu*int->int
       retourne la valeur de retour de fin de partie (1=gagne -1=perdu 0=en cours)"""
    if game.finJeu(jeu):
        if game.getGagnant(jeu)==joueur :
            return 1
        else :
            return -1
    return 0