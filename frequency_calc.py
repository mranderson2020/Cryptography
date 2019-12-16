import sys
import collections
import string


def freqCalc():
    """
    Entry function for the frequency calculator. Prompts the user for a file to read in and calculates the frequency
    of each character in the file. Prints the results to console.
    """
    try:
        print('Frequency Calculator\n')

        if len(sys.argv) < 2:
            file = input('Enter file path: ')
        else:
            file = sys.argv[1]

        fin = open(file)

        charCount = countCharacters(fin)
        printResults(charCount)

    except ValueError:
        print('\nMust enter an integer.')

    print('\n')


def countCharacters(fin):
    """
    Counts the frequency of each character in the given file.
    :param fin: Opened file to perform frequency calculation on
    :return: Dictionary containing the frequency of each character
    """
    charCount = {}

    for line in fin:
        for char in line:
            if char in charCount.keys():
                charCount[char] += 1
            else:
                charCount[char] = 1

    return charCount


def convertCharacterCountToList(charCount):
    """
    Converts the given character frequency count dictionary to a list containing only counts of letters (ignoring case).
    This is used for frequency attacks on ciphers which only use letters.
    :param charCount: Dictionary containing the frequency of each character
    :return: List containing the frequency counts of each letter
    """
    charList = [0]*26

    for index, char in enumerate(string.ascii_lowercase):
        if char in charCount:
            charList[index] += charCount[char]
        if char.upper() in charCount:
            charList[index] += charCount[char.upper()]

    return charList


def printResults(charCount):
    """
    Prints the character count dictionary to console.
    :param charCount: Dictionary containing the frequency of each character
    """
    charCountSorted = collections.OrderedDict(sorted(charCount.items()))

    for key, value in charCountSorted.items():
        if key == ' ':
            key = '\u2423'
        elif key == '\n':
            key = '\\n'
        print(key, ': ', str(value), sep='')


if __name__ == '__main__':
    freqCalc()
