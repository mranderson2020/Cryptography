from cryptomath import *
from frequency_calc import countCharacters, convertCharacterCountToList
from collections import deque

letterFrequencies = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002, 0.008, 0.040, 0.024, 0.067,
                     0.075, 0.019, 0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.023, 0.001, 0.020, 0.001]


def findKeyLength(ciphertext):
    """
    Performs the first step of the vigenere cipher attack to find the length of the key based on the given ciphertext.
    Returns the result.
    :param ciphertext: String representing the ciphertext
    :return: Integer representing the key length
    """
    ciphertext = ciphertext.lower()

    totalCoincidences = 0
    keyLength = 0
    cipherDisplaced = ciphertext

    i = len(ciphertext) - 1
    while i > totalCoincidences:
        coincidences = 0
        cipherDisplaced = ' ' + cipherDisplaced
        for index, char in enumerate(ciphertext):
            if char == cipherDisplaced[index]:
                coincidences += 1

        if totalCoincidences < coincidences:
            totalCoincidences = coincidences
            keyLength = len(ciphertext) - i

        i -= 1

    return keyLength


def vigenereCipherAttack(ciphertext):
    """
    Deciphers the given cipher text. Calls the necessary function to find the key length then attempts to decipher the
    key.
    :param ciphertext: String representing the ciphertext
    :return: String representing the key
    """
    ciphertext = ciphertext.lower()
    key = ''
    keyLength = findKeyLength(ciphertext)

    letterFreq = deque(letterFrequencies)

    while len(key) < keyLength:
        charList = countOccurrences(len(key), keyLength, ciphertext)
        largestDotProduct = 0
        shiftCount = 0

        i = 0
        while i < 26:
            dotProduct = sum(i[0] * i[1] for i in zip(charList, letterFreq))
            if largestDotProduct < dotProduct:
                largestDotProduct = dotProduct
                shiftCount = i

            letterFreq.rotate(1)
            i += 1

        key += getCharAtValue(shiftCount)

    return key


def countOccurrences(startingPos, keyLength, ciphertext):
    """
    Performs the step of counting the number of occurrences of each character given the key length, which indicates the
    increment size, and the starting position.
    :param startingPos: Index in the ciphertext to start counting at
    :param keyLength: Integer representing the key length
    :param ciphertext: String representing the ciphertext
    :return: List containing the frequencies of each character
    """
    ciphertext = ciphertext[startingPos:]
    ciphertext = ciphertext[::keyLength]
    charCount = countCharacters(ciphertext)
    charCountList = convertCharacterCountToList(charCount)
    charCountList[:] = [x / sum(charCountList) for x in charCountList]
    return charCountList


if __name__ == '__main__':
    cipher = input('Enter the ciphertext: ')
    vigenereCipherAttack(cipher)
