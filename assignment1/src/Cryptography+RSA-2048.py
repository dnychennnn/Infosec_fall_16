# -*- coding: utf-8 -*-

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

with open("./rsakey/public.pem", "rb") as key_file:
     public_key = serialization.load_pem_private_key(
         key_file.read(),
         password=None,
         backend=default_backend())

with open("./rsakey/private.pem", "rb") as key_file:
     private_key = serialization.load_pem_private_key(
         key_file.read(),
         password=None,
         backend=default_backend())

block_size = 16
#file i/o
message = open("512M+7",'r+b')
result = open("512M+7_result", 'wb')

finished = False

while not finished:
	chunk = message.read(10*block_size) #每次讀160個B
	key = RSA.importKey(pub) #import rsa-2048 public key
	''' padding '''
	if len(chunk) == 0 or len(chunk) % block_size != 0:
		padding_length = block_size - (len(chunk) % block_size)
		chunk += padding_length * chr(padding_length)
		finished = True
	result.write(cipher_text=public_key.encrypt(message, padding.OAEP(
		mgf=padding.MGF1(algorithm=hashes.SHA1()),
		algorithm=hashes.SHA1(),
		label=None
    	)
	)		
)
	plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA1()),
        algorithm=hashes.SHA1(),
        label=None
    )
)
	print plaintext==chunk
message.close()
result.close()

