# 🔐 RSA Encryption Project  

### Presented for: *Discrete Mathematics*  
**KNTU University** – *Dr. Khasteh*  

👨‍💻 **Authors**  
- Mahdi Jorati — *ID: 40319403*  
- Mohamad Amin Abdullahi — *ID: 40323103*  

📄 **Important:** Please make sure to read the **accompanying PDF report**.

---

## 📖 Introduction  
This project is an implementation of the **RSA cryptosystem** in Python, created as part of our Discrete Mathematics course at KNTU University.  

The program demonstrates:  
1. **Key Generation** – Prime number generation using the Miller–Rabin primality test, modulus computation, and creation of public/private keys.  
2. **Encryption & Decryption** – Supports both **strings** and **numeric messages**.  
3. **Interactive Demo (`Main` class)** – Users can select RSA key size (256, 512, 1024, or custom ≥256), enter a message, and see the encrypted & decrypted results.  
4. **Testing Suite (`Test` class)** – Runs automatic tests on string and numeric messages to verify correctness.  
5. **Attack Demo (`Attack` class)** – Shows why RSA with **small n** is insecure, by factorizing the modulus and recovering the private key.  

---

## 📂 Project Structure  
- **`RSA` class** → Handles prime generation, key generation, and encryption/decryption.  
- **`Main` class** → User interface: choose key size, enter a message, see encryption/decryption results.  
- **`Test` class** → Automatically tests encryption/decryption with different inputs.  
- **`Attack` class** → Demonstrates breaking RSA when `n` is small by factorization.  
- **PDF Report** → Explains the project in detail, including theory, mathematical analysis and implementation.  

---

## ▶️ How to Run  
1. Run the main demo:  
   ```bash
   python Main.py
* Choose a key size (256, 512, 1024, or custom ≥256).
* Enter a message (text or numbers).
* See the encrypted integer and the decrypted message.
2. Run the test suite (optional):
   ```bash
   Test.run() in Main.py
3. Run the attack demo (optional):
   ```bash
   Attack.run() in Main.py
