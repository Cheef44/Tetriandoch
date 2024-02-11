import os
import sys
sys.path.append(os.path.abspath('../src'))
from src import commands

def main():
    try:
        while True:
            enter = input('>>> ').split()
            if enter[0] == 'reg':
                pass
            if enter[0] == 'gen-key':
                pass
            if enter[0] == 'enc':
                print(commands.do_enc(enter))
    except KeyboardInterrupt:
        print('\nexit...')