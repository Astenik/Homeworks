#task 1

def _range(start, end):
    res = [None] * end
    i = start
    while i < end:
        res[i] = i 
        i += 1 
    return res 

def _map(function, lst: list):
    res = []
    for num in lst:
       res.append(function(num))
    return res 

def _zip(arr1: list, arr2: list):
    _min = min(len(arr1), len(arr2))
    res = [None] * _min
    for ind in range(_min):
        res[ind] = (arr1[ind], arr2[ind])
    return res 

def _enumerate(lst: list, start = 0):
    res = []
    for i in range(start, len(lst) + start):
        res.append((i, lst[i - start]))
    return res 

def _filter(func, lst: list):
    res = []
    for num in lst:
        if(func(num)):
            res.append(num)
    return res 

#task 2
#tik-tak-toe

import random

def insert_2(matrix: list) -> list:
    i = random.randint(0, 2)
    j = random.randint(0, 2)
    while matrix[i][j] != 0:
        i = random.randint(0, 3)
        j = random.randint(0, 3)
    matrix[i][j] = 2 
    return matrix 

def is_equal_line(lst: list, line: int) ->bool:
    num = lst[line][0]
    if num != 0:
        for i in range(len(lst[line])):
            if lst[line][i] != num:
                return False
        return True
    return False
def is_equal_column(lst: list, column: int) -> bool:
    num = lst[0][column]
    if num != 0: 
        for i in range(len(matrix)):
            if lst[i][column] != num:
                return False
        return True
    return False

def is_win(matrix: list) -> bool:
    for i in range(len(matrix)):
        if is_equal_column(matrix, i) or is_equal_line(matrix, i):
            return True
    j = 1
    num = matrix[0][0]
    while j < len(matrix):
        if (matrix[j][j] != num) or (num == 0):
            return False 
        j += 1 
    return True 
    k = 0
    j = len(matrix[0]) - 1 
    num1 = matrix[0][j]
    while k < len(matrix):
        if (matrix[k][j] != num1) or (num1 == 0):
            return False 
        k += 1 
        j -= 1 
    return True  

  
  
#task 3

def merge(nums1: list, nums2: list) -> list:
    i = j = 0
    res = []
    while (i < len(nums1)) and (j < len(nums2)):
        if nums1[i] < nums2[j]:
            res.append(nums1[i]);
            i += 1;
        else:
            res.append(nums2[j]);
            j += 1;
    
    while i < len(nums1):
        res.append(nums1[i])
        i += 1 
    
    while j < len(nums2):
        res.append(nums2[j])
        j += 1
    
    return res 


#task 5 

def is_sorted(lst: list) -> bool:
    i = 0
    while lst[i] == lst[i + 1]:
        i += 1 
    if lst[i] > lst[i + 1]:
        for j in range(i, len(lst) - 1):
            if lst[j] < lst[j + 1]:
                return False 
    elif lst[i] < lst[i + 1]:
        for j in range(i, len(lst) - 1):
            if lst[j] > lst[j + 1]:
                return False 
    return True 

  
  
  
  
  
  
