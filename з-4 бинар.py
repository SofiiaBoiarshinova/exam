def bin_search(list, n):
    start = 0
    end = len(list)
    while start <= end:
        mid = (start+end)//2
        if list[mid] == n:
            return mid
        if n < list[mid]:
            end = mid-1
        else:
            start = mid+1
    return -1
 
print(bin_search([2, 5, 7, 9, 11, 17, 222], 11))
print(bin_search([2, 5, 7, 9, 11, 17, 222], 12))
