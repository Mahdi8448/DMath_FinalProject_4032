from RSA import RSA


class Test:
    @staticmethod
    def run():
        print("=" * 50)
        print("                   RSA TEST    ")
        print("=" * 50)

        # For default, I'm using 512 bits. Change it as you wish
        rsa = RSA(512)
        print(" RSA instance created with 512-bit primes.\n")

        tests = [
            "Hello",
            "RSA Test",
            "Designed by Mahdi & Amin!"
        ]

        # String tests
        print(" Testing String Messages:")
        for msg in tests:
            cipher = rsa.encrypt(msg)
            message = rsa.decrypt(cipher)
            print(f" Input: {msg}")
            print(f"  → Cipher (int): {str(cipher)[:40]}...")
            print(f"  → Decrypted: {message}")
            print("-" * 40)

        # Numeric tests
        print("\n Testing Numeric Messages:")
        numbers = [42, 123456789, 98765432123456789]
        for num in numbers:
            # Convert number to string first
            msg = str(num)
            cipher = rsa.encrypt(msg)
            message = rsa.decrypt(cipher)
            print(f" Input (num): {num}")
            print(f"  → Cipher (int): {str(cipher)[:40]}...")
            print(f"  → Decrypted: {message}")
            print("-" * 40)

        print("\n All tests completed successfully.")
        print("=" * 50)


if __name__ == "__main__":
    Test.run()