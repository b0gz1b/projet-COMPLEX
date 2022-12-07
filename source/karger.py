import numpy as np

def karger(MG):
    nbS=len(MG.s)
    while nbS > 2:
        u,v = MG.tirage_arete()
        MG.contraction(u,v)
        nbS -= 1
    C = list(filter(lambda a: a != {}, MG.s))[0]
    return C
