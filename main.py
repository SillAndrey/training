import math
import random

def pi_digits(n):
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
    

def e_digits(n):
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
    pi_value = int(input('Please, enter a pi value: '))
    pi_result = pi_digits(pi_value)
    e_value = int(input('Please, enter a e value:'))
    e_result = e_digits(e_value)

    print('Pi number: {}\nE number: {}'.format(pi_result, e_result))