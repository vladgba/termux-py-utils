from cryptography.fernet import Fernet
import sys
import os
import gzip

keyfile = 'crypt.key'
key = None
def main():
    if len(sys.argv) < 3:
        print('usage: python filecrypt.py <file> <mode>')
        print('    <mode> can be "e" (encode) or "d" (decode)')
        return
    file = sys.argv[1]
    mode = sys.argv[2]
    print("File: " + file)
    
    if os.path.isfile(keyfile):
        key = load_key()
    else:
        key = write_key()
    
    if mode == "e":
        print('Mode: Encrypt')
        encrypt(file, key)
    elif mode == "d":
        print('Mode: Decrypt')
        decrypt(file, key)
    else:
        print('<mode> can be only "e" or "d"')
    
def write_key():
    key = Fernet.generate_key()
    with open(keyfile, 'wb') as key_file:
        key_file.write(key)
    return key

def load_key():
    key = open(keyfile, 'rb').read()
    return key
    
def encrypt(filename, key):
    f = Fernet(key)
    
    with open(filename, 'rb') as file:
        file_data = file.read()
    
    encrypted_data = gzip.compress(f.encrypt(file_data))
    with open(filename, 'wb') as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    f = Fernet(key)
    
    with open(filename, 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(gzip.decompress(encrypted_data))
    
    with open(filename, 'wb') as file:
        file.write(decrypted_data)

if __name__ == '__main__':
    main()
