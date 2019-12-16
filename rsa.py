from cryptomath import *
from random import randint


def rsa():
    """
    Generates the private and public keys for the RSA algorithm.
    :return: Three integers - public encrypt, private decrypt, public mod
    """
    p = randomPrime(10)
    q = randomPrime(10)
    n = p * q

    p1q1 = (p - 1) * (q - 1)
    e = randint(100, p1q1 / 2)
    while gcd(e, p1q1) != 1:
        e = randint(100, p1q1 / 2)

    d = findModInverse(e, p1q1)

    return e, d, n


def encrypt(e, n, m):
    """
    Encrypts the given message using the given encryption keys.
    :param e: Integer encryption key
    :param n: Integer mod
    :param m: Integer message
    :return: Integer cipher
    """
    return pow(m, e, n)


def decrypt(d, n, c):
    """
    Decrypts the given message using the given decryption keys.
    :param d: Integer decryption key
    :param n: Integer mod
    :param c: Integer cipher
    :return: Integer message
    """
    return pow(c, d, n)


def checkMessageValid(m):
    """
    Validates the message is an integer (due to not yet implementing a conversion from string to integer).
    :param m: Integer message
    :return: Boolean indicating whether message is an integer
    """
    try:
        int(m)
    except:
        print('Message must be an integer\n')
        return False
    return True


if __name__ == '__main__':
    print('Generating keys...')

    encryption, decryption, mod = rsa()

    print('Public keys: e = ', encryption, ' n = ', mod, sep='')
    print('Private keys: d = ', decryption, sep='')

    userIn = ''

    while userIn != '0':
        print('\n1) Encrypt\n2) Decrypt\n0) Exit')
        userIn = input('Enter a value from above: ')

        if userIn == '1':
            message = input('Enter plaintext (as an integer): ')
            if checkMessageValid(message):
                print(encrypt(encryption, mod, int(message)))
        elif userIn == '2':
            message = input('Enter ciphertext (as an integer): ')
            if checkMessageValid(message):
                print(decrypt(decryption, mod, int(message)))
