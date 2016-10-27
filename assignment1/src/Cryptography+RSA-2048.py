# -*- coding: utf-8 -*-

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import base64

#load公鑰
with open("./rsakey/public.pem", "rb") as key_file:
    b64data = '\n'.join(key_file.read().splitlines()[1:-1])
    derdata = base64.b64decode(b64data)
    public_key = serialization.load_der_public_key(derdata, backend=default_backend())
#load私鑰
with open("./rsakey/private.pem", "rb") as key_file:
    b64data = '\n'.join(key_file.read().splitlines()[1:-1])
    derdata = base64.b64decode(b64data)
    private_key = serialization.load_der_private_key(derdata, password=None, backend=default_backend()) 

block_size = 214 #A 2048-bit key can encrypt up to (2048/8) – 42 = 256 – 42 = 214 bytes.

#file i/o
message = open("512M+7",'r+b')
result = open("512M+7_result", 'wb')

#加密
block_content = ''
#從512M+7讀檔 讀到blocksize就進if加密
for word in message.read():
    block_content += word
    if len(block_content) == block_size:
        #使用公鑰加密
        ciphertext = public_key.encrypt(
            block_content,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA1()),algorithm=hashes.SHA1(),label = None))
        #使用司鑰解密
        plaintext = private_key.decrypt(
            ciphertext,
            padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
            )
        )
        print plaintext == block_content
        #測試答案是否正確
        block_content = ''      
message.close()
result.close()

