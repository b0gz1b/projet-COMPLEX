import numpy as np
import time
import uuid
import sys
from karger import *
from graphes import *

def main():
    n=10
    T=20
    it=(n*(n-1))//2

    for i in range(2):
        for g in range(3):
            if i==0:
                imp = "matrice"
                init = Multigraphe
            else:
                imp = "liste"
                init = MultigrapheList

            if g==0:
                name = "complet"
                gen = ncomplet
                cmin=n-1
            elif g==1:
                name = "cycle"
                gen = ncycle
                cmin=2
            else:
                name = "biparti"
                gen = lambda n : biparticomplet2k(n//2)
                cmin=n/2
            
            print("Mesure de karger sur",name,"avec",imp,"mesure sur",it)

            nbTrue = 0
            for _ in range(it):
                    
                G = init(gen(n))
                karger(G)
                if G.get_nb_arete()==cmin : nbTrue+=1

            print(it,"itérations ","NbTrue :",nbTrue,)
        
    return 0


if __name__ == '__main__':
    main()