def postive_or_negative(n):
    if n > 0:
        return "Positive"
    elif n == 0:
        return "Zero"
    else:
        return "Negative"
n = int(input("Enter the number: "))
print(postive_or_negative(n))