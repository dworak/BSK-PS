import string, rotnn
class vigenere():
    key=""
    word=""
    def __init__(self,key,word):
        self.key = key
        self.word = word
    def encrypt(self):
        odp = ""
        dlugosc = len(self.key)
        lista = []
        for i in range (0, len(self.word)):
            lista.append ((self.word[i],
                           (ord(self.key[(i % dlugosc)])-65)))
        for (let, rotacja) in lista:
            odp = odp + rotnn.rotate(let, rotacja)
        return odp

    def decrypt(self):
        odp = ""
        dlugosc = len(self.key)
        for i in range (0, len(self.word)):
            znak = self.word[i]
            if (znak in string.letters):
                key_ord = ord(self.word[(i % dlugosc)])
                ciph_ord = ord(znak)
                res_num = key_ord - ciph_ord
                if (res_num > 0):
                    out_char = chr(91-res_num)
                else:
                    out_char = chr(65- res_num)
            odp = odp + out_char
        return odp