def sum_of_n_numb(numbers):
    return sum(numbers)

n = int(input("How many number: "))
numbers = []

for i in range(n):
    num = int(input(f"Enter the number {i+1}: "))
    numbers.append(num)
print(sum_of_n_numb(numbers))