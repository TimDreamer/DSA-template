class UnionFind:
    def __init__(self, size):
        self.pars = list(range(size))
        self.ranks = [1] * size

    def find(self, i):
        if self.pars[i] == i:
            return i
        self.pars[i] = self.find(self.pars[i])
        return self.pars[i]

    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            if self.ranks[pi] >  self.ranks[pj]:
                self.pars[pj] = pi
            else:
                self.pars[pi] = pj
