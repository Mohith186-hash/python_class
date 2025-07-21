#defining a string
m="mohith"
t='tarak'
v='''venkatesh'''
print(m)#mohith

print(t)#tarak

print(v)#venkatesh

'''string methods '''
#1.case conversion method

print("hello".upper())#HELLO
print("HELLO".lower())#hello
print("python is a language".capitalize())#Python is a language
print("python is a language".title())#Python Is A Language
print("ß".casefold())#ss

#2.alignment &formating

print("python".center(10,'*'))#**python**
print("pytn".ljust(10,'*'))#pytn******
print("pyt".rjust(5,'*'))#**pyt
print("42".zfill(6))#000042
print("name:{},class:{},course:{}".format("tarak",9,"python full stack"))#name:tarak,class:9,course:python full stack
print("{name} is {class} is {course}".format_map({'name':'tarak','class':9,'course':"python full stack"}))#tarak is 9 is python full stack

#3.search and find methods

print("Hello".find("l"))#2
print("Hello".rfind("l"))#3
print("hello World".index("d"))#10
print("hello world".rindex("w"))#6
print("banana".count("a"))#3

#4.string Testing methods(boolean results

print("python is a coding language".startswith("py"))#true
print("tarak is  a good friend".endswith("nd"))#true
print("Hello world".isalpha())#false
print("123456789".isdigit())#true
print("abc12345".isalnum())#true
print("hello world".islower())#true
print("HELLO WORLD".isupper())#true
print(" ".isspace())#true
print("Hello World".istitle())#true
print("123".isdecimal())#true
print("⅕".isnumeric())#true
print("variable123".isidentifier())#true

#5.Replace& modify methods
print("python is a coding language".replace("p","h"))#hython is a coding language
print(("python is a coding").translate(str.maketrans("p","c")))#cython is a coding
print(str.maketrans("ae", "12"))#{97: 49, 101: 50}

#6.splitting & joining

print("python,is,a,coding,language".split())#['python,is,a,coding,language']
print("python is a coding language".rsplit(",",2))#['python', ' is a coding language']
print("python\nis\na\ncoding\nlanguage".splitlines())#['python', 'is', 'a', 'coding', 'language']
print(" ".join(["python","language"]))#python language
print("python-language".partition("-"))#('python', '-', 'language')
print("python-language".rpartition("-"))#('python', '-', 'language')

#7.whitespace& trimming methods
print(" hello world ".strip())#hello world
print("-------hello".lstrip("-"))#hello
print("hello------".rstrip("-"))#hello

#8.encoding and decoding
print("hello".encode("utf-8"))#b'hello'
print(b'hello'.decode("utf-8"))#hello


