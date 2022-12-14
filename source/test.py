import numpy as np
import time
import uuid
import sys
import copy
from graphes import *
from karger import *

def main(argv):
    
    # mat = ncomplet(1000)
    # isoles = list(np.random.choice(np.arange(1000),size=500,replace=False))
    # print(isoles,mat[isoles])
    # mat[isoles] = np.zeros((500,1000))
    # mat[:,isoles] = mat[isoles].T
    # print(len(MultigrapheList(mat).adjList.keys()))

    # m = MultigrapheList(ncomplet(10))
    # print(m)
    # print("karger stein\n")
    # print(kargerStein(m))
    # print(m.get_nb_arete())
    # print(m)
    # print("\n")
    print("Karger-Stein avec matrice")
    mref = Multigraphe(ncomplet(10))
    print(mref)
    C, card = kargerStein(mref)
    print(C,card)
    print("Karger-Stein avec listes")
    mref = MultigrapheList(ncomplet(10))
    print(mref)
    C, card = kargerStein(mref)
    print(C,card)
    # 
    # print("---Contraction 0 et 1")
    # m.contraction({0},{1})
    # mref.contraction(0,1)
    # print(m)
    # print(mref)
    # print("---Contraction {0,1} et 2")
    # m.contraction({2},{0,1})
    # mref.contraction(2,0)
    # print(m)
    # print(mref)
    

    return 0


if __name__ == '__main__':
    main(sys.argv[1:])