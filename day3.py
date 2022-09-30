# first task 

'''this program allows the userto enter
   five numbers (read as strings) 
   Creat a string that consists of the
   user's numbers seperated by plus
   sign.
   For instance, if the user enters 2, 
   5, 11, 33, 55, then the string should be 
   '2+5+11+33+55'.
''' 

res = ''
for num in range(4):
     res += input("insert number: ")
     res += '+' 
res += input("insert number: ") 

print(f"the result string is: {res}")




# second task 

'''this program gets the string
   from the user containing potential
   phone number and deside if it is valid
   number or not.
'''


def val_or_inval(phon_number: str):
      res = phon_number.split('-')
      if (len(res) > 4) or (len(res) < 3):
         return 'invalid'
      if res[0] == '1':
          for i in range(1, len(res) - 1):
              if len(res[i]) != 3:
                   return 'invalid' 
              for j in range(3):
                  if res[i][j] >= '0' and res[i][j] <= '9':
                      continue 
                  else:
                      return 'invalid'
          if len(res[-1]) != 4:
              return 'invalid'
          for j in range(4):
                  if (res[-1][j] >= '0') and (res[-1][j] <= '9'):
                      continue 
                  else:
                      return 'invalid' 
          return 'valid'
      else:
          for i in range(len(res) - 1):
              if len(res[i]) != 3:
                   return 'invalid' 
              for j in range(3):
                  if (res[i][j] >= '0') and (res[i][j] <= '9'):
                      continue 
                  else:
                      return 'invalid'
          if len(res[-1]) != 4:
              return 'invalid'
          for j in range(4):
                  if (res[-1][j] >= '0') and (res[-1][j] <= '9'):
                      continue 
                  else:
                      return 'invalid' 
          return 'valid'
                   
p_number = input("insert the phone number: ")

print(val_or_inval(p_number))




# 3-rd task 

'''this program give all
   palindrome numbers between
   100 and 1000.
''' 

def is_palindrome(number: int):
      cpy = number
      rev = 0 
      while cpy != 0:
           rev *= 10
           rev += cpy % 10 
           cpy //= 10 
      return number == rev 

res = []
for num in range(100, 1001):
      if is_palindrome(num):
          res.append(num)

print(f"palindrome numbers are: {res}")
























