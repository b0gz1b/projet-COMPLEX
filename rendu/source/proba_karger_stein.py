import numpy as np
import time
import uuid
import sys
from karger import *
from graphes import *

def main():

    for g in [4]:
        if g==0:
            name = "complet"
            init = Multigraphe
            gen = ncomplet
            cmin=lambda n: n-1
        elif g==1:
            name = "cycle"
            init = MultigrapheList
            gen = ncycle
            cmin=lambda n: 2
        elif g==2:
            name = "bicomplet"
            init = Multigraphe
            gen = lambda n : nbicomplet2k(n//2)
            cmin= lambda n: (n//2)-2
        elif g==3 :
            name = "bicomplet1coupe"
            init = Multigraphe
            gen = lambda n : nbicomplet2k1coupe(n//2)
            cmin= lambda n: 1
        else:
            name = "biparti"
            init = Multigraphe
            gen = lambda n : biparticomplet2k(n//2)
            cmin= lambda n: n//2
        
        filename = "output/kargerstein/data/"+name+"_"+str(uuid.uuid4())+".dat"
        print("Mesure de karger stein sur",name)
        for n in range(10,110,10):
            it = 50
            nbTrue = 0
            f = open(filename, "a")
            Gref = init(gen(n))
            # print(Gref,cmin(n))
            for _ in range(it):
                G = copy.deepcopy(Gref)
                c,card = kargerStein(G)
                # print(c,card)
                if card==cmin(n) : nbTrue+=1
            print(n,nbTrue/it,it,"itérations")
            f.write(str(n)+" "+str(nbTrue/it)+'\n')
            f.close()
    return 0


if __name__ == '__main__':
    main()