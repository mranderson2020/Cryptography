from cryptomath import *

alphaValues = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]


def knownPlaintext(plaintext, ciphertext):
    """
    Performs a known plaintext attach on an affine cipher. Requires at least two characters of both the plaintext and
    ciphertext to successfully decipher the alpha and beta values. Prints the results to console.
    :param plaintext: Known plaintext string
    :param ciphertext: Ciphertext string corresponding to the plaintext
    """
    if len(plaintext) < 2 or len(ciphertext) < 2:
        print('Must have at least 2 letters in plaintext and ciphertext.')
        return

    plaintext = plaintext.lower()
    ciphertext = ciphertext.lower()

    charVal1 = getCharValue(plaintext[0])
    charVal2 = getCharValue(plaintext[1])
    resultVal1 = getCharValue(ciphertext[0])
    resultVal2 = getCharValue(ciphertext[1])

    charValDifference = subtractMod(charVal1, charVal2, 26)
    resultValDifference = subtractMod(resultVal1, resultVal2, 26)

    # charValDiff * alpha = resultValDiff
    possibleAlpha = divisionMod(resultValDifference, charValDifference, 26)
    if possibleAlpha is None:
        print('Could not find an alpha value')
        return

    alpha = None
    for a in possibleAlpha:
        if a in alphaValues:
            alpha = a

    beta = subtractMod(resultVal1, charVal1 * alpha, 26)

    print('Alpha: ', alpha, sep='')
    print('Beta: ', beta, sep='')


if __name__ == '__main__':
    plain = input('Enter at least two letters of the plaintext: ')
    cipher = input('Enter at least two letters of the ciphertext: ')
    knownPlaintext(plain, cipher)
