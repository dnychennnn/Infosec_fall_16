# -*- coding: utf-8 -*-

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.backends import default_backend

backend = default_backend()
key = os.urandom(32)
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)

message = open("512M+7",'rb')
result = open("512M+7_result", 'wb')
finished = False

block_size = 16

# 每1024*blocksize加密
while not finished:
	encryptor = cipher.encryptor()
	chunk = message.read(1024*block_size)
	if len(chunk) == 0 or len(chunk) % block_size != 0:
		padding_length = block_size - (len(chunk) % block_size)
		chunk += padding_length * chr(padding_length)
		finished = True
	result.write(encryptor.update(chunk) + encryptor.finalize())
message.close()
result.close()

