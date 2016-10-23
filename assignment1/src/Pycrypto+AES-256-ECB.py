# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
import os

#隨機生成256bits的key
key = os.urandom(32)
iv = 'This is an IV'

block_size = AES.block_size

aes_256_ecb = AES.new(key, AES.MODE_ECB, iv)

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
    result.write(aes_256_ecb.encrypt(chunk))
message.close()
result.close()
