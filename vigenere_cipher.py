import re


def vigenereCipher():
    """
    Entry function for the Vigenere cipher. Prompts the user to use encryption or decryption, then prompts for the key
    and the plaintext or ciphertext.
    """
    method = -1

    while method != 0:
        try:
            print('Vigenere Cipher: ')

            method = int(input('Menu:\n1) Encrypt\n2) Decrypt\n0) Exit\nEnter a number: '))
            if method != 1 and method != 2:
                if method != 0:
                    print('Must enter 0, 1, or 2 to select encryption, decryption, or exit')
                continue

            key = input('Enter key (letters, no spaces): ')
            if re.search(r'[^a-zA-z]', key) is not None:
                print('\nKey must contain only letters.')
                continue

            text = input('Enter ' + ('plaintext' if method == 0 else 'ciphertext') + ' (no spaces): ')
            if re.search(r'[^a-zA-z]', text) is not None:
                print('\nText must contain only letters.')
                continue

            if method == 1:
                encrypt(key, text)
            elif method == 2:
                decrypt(key, text)

        except ValueError:
            print('\nMust enter an integer.')

        print('\n')


def encrypt(key, plaintext):
    """
    Encrypts the given plaintext with the given key using the vigenere cipher. Prints the resulting ciphertext to
    console.
    :param key: String representing the key
    :param plaintext: String representing the plaintext
    """
    key = key.lower()
    plaintext = plaintext.lower()
    ciphertext = ''

    for index, char in enumerate(plaintext):
        keyIndex = index % len(key)
        charNumber = ord(char) - 97
        keyNumber = ord(key[keyIndex]) - 97

        cipherNumber = (keyNumber + charNumber) % 26

        ciphertext += chr(cipherNumber + 97)

    print('\nCiphertext:', ciphertext)


def decrypt(key, ciphertext):
    """
    Decrypts the given ciphertext with the given key using the vigenere cipher. Prints the resulting plaintext to
    console.
    :param key: String representing the key
    :param ciphertext: String representing the ciphertext
    """
    key = key.lower()
    ciphertext = ciphertext.lower()
    plaintext = ''

    for index, char in enumerate(ciphertext):
        keyIndex = index % len(key)
        cipherNumber = ord(char) - 97
        keyNumber = ord(key[keyIndex]) - 97

        plainNumber = (cipherNumber - keyNumber) % 26
        if plainNumber < 0:
            plainNumber = 26 - abs(plainNumber)

        plaintext += chr(plainNumber + 97)

    print('\nPlaintext:', plaintext)


if __name__ == '__main__':
    vigenereCipher()
