from src import db, geniration_keys, encryption, decryption

def do_reg():
    enter_name = input('UserName: ')
    enter_password = input('UserPassword: ')
    
    return db.DataBase(enter_password, enter_name).create_db()

def do_genkey():
    enter_name = input('UserName: ')
    enter_password = input('UserPassword: ')
    if db.DataBase(enter_password, enter_name).log_in_db():
        geniration_keys.Keys().run()
        return 'The keys were generated successfully and are located along the path data/'
    else:
        return 'Check that the entered data is correct'
    
def do_enc(enter:list):
    try:
        enter = enter[0:]
        enter_path = enter[-2]
        enter_file = enter[-1]
        if enter[1] == '-t':
            enter_data = enter[enter.index('-t')+1:enter.index('-f')-1]
            return encryption.EncryptionText(''.join(enter_data), enter_path, enter_file).encryption_text()
        elif enter[1] == '-ft':
            enter_data = enter[enter.index('-ft')+1:enter.index('-f')]
            return encryption.EncryptionFile(''.join(enter_data), enter_path, enter_file).encryption_file()
        else:
            return 'Missing parameter/s. The command should look like this: enc -t <text> -f <path_enc_file> <enc_file> or enc -ft <file> -f <path_enc_file> <enc_file>'
    except IndexError:
        return 'Missing parameter/s. The command should look like this: enc -t <text> -f <path_enc_file> <enc_file> or enc -ft <file> -f <path_enc_file> <enc_file>'

def do_dec(enter:list):
    try:
        enter = enter[0:]
        enter_path = enter[-2]
        enter_file = enter[-1]
        if enter[1] == '-ft':
            enter_data = enter[enter.index('-ft')+1:enter.index('-f')]
            return decryption.Decryption(''.join(enter_data), enter_path, enter_file).decryption()
        elif enter[1] == '-nf':
            enter_data = enter[enter.index('-ft')+1:]
            return decryption.Decryption(''.join(enter_data), enter_path, none_file=True).decryption()
        else:
            return 'Missing parameter/s. The command should look like this: dec -ft <file> -f <path_dec_file> <enc_file> or dec -nf -ft <file> -f <path_dec_file> <enc_file>'
    except IndexError:
        return 'Missing parameter/s. The command should look like this: dec -ft <file> -f <path_dec_file> <enc_file> or dec -nf -ft <file> -f <path_dec_file> <enc_file>'