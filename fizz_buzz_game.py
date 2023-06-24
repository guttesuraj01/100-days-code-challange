for n in range(1,20):
    if n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    if n % 3 == 0 and n % 5 == 0:
        print('fizzbuzz')
    else:
        print(n)