from random import randint


def findModInverse(num, mod):
    """
    Finds the inverse of a number under modulus
    :param num: Integer to inverse
    :param mod: Mod under which to inverse
    :return: Integer representing inverse of num
    """
    result, s, t = extendedgcd(num, mod)

    if abs(s) >= mod:
        s = s % mod

    if s > 0:
        return s
    else:
        return mod - abs(s)


def gcd(a, b):
    """
    Calculates the gcd of two integers
    :param a: Integer a
    :param b: Integer b
    :return: Integer - gcd(a,b)
    """
    if a == 0:
        return b
    else:
        return gcd(b % a, a)


def extendedgcd(a, b):
    """
    Calculates the extended gcd of two integers. Returns d, x, and y from the equation ax + by = d
    :param a: Integer a
    :param b: Integer b
    :return: Integers - d, x, y
    """
    if a == 0:
        return b, 0, 1
    else:
        euclid, x, y = extendedgcd(b % a, a)
        return euclid, y - (b // a) * x, x


def isPrime(n):
    """
    Checks if the given number is a prime using the Miller-Rabin primality test
    :param n: Integer to check primality of
    :return: Boolean indicating whether the number is prime
    """
    m = n - 1
    k = 0

    while m % 2 == 0 and m != 0:
        m //= 2
        k += 1

    a = 2
    b = pow(a, m, n)

    if b == 1 or b == n-1:
        return True

    while k > 0:
        k -= 1
        b = pow(b, 2, n)

        if b == 1:
            return False
        if b == n-1:
            return True

    return False


def randomPrime(b):
    """
    Returns a random prime number within the range of 2^(b+1) - 1 and 2^b - 1
    :param b: Integer boundary
    :return: Integer prime number
    """
    rand = randint(2 ** b - 1, 2 ** (b+1) - 1)

    while not isPrime(rand):
        rand = randint(2 ** b - 1, 2 ** (b+1) - 1)

    return rand


def isPrimitiveRoot(a, n):
    """
    Tests if the given number (a) is a primitive root (mod n)
    :param a: Integer to test if primitive root
    :param n: Integer mod to test under
    :return: Boolean indicating if a is primitive root
    """
    generatedValues = [a]

    for i in range(1, n):
        value = (a ** i) % n
        if value not in generatedValues:
            generatedValues.append(value)

    if len(generatedValues) != (n-1):
        return False
    return True


def isSquareMod(a, n):
    """
    Test if the given number (a) is a square (mod n)
    :param a: Integer to test if it is a square
    :param n: Integer mod under which to test
    :return: Boolean indicating if a is a square
    """
    a = a % n

    for i in range(2, n):
        if (i ** 2) % n == a:
            return True
    return False


def getCharValue(char):
    """
    Returns the integer value (0 - 25) of the given character
    :param char: Character to get value of
    :return: Integer representing character's value
    """
    return ord(char) - 97


def getCharAtValue(value):
    """
    Returns the character with the given value (0 - 25)
    :param value: Value of the character
    :return: Character with the given value
    """
    return chr(value + 97)


def addMod(a, b, n):
    """
    Adds two numbers together under mod n
    :param a: Integer a to add
    :param b: Integer b to add
    :param n: Integer mod
    :return: Result of a + b (mod n)
    """
    return (a + b) % n


def subtractMod(a, b, n):
    """
    Subtracts two numbers under mod n
    :param a: Integer a
    :param b: Integer b
    :param n: Integer mod
    :return: Result of a - b (mod n)
    """
    result = (a - b) % n

    if result < 0:
        result = n - result

    return result


def divisionMod(dividend, divisor, n):
    """
    Divides two numbers under mod n. Returns all results of divisor * num (mod n) == dividend
    :param dividend: Integer dividend
    :param divisor: Integer divisor
    :param n: Integer mod
    :return: Tuple containing all results
    """
    results = ()

    for i in range(2, n):
        if (divisor * i) % n == dividend:
            results = results + tuple([i])

    if len(results) == 0:
        return None
    return results


if __name__ == '__main__':
    print('3 inverse (mod 26):', findModInverse(3, 26))

    print('\nIs primes:')
    print(isPrime(561))
    print(isPrime(11))
    print(isPrime(15))
    print(isPrime(113))
    print(isPrime(11005))
    print(isPrime(12490243))

    print("\nPrimitive Roots:")
    print(isPrimitiveRoot(3, 7))
    print(isPrimitiveRoot(2, 13))
    print(isPrimitiveRoot(3, 13))
