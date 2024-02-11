from .encryption import Encryption
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os
import chardet

class Decryption(Encryption):
    def decryption(self):
        decrypt = AES.new(self.decrypt_sync_key(), AES.MODE_CFB, self.vectore())
        with open(self.data, 'rb') as enc_file:
            enc_file = enc_file.read()
        decrypt_data = decrypt.decrypt(enc_file)
        if not os.path.exists(self.enc_path):
            os.mkdir(self.enc_path)
            with open(f'{self.enc_path}/{self.file}', 'w+', encoding='utf-8') as decryption_file:
                decryption_file.write(decrypt_data.decode(chardet.detect(decrypt_data)['encoding']))
        return f'Decryption was successful, your files are in: {self.enc_path}/{self.file}'