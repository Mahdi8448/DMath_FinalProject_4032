import sys
import time
import threading

from RSA import RSA

class Main:
    @staticmethod
    def run():
        # Title banner
        print("=" * 50)
        print("                 RSA ENCRYPTION ")
        print("=" * 50)

        print("\nChoose RSA key size:")
        print("1. 256 bits")
        print("2. 512 bits")
        print("3. 1024 bits")
        print("4. Custom size (must be >= 256)")

        choice = input("\nEnter choice (1/2/3/4): ").strip()

        match choice:
            case "1":
                bits = 256
            case "2":
                bits = 512
            case "3":
                bits = 1024
            case "4":
                try:
                    bits = int(input("Enter custom bit size (>= 256): ").strip())
                    if bits < 256:
                        print("Too small, defaulting to 256 bits.")
                        bits = 256
                except ValueError:
                    print("Invalid input, defaulting to 256 bits.")
                    bits = 256
            case _:
                print("Invalid choice, defaulting to 256 bits.")
                bits = 256

        stop_animation = False

        def animate():
            dots = 0
            while not stop_animation:
                sys.stdout.write("\r  Generating RSA keys" + "." * dots + " " * (3 - dots))
                sys.stdout.flush()
                dots = (dots + 1) % 4
                time.sleep(0.5)

        t = threading.Thread(target=animate)
        t.start()

        start_time = time.time()

        rsa = RSA(bits)

        end_time = time.time()
        elapsed = end_time - start_time

        stop_animation = True
        t.join()

        sys.stdout.write("\r" + " " * 50 + "\r")
        sys.stdout.flush()

        print(f"  Keys generated in {elapsed:.2f} seconds.\n")

        message = input("  Enter a message to encrypt (both numeric & alphabetic is allowed): ")

        cipher = rsa.encrypt(message)

        print("\n" + "=" * 50)
        print("                RSA RESULTS  ")
        print("=" * 50)
        print(f"Key Size : {bits} bits\n")

        def short(num, length=30):
            s = str(num)
            return s if len(s) <= length else f"{s[:15]}...{s[-15:]}"

        print(" Public Key:")
        print(f" e = {rsa.e}")
        print(f" n = {short(rsa.n)}\n")

        print(" Encrypted Message (as integer):")
        print(f" {short(cipher)}\n")

        print(" Private Key:")
        print(f" d = {short(rsa.d)}")
        print(f" n = {short(rsa.n)}\n")

        decrypted = rsa.decrypt(cipher)
        print(" Decrypted Message:")
        print(f" {decrypted}")
        print("=" * 50)

if __name__ == "__main__":
    Main.run()