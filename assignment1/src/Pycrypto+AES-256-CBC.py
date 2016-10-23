# -*- coding: utf-8 -*-

from Crypto.Cipher import AES

# 產生256bits的key
key = 'This is a KEY123This is a key123'
iv = 'This is an IV123'

block_size = AES.block_size

aes_256_cbc = AES.new(key, AES.MODE_CBC, iv)
#file i/o
message = open("512M+7",'r+b')
result = open("512M+7_result", 'wb')

finished = False

# 每1024*blocksize加密
while not finished:
    chunk = message.read(1024*block_size)
    if len(chunk) == 0 or len(chunk) % block_size != 0:
        padding_length = block_size - (len(chunk) % block_size)
        chunk += padding_length * chr(padding_length)
        finished = True
    result.write(aes_256_cbc.encrypt(chunk))
message.close()
result.close()
