'''1.print number form 1 to N
def print_numbers(n): 
    if n == 0:
        return
    print_numbers(n - 1)
    print(n, end=" ")
print_numbers(5)
print_numbers(3)

2. print numbbers from N to 1
def numbers(n):
    if n==0:
        return
    print(n, end=" ")
    numbers(n-1)
numbers(5)

3.sum of n natural number
def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)
print(sum(4))
4.factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(5))

5.reverse
def reverse(s):
    if len(s)==0:
        return ""
    return reverse(s[1:]) + s[0]
print(reverse("hello"))

7.sum of digits
def sum(s):
    if len(s) == 0:
        return 0
    return int(s[0]) + sum(s[1:])
s=input("")
print(sum(s))'''

def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)
print(sum_digits(123))


