# -*- coding: utf-8 -*-

#  加密解密所用对象不能为同一个
# 1. 先使用openssl生成公私钥对
# openssl genrsa -out privkey.pem 2048
# 2. 将上一步生成的RSA私钥转换成PKCS#8编码，作为最终使用的私钥。
# openssl pkcs8 -topk8 -in rsa_private_key_2048.pem -out pkcs8_rsa_private_key_2048.pem -nocrypt
# 3. 导出RSA公钥，以X509编码，作为最终交换的公钥。
# openssl rsa -in rsa_private_key_2048.pem -out rsa_public_key_2048.pem -pubout
# RSA不适合用于长段文本加解密(pycrypto限制256字符)，一般用来传输密钥，之后通过密钥通过对称加密传输内容

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto import Random

#取得由openssl產生的public key and private key
with open('../rsa_public_key_2048.pem', 'r') as f:
    pub = f.read()

with open('../pkcs8_rsa_private_key_2048.pem', 'r') as f:
    pri = f.read()

block_size = 16
#file i/o
message = open("512M+7",'r+b')
result = open("512M+7_result", 'wb')

dsize = SHA.digest_size

finished = False

while not finished:
	chunk = message.read(10*block_size) #每次讀160個B
	key = RSA.importKey(pub) #import rsa-2048 public key
	sentinel = Random.new().read(15 + dsize)
	cipher = PKCS1_v1_5.new(key)
	''' padding '''
	if len(chunk) == 0 or len(chunk) % block_size != 0:
		padding_length = block_size - (len(chunk) % block_size)
		chunk += padding_length * chr(padding_length)
		finished = True
	result.write(cipher.encrypt(chunk))
	privkey = RSA.importKey(pri)
	cipher2 = PKCS1_v1_5.new(privkey)
	print cipher2.decrypt(cipher.encrypt(chunk), sentinel)==chunk
message.close()
result.close()



