import numpy as np
import time
import uuid
import sys
import copy
from graphes import *

def main(argv):
    g = int(argv[0])
    if g==0:
        name = "complet"
    elif g==1:
        name = "cycle"
    elif g==2:
        name = "biparti"  
    else:
        name = "rand08"

    print("Mesure de contraction sur",name)

    filename = "output/contraction/data/"+name+"_"+str(uuid.uuid4())+".dat"
    for n in range(1000,10001,500):
        f = open(filename, "a")
        mesures = []

        if g==0:
            G = Multigraphe(ncomplet(n))
        elif g==1:
            G = Multigraphe(ncycle(n))
        elif g==2:
            G = Multigraphe(biparticomplet2k(n//2))  
        else:
            G = Multigraphe(ngraphep(n,0.8))

        for a in range(50):
            u,v = tirage_arete(G)
            start = time.time()
            G.contraction(u,v)
            end = time.time()
            mesures.append(end-start)
        print("Taille :",n,"Temps :",np.mean(mesures),u,v)
        f.write(str(n)+" "+str(np.mean(mesures))+'\n')
        f.close()
    return 0


if __name__ == '__main__':
    main(sys.argv[1:])