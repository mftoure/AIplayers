import sys
sys.path.append("../..")
import game

pmax = 2

coefs=[5,-4,4,1,1]

    

def dot(L1,L2):
    return sum(x*y for x,y in zip(L1,L2))

def saisieCoup(jeu):
    
    """ jeu -> coup
        Retourne un coup a jouer
    """

    global moi
    moi=game.getJoueur(jeu)
    global adv
    adv = moi % 2 +1
    
    
    coups = game.getCoupsValides(jeu)
    
    


    return decision(jeu,coups)[0]




def decision(jeu,coups):
    """ jeu*coups-> [coup, scoremax]
        retourne le coup et le score qui donne un plus grand score
    """
    
    
    copie=game.getCopieJeu(jeu)
    
    
    
    
    scoremax,meill_coup= estimation(copie,None,True,float('-inf'),float('inf'),0)
    
   
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
    """Jeu*coup->double
       retourne le poids du coup passe en parametre a partir de la somme des coef
       et de differentes fonctions d'evaluation"""

    global moi
    
    if game.finJeu(jeu):
        return getFinDePartie(jeu,moi) 
    
    else:
        score = [game.getScores(jeu)[moi -1],getCasesDes(jeu,moi),getCasesAv(jeu,moi),getNbGraines(jeu,moi),getPrises(jeu,moi)]

        return dot(coefs,score)
      
       



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
    global moi
    if game.finJeu(jeu):
        if game.getGagnant(jeu)==moi :
            return 1000
        else :
            return -1000

    return 0
