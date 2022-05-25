word = str(input())
def is_palindrome(x):
 x = len(word)
 i = 0
 x = x - 1
 k = 0
 while x - i >= i:
      if word[x - i] == word[i]:
          i += 1
      else:
          k = 1
          break
 if k == 1:
    print("no")
 else:
    print("yes")
print(is_palindrome(word))