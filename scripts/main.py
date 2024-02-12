import os
import sys
sys.path.append(os.path.abspath('../src'))
from src import commands

def main():
    try:
        while True:
            enter = input('>>> ').split()
            if enter[0] == 'reg':
                commands.do_reg()
            if enter[0] == 'gen-key':
                print(commands.do_genkey())
            if enter[0] == 'enc':
                print(commands.do_enc(enter))
            if enter[0] == 'dec':
                print(commands.do_dec(enter))
            if enter[0] == 'help':
                print(commands.do_help())
    except KeyboardInterrupt:
        print('\nexit...')