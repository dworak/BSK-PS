file = open("C:\\Users\\Dworak\\Dropbox\\Studia\\SEM6\\BSK\\ps\\BSK-PS\\4-5\\test2.bin","r+b").read()
#file = open("C:\\Users\\Dworak\\Downloads\\img032.jpg","r+b")
#print list(cleaned)
print [chr(ord(c)) for c in file]