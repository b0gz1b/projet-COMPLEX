import numpy as np
import time
import uuid
import sys
import copy
from graphes import *
from karger import *

def main(argv):
    
    m = MultigrapheList(ncomplet(5))
    print(m)
    print(karger(m))
    print(m.get_nb_arete())
    print(m)
    print("\n")
    mref = Multigraphe(ncomplet(5))
    print(mref)
    print(karger(mref))
    print(mref.get_nb_arete())
    print(mref)
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