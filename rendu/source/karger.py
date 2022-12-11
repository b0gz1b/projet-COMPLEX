import numpy as np
import copy

def karger(MG):
    nbS=MG.get_nb_sommet()
    while nbS > 2:
        u,v = MG.tirage_arete()
        MG.contraction(u,v)
        nbS -= 1
    C = list(filter(lambda a: a != {}, MG.s))[0]
    return C

def kargerIt(MG,T):
    G=copy.deepcopy(MG)
    sopt=karger(G)
    Gopt=G
    mopt=G.get_nb_arete()
    for _ in range(T-1):
        G=copy.deepcopy(MG)
        s=karger(G)
        m=G.get_nb_arete()
        if m<mopt:
            Gopt=G
            sopt=s
            mopt=m
    MG.copy(Gopt)

    return sopt,mopt

def contraction_partielle(MG,t):
    nbS = MG.get_nb_sommet()
    while nbS > t:
        u,v = MG.tirage_arete()
        MG.contraction(u,v)
        nbS -= 1

def kargerStein(MG):
    nbS = MG.get_nb_sommet()
    if nbS <= 6:
        return MG.rechercheExhaustive()
    else:
        t = np.ceil(1+nbS/np.sqrt(2))
        MG2 = copy.deepcopy(MG)
        contraction_partielle(MG,t)
        s1,m1 = kargerStein(MG)
        contraction_partielle(MG2,t)
        s2,m2 = kargerStein(MG2)
        if m1 < m2:
            return s1,m1
        else:
            return s2,m2
