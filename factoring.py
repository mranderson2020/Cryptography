from cryptomath import *
import math


def factorPollardP1(n, bound):
    """
    Factors n using the given bound using the Pollard p-1 method
    :param n: Integer to factor
    :param bound: Integer bound to use for Pollard p-1 method
    :return: Integer representing one factor
    """
    b = 2
    for i in range(2, bound):
        b = pow(b, i, n)
        d = gcd(b-1, n)
        if 1 < d < n:
            return d
    return -1


def pollardP1(n):
    """
    Entry function for the Pollard p-1 factorization method. Factors the given value using Pollard p-1 method.
    :param n: Integer to factor
    :return: Two integers - each a factor of n
    """
    bound = int(pow(n, (1/27)))
    result = -1

    while bound < n and result == -1:
        result = factorPollardP1(n, bound)
        bound += 1

    return result, n // result


def fermat(n):
    """
    Factors the given value using Fermat's factorization method.
    :param n: Integer to factor
    :return: Two integers - each a factor of n
    """
    a = math.ceil(math.sqrt(n))
    b2 = a * a - n
    b = math.sqrt(b2)

    while b * b != b2:
        a += 1
        b2 = a * a - n
        b = math.sqrt(b2)

    f = int(a - math.sqrt(b2))
    return f, n // f


def pollardRho(n):
    """
    Factors the given alue using Pollard rho factorization method.
    :param n: Integer to factor
    :return: Two integers - each a factor of n
    """
    a = 2
    b = 2
    d = 1

    while d == 1:
        a = pollardRhoG(a, n)
        b = pollardRhoG(pollardRhoG(b, n), n)
        d = gcd(abs(a - b), n)

    if d == n:
        return -1, -1
    else:
        return d, n // d


def pollardRhoG(x, n):
    """
    g(x) function for the Pollard rho method. In most cases, it is set to x^2 - 1 (mod n), so that is what I've set it
    to here
    :param x: Integer value to pass through function g(x)
    :param n: Integer mod
    :return: Integer result of g(x)
    """
    return (x * x - 1) % n


def wheelFactorization(n):
    """
    Factors the given value using the wheel factorization method.
    :param n: Integer to factor
    :return: Two integers - each a factor of n
    """
    test = False

    if n % 2 == 0:
        return 2, n // 2
    elif n % 3 == 0:
        return 3, n // 3
    elif n % 5 == 0:
        return 5, n // 5

    k = 7
    i = 1
    inc = [4, 2, 4, 2, 4, 6, 2, 6]

    while test == False and k * k <= n:
        test = (n % k == 0)
        if test:
            return k, n // k

        k = k + inc[i]
        if i < 8:
            i += 1
        else:
            i = 1

    return -1, -1


def factor(n, m):
    """
    Entry function for factorization methods. Passes on value to factor to the desired function and prints the results
    to console.
    :param n: Integer to factor
    :param m: Method to use: 1 - Fermat, 2 - Pollard rho, 3 - Pollard p-1, 4 - Wheel method
    """
    if m == 1:
        factor1, factor2 = fermat(n)
    elif m == 2:
        factor1, factor2 = pollardRho(n)
    elif m == 3:
        factor1, factor2 = pollardP1(n)
    elif m == 4:
        factor1, factor2 = wheelFactorization(n)
    else:
        return

    if factor1 == -1:
        print('No factors found\n')
    else:
        print('Factors: ', factor1, ', ', factor2, '\n', sep='')


if __name__ == '__main__':
    while True:
        print('1) Fermat\'s Method\n2) Pollard rho\n3) Pollard p-1\n4) Wheel Factorization\n0) Exit')
        method = int(input('Choose a factor method: '))

        if method == 0:
            exit(0)

        number = int(input('Enter a composite number (n): '))

        factor(number, method)