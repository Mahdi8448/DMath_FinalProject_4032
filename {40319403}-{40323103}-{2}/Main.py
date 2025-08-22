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