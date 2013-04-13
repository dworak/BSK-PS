'''
Created on Apr 7, 2013

@author: Dworak
'''
import ctypes
import os
from copy import copy  
from random import randint, seed,shuffle, choice
import string

STD_OUTPUT_HANDLE = -11
BLUE    = 0x0001
GREEN   = 0x0002
RED     = 0x0004
PURPLE  = 0x0005
YELLOW  = 0x0006
WHITE   = 0x0007
GRAY    = 0x0008
GREY    = 0x0008
AQUA    = 0x0009
CYAN    = 0x0003

kolory = [CYAN,GREEN,RED,PURPLE,YELLOW,WHITE,GRAY,GREY,AQUA]
alfabet=range(0,26) 
def get_csbi_attributes(handle):
    import struct
    csbi = ctypes.create_string_buffer(22)
    res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, csbi)
    assert res

    (bufx, bufy, curx, cury, wattr,
    left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
    return wattr

handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
reset = get_csbi_attributes(handle)
      
class enigma:
    def __init__(self, iloscRotorow,znakiSpecjalne,password):  
        self.znakiSpecjalne=znakiSpecjalne  
        self.iloscRotorow=iloscRotorow		
        self.rotory=[]
        self.password = password
        self.passwordLen = len(password)
		#tworzenie poszczegolnych wirnikow  
        for i in range(0,self.iloscRotorow): 
            self.rotory.append(rotor())
            if(i<self.passwordLen):
                self.rotory[i].create(self.password[i],i)
            else:
                self.rotory[i].create(self.password[i%self.passwordLen],i)  
  
        #tworzenie reflektora
        _alfabet=copy(alfabet)  
        self.reflector=copy(alfabet)  
        while len(_alfabet)>0:  
            a=choice(_alfabet)  
            _alfabet.remove(a)  
            b=choice(_alfabet)  
            _alfabet.remove(b)  
            self.reflector[a]=b  
            self.reflector[b]=a  
  
    def podgladUstawien(self):		
        print 'Ilosc wirnikow: ', self.iloscRotorow ,"\n\nUstawienia poczatkowe wirnikow:"		
        for i in range(0,self.iloscRotorow):
            kolor = choice(kolory)			
            print ",".join([chr(i+65) for i in self.rotory[i].transformation])		
        print '\nUstawienia bebna odwracajacego:\n'
        for i  in self.reflector:
            print '(',unichr(i+65),'\t',unichr(self.reflector[i]+65),')'
        print '\n'  
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
				#przejscie przez poszczegolne rotory
                for i in range(0,self.iloscRotorow):  
                    num=self.rotory[i].passthrough(num)  
                num=self.reflector[num] #przejscie przez beben  
                for i in range(0,self.iloscRotorow): #przejscie z powrotem przez poszczegolne rotory  
                    num=self.rotory[self.iloscRotorow-i-1].passthroughrev(num)  
                ciphertext+=""+chr(97+num) # dodaj zaszyfrowana litere do tekstu wynikowego  
				#obsluga obrotu rotorow, jesli zajdzie potrzeba
                for i in range(0,self.iloscRotorow):  
                    if ( ln % ((i*6)+1) == 0 ):  
                        self.rotory[i].rotate()
        return ciphertext  
class rotor:  
    def create(self, password, nrRotoru):  
        self.transformation=copy(alfabet)
        self.nrRotoru=nrRotoru
        #self.list = list(password)
        #print self.list
        #self.ordlist = [ord(i) for i in self.list]
        #''.join([str(n) for n in self.ordlist])
        #print ord(password)
        seed(ord(password)) 
        shuffle(self.transformation) #odpowiednie losowe pomieszanie wartosci do rotora
        return  
    def passthrough(self,i):  
        return self.transformation[i]  
    def passthroughrev(self,i):  
        return self.transformation.index(i)  
    def rotate(self):  
        self.transformation=przestaw(self.transformation, 1, self.nrRotoru)  
    def setcog(self,a):  
        self.transformation=a  
        
def przestaw(l, n, nr):
    a = l[n:] + l[:n]
    kolor = kolory[nr%len(kolory)]
    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, kolor)
    print '('+str(nr)+')'+nr*" "+"".join([chr(i+65) for i in a])
    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
    return a

#file = open("C:\\Users\\Dworak\\Dropbox\\Studia\\SEM6\\BSK\\ps\\BSK-PS\\4-5\\test.txt","r+b")
#plaintext=file.read()

fileName = raw_input("Czy chcesz podac inna sciezke niz standardowa? (jesli tak podaj, w przeciwnym wypadku ENTER)\nSciezka do pliku: ")
if(len(fileName)==0): 
	plaintext= open("C:\\Users\\Dworak\\Dropbox\\Studia\\SEM6\\BSK\\ps\\BSK-PS\\4-5\\wejscie.txt","r+b").read()
else:
	if(os.path.exists(os.path.abspath(str(fileName)))):
		plaintext = open(str(fileName),"r").read()
	else:
		print "Podany plik nie istnieje"
		exit()
	
#raw_input("Podaj tekst do zakodaowania: ")
numberOfRotors = raw_input("Podaj ilosc rotorow: ")
passwordToGetRotorsPosition = raw_input("Podaj haslo do odczytu poczatkowych pozycji rotorow: ") 
x=enigma(int(numberOfRotors),True,passwordToGetRotorsPosition)   
x.podgladUstawien();
print '\nTekst do zaszyfrowania, odszyfrowania:\n'+plaintext+'\n'
print '\nPoszczegolne obroty wirnikow: '  
ciphertext=x.encode(plaintext)  
print '\nTekst zaszyfrowany, odszyfrowany\n'+ciphertext+'\n'
file = open("C:\\Users\\Dworak\\Dropbox\\Studia\\SEM6\\BSK\\ps\\BSK-PS\\4-5\\wyjscie.txt","w")
file.write(ciphertext)
#x.reset()
'''
ciphertext = raw_input("Podaj tekst do odszyfrowania: ")
numberOfRotors = raw_input("Podaj ilosc rotorow: ")
passwordToGetRotorsPosition = raw_input("Podaj haslo do odczytu poczatkowych pozycji rotorow: ")
y=enigma(int(numberOfRotors),True,passwordToGetRotorsPosition)   
plaintext=y.encode(ciphertext)
file = open("C:\\Users\\Dworak\\Dropbox\\Studia\\SEM6\\BSK\\ps\\BSK-PS\\4-5\\wejscie_zakodowane.txt","w")
file.write(plaintext)
print ("\nTekst odszyfrowany:\n"+plaintext+"\n")
'''
'''
rotorsConfigInt = []
for row in x.oCogs:
    print ''.join(map(str, row)) 
    rotorsConfigInt.append(''.join(map(str, row)))
result = ''.join(rotorsConfigInt)
print result
'''