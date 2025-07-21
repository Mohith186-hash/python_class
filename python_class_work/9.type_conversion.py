#type conversions

#int
a=356

print(float(a))#356.0

print(str(a))#356

print(bool(a))#true

b=0
print(bool(b))#False

print(list(a))#'int' object is not iterable

print(set(a))#'int' object is not iterable

print(tuple(a))#'int' object is not iterable

print(dict(a))#'int' object is not iterable


#float

tarak=155.5

print(int(tarak))#155

print(str(tarak))#155.5

print(bool(tarak))#True

mohith=0
print(bool(mohith))#False

print(list(tarak))#'float' object is not iterable

print(set(tarak))#'float' object is not iterable

print(tuple(tarak))#'float' object is not iterable

print(dict(tarak))#'float' object is not iterable



#str

a=int("10")
print(a)#10

a=int("10.99")
print(a)# invalid literal for int() with base 10: '10.99'


a=int("power")
print(a)#invalid literal for int() with base 10: 'power'


a=float('8.5')
print(a)#8.5

a=float('mohith')
print(a)#could not convert string to float: 'mohith'

a='mohith'
print(bool(a))#True

print(list(a))#['m', 'o', 'h', 'i', 't', 'h']

print(tuple(a))#('m', 'o', 'h', 'i', 't', 'h')

print(set(a))#{'i', 'o', 'm', 'h', 't'}

print(dict(a))# dictionary update sequence element #0 has length 1; 2 is required

#list

g=[3,4,5,6,7,8,9]

print(int(g))#int() argument must be a string, a bytes-like object or a real number, not 'list'

print(float(g))#float() argument must be a string or a real number, not 'list'

print(str(g))#'[3,4,5,6,7,8,9]'

print(bool(g))#True

print(tuple(g))#(3, 4, 5, 6, 7, 8, 9)

print(set(g))#{3, 4, 5, 6, 7, 8, 9}

print(dict(g))#cannot convert dictionary update sequence element #0 to a sequence

#tuple

h=(1,4,5,6,7,8)

print(int(h))#int() argument must be a string, a bytes-like object or a real number, not 'tuple'

print(float(h))#float() argument must be a string or a real number, not 'tuple'

print(str(h))#'(1, 4, 5, 6, 7, 8)'

print(bool(h))#True

print(list(h))#[1, 4, 5, 6, 7, 8]

print(set(h))#{1, 4, 5, 6, 7, 8}

print(dict(h))#cannot convert dictionary update sequence element #0 to a sequence

#set

k={2,3,5,6,7,9}

print(int(k))#int() argument must be a string, a bytes-like object or a real number, not 'set'

print(float(k))#float() argument must be a string or a real number, not 'set'

print(str(k))#'{2, 3, 5, 6, 7, 9}'

print(bool(k))#True

print(list(k))#[2, 3, 5, 6, 7, 9]

print(tuple(k))#(2, 3, 5, 6, 7, 9)

print(dict(k))#cannot convert dictionary update sequence element #0 to a sequence

#dict

m={1:4,3:4,7:6}

print(int(m))#int() argument must be a string, a bytes-like object or a real number, not 'dict'

print(float(m))#float() argument must be a string or a real number, not 'dict'

print(str(m))#'{1: 4, 3: 4, 7: 6}'

print(bool(m))#True

print(list(m))#[1, 3, 7]

print(tuple(m))#(1, 3, 7)

print(set(m))#{1, 3, 7}

#boolean

boolean= True

int(True)#1
int(False)#0

float(False)#0.0
float(True)#1.0

str(False)#'False'

list(False)#'bool' object is not iterable

tuple(False)#'bool' object is not iterable

set(False)#'bool' object is not iterable

dict(False)#'bool' object is not iterable

#Dictionary con

d = [('name', 'tarak'), ('batch', 'pfs30'), ('age','22'),('gender','male')]

print(dict(d))

#{'name': 'tarak', 'batch': 'pfs30', 'age': '22', 'gender': 'male'}






















