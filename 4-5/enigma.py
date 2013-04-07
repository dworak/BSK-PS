'''
Created on Apr 7, 2013

@author: Dworak
'''
from random import shuffle,randint,choice, seed  
from copy import copy  
alphabet=range(0,26)  
      
class enigma:
    def __init__(self, iloscRotorow,znakiSpecjalne,password):  
        self.znakiSpecjalne=znakiSpecjalne  
        self.iloscRotorow=iloscRotorow  
        self.rotory=[]  
        self.oCogs=[] # kopia polozenia wirnikow, do resetu  
        self.password = password
        self.passwordLen = len(password)
        for i in range(0,self.iloscRotorow): #tworzenie poszczegolnych wirnikow  
            self.rotory.append(rotor())
            if(i<self.passwordLen):
                self.rotory[i].create(self.password[i])
            else:
                self.rotory[i].create(self.password[i%self.passwordLen])
            self.oCogs.append(self.rotory[i].transformation)  
  
        #tworzenie bebna odwracajacego
        _alphabet=copy(alphabet)  
        self.reflector=copy(alphabet)  
        while len(_alphabet)>0:  
            a=choice(_alphabet)  
            _alphabet.remove(a)  
            b=choice(_alphabet)  
            _alphabet.remove(b)  
            self.reflector[a]=b  
            self.reflector[b]=a  
  
    def podgladUstawien(self):  
        print 'Ilosc wirnikow: ', self.iloscRotorow ,"\n\nUstawienia poczatkowe wirnikow:"  
        for i in range(0,self.iloscRotorow):  
            print ([self.rotory[i].transformation])  
        print 'Ustawienia bebna odwracajacego:\n',self.reflector,'\n'  
  
    def reset(self):  
        for i in range(0,self.iloscRotorow):  
            self.rotory[i].setcog(self.oCogs[i])  
  
    def encode(self,text):  
        ln=0  
        ciphertext=""  
        for l in text.lower():  
            num=ord(l)%97  
            if (num>25 or num<0):  
                if (self.znakiSpecjalne):
                    ciphertext+=l  
                else:  
                    pass  
            else:  
                ln+=1  
                for i in range(0,self.iloscRotorow): #przejscie przez poszczegolne rotory 
                    num=self.rotory[i].passthrough(num)  
  
                num=self.reflector[num] #przejscie przez beben  
  
                for i in range(0,self.iloscRotorow): #przejscie z powrotem przez poszczegolne rotory  
                    num=self.rotory[self.iloscRotorow-i-1].passthroughrev(num)  
                ciphertext+=""+chr(97+num) # dodaj zaszyfrowana litere do tekstu wynikowego  
  
                for i in range(0,self.iloscRotorow): #obracanie rotorow  
                    if ( ln % ((i*6)+1) == 0 ):  
                        self.rotory[i].rotate()  
        return ciphertext  
class rotor:  
    def create(self, password):  
        self.transformation=copy(alphabet)
        #self.list = list(password)
        #print self.list
        #self.ordlist = [ord(i) for i in self.list]
        #''.join([str(n) for n in self.ordlist])
        #print ord(password)
        seed(ord(password)) 
        shuffle(self.transformation) #odpowiednie pomieszanie wartosci do rotora
        return  
    def passthrough(self,i):  
        return self.transformation[i]  
    def passthroughrev(self,i):  
        return self.transformation.index(i)  
    def rotate(self):  
        self.transformation=przestaw(self.transformation, 1)  
    def setcog(self,a):  
        self.transformation=a  
		
def przestaw(l, n): 
    return l[n:] + l[:n]  		

#file = open("C:\\Users\\Dworak\\Dropbox\\Studia\\SEM6\\BSK\\ps\\BSK-PS\\4-5\\test.txt","r+b")
#plaintext=file.read()
plaintext = "dworakowski lukasz mam na imie a moja mama to malgorzata"
 
x=enigma(3,True,"hasloDoGenerowania")   
x.podgladUstawien();
print ("Teskt do zaszyfrowanie:\n"+plaintext+"\n")  
ciphertext=x.encode(plaintext)  
print ("Tekst zaszyfrowany\n"+ciphertext+"\n")
#x.reset()
  
 
y=enigma(3,True,"hasloDoGenerowania")   
plaintext=y.encode(ciphertext)
print ("Plaintext:\n"+plaintext+"\n")

'''
rotorsConfigInt = []
for row in x.oCogs:
    print ''.join(map(str, row)) 
    rotorsConfigInt.append(''.join(map(str, row)))
result = ''.join(rotorsConfigInt)
print result
'''