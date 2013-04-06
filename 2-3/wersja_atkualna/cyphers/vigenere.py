'''
Created on Mar 25, 2013

@author: dracco
'''
import string
import rotnn
class vigenere:
    key=""
    word=""
    def __init__(self,key):
        self.key = key
    def encrypt(self, word):
        odp = ""
        dlugosc = len(self.key)
        lista = []
        for i in range (0, len(word)):
            lista.append ((word[i],
                           (ord(self.key[(i % dlugosc)])-65)))
        for (let, rotacja) in lista:
            odp = odp + rotnn.rotate(let, rotacja)
        return odp

    def decrypt(self, word):
        odp = ""
        dlugosc = len(self.key)
        for i in range (0, len(word)):
            znak = word[i]
            if (znak in string.letters):
                key_ord = ord(word[(i % dlugosc)])
                ciph_ord = ord(znak)
                res_num = key_ord - ciph_ord
                if (res_num > 0):
                    out_char = chr(91-res_num)
                else:
                    out_char = chr(65- res_num)
            odp = odp + out_char
        return odp

if __name__ == '__main__':
    c = vigenere("BREAKBREAKBR")
    print c.encrypt("CRYPTOGRAPHY") or ""