import time
tmp= time.time()


import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_humain
game.joueur1=joueur_humain
game.joueur2=joueur_humain

def initialiseJeu():

    jeu=[]
    plateau=[[4,4,4,4,4,4],[4,4,4,4,4,4]]
    jeu.append(plateau)
    jeu.append(1)
    jeu.append(None)
    jeu.append([])
    jeu.append([0,0])

    return jeu

def estAffame(jeu):
    j = game.getJoueur(jeu)
    adv = jeu[1]%2 +1
    return (sum(jeu[0][adv - 1])==0)

def nourrit(jeu,coup):

    j=game.getJoueur(jeu)
    if j==1:
        return coup[1]<game.getCaseVal(jeu,coup[0],coup[1])
    return game.getCaseVal(jeu, coup[0],coup[1])>= 5 - coup[1]

def getCoupsValides(jeu):
    
    a=estAffame(jeu)
    j=game.getJoueur(jeu)

    return[(j-1,i) for i in range (6) if game.getCaseVal(jeu,j-1,i)>0 and ((not a) or nourrit(jeu,(j-1,i)))]

def nextCase(l,c,horaire=False):

    if horaire:
        if c==5 and l==0:
            return (1,c)
        if c==0 and l==1:
            return (0,c)
        if l==0:
            return (l,c+1)
        if l==1:
            return (l,c-1)
    else:
        if c==0 and l ==0:
            return (1,0)
        if c==5 and l==1:
            return (0,5)
        if (l==0):
            return (l,c-1)
        if (l==1):
            return (l,c+1)

def distribue(jeu,case):
    
    v=game.getCaseVal(jeu,case[0],case[1])
    jeu[0][case[0]][case[1]]=0
    
    nc=case
    while v>0 :
    
        nc=nextCase(nc[0],nc[1])
        
        if not nc==case :
            
            jeu[0][nc[0]][nc[1]]+=1
            v-=1
    return nc

def joueCoup(jeu,coup):

    """jeu*coup->void
       joue le coup joue par le joueur, met a jour le plateau et les scores"""
    
    case=distribue(jeu,coup)
    print(case)
    save=game.getCopieJeu(jeu)
    l=case[0]
    c=case[1]
    j=jeu[1]
    v=game.getCaseVal(jeu,l,c)
    print(v)
    
    while (l==(j%2+1) -1):
        print(v)
        if ((v==2) or (v==3)):
            
            jeu[0][l][c]=0
            jeu[4][j - 1]+=v
            
        l,c=nextCase(l,c,True)
        v=game.getCaseVal(jeu,l,c)
        if estAffame(jeu):
            jeu[0]=save[0]
            jeu[-1]=save[-1]
    

    
    jeu[1]=jeu[1]%2+1
    jeu[2]= None
    jeu[3].append(coup)
    



#def finJeu(jeu):
#        
#    if (jeu[3]!=[]  and len(jeu[3])>=100 ):
#        return True

#    if (jeu[2]!=None and len(jeu[2])==0) :
#        return True

#    if jeu[4][0]>24 or jeu[4][1]>24:
#        return True

#    else :
#        return False

def finJeu(jeu):
    
    #if jeu[3]==[]:
    #    return False
    
    #if jeu[2] is None:
    #    return False
    
    #return len(jeu[3])==64 or jeu[2]==[]
    coups=getCoupsValides(jeu)
    

    return len(coups)==0 or len(jeu[3])>=100
    





def copieJeu(jeu):
    plateau=[]
    for i in range (2):
        plateau.append([])
        for j in range (6):
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