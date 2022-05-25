def fact(n):
    if (n <= 1):
        return 1
    else:
        return (n * fact(n-1))
n = int(input("Введите число:"))
print("Факториал числа равен:")
print(fact(n))
