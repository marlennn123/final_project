import random

def gen_number(number):
    a = random.randint(0, number)
    b = random.randint(0, number)
    print(a, b)

num = int(input(': '))

gen_number(num)