# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Counter
import os


# 產生256bits的key
key = os.urandom(32)
# 生成counter
rand_gen = Random.new()
iv = rand_gen.read(8)
ctr_e = Counter.new(64, prefix=iv)

block_size = AES.block_size

aes_256_ctr = AES.new(key, AES.MODE_CTR, counter=ctr_e)
message = open("512M+7",'r+b')
result = open("512M+7_result", 'wb')
finished = False

# 每1024*blocksize加密
while not finished:
    chunk = message.read(1024*block_size)
    # 實做padding
    if len(chunk) == 0 or len(chunk) % block_size != 0:
        padding_length = block_size - (len(chunk) % block_size)
        chunk += padding_length * chr(padding_length)
        finished = True
    result.write(aes_256_ctr.encrypt(chunk))
message.close()
result.close()
