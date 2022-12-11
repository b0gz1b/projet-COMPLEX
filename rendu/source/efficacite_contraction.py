import numpy as np
import time
import uuid
import sys
import copy
from karger import *
from graphes import *

def main(argv):
    i = int(argv[0])
    g = int(argv[1])

    if i==0:
        imp = "matrice"
        init = Multigraphe
    else:
        imp = "liste"
        init = MultigrapheList

    if g==0:
        name = "complet"
        gen = ncomplet
    elif g==1:
        name = "cycle"
        gen = ncycle
    elif g==2:
        name = "biparti"
        gen = lambda n : biparticomplet2k(n//2)
    else:
        name = "rand08"
        gen = lambda n : ngraphep(n,0.8 if len(argv) < 3 else int(argv[2]))

    print("Mesure de contraction sur",name,"avec",imp)

    filename = "output/contraction/"+imp+"_adjacence/data/"+name+"_"+str(uuid.uuid4())+".dat"
    for n in range(1000,10001,500):
        f = open(filename, "a")
        mesures = []
        save = init(gen(n))
        for a in range(50):
            G = copy.deepcopy(save)
            u,v = G.tirage_arete()
            start = time.time()
            G.contraction(u,v)
            end = time.time()
            mesures.append(end-start)
        print("Taille :",n,"Temps :",np.mean(mesures))
        f.write(str(n)+" "+str(np.mean(mesures))+'\n')
        f.close()
    return 0


if __name__ == '__main__':
    main(sys.argv[1:])