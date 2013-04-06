'''
Created on Mar 25, 2013

@author: dracco
'''
from cypher import cypher
from main.Totient import Totient

class caesar:
    key = 12
    n = 26
    lower = 97
    upper = 65
    def __init__(self, key):
        if type(key) == str:
            key = int(key)
        self.key = key
        key0 = self.key/10
        key1 = self.key%10
        higher = max(key0, key1, )
        for i in range(2,higher):
            assert key0%i != 0 and key1%i != 0

    def encrypt(self, word):
        k = list(word)
        k0 = self.key/10
        k1 = self.key%10
        for i in range(len(k)):
            char = ord(k[i])
            scale = 0
            if self.lower <= char <= self.lower+self.n:
                scale = self.lower
            elif self.upper <= char <= self.upper+self.n:
                scale = self.upper
            ascii = char - scale
            if ascii > self.n:
                return word
            k[i] = chr(((ascii*k1 + k0 ) % self.n) + scale)
        return "".join(k)
    
    def decrypt(self, word):
        k = list(word)
        k0 = self.key/10
        k1 = self.key%10
        phi = Totient(self.n)
        for i in range(len(k)):
            char = ord(k[i])
            scale = 0
            if self.lower <= char <= self.lower+self.n:
                scale = self.lower
            elif self.upper <= char <= self.upper+self.n:
                scale = self.upper
            ascii = char - scale
            if ascii > self.n:
                return word
            k[i] = chr( ( ( ascii + (self.n-k0) )* (k1**(phi-1)) % self.n) + scale)
        return "".join(k)
    
if __name__ == '__main__':
    c = cypher()
    try:
        c = caesar(21)
    except:
        print "Invalid key"
    word = "CRYPTOGRAPHY"
    print c.decrypt(c.encrypt(word)) == word