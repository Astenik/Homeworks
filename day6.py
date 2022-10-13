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

def  is_win(board: list):
    for i in range(3):
        c1 = 0
        c2 = 0
        for j in range(3):
            if board[i][j] == 'X':
                c1 += 1 
            elif board[i][j] == 'O':
                c2 += 1 
        if (c1 == 3) or (c2 == 3):
            return True
    i = 0
    for k in range(3):
        if board[i][k] == board[i + 1][k] == board[i + 2][k]:
            return True 
    if board[i][i] == board[i + 1][i + 1] == board[i + 2][i + 2]:
        return True 
    if board[i][i + 2] == board[i + 1][i + 1] == board[i + 2][i]:
        return True 
    return False
  
  
  
  
  
  
  
  
  
  
