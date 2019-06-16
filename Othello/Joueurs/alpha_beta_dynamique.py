#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

pmax = 3 



def saisieCoup(jeu):
    

    global moi
    moi=game.getJoueur(jeu)
    global adv
    adv = moi % 2 +1
    
    global tour

    tour=(game.getScores(jeu)[moi-1]+game.getScores(jeu)[adv-1])
    
    coups=game.getCoupsValides(jeu)
    """ jeu -> coup
        Retourne un coup a jouer
    """
    


    return decision(jeu,coups)[0]




def decision(jeu,coups):
    """ jeu*coups-> [coup, scoremax]
        retourne le coup et le score qui donne un plus grand score
    """
    
    
    copie=game.getCopieJeu(jeu)
    
    
    

    # on fait un appel d'estimation sur le premier noeud avec coup qui est initialisé à None, me = True et alpha, beta respectivement en - infini et en + infini
    # et p qui est à 0
    
    scoremax,meill_coup = estimation(copie,None,True,float('-inf'),float('inf'),0)
    
   
    #for cp in coups:
    #   copie=game.getCopieJeu(jeu)
    #   game.joueCoup(copie,cp)


    #   s = estimation(copie,False,float('-inf'),float('inf'))
       
    #   if ( s == scoremax):
    #    print("((((((((((((")
    #    break
    
    # res=[]
    #res.append(cp)
    #res.append(s)
    
    return [meill_coup,scoremax]




def estimation(jeu,coup,me,alpha,beta,p=1):
  

    
    global pmax
    
    
    
    
    print(tour)

    if p==pmax or game.finJeu(jeu):
        return evaluation(jeu),coup
    
    vmax = None
  
        
    coups= game.getCoupsValides(jeu)
    for cp in coups:
        
        copie=game.getCopieJeu(jeu)
        game.joueCoup(copie,cp)
        
        if me:
            
            v,cop = estimation(copie,cp,False,alpha,beta,p+1)

            if vmax is None:
                
                vmax =v
                meill_coup = cp

                
            if (vmax<v):
                vmax =v
                meill_coup = cp
            
            
            alpha = max(alpha,vmax)
            
            if beta<=alpha:
                
                break
                
        else:
            
            v,cop = estimation(copie,cp,True,alpha,beta,p+1) 
            
            if vmax is None:
                
                vmax = v
                meill_coup=cp
        
        
            if (vmax>v):
                
                vmax=v
                meill_coup=cp
            
            
            beta = min(beta,vmax)
            

            if beta <=alpha:
                
                break    
    
    
    return vmax,meill_coup




def evaluation(jeu):
    
    global tour
    
    global moi
    
    
    if game.finJeu(jeu):
        return jeufini(jeu)
    else:
        
        
        res= (66-tour)*nombre_de_cases_coin(jeu)+(-60+tour)*nombre_de_mauvaises_cases_X(jeu)+(-63+tour)*nombre_de_mauvaises_cases_C(jeu)
        
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








