import numpy as np
import time
import uuid
import sys
from karger import *
from graphes import *

def main(argv):
    g = int(argv[0])

    if g==0:
        name = "complet_"
    elif g==1:
        name = "cycle_"
    elif g==2:
        name = "biparti_"  
    else:
        name = "rand08_"

    print("Mesure de karger sur",name)

    filename = "output/karger/matrice_adjacence/data/"+name+str(uuid.uuid4())+".dat"
    for n in range(100,1001,50):
        f = open(filename, "a")
        mesures = []

        for a in range(1):
            if g==0:
                G = Multigraphe(ncomplet(n))
            elif g==1:
                G = Multigraphe(ncycle(n))
            elif g==2:
                G = Multigraphe(biparticomplet2k(n//2))  
            else:
                G = Multigraphe(ngraphep(n,0.8))
            
            u,v = tirage_arete(G)
            start = time.time()
            karger(G)
            end = time.time()
            mesures.append(end-start)

        print("Taille :",n,"Temps :",np.mean(mesures),u,v)
        f.write(str(n)+" "+str(np.mean(mesures))+'\n')
        f.close()
    return 0


if __name__ == '__main__':
    main(sys.argv[1:])