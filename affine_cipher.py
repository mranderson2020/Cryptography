from cryptomath import *
import re


def affineCipher():
    """
    Entry function for the affine cipher. Gets user input and calls necessary functions to encrypt or decrypt messages.
    """
    method = -1

    while method != 0:
        try:
            print('Affine Cipher (mod 26 - letters only): \u03B1x + \u03B2\n')

            method = int(input('Menu:\n1) Encrypt\n2) Decrypt\n0) Exit\nEnter a number: '))
            if method != 1 and method != 2:
                if method != 0:
                    print('Must enter 0, 1, or 2 to select encryption, decryption, or exit')
                continue

            alpha = int(input('Enter alpha (\u03B1): '))
            if gcd(alpha, 26) != 1:
                print('Alpha (\u03B1) must be a co-prime of 26 (i.e. gcd(\u03B1, 26) = 1)')
                continue

            beta = int(input('Enter beta (\u03B2): '))
            text = input('Enter ' + ('plaintext' if method == 0 else 'ciphertext') + ': ')
            if re.search(r'[^a-zA-z]', text) is not None:
                print('\nPlaintext and ciphertext must contain only letters.')
                continue

            if method == 1:
                encrypt(alpha, beta, text)
            elif method == 2:
                decrypt(alpha, beta, text)

        except ValueError:
            print('\nMust enter an integer.')

        print('\n')


def encrypt(alpha, beta, plaintext):
    """
    Encrypts the given plaintext using the given alpha and beta values for an affine cipher. Prints the ciphertext.
    :param alpha: Integer alpha value
    :param beta: Integer beta value
    :param plaintext: Plaintext string
    """
    ciphertext = ''

    for char in plaintext:
        charNumber = ord(char) - 97
        cipherCharNumber = ((charNumber * alpha) + beta) % 26
        ciphertext += chr(cipherCharNumber + 97)

    print('\nCiphertext:', ciphertext)


def decrypt(alpha, beta, ciphertext):
    """
    Decrypts the given ciphertext using the given alpha and beta values for an affine cipher. Prints the plaintext.
    :param alpha: Integer alpha value
    :param beta: Integer beta value
    :param ciphertext: Ciphertext string
    """
    inverse = findModInverse(alpha, 26)

    plaintext = ''

    for char in ciphertext:
        charNumber = ord(char) - 97
        charNumber = (inverse * (charNumber - beta)) % 26
        plaintext += chr(charNumber + 97)

    print('\nPlaintext:', plaintext)


if __name__ == '__main__':
    affineCipher()
