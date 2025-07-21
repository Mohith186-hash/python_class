#list methods

numbers=[10,20,30,45,55]
numbers.append(54)
print(numbers) #[10, 20, 30, 45, 55, 54]
numbers.extend([25,35])
print(numbers)#[10, 20, 30, 45, 55, 54, 25, 35]
numbers.insert(1,35)
print(numbers)#[10, 35, 20, 30, 45, 55, 54, 25, 35]
numbers.remove(30)
print(numbers)#[10, 35, 20, 45, 55, 54, 25, 35]
numbers.pop(2)
print(numbers)#[10, 35, 45, 55, 54, 25, 35]
numbers.clear()
print(numbers)#[]
numbers=[10,20,30,45,55]
print(numbers.index(20))#1
numbers=[10,20,33,33,45,33,55]
print(numbers.count(33))#3
numbers=[10,20,30,45,55,6,88,90,33,45]
numbers.sort()
print(numbers)#[6, 10, 20, 30, 33, 45, 45, 55, 88, 90]
numbers.sort(reverse=True)
print(numbers)#[90, 88, 55, 45, 45, 33, 30, 20, 10, 6]
numbers.reverse()
print(numbers)#[6, 10, 20, 30, 33, 45, 45, 55, 88, 90]
numbers=[10,20,30,45,55,6,88,90,33,45]
k=numbers.copy()
print(k)#[10, 20, 30, 45, 55, 6, 88, 90, 33, 45]
print(max(numbers))#90
print(min(numbers))#6
print(sorted(numbers))#[6, 10, 20, 30, 33, 45, 45, 55, 88, 90]
print(sum(numbers))#422
print(len(numbers))#10
print(any(numbers))#True
print(all(numbers))#True



