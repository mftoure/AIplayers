#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import reduce

def initialiseJeu():
    jeu=[]
    jeu.append([[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 2, 0, 0, 0], [0, 0, 0, 2, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]])
    
    
    
    jeu.append(1)
    
    jeu.append(None)
    jeu.append([])
    
    jeu.append([0,0])
    
    return jeu


def entourageVide(jeu,l,c):

    """renvoie les cases vides qui sont aux alentours d'une case (l,c)"""

    return {(l+i,c+j) for i in [-1,0,1] for j in [-1,0,1] if (c+j<=7) and (c-j>=0) and (l+i<=7) and (c-j>=0) and jeu[0][l+i][c+j]==0}

def coups(jeu):
    """renovie la liste des cases vides qui sont aux alentours des pions adverses"""
    adv=jeu[1]%2+1
    
    s=[entourageVide(jeu,l,c) for l in range(8) for c in range(8) if jeu[0][l][c] == adv]

    #fait l'union de chaque case: on aura donc pas d'occurences

    #fait l'union des ensembles
    s=reduce(lambda a,b: a|b , s)
    
    return s

def checkEncadrementsdirection(jeu,case,i,j):
    """ renvoie True si on trouve des pions adverses à encadrer"""
    ok=False    
    l,c=case
    while True:
        l+=i
        c+=j
        if (l>7) or (l<0) or (c>7) or (c<0):
            return False
        if jeu[0][l][c]==0:
            return False
        if jeu[0][l][c]==jeu[1]:
            return ok
        ok=True



def getEncadrements(jeu,case,all=True):
    """ renvoie la liste des directions dans lesquelles on a des pions adverses à encadrer"""
    L=[]
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if i==0 and j==0:
                continue
            if checkEncadrementsdirection(jeu,case,i,j):
                L.append((i,j))
                if not all:
                    break
    return L



def getCoupsValides(jeu):
    """ renvoie la liste des coups valides"""
    coup=coups(jeu)
    return [x for x in coup if len(getEncadrements(jeu,x,False))>0]



def joueCoup(jeu,coup):
    #print(jeu[4][jeu[1]])
    jeu[0][coup[0]][coup[1]]=jeu[1]
    jeu[4][jeu[1]-1]+=1
    

    for x in getEncadrements(jeu,coup):
        retournePions(jeu,coup,x)
    jeu[3].append(coup)
    jeu[2]=None
    jeu[1]=jeu[1]%2+1

def retournePions(jeu, coup, d):
    """ retourne les pions de l'adversaire"""

    x = coup[0] + d[0]
    y = coup[1] + d[1]
    
    
    while(jeu[0][x][y] != jeu[1]):
        jeu[0][x][y] = jeu[1]
        x+=d[0]
        y+=d[1]
        jeu[4][jeu[1]-1]+=1
        jeu[4][jeu[1]%2]-=1


def finJeu(jeu):
    
    #if jeu[3]==[]:
    #    return False
    
    #if jeu[2] is None:
    #    return False
    
    #return len(jeu[3])==64 or jeu[2]==[]
    coups=getCoupsValides(jeu)
    

    return len(coups)==0 
    



	
def copieJeu(jeu):
    plateau=[]
    for i in range (8):
        plateau.append([])
        for j in range (8):
            plateau[i].append(jeu[0][i][j])

    joueur=jeu[1]
    coupsValides=[]
    if (jeu[2]!=None):
        for el in jeu[2]:
            coupsValides.append(el)
    else:
        coupsValides=None

    coupsJoues=[]
    for el in jeu[3]:
        coupsJoues.append(el)
    score=[]
    for el in jeu[4]:
        score.append(el)
    
    return [plateau,joueur,coupsValides,coupsJoues,score]