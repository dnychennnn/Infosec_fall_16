# -*- coding: utf-8 -*-

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import base64


def load_public_key():
    '''
    載入公鑰
    '''
    with open("./rsakey/public.pem", "rb") as key_file:
        b64data = '\n'.join(key_file.read().decode('utf-8').splitlines()[1:-1])
        derdata = base64.b64decode(b64data)
        return serialization.load_der_public_key(
            derdata, backend=default_backend())


def load_private_key():
    '''
    載入私鑰
    '''
    with open("./rsakey/private.pem", "rb") as key_file:
        b64data = '\n'.join(key_file.read().decode('utf-8').splitlines()[1:-1])
        derdata = base64.b64decode(b64data)
        return serialization.load_der_private_key(
            derdata, password=None, backend=default_backend())


def get_ciphertext(plaintext):
    '''
    使用公鑰加密
    '''
    public_key = load_public_key()
    return public_key.encrypt(
        plaintext.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )


def get_plaintext(ciphertext):
    '''
    使用私鑰解密
    '''
    private_key = load_private_key()
    return private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )


def encrypt(message):
    '''
    從 message 逐字讀入內容，長度到達 BLOCK_SIZE 就進行加密
    '''

    # A 2048-bit key can encrypt up to (2048/8) – 42 = 256 – 42 = 214 bytes.
    BLOCK_SIZE = 214

    TOTAL_BLOCKS = int(len(message) / BLOCK_SIZE)

    blocks = []
    block_content = ''
    for word in message:
        block_content += word
        if len(block_content) == BLOCK_SIZE:
            ciphertext = get_ciphertext(block_content)
            plaintext = get_plaintext(ciphertext)

            # 測試答案是否正確
            if plaintext.decode('utf-8') == block_content:
                block_content = ''
                blocks.append(ciphertext)
                print('Finished ' + str(len(blocks)) + ' blocks')
                print(str(TOTAL_BLOCKS - len(blocks)) + ' to go...')
            else:
                print('ERROR: Plaintext does not match decrypted data')
                return None

    return blocks


if __name__ == '__main__':
    with open("512M+7", 'r+b') as f_message, open("512M+7_result", 'wb') as f_result:
        f_result.write(encrypt(f_message.read().decode('utf-8')))
        f_message.close()
        f_result.close()
