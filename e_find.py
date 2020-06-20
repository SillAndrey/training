import math
import random


def e_digits(n):
    '''Find e to the Nth Digit'''
    if n >= 1000:
        return 'Very big value'

    E = str(math.e)
    E = E[0:E.index('.')]
    E += '.'
    i = 0

    while i < n:
        random_value = random.choice([0,1,2,3,4,5,6,7,8,9])
        E += str(random_value)
        i += 1

    return E

if __name__ == "__main__":
    n = int(input('N: '))

    print('E: {}'.format(e_digits(n)))