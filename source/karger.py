import numpy as np

def tirage_arete(MG):
    distrib = np.cumsum(MG.mat / sum(sum(MG.mat)))
    a = np.random.rand()
    for i in range(len(distrib)):
        if a < distrib[i]:
            u = i % len(MG.mat)
            v = i // len(MG.mat)
            return u,v

def karger(MG):
    nbS=len(MG.s)
    while nbS > 2:
        u,v = tirage_arete(MG)
        MG.contraction(u,v)
        nbS -= 1
    return list(filter(lambda a: a != {}, MG.s))[0]