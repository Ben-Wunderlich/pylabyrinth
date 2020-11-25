
class DisjointKringle:
    def __init__(self, startelems):
        self.maindict = dict()
        self.diffSets = len(startelems)
        for i, el in enumerate(startelems):
            self.maindict[el] = i
            #print(el)

    def areBros(self, mario, luigi):
        return self.maindict[mario] == self.maindict[luigi]
    
    def union(self, mario, luigi):
        self.diffSets -=1
        marioVal = self.maindict[mario]
        luigiVal = self.maindict[luigi]
        for el in self.maindict.keys():
            if self.maindict[el] == luigiVal:
                self.maindict[el] = marioVal

    def numSets(self):
        return self.diffSets