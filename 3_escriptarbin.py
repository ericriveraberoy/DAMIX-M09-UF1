from Crypto.Hash import SHA256
from Crypto.Cipher import AES


file_mg = open("foto_a_encriptar.png","rb")
file_enc = open("dades.enc","wb")
blocs = 8192

clau = raw_input("Introdueix la clau: ").encode("utf-8")
objh = SHA256.new(clau)
resum = objh.digest()

iv = b"1111111111111111"
obj= AES.new(resum, AES.MODE_CBC, iv)

while True:
    bloc = file_mg.read(blocs)
    if not bloc:
        break
    #padding
    nombre= len(bloc)
    mod = nombre % 16
    if mod > 0:
        padding = 16 - mod
        bloc += b"0" * padding
    #crypt
    enc = obj.encrypt(bloc)
    file_enc.write(enc)


file_mg.close()
file_enc.close()
