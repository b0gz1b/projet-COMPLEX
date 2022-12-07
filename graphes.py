import numpy as np
import itertools
import copy

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
        self.mat[u] += self.mat[v]
        self.mat[v] = np.zeros(len(self.mat),dtype='int32')
        self.mat[:,u] = self.mat[u]
        self.mat[:,v] = self.mat[v]
        self.mat[u,v] = 0
        self.s[u].update(self.s[v]) # Nouveau nom du sommet
        self.s[v] = {}

    def tirage_arete(self):
        n = len(self.mat)
        num_arete = np.random.randint(self.get_nb_arete())
        i = 0

        for u in range(n-1):
            for v in range(u+1,n):
                nb = self.mat[u,v]
                if nb > 0:
                    if num_arete <= i + self.mat[u,v]:
                        return u, v
                    i += self.mat[u,v]

    def get_nb_arete(self):
        return np.sum(self.mat)//2
    
    def copy(self,G):
        self.mat=copy.deepcopy(G.mat)
        self.s=copy.deepcopy(G.s)

class MultigrapheList:
    def __init__(self,mat):
        tMat = len(mat)
        self.adjList = {i:[] for i in range(tMat)}
        for i in range(tMat):
            for j in range(tMat):
                if mat[i][j] != 0:
                    self.adjList[i].append(j)
        self.s = [{i} for i in range(tMat)]
    def __str__(self):
        return str(self.adjList)+"\n"+str(self.s)

    def contraction(self,u,v):
        su, u = find_set_containing_elem(u,self.s)
        sv, v = find_set_containing_elem(v,self.s)
        sommets_a_ajouter = [n for n in self.adjList[v] if not n in su] # Liste des sommets à ajouter aux adjacents de u 
        self.adjList[u] = list(filter(lambda a: not a in sv, self.adjList[u])) # On retire toute les arêtes (u,v)
        self.adjList[u] += sommets_a_ajouter # On ajoute les sommets aux voisins de u
        self.adjList.pop(v) # On supprime v et ses arêtes
        self.s[u].update(sv)
        self.s[v] = {}

    def tirage_arete(self):
        num_arete = np.random.randint(2*self.get_nb_arete())
        i = 0
        for u,l in self.adjList.items():
            if num_arete - i < len(l) :
                return u , l[num_arete - i]
            i += len(l)

    def get_nb_arete(self):
        return len(list(itertools.chain(*self.adjList.values())))//2
        
    def copy(self,G):
        self.adjList=copy.deepcopy(G.adjList)
        self.s=copy.deepcopy(G.s)
        
def ncycle(n):
    return np.array([[1 if (j == i+1 or i == j+1 or (i==0 and j==n-1) or (j==0 and i==n-1)) else 0 for j in range(n)] for i in range(n)])

def ncomplet(n):
    return np.array([[0 if j==i else 1 for j in range(n)] for i in range(n)])

def biparticomplet2k(k):
    return np.array([[0 if (j<k and i<k) or (j>=k and i>=k) else 1 for j in range(2*k)] for i in range(2*k)])

def ngraphep(n,p):
    r = np.random.rand(n*n)
    return np.array([[1 if j!=i and r[j*i]<p else 0 for j in range(n)] for i in range(n)])


def find_set_containing_elem(e,ls):
    for i in range(len(ls)):
        if e in ls[i]:
            return ls[i],i