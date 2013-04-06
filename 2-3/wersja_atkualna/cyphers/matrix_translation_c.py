'''
Created on Mar 25, 2013

@author: dracco
'''
import math

class matrix_translation_c:
    key = ""
    def __init__(self,key):
        self.key = key

    def __make_table__(self, k, word):
        pos = 0
        row = 0
        tab = []
        keys = sorted(k.keys())
        c = 0
        while True:
            for idx in k[keys[c]]:
                tab += [""]
                for i in range(idx+1):
                    tab[row] += word[pos]
                    pos += 1
                    if (pos >= len(word)):
                        return tab
                row += 1
            c = (c + 1) % len(keys)
        return tab

    def encrypt(self,word):
        word = word.replace(" ","")
        k = list(set(self.key))
        k.sort()
        k = dict(zip(k, [None]*len(k)))
        res = ""
        for c in range(len(self.key)):
            if k[self.key[c]] is None:
                k[self.key[c]] = [c]
            else:
                k[self.key[c]] += [c]

        tab = self.__make_table__(k, word)
        for c in sorted(k.keys()):
            for idx in k[c]:
                for col in tab:
                    if idx < len(col):
                        res += col[idx]
        return res

if __name__ == '__main__':
    c = matrix_translation_c("convenience")
    print c.encrypt("here is a secret message enciphered by transposition") or ""