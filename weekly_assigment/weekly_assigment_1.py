#1st Question "The Birthday date"
s = input()
l = s.split('-')
l.reverse()
print(s)
print('/'.join(l))

#2nd Question "Even Odd Game"
n = int(input())
print(n)
if n%2 == 0:
    print("Even Winner")
else:
    print("Odd Winner")

#3rd Question "Vowel Replacer Bot"
s = input()
print(s)
v = ['a','e','i','o','u','A','E','I','O','U']
for i in s:
    if i in v:
        s = s.replace(i,'*')
print(s)

#4th Question "Shoping Cart Analyzer"

n = list(map(float, input().split()))
print(n)
print(sum(n))
print(max(n))


#5th Question " Secure Login System"

credentials = ("admin", "python123")
username = input()
password = input()
if credentials[0] == username and credentials[1] == password:
    print("Login Successful")
else:
    print("Access Denied")


#6th Question "Remove Duplicates"

s = set(input().split(','))
lis = list(s)

print(sorted(lis))

#7th Question " Student Marks Record"

n = int(input())
d = dict()
for i in range(n):
    student, marks = input().split()
    marks = int(marks)
    d[student] = marks
print(d)
t = max(d, key=d.get)
print(t)


#8th Question "Reverse My Words"
s = input()
words = s.split()
r_word = ''

for word in words:
    r_word = r_word + (word[::-1])
    r_word = r_word + " "
print(r_word)

#or
rs_word = [w[::-1] for w in words]
print(' '.join(rs_word))

#9th Question "Clean My List"
numbers = input().split()
clean_lis=[]
n = len(numbers)
for i in range(n):
    if int(numbers[i]) != 0:
        clean_lis.append(int(numbers[i]))
print(clean_lis)

#10th Question "The Frequecy Counter"

string = input()
d = {}
for i in string:
    if i not in d and i != ' ':
        d[i] = (string.count(i))
print(d)