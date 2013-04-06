class matrix_translation():
    key = list("34152")
    d = 5
    def __init__(self,key,d):
        self.key = key
        self.d = d
    def encrypt(self,word):
        dlugosc = len(word)
        licznik = 0
        if(dlugosc%self.d==0):
            tablica = (dlugosc/self.d+1)*[(self.d)*[None]]
            for i in range(0, len(tablica)):
                tablica[i] = list(word[licznik:licznik+self.d])
                licznik+=self.d
        else:
            tablica = (dlugosc/self.d+1)*[(self.d+dlugosc%self.d)*[None]]
            for i in range(0, len(tablica)):
                tablica[i] = list(word[licznik:licznik+self.d])
                licznik+=self.d
        odp=""
        for i in range(0,self.d):
            for n in tablica:
                try:
                    for k in n[int(self.key[i])-1]:
                        odp+=k
                except IndexError:
                    continue
        return odp