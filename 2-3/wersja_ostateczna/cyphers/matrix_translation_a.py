'''
Created on Mar 19, 2013

@author: dracco
'''
import math

class matrix_translation_a:
    key = ["3","4","1","5","2"]
    def __init__(self,key):
        if type(key) is str:
            self.key = key.split("-")
        else:
            self.key = key
            
    def encrypt(self,word):
        dlugosc = len(word)
        licznik = 0
        if(dlugosc%len(self.key)==0):
            tablica = (dlugosc/len(self.key)+1)*[(len(self.key))*[None]]
            for i in range(0, len(tablica)):
                tablica[i] = list(word[licznik:licznik+len(self.key)])
                licznik+=len(self.key)
        else:
            tablica = (dlugosc/len(self.key)+1)*[(len(self.key)+dlugosc%len(self.key))*[None]]
            for i in range(0, len(tablica)):
                tablica[i] = list(word[licznik:licznik+len(self.key)])
                licznik+=len(self.key)
        odp=""
        for i in range(0,len(self.key)):
            for n in tablica:
                try:
                    for k in n[int(self.key[i])-1]:
                        odp+=k
                except IndexError:
                    continue
        return odp
    
    def decrypt(self,word):
        klen = len(self.key); wlen = len(word)
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
                pos = int(self.key[col-1])
            if lack > 0 and int(self.key[col-1]) > lack:
                loop = rows - 1
            else:
                loop = rows
            res[pos-1] = l
            pos += klen
            counter = (counter+1)%loop
        return "".join(res)

if __name__ == '__main__':
    c = matrix_translation_a("3-4-1-5-2")
    print c.encrypt("CRYPTOGRAPHYOSA") or ""