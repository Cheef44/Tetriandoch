import os
import sys
sys.path.append(os.path.abspath('../src'))
from src import db

def main():
    try:
        while True:
            enter = input('>>> ')
            if enter == 'reg':
                enter_name = input('UserName: ')
                enter_password = input('UserPassword: ')
                print(db.DataBase(enter_password, enter_name).create_db())
    except KeyboardInterrupt:
        print('\nexit...')