from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
import os

class Encrtption:
    global iv
    if not os.path.exists('data/vectore.iv'):
        with open('data/vectore.iv', 'wb') as vectore:
            g = os.urandom(16)
            vectore.write(g)
            
    with open('data/vectore.iv', 'rb') as iv:
        iv = iv.read()
    
    def __init__(self, data:str, enc_path, file, path_async_key='data/asynckey', path_sync_key='data/synckey.pub') -> None:
        self.data = data
        self.enc_path = enc_path
        self.file = file
        self.path_async_key = path_async_key
        self.path_sync_key = path_sync_key
    
    def decrypt_sync_key(self):
        with open(self.path_async_key, 'rb') as private_key:
            private_key = private_key.read()
            private_key = RSA.import_key(private_key)
            
        with open(self.path_sync_key, 'rb') as sync_key:
            sync_key = sync_key.read()
            
        decrypt = PKCS1_OAEP.new(private_key)
        decrypt = decrypt.decrypt(sync_key)
        
        return decrypt

class EncrtptionText(Encrtption):
    def encryption_text(self):
        encrypt = AES.new(self.decrypt_sync_key(), AES.MODE_CFB, iv)
        encrypt_text = encrypt.encrypt(bytes(self.data, encoding='utf8'))
        if not os.path.exists(self.enc_path):
            os.mkdir(self.enc_path)
            with open(f'{self.enc_path}/{self.file}.aes', 'wb') as encrypt_file:
                encrypt_file.write(encrypt_text)
                
            return f'Your encrypted file is in {self.enc_path}'
        else:
            return f'The entered directory exists'

class EncryptionFile(Encrtption):
    def encryption_file(self):
        with open(self.data, 'rb') as file:
            file = file.read()
        encrypt = AES.new(self.decrypt_sync_key(), AES.MODE_CFB, iv)
        encrypt_data = encrypt.encrypt(bytes(self.data, encoding='utf8'))
        if not os.path.exists(self.enc_path):
            os.mkdir(self.enc_path)
            with open(f'{self.enc_path}/{self.file}.aes', 'wb') as encrypt_file:
                encrypt_file.write(encrypt_data)
                
            return f'Your encrypted file is in {self.enc_path}'
        else:
            return f'The entered directory exists'