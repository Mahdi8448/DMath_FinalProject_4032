from RSA import RSA


class Attack:
    @staticmethod
    def factorize_n(n):
        # We can use a simple factorization when n is small
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return i, n // i
        return None, None

    @staticmethod
    def run():
        print("||" + "=" * 47 + "||")
        print("              RSA ATTACK (SMALL n)   ")
        print("||" + "=" * 47 + "||")

        # Generate a VERY small RSA key for demonstration
        rsa = RSA(16)  # 16-bit primes will give us ~32-bit n (tiny & insecure)

        # Using numeric message directly
        # I tried to do the same with Strings, but n is too short
        # for parsing UTF-8 format.
        message_num = 12345
        cipher = rsa.encrypt_number(message_num)

        print(f" -> Original Numeric Message: {message_num}")
        print(f"Cipher (int): {cipher}\n")

        # Our attacker only sees (e, n) and the ciphertext
        e, n = rsa.e, rsa.n
        print(f"Attacker knows Public Key: (e={e}, n={n})")

        # Step 1: Factorize n
        p, q = Attack.factorize_n(n)
        if p is None or q is None:
            print(" Failed to factorize n (too large). Use smaller bit size.")
            return
        print(f"Factored n = {n} into p={p}, q={q}")

        # Step 2: Compute phi_n
        phi_n = (p - 1) * (q - 1)

        # Step 3: Compute d = e^-1 mod phi_n
        d = rsa.modinv(e, phi_n)
        print(f"Recovered Private Key: d={d}")

        # Step 4: Decrypt
        recovered_num = pow(cipher, d, n)
        print(f"\n -> Attacker Decrypted Numeric Message: {recovered_num}")
        print("||" + "=" * 47 + "||")


if __name__ == "__main__":
    Attack.run()
