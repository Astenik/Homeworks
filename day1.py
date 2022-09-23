# first homework

'''this small project asks user to enter the
   number and the checs if the number
   is odd or even.'''
   
number = int(input("insert the number: "))
if number % 2 ==  0:
      print("the number is even.")
else: 
      print("the number is odd.")
      

# second homework

'''this small project asks user to enter the
   character and the checs if the character
   is consonant or vowel.'''
   
sym = input("insert a character: check that your char is lowercase: ")
if len(sym) > 1:
      print("Wrong input.")
elif sym in ('a', 'e', 'o', 'i', 'u'): 
      print("the character is vowel.")
else:
      print("the character is consonant.")
      
   
# thired homework

'''this small project asks user to enter the
   n number and  prints fibonachii n-th number.'''
   
def fib(number: int):
      '''this function count the fibonachi number-th member.'''
      if n <= 2 and n >= 0:
           return 1 
      num1 = 1
      num2 = 1 
      num = num1 + num2
      count = number - 3
      while count > 0:
          num1 = num2
          num2 = num
          num = num1 + num2
          count -= 1 
      return num 

n = int(input("insrt the n: "))
print(f"the n-th number of fibonachi is: {fib(n)}")


# 4-th homework

'''this project asks the number from a user
   and counts sum of digits of that number.'''
 
def sum_of_dig(number: int):
     '''this function counts the sum of 
        digits of number.
        number is the argument of function.'''
     num = number
     _sum = 0
     while num != 0:
         _sum += num % 10 
         num //= 10 
     return _sum 

number = int(input("insert the number: "))
print(f'the sum of digits of your number is: {sum_of_dig(number)}')


# 5-th homework

'''this project prints at the screen
   *****
   *   *
   *   *
   *   *
   *****
   '''
def matrix(length: int, high: int):
      count1 = 1;
      lst = [];
      res = [];
      while count1 <= length:
          lst.append('*');
          count1 += 1;
      res.append(lst); 
      count1 = 1;
      count2 = high - 2; 
      mid = ['*']
      while count1 < length - 1:
          mid.append(' ')
          count1 += 1;
      mid.append('*')
      while count2 > 0:
          res.append(mid);
          count2 -= 1;
      res.append(lst);
      for num in res:
          print(''.join(num));

matrix(5, 5)



