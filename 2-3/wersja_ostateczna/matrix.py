'''
Created on Mar 25, 2013

@author: dracco
'''
import math
import itertools

class matrix_translation_b:
    key = ""
    def __init__(self,key):
        self.key = key

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

        for c in sorted(k.keys()):
            for idx in k[c]:
                for i in range(int(math.ceil(1.0 * len(word) / len(self.key)))):
                    index = idx + i*(len(self.key))
                    if index < len(word): 
                        res += word[index]
        return res

    def decrypt(self,word):
        k = list(set(self.key))
        k.sort()
        k = dict(zip(k, [None]*len(k)))
        res = ""
        for c in range(len(self.key)):
            if k[self.key[c]] is None:
                k[self.key[c]] = [c]
            else:
                k[self.key[c]] += [c]

        key = list(itertools.chain(*k.values()))

        klen = len(key); wlen = len(word)
        lack = wlen%klen
        rows = math.ceil(wlen/(klen * 1.0))
        res = [None]*wlen
        col = 0
        counter = 0
        loop = 0
        print lack
        pos = 0
        for l in word:
            print "Letter:",l
            if counter == 0:
                col += 1
                pos = int(key[col-1])
            print "Counter:",counter
            if lack > 0 and int(key[col-1]) > lack:
                loop = rows - 1
            else:
                loop = rows
            print "Loop:",loop,"key & col",key[col-1], col, "Pos:",pos
            res[pos-1] = l
            pos += klen
            counter = (counter+1)%loop
        return "".join(res)

if __name__ == '__main__':
    c = matrix_translation_b("convenience")
    print c.encrypt("here is a secret message enciphered by transposition") or ""