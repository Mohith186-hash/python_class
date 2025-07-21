#dictionary

#adding and updating
student={
    "name":"tarak",
    "age":21,
}
print(student)#{'name': 'tarak', 'age': 21}
student["course"]="python full stack"
student["city"]="vijayawada"
print(student)#{'name': 'tarak', 'age': 21, 'course': 'python full stack', 'city': 'vijayawada'}

#removing
age=student.pop("age")
print(age)#21
print(student)#{'name': 'tarak', 'course': 'python full stack', 'city': 'vijayawada'}

del student["course"]
print(student)#{'name': 'tarak', 'city': 'vijayawada'}

student={
    "name":"tarak",
    "age":21,
    "course":"python full stack",
    "city":"vijayawada",
}
print(student)#{'name': 'tarak', 'age': 21, 'course': 'python full stack', 'city': 'vijayawada'}
print(student.popitem())#('city', 'vijayawada')
print(student.clear())#None

#Dictionary methods
student={
    "name":"tarak",
    "age":21,
    "course":"python full stack",
    "city":"vijayawada",
}
print(student.get("course"))#python full stack
print(student.setdefault("gender","male"))#male
print(student)#{'name': 'tarak', 'age': 21, 'course': 'python full stack', 'city': 'vijayawada', 'gender': 'male'}

#dictionary removing data

student.pop("age")
print(student)#{'name': 'tarak', 'course': 'python full stack', 'city': 'vijayawada', 'gender': 'male'}

student.popitem()
print(student)#{'name': 'tarak', 'course': 'python full stack', 'city': 'vijayawada'}

del student["name"]
print(student)#{'course': 'python full stack', 'city': 'vijayawada'}

student.clear()
print(student)#{}

#built in functions

student={
    "name":"tarak",
    "age":21,
    "course":"python full stack",
    "city":"vijayawada",
}
print(len(student)) #4

print(max(student))#name

print(min(student))#age

print(sorted(student))#['age', 'city', 'course', 'name']


#nested dictionaries

students={
    "tarak":{"age":21,"course":"pfs","city":"vijayawada"},
    "venkatesh":{"age":22,"course":"jfs","city":"vijawada"}
}

print(students["tarak"]["city"])#vijayawada


#dictionary comprehension

n={x: x*x*x for x in range(1,8)}
print(n)#{1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343}

#Real-Time problem using dictionaries

n="hello world hello mohith"
word_count={}

for word in n.split():
    word_count[word] = word_count.get(word,0) +1
print(word_count)#{'hello': 2, 'world': 1, 'mohith': 1}






