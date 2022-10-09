#first task

'''
this program asks the user for an hour between 1 and 12
asks them to enter am or pm, and asks them how many 
hours into the future they want to go. This program prints 
out what the hour will be that many hours into the 
future printing am or pm as appropriate.
'''

hour = int(input("enter the hour: "))
am_pm = int(input("enter am(1) or pm(0): "))
hours = int(input("How many hoursahead? "))

time = (hour + hours) % 12 
if time == (hour + hours):
     if am_pm == 1:
          print(f"the time is: {time} am.")
     else:
          print(f"the time is: {time} pm.")

else:
      if am_pm == 1:
          print(f"the time is: {time} pm.")
      else:
          print(f"the time is: {time} am.")

          
#second task

import random
quiz = {
         "what the longers river is?": "Nile",
         "What programming language is faster Python or C++?" : "C++",
         "What programming language is interpreted Python or c++?" : "Python",
         "Who invented first bulb?" : "Thomas Edison",
         "What country is the smallest?" : "Vatican",
         "Who is Pyuthagoras" : "philosopher",
         "Is Java interpreted or compiled?": "interpreted",
         "Is C++ interpreted or compiled?" : "compiled",
         "is the Amazon the second longest river or the first?" : "second",
         "Who was the armenian millinaire in America that had busines of casino?" : "Kirk Kerkorian"
       }

count = 4
right_answers = 0
lst = []
for num in quiz.keys():
      lst.append(num)
while count > 0:
     question = random.choice(lst)
     print(question) 
     answer = input("answer: ")
     if answer == quiz[question]:
         right_answers += 1 
     count -= 1
     

print(f"your right answers' count is: {right_answers}")


#3-rd task

def count(lst, i, j):
    c = 0
    if i == 0:
        k = 0 
    else:
        k = -1
    if (i != 4) and (j != 4):
        while k < 2:
            if j == 0:
                q = 0
            else:
                q = -1
            while q < 2:
                if lst[i + k][j + q] == 'M':
                    c += 1 
                q += 1
            k += 1 
    elif (i == 4) and (j != 4):
        while k < 1:
            if j == 0:
                q = 0
            else:
                q = -1
            while q < 2:
                if lst[i + k][j + q] == 'M':
                    c += 1 
                q += 1
            k += 1  
    elif (i == 4) and (j == 4):
        while k < 1:
            if j == 0:
                q = 0
            else:
                q = -1
            while q < 1:
                if lst[i + k][j + q] == 'M':
                    c += 1 
                q += 1
            k += 1  
    elif (i != 4) and (j == 4):
        while k < 2:
            if j == 0:
                q = 0
            else:
                q = -1
            while q < 1:
                if lst[i + k][j + q] == 'M':
                    c += 1 
                q += 1
            k += 1  
    return c 

matrix = []
line = []
for i in range(5):
    for j in range(5):
        line.append(input("insert 0 or M: "))
    matrix.append(line)
    line = [] 

res_matrix = []
res_line = []
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 'M':
            res_line.append('M')
        elif matrix[i][j] == '0':
            res_line.append(count(matrix, i, j))
    res_matrix.append(res_line) 
    res_line = []

for i in range(5):
    for j in range(5):
        print(res_matrix[i][j], end = ' ')
    print(' ')

    
    
















