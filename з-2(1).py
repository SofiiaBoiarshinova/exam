num = list(map(int, input().split()))
def filter_even(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False
out = filter(filter_even, num)
print("Отфильтрованный список: ", list(out))