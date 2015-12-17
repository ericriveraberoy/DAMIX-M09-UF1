from Crypto.Cipher import AES

clau = b"1234567890123456"
iv = b"iv12345678901234"
obj = AES.new(clau, AES.MODE_CBC, iv)

# Codifiquem un missatge
missatgeclar = input("Missatge clar:").encode("utf-8")
while (len(missatgeclar) % 16 != 0):
    print("Ha de ser multiple de 16!")
    missatgeclar = input("Missatge clar:").encode("utf-8")

missatgecodificat = obj.encrypt(missatgeclar)
print(missatgeclar)
print(missatgecodificat)

# Decodifiquem el missatge
obj2 = AES.new(clau, AES.MODE_CBC, iv)
missatgedecodificat = obj2.decrypt(missatgecodificat)
print(missatgedecodificat)
