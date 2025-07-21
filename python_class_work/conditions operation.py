a=int(input("enter a: "))
b=int(input("enter b: "))

if a>b:
    print(f"{a} is greater than {b}")
elif a==b:
    print(f"{a} is equal than {b}")
else:
    print(f"{b} is greater than {a}")

'''enter a: 10
enter b: 10
10 is equal than 10'''

a=int(input("enter a : "))

if a%2==0 and a%3==0:
    print(f"2 and 3")
elif a%2==0:
    print(f" only 2")
elif a%3==0:
    print(f" only 3")
else:
    print(f"not div by 2 and 3")

'''enter a : 6
2 and 3'''
