from string import digits
from random import choice

# the program guesses a random number
if __name__ == "__main__":
    counter = 3

    while counter > 0:
       
        number = int(choice(digits))

        guess_number = int(input('Please, enter a number: '))
        
        if guess_number == number:
            print('***YOU WIN***')
            break
        elif guess_number > number:
            print('Number very large')
        elif guess_number < number:
            print('Number very small')
        else:
            print('Invalid value')
        counter -= 1
        print('You have {} attempts'.format(counter))
        
