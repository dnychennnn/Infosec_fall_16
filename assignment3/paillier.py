#!/usr/bin/env python
from paillier import paillier
from sys import maxint

def generate_keypair(x):
    return paillier.generate_keypair(x)

def encrypt_x(pub, p):
    return paillier.encrypt(pub, p)

def encrypt_y(pub, p):
    return paillier.encrypt(pub, p)

def decrypt(priv, pub, z):
    return paillier.decrypt(priv, pub, cz)

def add(pub, x, y):
    return paillier.e_add(pub, x, y)


if __name__ == '__main__':
    priv, pub = generate_keypair(512)

    x, y = maxint, maxint
    cx, cy = encrypt_x(pub, x), encrypt_y(pub, y)

    cz = add(pub, cx, cy)

    z = decrypt(priv, pub, cz)
