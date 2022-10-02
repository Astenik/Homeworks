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



# 4-th task

'''
   this project produces a list of the gaps
   between consecutive entries in L.
   Then find the maximum gap size and
   the percentage of gaps that have 
   size 2.
'''

size = int(input("insert the size of your list: "));

L = [None] * size;
for num in range(size):
     L[num] = int(input("insert L's num: "));

gaps = [];
_max = 0;
for i in range(size - 1):
     for j in range(i + 1, size):
         k = L[j] - L[i];
         gaps.append(k);
         _max = max(_max, k);

print(f"the max gap is: {_max}")

count = 0;
for num in gaps:
     if num == 2:
          count += 1;

percentage = count * 100 / len(gaps);

print(f"the percentage of 2's in gaps is: {percentage}")



# 5-th task


count = int(input("How many products you have? "))

products_and_pices = {} 

for i in range(count):
     name = input("insert product name: ")
     pice = int(input("insert product pice: "))
     products_and_pices[name] = pice;

num = input("insert the product name you want to know the pice: ")

if num in products_and_pices:
      print(f"your product pice is: {products_and_pices[num]}")

else:
      print("your product is not in list.")


# 6-th task

count = int(input("insert the count of users: "));

users = {};

for i in range(count):
     name = input("insert the user name: ");
     phone = input("insert the user phone: ");
     email = input("insert the user email: ");
     users[f'user{i}'] = { 'name': name,
                  'phone': phone,
                  'email' : email }

for user in users:
     if users[user]['email'] == '':
          print("user that don't have email.")
          print(users[user]['name']);
     if users[user]['phone'][-1] == '8':
          print("user whos phone number ends with 8.")
          print(users[user]['name']);

            
# 7-th task

matrix = [];
L = []
for i in range(5):
     for j in range(5):
          L.append(int(input("insert number: ")))
     matrix.append(L)

counts = {};

for i in range(5):
     for j in range(5):
         num = matrix[i][j]
         if f"num{num}" in counts:
              counts[f"num{num}"] += 1;
         else:
              counts[f"num{num}"] = 1; 

res = [];
for num in counts:
    res.append(counts[num]);

sorted(res);
print(res[:3])
