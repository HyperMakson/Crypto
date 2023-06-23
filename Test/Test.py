'''from itertools import cycle
 
key = "243434"
message = "this is my message, see if it can be encrypted completely."
 
cipher_text = "".join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(message, cycle(key)))
print(cipher_text)
plain_text = "".join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(cipher_text, cycle(key)))
print(plain_text)'''
'''def find_mod_inv(a,m):

    for x in range(1,m):
        if((a*x) % m == 1):
            return x
    raise Exception('The modular inverse does not exist.')


a = 156
m = 2432
print(find_mod_inv(a,m))'''
from math import gcd
from random import randint

p = 117
mod = 117 - 1

def is_coprime(mod):
    k = randint(1, mod)
    while (gcd(k, mod) != 1):
        k = randint(1, mod)
    return k

print(is_coprime(mod))