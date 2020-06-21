def Factor(n):
    '''
    find all Prime Factors (if there are any) and display them.
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
    number = int(input('Enter a number: '))
    print(Factor(number))