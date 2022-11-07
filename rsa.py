from math import gcd

p = 17
q = 23
n = p * q
phi = (p - 1) * (q - 1)
e = 0
d = 0

for i in range(2, phi):
    if gcd(i, phi) == 1:
        e = i
        break

for j in range(2,phi):
    if (j * e ) % phi == 1:
        d = j
        break

def encrypt(array):
    return [((m ** e) % n) for m in array]
def decrypt(array):
    return [chr(((m ** d) % n)) for m in array]
if(input("Do you want to decrypt a message? (y/n): ") == "y"):
    messages = input("Enter the message to decrypt: ")
    decrypted = decrypt([int(m) for m in messages.split(",")])
    print("Decrypted Messages: ", "".join(decrypted))

else:
    messagesToEncrypt = input("Enter the message to encrypt: ")
    print("Encrypted message: ", encrypt([ord(c) for c in messagesToEncrypt]))