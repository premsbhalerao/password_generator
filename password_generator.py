import random

print('welcome to your password generator')

chars = 'abcdefghijklmnopurstuvwxzABCDEFGHIJKLMNOPURSTUVWXZ!@#$%^&*().,?0123456789'

number = input('amount of passwords to generate: ')
number = int(number)

length = input('your password length : ')

length = int(length)

print('\nhere are your passwords : ')

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)