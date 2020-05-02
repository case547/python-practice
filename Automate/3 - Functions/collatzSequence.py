print('Enter a number:')
try:
    n = int(input())
except ValueError:
    print('You must enter an integer')

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

while n != 1:
    n = collatz(int(n))