from src import db, geniration_keys, encryption

def do_reg():
    enter_name = input('UserName: ')
    enter_password = input('UserPassword: ')
    
    return db.DataBase(enter_password, enter_name).create_db()

def do_genkey():
    geniration_keys.Keys().run()
    
def do_enc(enter:list):
    enter = enter[0:]
    enter_text = enter[enter.index('-t'):enter.index('-f')-1]
    enter_path = enter[-2]
    enter_file = enter[-1]
    
    return encryption.EncrtptionText(''.join(enter_text), enter_path, enter_file).encryption_text()