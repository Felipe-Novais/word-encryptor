'''
Word encrypter/decrypter
'''

import os

# functions responsible for encrypting and decrypting

def index_verifier(x):
    for i, letter in numerated_alphabet:
        if x == letter:
            return i
    
def word_encrypter():
    global encrypted_word
    
    for letter in word:
        base_index = index_verifier(letter)
        converted_index = base_index + key_int

        while converted_index >= len(alphabet):
            converted_index -= len(alphabet)

        encrypted_word += alphabet[converted_index]    

def word_decrypter():
    global key_int
    global decrypted_word
    
    for letter in word:
        key_int = int(key)
        base_index = index_verifier(letter)

        while key_int != 0:
            base_index -= 1
            key_int -= 1

        while base_index < 0:
            base_index += len(alphabet)

        decrypted_word += alphabet[base_index]

# setting up important variables

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numerated_alphabet = []
alphabet_str = 'abcdefghijklmnopqrstuvwxyz'


for letter in enumerate(alphabet):
    numerated_alphabet.append(letter)

# starting the program and verifying each required input

print('Welcome! This program is a word encrypter/decrypter.\n')

while True:
    print('Select what you wish to do by inputing one of the following letters:\n')
    print('E = encrypt\nD = decrypt\n')

    while True:
        e_or_d = input().lower()
    
        if len(e_or_d) > 1:
            os.system('cls')
            print('Please type only one character.\n')
            print('E = encrypt\nD = decrypt\n')
            continue

        elif len(e_or_d) == 0:
            os.system('cls')
            print('Please type something.\n')
            print('E = encrypt\nD = decrypt\n')
            continue

        elif e_or_d not in alphabet_str:
            os.system('cls')
            print('Please type a letter.\n')
            print('E = encrypt\nD = decrypt\n')
            continue

        elif e_or_d != 'e' and e_or_d != 'd':
            os.system('cls')
            print('Please type one of the specified letters.\n')
            print('E = encrypt\nD = decrypt\n')
            continue

        elif e_or_d == 'e' or e_or_d == 'd':
            break

    os.system('cls')

    while True:

        if e_or_d == 'e':
            print('\nEnter the word you wish to encrypt: ', end='')
            word = input().lower()

            if len(word) == 0:
                os.system('cls')
                print('Please input something.')
                continue

            elif word.isalpha() == False:
                os.system('cls')
                print('Please enter only letters.')
                continue

            break
    
        elif e_or_d == 'd':
            os.system('cls')
            print('\nEnter the word you wish to decrypt: ', end='')
            word = input().lower()
        
            if len(word) == 0:
                os.system('cls')
                print('Please input something.')
                continue

            elif word.isalpha() == False:
                os.system('cls')
                print('Please enter only letters.')
                continue

            break

    os.system('cls')
    
    while True:
        key = input('Enter the encrypting key: ')

        if len(key) == 0:
            os.system('cls')
            print('Please type something.\n')
            continue

        elif key.isdigit() == False:
            os.system('cls')
            print('Please type only integer numbers.')
            continue

        break

    os.system('cls')
    key_int = int(key)
    encrypted_word = ''
    decrypted_word = ''

    if e_or_d == 'e':
        word_encrypter()
        print(f'{word} encrypted is: \n{encrypted_word}\n')
    elif e_or_d == 'd':
        word_decrypter()
        print(f'{word} decrypted is: \n{decrypted_word}\n')

    print('Do you wish to enter a new word to encrypt/decrypt? [y/n]')

    while True:
        redo = input().lower()

        if len(redo) > 1:
            os.system('cls')
            print('Please type only one character.\n')
            print('Do you wish to enter a new word to encrypt/decrypt? [y/n]')
            continue

        elif len(redo) == 0:
            os.system('cls')
            print('Please type something.\n')
            print('Do you wish to enter a new word to encrypt/decrypt? [y/n]')
            continue

        elif redo not in alphabet_str:
            os.system('cls')
            print('Please type a letter.\n')
            print('Do you wish to enter a new word to encrypt/decrypt? [y/n]')
            continue

        elif redo != 'y' and redo != 'n':
            os.system('cls')
            print('Please type one of the specified letters.\n')
            print('Do you wish to enter a new word to encrypt/decrypt? [y/n]')
            continue

        elif redo == 'y' or redo == 'n':
            break

    if redo == 'y':
        os.system('cls')
        continue
    elif redo == 'n':
        os.system('cls')
        print('Thanks for utilizing me!')
        break