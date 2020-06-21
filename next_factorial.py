def next_factorial(n):
    '''
    find all Prime Factors (if there are any) and display them.
    program find prime numbers until the user chooses to stop asking for the next one.
    '''
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)

    return Ans

if __name__ == "__main__":
    n = int(input('Please, enter factorial: '))
    result = next_factorial(n)
    iterable_obj = iter(result)

    while True:
        select = input('\nEnter \'next\', for next prime number, or \'stop\' for exit: ')

        if select == 'next':
            try:
                print(iterable_obj.__next__())
            except StopIteration:
                print('iteration is over')
                break
        elif select == 'stop':
            break