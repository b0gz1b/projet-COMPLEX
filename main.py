import numpy as np
import time
import uuid

# Un multigraphe sera représenté par une matrice d'adjacence 
# dans laquelle M[i,j] sera le nombre d'arête entre ui et uj.

class Multigraphe:
    def __init__(self,mat):
        self.mat = np.array(mat)
        self.s = [{i} for i in range(len(mat))]
    
    def __str__(self):
        return np.array2string(self.mat) + "\n" + str(self.s)

    def contraction(self,u,v):
        self.mat[u,v] = 0
        self.mat[v,u] = 0
        self.mat[u] = self.mat[u] + self.mat[v]
        self.mat[:,u] = self.mat[u]
        self.mat[v] -= self.mat[v]
        self.mat[:,v] = self.mat[v]
        self.s[u].update(self.s[v]) # Nouveau nom du sommet
        self.s[v] = {}
    
def karger(MG):
    nbS=len(MG.s)
    while nbS > 2:
        u,v = tirage_arete(MG)
        MG.contraction(u,v)
        nbS -= 1
        # print(MG)
    return list(filter(lambda a: a != {}, MG.s))[0]

def main():
    print(karger(Multigraphe(ncomplet(10))))
    for n in range(1000,10001,1000):
        f = open("output/randgraphe06.dat", "a")
        mesures = []
        G = Multigraphe(ngraphep(n,0.6))
        for a in range(1,4):
            u,v = np.random.choice(list(filter(lambda a: a != {}, G.s)),2)
            start = time.time()
            G.contraction(u,v)
            end = time.time()
            mesures.append(end-start)
        print("Taille :",n,"Temps :",np.mean(mesures))
        f.write(str(n)+" "+str(np.mean(mesures))+'\n')
        f.close()
    return 0

def ncycle(n):
    return np.array([[1 if (j == i+1 or i == j+1 or (i==0 and j==n-1) or (j==0 and i==n-1)) else 0 for j in range(n)] for i in range(n)])

def ncomplet(n):
    return np.array([[0 if j==i else 1 for j in range(n)] for i in range(n)])

def biparticomplet2k(k):
    return np.array([[0 if (j<k and i<k) or (j>=k and i>=k) else 1 for j in range(2*k)] for i in range(2*k)])

def ngraphep(n,p):
    r = np.random.rand(n*n)
    return np.array([[1 if j!=i and r[j*i]<p else 0 for j in range(n)] for i in range(n)])

def tirage_arete(MG):
    distrib = np.cumsum(MG.mat / sum(sum(MG.mat)))
    a = np.random.rand()
    for i in range(len(distrib)):
        if a < distrib[i]:
            u = i % len(MG.mat)
            v = i // len(MG.mat)
            return u,v


if __name__ == '__main__':
    main()