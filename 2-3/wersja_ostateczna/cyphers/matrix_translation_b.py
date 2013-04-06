'''
Created on Mar 25, 2013

@author: dracco
'''
import math

class matrix_translation_b:
    key = ""
    def __init__(self,key):
        self.key = key

    def __make_key__(self):
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
        map = dict(zip(l,range(1,len(l)+1)))
        l = []
        for i in sorted(map.keys()):
            l += [map[i]]
        return l

    def encrypt(self,word):
        word = word.replace(" ","")
        key = self.__make_key__()
        res = ""
        for k in key:
            row = 0
            while True:
                pos = k + (row * len(key))
                if pos > len(word):
                    break
                else:
                    #print k, row, pos, word[pos-1]
                    res += word[pos-1]
                    row += 1
            #print
        return res

    def decrypt(self,word):
        key = self.__make_key__()

        klen = len(key); wlen = len(word)
        lack = wlen%klen
        rows = math.ceil(wlen/(klen * 1.0))
        res = [None]*wlen
        col = 0
        counter = 0
        loop = 0
        pos = 0
        for l in word:
            if counter == 0:
                col += 1
                pos = int(key[col-1])
            if lack > 0 and int(key[col-1]) > lack:
                loop = rows - 1
            else:
                loop = rows
            res[pos-1] = l
            pos += klen
            counter = (counter+1)%loop
        return "".join(res)

if __name__ == '__main__':
    c = matrix_translation_b("convenience")
    msg = "here is a secret message enciphered by transposition"
    print c.__make_key__()
    enc = c.encrypt(msg)
    print msg.replace(" ", "") == c.decrypt(c.encrypt(msg))