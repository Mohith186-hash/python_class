#1.arthematic
a=int(input("enter a value:"))#enter a value:10
b=int(input("enter b value:"))#enter b value:5
print("addtion of 2 values:",a+b)#addtion of 2 values: 15
print("subtraction of 2 values:",a-b)#subtraction of 2 values: 5
print("multiplication of 2 values:",a*b)#multiplication of 2 values: 50
print("divsion of 2 values:",a/b)#divsion of 2 values: 2.0
print("floor division of 2 values:",a//b)#floor division of 2 values: 2
print("modulus of 2 values:",a%b)#modulus of 2 values: 0
print("exponentiation of 2 values:",a**b)#exponentiation of 2 values: 100000

#2.comparsion
a=int(input("enter a value:"))#enter a value:25
b=int(input("enter b value:"))#enter b value:5
print("equal to of 2 values:",a==b)#equal to of 2 values: False
print("not equal to of 2 values:",a!=b)#not equal to of 2 values: True
print("greater than to of 2 values:",a>b)#greater than to of 2 values: True
print("less than to of 2 values:",a<b)#less than to of 2 values: False
print("greater than or equal to of 2 values:",a>=b)#greater than or equal to of 2 values: True
print("less than or equal to of 2 values:",a<=b)#less than or equal to of 2 values: False

#assigment 
n=int(input("enter n value:"))#enter n value:10
n+=2
print("add and assign of value:",n)#add and assign of value: 12
n-=5
print("sub and assign of value:",n)#sub and assign of value: 7
n*=6
print("mul and assign of value:",n)#mul and assign of value: 42
n/=3
print("div and assign of value:",n)#div and assign of value: 14.0
n//=4
print("floor div and assign of value:",n)#floor div and assign of value: 3.0
n%=2
print("modulus and assign of value:",n)#modulus and assign of value: 1.0
n**=4
print("exponentiate and assign of value:",n)#exponentiate and assign of value: 1.0

#Membership Operators
names=["sumanth","tarak","sanjay","charan","jyothi"]
print("in result:","rahul" in names)#in result: False
print("in result:","mohith" not in names)#in result: True


#Identity Operators
l=[1,2,3,4]
b=[1,2,3,4]
print("l is b:",l is b)#l is b: False
a=b
print("a is b:",a is b)#l is b: False
print("id(l)",id(l))#id(l) 2312273289408
print("id(b)",id(b))#id(b) 2312273247360
print("id(a)",id(a))#id(a) 2312273247360
print("a is not b:",a is not b)#a is not b: False
print("l is not b:",l is not b)#l is not b: True

#bitwise operator
'''1-001
2-010
3-011
4-100
5-101
6-110
7-111

3-011
5-101
-------
3&5=001=1'''
print("3&5:",3&5)#3&5: 1


'''4-100
5-101
--------
4|5=101=5'''
print("4|5:",4|5)#4|5: 5


'''5-101
6-110
---------
5^6=011=3'''
print("5^6:",5^6)#5^6: 3


'''1-001
--------
~1=110'''
print("~1:",~1)#~1: -2

'''6-110
--------
6 << 1 = 1100'''
print("6 << 1:",6 << 1)#6 << 1: 12
'''5-101
--------
5 >> 1 = 0101'''
print("5 >> 1:",5 >> 1)#5 >> 1: 2

#logical operator
x = 10
y = 8

print(x>5 and y<10) #true 
print(x>8 or y< 10) #true
print(not(x>5)) # false



      

