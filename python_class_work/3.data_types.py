#int class
a=123
print(type(a))#<class 'int'>

#float
a=float(input("enter a value:"))
print(type(a)) #<class 'float'>

#complex
a=3+2j
print(type(a)) #<class 'complex'>

#list
a=["mohith","tarak","venkatesh","raghu"]
print(type(a)) #<class 'list'>

#string
a="virat kohli"
print(type(a)) #<class 'str'>
print(a)#virat kohli

#tuple
a = (100,"mohith",30.0)
b = (20,"tarak",50.0)
print(a)#<class 'tuple'>
print(b)#<class 'tuple'>
print(a,b) #(100, 'mohith', 30.0) (20, 'tarak', 50.0)

#set
a={"mohith","tarak","venkatesh"}
print(type(a)) #<class 'set'>
print(a) #{'tarak', 'venkatesh', 'mohith'}

#dict
student_details={"name": "ram","class":9,"percentage":80.5}
print(type(student_details))
print(student_details)
#<class 'dict'>
{'name': 'ram', 'class': 9, 'percentage': 80.5}

#boolen
print(bool(0))
print(bool(1))
#False True

#none
x = None
print(type(x))
print(x)
#<class 'NoneType'>None




