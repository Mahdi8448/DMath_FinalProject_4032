"""
RoadMap:
1.Generating two large prime numbers and applying "Miller-Rabin" test.
2.Calculating Euler functions.
3.Creating public key.
4.Creating privet key (using Euclidean Algorithm).
5.Encryption & decryption.
6.Applying primary tests.
7.Carrying possible attacks & security checks.
"""

import random

rand = random.SystemRandom()

'''
------------------------ STEP ONE --------------------------
------------ GENERATING TWO LARGE PRIME NUMBERS ------------
'''


def single_test(n, a):
    # First, finding 'd' and 's' such n - 1 = 2^s * d
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d >>= 1
    # Now 'd' is the odd part of n-1

    # Calculate x = a^d mod n.
    x = pow(a, d, n)

    # If x is 1 or n-1, the number passes the test for this 'a'.
    if x == 1 or x == n - 1:
        return True

    # Now, repeatedly square x for s-1 times.
    # If we find n-1, it also passes the test.
    for i in range(s - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True

    # If the loop completes without finding 1 or n-1, n is composite.
    return False


''' --- Second Approach -----
    exp =  n - 1
    while not exp & 1:
        exp >>= 1

    if pow(a, exp, n) == 1:
        return True

    while exp < n - 1:
        if pow(a, exp, n) == n - 1:
            return True

        exp <<= 1

    return False
'''


def miller_rabin(n, k=40):
    # Handling numbers lower than 4.
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Applying the test 'k' times(usually 40).
    for i in range(k):
        a = rand.randrange(2, n - 1)
        if not single_test(n, a):
            return False

    return True


def gen_prime(bits):
    while True:
        # Generating a random number.
        a = random.getrandbits(bits)

        # Making sure 'a' has its highest bit set to 1.
        a |= (1 << bits - 1)

        # Making the least significant bit 1.
        # Ensures our number is odd.
        a |= 1
        if miller_rabin(a):
            return a


'''
------------------------ STEP TWO --------------------------
--------------- CALCULATING EULER FUNCTION -----------------
'''


# Calculate n (used for the public and private keys)
def calc_n(self, p, q):
    return p * q


# Calculating phi_n(n)
# Number of "numbers" that are coprime with n.
def calc_phi_n(self, p, q):
    return (p - 1) * (q - 1)


'''
------------------------ STEP THREE --------------------------
-------------------- CREATING PUBLIC KEY ---------------------
'''


# A helper function to calculate gcd.
def gcd(self, a, b):
    while b:
        temp = a
        a = b
        b = temp % b
    return a


# We call public exponent in RSA encryption 'e'.
# 'e' must satisfy two conditions: (1 < e < phi_n) & (being coprime with phi_n).
# The number 65537 is a common choice for 'e'. More details in PDF.
def find_e(self, phi_n):
    e = 65537
    if self.gcd(e, phi_n) == 1:
        return e

    # Making sure e is coprime with phi_n.
    while self.gcd(e, phi_n) != 1:
        e += 2
    return e

'''
------------------------ STEP FOUR --------------------------
-------------------- CREATING PRIVET KEY ---------------------
'''

# Extended Euclidean Algorithm
def extended_Euclid_gcd(self, a, b):
    # Initializing the variables
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    # Loop until remainder becomes zero
    while r != 0:
        quotient = old_r // r
            # Update remainders
        old_r, r = r, old_r - quotient * r

        # Update s coefficients
        old_s, s = s, old_s - quotient * s
        # Update t coefficients
        old_t, t = t, old_t - quotient * t

    # Final result will be: gcd = old_r, coefficients = old_s, old_t
    return old_r, old_s, old_t

''' 
--------- Algorithm with use of recursion ---------
def extended_Euclid_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_Euclid_gcd(b % a, a)
    t = t1 - (b // a) * t1
    s = s1
    return gcd, t, s
'''

def modinv(self, a, m):
    # Calculating the modular inverse of a mod m.
    # This finds 's' such that (a * s) % m = 1.
    g, s, t = self.extended_Euclid_gcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    return s % m

'''
------------------------ STEP FIVE --------------------------
----------------- ENCRYPTION & DECRYPTION -------------------
'''

def encrypt(self, plaintext: str):
    # Using UTF-8 character encoding standard.
    msg_int = int.from_bytes(plaintext.encode('utf-8'), 'big')
    cipher_int = pow(msg_int, self.e, self.n)
    return cipher_int

def decrypt(self, ciphertext: int):
    msg_int = pow(ciphertext, self.d, self.n)
    length = (msg_int.bit_length() + 7) // 8
    return msg_int.to_bytes(length, 'big').decode('utf-8')

# I couldn't use UTF-8 strings in Attack class as 'n' is too short
# So, our tests in Attack class uses these two functions
def encrypt_number(self, number: int):
    if number >= self.n:
        raise ValueError("Number too large for this RSA modulus!")
    return pow(number, self.e, self.n)

def decrypt_number(self, ciphertext: int):
    return pow(ciphertext, self.d, self.n)
