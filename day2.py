#first homework

'''
This program asks the user for a weight
in kilograms and converts it to pounds.
1 Kg = 2.2 Pound.
'''

weight = float(input("insert the weight with kilograms: "))

print(f"yourweight with pounds is equal to: {2.2 * weight}")


#second homework

'''
This program generates and 
prints 50 random integers
each integer between 3 and 6.
'''

import random

res = [None] * 50
for num in range(50):
      res[num] = random.randint(3, 6)

print(f"50 numbers are: {res}")


#3-rd homework

'''
This program asks the user 
to enter two integers: x and y.
And clculates 
|x - y| / x + y.
'''

num1 = int(input("insert first integer: "))
num2 = int(input("insert second integer: "))
res = num1 - num2
if res < 0:
    res = res - 2 * res

res = res / (num1 + num2)

print(f"resul is: {res}")



#4-th homework

'''
This program counts how many
leap years there have been
between 1600 and that year.
'''
year = int(input("insert year: "))
num = year - 1600
count = num // 4 
x = num // 100 
count -= x 
x = num // 400 
count += x 

print(f"the count of leap years is: {count}")


#5-th homework

'''
This program prints perfect
numbers in interval (0, num)
'''

def is_pefect(num: int):
      if num == 1:
          return False
      s = 1
      for n in range(2, num):
           if num % n == 0:
               s += n
      return s == num

number = int(input("insert number: "))
res = []
for num in range(1, number):
     if is_pefect(num):
         res.append(num)

print(f"perfec numbers are: {res}")




