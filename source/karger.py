import numpy as np
import copy
def karger(MG):
    nbS=len(MG.s)
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