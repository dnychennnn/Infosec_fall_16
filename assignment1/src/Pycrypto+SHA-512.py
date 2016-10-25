# -*- coding: utf-8 -*-

from Crypto.Hash import SHA512

#file i/o
message = open("512M+7",'r+b')
result = open("512M+7_result", 'wb')

finished = False

block_size = 32

while not finished:
	chunk = message.read(1024*block_size) #每次讀個B
	if len(chunk) == 0:
		finished = True
	hash = SHA512.new() #產生一個hash物件
	hash.update(chunk)
	result.write(hash.digest()) #Continue hashing of a message by consuming the next chunk of data.	
	print len(hash.digest()) #print出Hash後的資料長度：應該為64B
message.close()
result.close()
