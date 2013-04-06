import itertools
class rail():
    key = 1
    iter = 1
    decr = False
    def __init__(self, key):
        self.key = key
    
    def counter(self):
        act = self.iter
        if self.iter == self.key:
            self.decr = True
        elif self.iter == 1:
            self.decr = False
        if self.decr == True:
            self.iter -= 1
        else:
            self.iter += 1
        return act
    
    def encrypt(self, word):
        encrypted = []
        for i in range(self.key):
            encrypted.append([])
        
        for l in word:
            encrypted[self.counter()-1].append(l)
        
        return "".join(list(itertools.chain(*encrypted)))


    def decrypt(self,word, key):
        zakres = range(len(word))
        pos = []
        fence = [[None] * len(zakres) for n in range(key)]
        rails = range(key - 1) + range(key - 1, 0, -1)
        for n, x in enumerate(zakres):
            fence[rails[n % len(rails)]][n] = x
        for rail in fence:
            for c in rail:
                if c is not None:
                    pos.append(c)
        return ''.join(word[pos.index(n)] for n in zakres)