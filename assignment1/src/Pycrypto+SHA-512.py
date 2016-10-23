# -*- coding: utf-8 -*-

from Crypto.Hash import SHA512

#file i/o
message = open("512M+7",'r+b')
result = open("512M+7_result", 'wb')

finished = False

block_size = 16

while not finished:
	hash = SHA512.new() #產生一個hash物件
	chunk = message.read(1024*block_size) #每次讀160個B
	''' padding '''
	if len(chunk) == 0 or len(chunk) % block_size != 0:
		padding_length = block_size - (len(chunk) % block_size)
		chunk += padding_length * chr(padding_length)
		finished = True
	hash.update(chunk)
	result.write(hash.digest()) #Continue hashing of a message by consuming the next chunk of data.	
	# print hash.hexdigest() #print出16進位的加密資料
message.close()
result.close()
