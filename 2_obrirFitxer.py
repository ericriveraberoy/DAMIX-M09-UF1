from Crypto.Cipher import AES

# Obrim un fitxer de text i fiquem el contingut en un array
fitxer = open("fitxer.txt", 'r')
linies = fitxer.readlines()
fitxer.close()

# Passem el contingut del array a un String
missatge = ""
for linia in linies:
    missatge = missatge + linia

# Codigiquem el missatge tenint en compte que els
# caracters sempre han de ser multiples de 16
#   1. Generem les claus i l'objecte encarregat de la encriptacio/desencriptacio
clau = b"1234567898765432"
iv = b"1111111111111111"
obj = AES.new(clau, AES.MODE_CBC, iv)

#   2. Abans de encriptar, comprovem que l'String sigui multiple de 16
#      (afegim 0 al final si es necessari).
num = len(missatge)
mod = num % 16
if mod > 0:
    padding = 16 - mod
    missatge += "0" * padding

#   3. Encriptem el missatge
codificat = obj.encrypt(missatge)

#   4. Mostrem el missatge encriptat
print("Missatge original:", missatge[:num])
print("Missatge codificat:", codificat)

#   5. Desencriptem el missatge i el mostrem
obj2 = AES.new(clau, AES.MODE_CBC, iv)
deco = obj2.decrypt(codificat)
print("Missatge descodificat:", deco[:num])
