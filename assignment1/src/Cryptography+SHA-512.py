# -*- coding: utf-8 -*-
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

#file i/o
message = open("512M+7",'r+b')
result = open("512M+7_result", 'wb')

finished = False
block_size = 1024
while not finished:
	chunk = message.read(block_size*1024) #每次讀160個B
	if len(chunk) == 0:
		finished = True
	digest = hashes.Hash(hashes.SHA512(), backend=default_backend())
	digest.update(chunk)
	cipher_text = digest.finalize()
	result.write(cipher_text) #Continue hashing of a message by consuming the next chunk of data.	
	print len(cipher_text) #print出Hash後的資料長度：應該為64B＝512bits
	# print hash.hexdigest() #print出16進位的加密資料
message.close()
result.close()
