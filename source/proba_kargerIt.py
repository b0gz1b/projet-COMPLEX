import numpy as np
import time
import uuid
import sys
from karger import *
from graphes import *

def main():

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
                tS=5
                nI=6
                nS=107
                it=1000
            elif g==1:
                name = "bicomplet"
                gen = nbicomplet
                tS=20
                nI=6
                nS=57
                it=500
            else:
                name = "biparti"
                gen = lambda n : biparticomplet2k(n//2)
                tS=6
                nI=10
                nS=101
                it=1000
            print("Mesure de karger sur",name,"avec",imp)
            filename = "../output/kargerIt/"+imp+"_adjacence/data/"+name+".dat"
            
            for n in range(nI,nS,10):
                f = open(filename, "a+")
                if g==0:
                    cmin=n-1
                elif g==1:
                    cmin=n//2-2
                else:
                    cmin=n/2
                
                for T in range(1,tS):
                    nbTrue = 0
                    for _ in range(it):
                            
                        G = init(gen(n))
                        _,nbA=kargerIt(G,T)

                        if nbA==cmin : nbTrue+=1
                    print("T= ",T,", n= ",n,"NbTrue :",nbTrue)
                    f.write(str(n)+" "+str(T)+" "+str(nbTrue)+"\n")
                f.close()
    return 0


if __name__ == '__main__':
    main()