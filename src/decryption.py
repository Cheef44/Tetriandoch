from .encryption import Encryption
from Crypto.Cipher import AES
import os
import chardet

class Decryption(Encryption):
    def __init__(self, data: str, enc_path, file=None, path_async_key='data/asynckey', path_sync_key='data/synckey.pub', none_file=False) -> None:
        super().__init__(data, enc_path, file, path_async_key, path_sync_key)
        self.none_file = none_file
        
    def decryption(self):
        try:
            decrypt = AES.new(self.decrypt_sync_key(), AES.MODE_CFB, self.vectore())
            with open(self.data, 'rb') as enc_file:
                enc_file = enc_file.read()
            decrypt_data = decrypt.decrypt(enc_file)
            decrypt_data = decrypt_data.decode(chardet.detect(decrypt_data)['encoding'])
            if not self.none_file:
                if not os.path.exists(self.enc_path):
                    os.mkdir(self.enc_path)
                    with open(f'{self.enc_path}/{self.file}', 'w+', encoding='utf-8') as decryption_file:
                        decryption_file.write(decrypt_data)
                        
                return f'Decryption was successful, your files are in: {self.enc_path}/{self.file}'
            else:
                return decrypt_data
        except ValueError:
            return 'Encryption keys were not found'