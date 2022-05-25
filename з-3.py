def square(list):
    res = [i**2 for i in map(int, list.split())]
    return res
 
lst = input()
print(*square(lst))