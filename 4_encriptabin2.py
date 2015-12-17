from Crypto.Hash import SHA256
from Crypto.Cipher import AES

file_mg = open("foto_desencriptada.png","wb")
file_enc = open("dades.enc","rb")



clau = raw_input("Introdueix la clau: ").encode("utf-8")
objh = SHA256.new(clau)
resum = objh.digest()

iv = b"1111111111111111"
obj = AES.new(resum, AES.MODE_CBC, iv)

blocs = 8192
while True:
    #read blocs
    bloc = file_enc.read(blocs)
    if not bloc:
        break

    #decrypt
    dec = obj.decrypt(bloc)
    file_mg.write(dec)

file_mg.close()
file_enc.close()
