from Crypto.Hash import SHA256
from Crypto.Cipher import AES

clau = b'1234567890123456'
objh = SHA256.new(clau)

resum = objh.digest()
iv = b'1234567890123456'
print(objh.hexdigest())

obj = AES.new(resum, AES.MODE_CBC, iv)
