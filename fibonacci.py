def fibonacci_series(n):
    '''
    generate the Fibonacci sequence to 
    that number or to the Nth number.
    '''

    a, b = 0, 1

    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

if __name__ == "__main__":
    value = int(input('Please, enter a fibonacci series number: '))
    
    fibonacci_series(value)