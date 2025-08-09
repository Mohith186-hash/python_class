'''
#
def sum(a,b):
    return a+b
print(f"The sum is : {2+5}")


#
def squares(a):
    return a*a
print(squares(12))

#
def circle(r):
    return 3.14*r*r
print(circle(4))

#
def greet(name):
    print(f'hello {name}')
name=input()
greet(name)

#
def conctof(deg):
    return deg*9/5+32
deg = float(input())
print(f'Temperature in fahrenheit: {conctof(deg)}')

#
def multiply(a,b,c):
    return a*b*c
a,b,c=list(map(int,input().split()))
print(multiply(a,b,c))

#
def interest(p,t,r):
    return p*t*r/100
p,t,r=tuple(map(int,input().split()))
print(interest(p,t,r))


#
def length(s):
    l=0
    for _ in s:
        l+=1
    return l
s=input()
print(length(s))'''

#

def removei(l,val):
    while val in l:
        l.remove(val)
    return l

val=int(input())
l=list(map(int,input().split()))

print(removei(l,val))

