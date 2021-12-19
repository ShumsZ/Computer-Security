# RSA encoder and decoder (only number inputs)

# RSA is based on the problem of factorization of large prime numbers
# This program is designed to encode and decode word using the RSA algorithm

# Algorithm:
# Step 1. Choose 2 very large prime numbers p and q
# We use the Crypto.Util package provided by python to generate our keys, p, q and d
# Step 2. calculate modulus N = p * q
# Step 3. calculate the totient (represented as phi(N)) = (p - 1)(q - 1). the totient is the number of coprimes of N.
# Step 4. calculate 'e' such that it is smaller than totient and e is a coprime of the totient.
# I use e to be 2^16 + 1 = 65537 which is a common choice.
# Having 'e' too small, opens it up to potential ways to crack the algorithm
# Step 5 - compute private key d

# Step 1
# Cryptodome is a great package and we use the number file from it.
# However installing Cryptodome is somewhat of a nightmare so here is a brief overview on what to do should you run into issues.
# use 'pip install pycryptodomex'. Before that however I would suggest you make sure there arent any previous versions of this.
# For more details, check out this discussion: https://github.com/DP-3T/reference_implementation/issues/1
# Once you have done the pip install, install the 'Cryptodome' package in your IDE and it should work

import Cryptodome.Util.number


p = Cryptodome.Util.number.getPrime(512)
q = Cryptodome.Util.number.getPrime(512)

# Step 2
# Our N is 1024 bits as p and q are 512 bits each making this value of N impossible to factorise
N = p * q

# Step 3
phi = (p - 1) * (q - 1)

# Step 4
e = 65537

# Step 5
# the formula de mod(phi) = 1 means that when d and e are multipled, the remainder of dividing this with phi is 1.
# Hence d is the modular multiplicative inverse
d = Cryptodome.Util.number.inverse(e, phi)


# Encryption

def encrypt(word):
    encryption = (word ** e) % N
    return encryption


# Decryption: to decrypt, we use the private key d along with public key e and N (hence this is an asymmetric encryption)

def decrypt(cipher):
    message = (cipher ** d) % N
    return message


word = 5
encryption = encrypt(word)
print(encryption)

decryption = decrypt(encryption)
print(decryption)
