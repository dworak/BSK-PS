'''
Created on Mar 19, 2013

@author: dracco
'''

import itertools

class rail:
    key = 1
    iter = 1
    decr = False
    def __init__(self, key):
        if type(key) == str:
            key = int(key)
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

    def decrypt(self,word):
        zakres = range(len(word))
        pos = []
        fence = [[None] * len(zakres) for n in range(self.key)]
        rails = range(self.key - 1) + range(self.key - 1, 0, -1)
        for n, x in enumerate(zakres):
            fence[rails[n % len(rails)]][n] = x

        for rail in fence:
            for c in rail:
                if c is not None:
                    pos.append(c)

        return ''.join(word[pos.index(n)] for n in zakres)

if __name__ == '__main__':
    c = rail(3)
    print c.encrypt("CRYPTOGRAPHY") or ""