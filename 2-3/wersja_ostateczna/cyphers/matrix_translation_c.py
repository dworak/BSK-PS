'''
Created on Mar 25, 2013

@author: dracco
'''
import math
from timeit import itertools

class matrix_translation_c:
    key = ""
    def __init__(self,key):
        self.key = key

    def __make_key__(self):
        k = list(set(self.key))
        k.sort()
        k = dict(zip(k, [None]*len(k)))
        for c in range(len(self.key)):
            if k[self.key[c]] is None:
                k[self.key[c]] = [c]
            else:
                k[self.key[c]] += [c]
        return k

    def __make_key2__(self):
        k = list(set(self.key))
        k.sort()
        l = [None]*len(self.key)
        key = dict(zip(k, [None]*len(k)))
        for c in range(len(self.key)):
            if key[self.key[c]] is None:
                key[self.key[c]] = [c+1]
            else:
                key[self.key[c]] += [c+1]
        i = 0
        for c in sorted(key):
            for idx in key[c]:
                i+=1
                l[idx-1] = i
        map = dict(zip(range(1,len(l)+1),l))
        l = []
        for i in sorted(map.keys()):
            l += [map[i]]
        return l

    def __make_table__(self, k, word):
        pos = 0
        row = 0
        tab = []
        for c in sorted(k.keys()):
            for idx in k[c]:
                tab += [""]
                for i in range(idx+1):
                    tab[row] += word[pos]
                    pos += 1
                    if (pos >= len(word)):
                        return tab
                row += 1
        return tab

    def encrypt(self,word):
        word = word.replace(" ","")
        res = ""
        k = self.__make_key__()
        tab = self.__make_table__(k, word)
        for t in tab:
            for c in t:
                print c,
            print
        for c in sorted(k.keys()):
            for idx in k[c]:
                for col in tab:
                    if idx < len(col):
                        res += col[idx]
        return res

    def decrypt(self,word):
        word = word.replace(" ","")
        res = ""
        k = self.__make_key2__()
        print k
        for i in k:
            row = 0
            while True:
                pos = i+(row*len(k))
                if pos >= len(word):
                    break
                print word[pos],
                row += 1
        

if __name__ == '__main__':
    c = matrix_translation_c("convenience")
    enc = c.encrypt("here is a secret message enciphered by transposition")
    print enc or ""
    print c.decrypt(enc)