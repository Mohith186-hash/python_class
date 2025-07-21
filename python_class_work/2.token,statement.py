# Assignment statement
x=10
print(x) #Function call statement 
# o/p:-10

#addition
a=25
b=25
print("addition:",a+b) #addition: 50

#multiplication
a=10
b=8
print("multiplication:",a*b) #multiplication: 80

#subtraction
a=25
b=10
print("subtraction:",a-b) #subtraction: 15


#keywords
import keyword

print(keyword.kwlist)
print(len(keyword.kwlist)) #['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#35

#multiple assigment
a,b,c=10,200,30
print(a,b,c) #10 200 30

#reassigment
a=10
a=30
b=1000
b=-1000
print("reassign of a,b:",a,b) #reassign of a,b: 30 -1000

#swapping variables
mohith=100
tarak=200
mohith,tarak=tarak,mohith
print("swapping of mohith and tarak : ",mohith,tarak) #swapping of mohith and tarak :  200 100


#deleting variable
a=100
del a
print(a)) # name 'a' is not defined

