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
        name = "rand05"
        gen = lambda n : ngraphep(n,0.5 if len(argv) < 3 else int(argv[2]))

    print("Mesure de karger sur",name,"avec",imp)

    filename = "output/karger/"+imp+"_adjacence/data/"+name+"_"+str(uuid.uuid4())+".dat"
    filename2 = "output/karger/"+'liste'+"_adjacence/data/"+name+"_"+str(uuid.uuid4())+".dat"
    for n in range(100,1001,50):
        f = open(filename, "a")
        f2 = open(filename2, "a")
        mesures = []
        mesures2 = []
        for a in range(5):
            m = gen(n)
            G = init(m)
            G2 = MultigrapheList(m)
            start = time.time()
            karger(G)
            end = time.time()
            mesures.append(end-start)
            start = time.time()
            karger(G2)
            end = time.time()
            mesures2.append(end-start)

        print("Taille :",n,"Temps :",np.mean(mesures))
        print("Taille :",n,"Temps :",np.mean(mesures2))
        f.write(str(n)+" "+str(np.mean(mesures))+'\n')
        f2.write(str(n)+" "+str(np.mean(mesures2))+'\n')
        f.close()
        f2.close()
    return 0


if __name__ == '__main__':
    main(sys.argv[1:])