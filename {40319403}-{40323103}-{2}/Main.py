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

