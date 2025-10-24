def even_or_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"
n = int(input("Enter the Value: "))
print(even_or_odd(n))