from cryptomath import *


def promptForRecurrenceRelation():
    """
    Prompts the user for the required data for a recurrence relation for the LFSR cipher. Then, passes the relation of
    to another function to get the initial recurrence values.
    """
    print('Linear Feedback Shift Register Sequence:')
    print('x_[m+#] = ...')
    m = int(input('Please select a value for # above: '))

    print('\nx_[m+', m, '] = ', sep='', end='')
    for i in reversed(range(1, m)):
        print('Cx_[m+', i, '] + ',  sep='', end='')
    print('Cx_[m]')

    coefficients = ''
    validInput = False
    while not validInput:
        coefficients = input('Enter ' + str(m) + ' coefficients (0 or 1) for each C in the order above (spaces not '
                                                 'required): ').replace(' ', '')

        if len(coefficients) == m:
            validInput = checkCoefficients(coefficients)
        else:
            validInput = False
            print('Enter exactly', m, 'coefficients.\n')

    coefficientsList = []
    for c in coefficients:
        if c == '0':
            coefficientsList.append(0)
        elif c == '1':
            coefficientsList.append(1)

    print('\nLinear Recurrence Relation:\nx_[m+', m, '] = ', sep='', end='')
    for index, coef in enumerate(coefficientsList):
        if coef == 1 and index != len(coefficientsList)-1:
            print('x_[m+', len(coefficientsList)-index-1, '] + ', sep='', end='')

    if coefficientsList[len(coefficientsList)-1] == 1:
        print('x_[m]\n')
        
    initialValues = getInitialValues(m)

    promptForOperation(coefficientsList, initialValues)


def getInitialValues(m):
    """
    Prompts the user for the initial values for the recurrence relation. Returns those values as a list.
    :param m: Number of initial values required
    :return: Initial values stored as a list
    """
    values = ''
    validInput = False
    while not validInput:
        values = input('Enter ' + str(m) + ' initial values (0 or 1; spaces not required): ').replace(' ', '')

        if len(values) == m:
            validInput = checkCoefficients(values)
        else:
            validInput = False
            print('Enter exactly', m, 'values.\n')

    valuesList = []
    for c in values:
        if c == '0':
            valuesList.append(0)
        elif c == '1':
            valuesList.append(1)

    return valuesList


def promptForOperation(coefficients, initialValues):
    """
    Prompts the user for the desired operation, either encryption or decryption.
    :param coefficients: List storing the recurrence relation coefficients
    :param initialValues: List storing the initial values for the recurrence relation
    """
    userIn = ''

    while userIn != '0':
        print('\n1) Encrypt\n2) Decrypt\n0) Exit')
        userIn = input('Enter a value from above: ')

        if userIn == '1':
            encrypt(coefficients, initialValues)
        elif userIn == '2':
            decrypt(coefficients, initialValues)


def encrypt(coefficients, initialValues):
    """
    Prompts the user for a plaintext binary string to encrypt using the LFSR cipher. Encrypts the plaintext and prints
    the result.
    :param coefficients: List storing the recurrence relation coefficients
    :param initialValues: List storing the initial values for the recurrence relation
    """
    plaintext = ''
    validInput = False
    while not validInput:
        plaintext = input("Enter plaintext binary string (0's and 1's): ").replace(' ', '')

        validInput = checkCoefficients(plaintext)

    plaintextList = []
    for p in plaintext:
        if p == '0':
            plaintextList.append(0)
        elif p == '1':
            plaintextList.append(1)

    key = extendKey(coefficients, initialValues, len(plaintext))
    ciphertext = addBits(plaintextList, key)

    print('Ciphertext:', ''.join(str(c) for c in ciphertext))


def decrypt(coefficients, initialValues):
    """
    Prompts the user for a ciphertext binary string to decrypt using the LFSR cipher. Decrypts the ciphertext and prints
    the result.
    :param coefficients: List storing the recurrence relation coefficients
    :param initialValues: List storing the initial values for the recurrence relation
    """
    ciphertext = ''
    validInput = False
    while not validInput:
        ciphertext = input("Enter ciphertext binary string (0's and 1's): ").replace(' ', '')

        validInput = checkCoefficients(ciphertext)

    ciphertextList = []
    for p in ciphertext:
        if p == '0':
            ciphertextList.append(0)
        elif p == '1':
            ciphertextList.append(1)

    key = extendKey(coefficients, initialValues, len(ciphertext))
    ciphertext = addBits(ciphertextList, key)

    print('Plaintext:', ''.join(str(c) for c in ciphertext))


def addBits(a, b):
    """
    Adds two bits together, effectively XORing them. Returns the result
    :param a: Bit a
    :param b: Bit b
    :return: The result of a + b (mod 2)
    """
    result = []
    for index in range(len(a)):
        result.append(addMod(a[index], b[index], 2))

    return result


def extendKey(coefficients, initialValues, length):
    """
    Extends the key (initial values) to match the desired length.
    :param coefficients: List storing the recurrence relation coefficients
    :param initialValues: List storing the initial values for the recurrence relation
    :param length: The desired length of the key
    :return: List storing the values of the key
    """
    key = initialValues

    for i in range(len(initialValues), length):
        newValue = 0

        for index, c in enumerate(coefficients):
            if c == 1:
                newValue = addMod(newValue, key[i - index - 1], 2)

        key.append(newValue)

    return key


def checkCoefficients(coef):
    """
    Checks that the given coefficient values are valid, i.e. they are only 0 or 1.
    :param coef: List storing the recurrence relation coefficients
    :return: Boolean indicating whether the coefficients are valid
    """
    for c in coef:
        if c != '0' and c != '1':
            print('Values can only be 0 or 1.\n')
            return False

    return True


if __name__ == '__main__':
    promptForRecurrenceRelation()
