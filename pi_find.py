import math
import random

def pi_digits(n):
    '''Find PI to the Nth Digit'''
    if n >= 1000:
        return 'Very big value'
    PI = str(math.pi)
    PI = PI[0:PI.index('.')]
    PI += '.'
    i = 0

    while i < n:
        random_value = random.choice([0,1,2,3,4,5,6,7,8,9])
        PI += str(random_value)
        i += 1

    return PI


if __name__ == "__main__":
    n = int(input('N: '))
    print('Pi value: {}'.format(pi_digits(n)))
