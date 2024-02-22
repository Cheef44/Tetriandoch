from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

#Класс для функция связанных с ключами
class Keys:
    #Метож генерации синхронного ключа
    def gen_sync_key(self):
        with open('data/synckey.pub', 'wb') as key:
            key.write(get_random_bytes(32))
    
    #Метод генерации асинхронного ключа
    def gen_async_key(self):
        keys = RSA.generate(1024)
        with open('data/asynckey.pub', 'wb') as key_pub:
            key_pub.write(keys.public_key().export_key())
        with open('data/asynckey', 'wb') as key_private:
            key_private.write(keys.export_key())
    
    #Метод шифрования синхронного ключа с помощью асинхронного шифрования
    def synchronous_key_encryption(self):
        with open('data/synckey.pub', 'rb') as sync_key:
            sync_key = sync_key.read()
        with open('data/asynckey.pub', 'rb') as async_key:
            async_key = RSA.import_key(async_key.read())
        
        encrypt = PKCS1_OAEP.new(async_key)
        encrypt = encrypt.encrypt(sync_key)
        with open('data/synckey.pub', 'wb') as sync_key:
            sync_key.write(encrypt)
    #Функция для запуска всех методов      
    def run(self):
        self.gen_sync_key()
        self.gen_async_key()
        self.synchronous_key_encryption()