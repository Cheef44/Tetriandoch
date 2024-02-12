from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
import os

class Encryption:
    def vectore(self):
        try:
            if not os.path.exists('data/vectore.bin'):
                with open('data/vectore.bin', 'wb') as vectore:
                    g = os.urandom(16)
                    vectore.write(g)
                    
            with open('data/vectore.bin', 'rb') as iv:
                iv = iv.read()
            return iv
        except FileNotFoundError:
            return 'Encryption keys were not found'
        
    def __init__(self, data:str, enc_path, file, path_async_key='data/asynckey', path_sync_key='data/synckey.pub') -> None:
        self.data = data
        self.enc_path = enc_path
        self.file = file
        self.path_async_key = path_async_key
        self.path_sync_key = path_sync_key
    
    def decrypt_sync_key(self):
        try:
            with open(self.path_async_key, 'rb') as private_key:
                private_key = private_key.read()
                private_key = RSA.import_key(private_key)
                
            with open(self.path_sync_key, 'rb') as sync_key:
                sync_key = sync_key.read()
                
            decrypt = PKCS1_OAEP.new(private_key)
            decrypt = decrypt.decrypt(sync_key)
            
            return decrypt
        except FileNotFoundError:
            return 'Encryption keys were not found'

class EncryptionText(Encryption):
    def encryption_text(self):
        try:
            encrypt = AES.new(self.decrypt_sync_key(), AES.MODE_CFB, self.vectore())
            encrypt_text = encrypt.encrypt(bytes(self.data, encoding='utf8'))
            if not os.path.exists(self.enc_path):
                os.mkdir(self.enc_path)
                with open(f'{self.enc_path}/{self.file}.aes', 'wb') as encrypt_file:
                    encrypt_file.write(encrypt_text)
                    
                return f'Your encrypted file is in {self.enc_path}'
            else:
                return f'The entered directory exists'
        except ValueError:
            return 'Encryption keys were not found'

class EncryptionFile(Encryption):
    def encryption_file(self):
        try:
            with open(self.data, 'r',encoding='utf-8') as file:
                file = file.read()
            encrypt = AES.new(self.decrypt_sync_key(), AES.MODE_CFB, self.vectore())
            encrypt_data = encrypt.encrypt(bytes(file, encoding='utf-8'))
            if not os.path.exists(self.enc_path):
                os.mkdir(self.enc_path)
                with open(f'{self.enc_path}/{self.file}.aes', 'wb') as encrypt_file:
                    encrypt_file.write(encrypt_data)
                    
                return f'Your encrypted file is in {self.enc_path}'
            else:
                return f'The entered directory exists'
        except ValueError:
            return 'Encryption keys were not found'