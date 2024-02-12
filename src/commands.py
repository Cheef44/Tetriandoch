from src import db, geniration_keys, encryption, decryption

def do_reg():
    enter_name = input('UserName: ')
    enter_password = input('UserPassword: ')
    
    return db.DataBase(enter_password, enter_name).create_db()

def do_genkey():
    geniration_keys.Keys().run()
    
def do_enc(enter:list):
    enter = enter[0:]
    enter_path = enter[-2]
    enter_file = enter[-1]
    if enter[1] == '-t':
        enter_data = enter[enter.index('-t')+1:enter.index('-f')-1]
        return encryption.EncryptionText(''.join(enter_data), enter_path, enter_file).encryption_text()
    elif enter[1] == '-ft':
        enter_data = enter[enter.index('-ft')+1:enter.index('-f')]
        return encryption.EncryptionFile(''.join(enter_data), enter_path, enter_file).encryption_file()

def do_dec(enter:list):
    enter = enter[0:]
    enter_path = enter[-2]
    enter_file = enter[-1]
    if enter[1] == '-ft':
        enter_data = enter[enter.index('-ft')+1:enter.index('-f')]
        return decryption.Decryption(''.join(enter_data), enter_path, enter_file).decryption()
    elif enter[1] == '-nf':
        enter_data = enter[enter.index('-ft')+1:]
        return decryption.Decryption(''.join(enter_data), enter_path, none_file=True).decryption()