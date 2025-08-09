def Welcome():
    return("Welcome to the Python Quiz Game!")

def first_Que():
    print("Question 1: What is the output of: print(type([]))?\n"
        "a) <class 'list'>\n" 
        "b) <class 'dict'>\n" 
        "c) <class 'set'>\n" 
        "d) <class 'tuple'>")
    op  = input("Your answer(a/b/c/d): ").lower()
    if op == "a":
        print("Correct")
        return True
    else:
        print("Wrong")
        return False
def second_Que():
    print("Question 2: What is the output of: \n"
          "x = [10, 20, 30]\n"
          "print(sum(x))\n"
          "a) 60\n"
          "b) 10\n"
          "c) 30\n"
          "d) Error")
    op = input("Your answer (a/b/c/d): ").lower()
    if op == "a":
        print("Correct")
        return True
    else:
        print("Wrong")
        return False
def third_Que():
    print("Question 3: Which operator is used to check equality? \n"
          "a) = \n"
           "b) == \n"
           "c) != \n"
           "d) equals")
    op = input("Your answer (a/b/c/d): ").lower()
    if op == "b":
        print("Correct")
        return True
    else:
        print("Wrong")
        return False
def fourth_Que():
    print("Question 4: Which is a valid variable name? \n"
          "a) 1name \n"
           "b) name-1 \n"
           "c) name_1 \n" 
           "d) @name")
    op = input("Your answer (a/b/c/d): ").lower()
    if op == "c":
        print("Correct")
        return True
    else:
        print("Wrong")
        return False
def fifth_Que():
    print("Question 5: Which data type is immutable? \n"
           "a) list \n"
            "b) dict \n"
            "c) set \n"
            "d) tuple ")
    op = input("Your answer (a/b/c/d): ").lower()
    if op == "d":
        print("Correct")
        return True
    else:
        print("Wrong")
        return False
def sixth_Que():
    print("Question 6: What is the correct way to take multiple inputs in one line? \n"
          "a) input().split(",")\n"
           "b) map(int, input().split(","))\n"
            "c) int(input()) * 2\n"
            "d) list(input()))")
    op = input("Your answer (a/b/c/d): ").lower()
    if op == "b":
        print("Correct")
        return True
    else:
        print("Wrong")
        return False
def seventh_Que():
    print("Question 7: Which data structure uses key-value pairs? \n"
         "a) List\n"
          "b) Set\n"
          "c) Tuple\n"
          "d) Dictionary")
    op = input("Your answer (a/b/c/d): ").lower()
    if op == "d":
        print("Correct")
        return True
    else:
        print("Wrong")
        return False
def eighth_Que():
    print("Question 8: What is the default return value of a function if no return statement is used? \n"
         "a) 0\n"
         "b)\"\"\n"
          "c) None\n"
          "d) Error")
    op = input("Your answer (a/b/c/d): ").lower()
    if op == "c":
        print("Correct")
        return True
    else:
        print("Wrong")
        return False
def nineth_Que():
    print("Question 9:What is the correct syntax to import the math module? \n"
          "a) include math\n"
           "b) use math\n"
           "c) import math\n"
           "d) require math")
    op = input("Your answer (a/b/c/d): ").lower()
    if op == "c":
        print("Correct")
        return True
    else:
        print("Wrong")
        return False
def tenth_Que():
    print("Question 10: Which loop is used when the number of iterations is unknown?\n"
          "a) while\n"
           "b) repeat\n"
           "c) for\n"
            "d) until")
    op = input("Your answer (a/b/c/d): ").lower()
    if op == "a":
        print("Correct")
        return True
    else:
        print("Wrong")
        return False
def eleventh_Que():
    print("Question 11: What is the output of:\n"
          'print("Python"[::-1])\n'
          "a) Python\n"
           "b) PYTHON\n"
            "c) nohtyP\n"
           "d) Error")
    op = input("Your answer (a/b/c/d): ").lower()
    if op == "c":
        print("Correct")
        return True
    else:
        print("Wrong")
        return False
def twelveth_Que():
    print("Question 12: What will range(3) generate? \n"
         "a) 1 2 3\n"
         "b) 0 1 2\n"
          "c) 0 1 2 3\n"
         "d) Error")
    op = input("Your answer (a/b/c/d): ").lower()
    if op == "b":
        print("Correct")
        return True
    else:
        print("Wrong")
        return False
def thirteenth_Que():
    print("Question 13: Which of the following creates a set? \n"
         "a) [1, 2, 3]\n"
          "b) (1, 2, 3)\n"
          "c) {1, 2, 3}\n"
          "d) {'a':1, 'b':2}")
    op = input("Your answer (a/b/c/d): ").lower()
    if op == "c":
        print("Correct")
        return True
    else:
        print("Wrong")
        return False
def fourteenth_Que():
    print("Question 14: What is the output of:\n"
          'print("hello".capitalize())\n'
        "a) hello\n"
        "b) Hello\n"
        "c) HELLO\n"
        "d) hELLO")
    op = input("Your answer (a/b/c/d): ").lower()
    if op == "b":
        print("Correct")
        return True
    else:
        print("Wrong")
        return False
def fifteenth_Que():
    print("Question 15: What is the correct way to check if two values are not equal?\n"
          "a) a <> b\n"
           "b) a != b\n"
           "c) a =! b\n"
           "d) not a = b")
    op = input("Your answer (a/b/c/d): ").lower()
    if op == "b":
        print("Correct")
        return True
    else:
        print("Wrong")
        return False
def sixteenth_Que():
    print("Question 16: Which loop is not available in Python?\n"
         "a) while\n"
          "b) for\n"
          "c) do-while\n"
          "d) nested")
    op = input("Your answer (a/b/c/d): ").lower()
    if op == "c":
        print("Correct")
        return True
    else:
        print("Wrong")
        return False
def seventeenth_Que():
    print("Question 17: What will print(len('Hello World')) output?\n"
          "a) 10\n"
          "b) 11\n"
          "c) 12\n"
          "d) Error")
    op = input("Your answer (a/b/c/d): ").lower()
    if op == "c":
        print("Correct")
        return True
    else:
        print("Wrong")
        return False
def eighteenth_Que():
    print("Question 18: Which one is NOT a Python data type?\n"
          "a) list\n"
          "b) dict\n"
          "c) set\n"
          "d) map")
    op = input("Your answer (a/b/c/d): ").lower()
    if op == "d":
        print("Correct")
        return True
    else:
        print("Wrong")
        return False
def nineteenth_Que():
    print("Question 19: What is used to define a block of code in Python?\n"
         "a) Curly braces {}\n"
          "b) Identation \n"
          "c) Parenthesis() \n"
          "d) Square brackets []")
    op = input("Your answer (a/b/c/d): ").lower()
    if op == "b":
        print("Correct")
        return True
    else:
        print("Wrong")
        return False
def twenty_Que():
    print("Question 20: What is the result of type('100')? \n"
         "a) int\n"
          "b) float\n"
         "c) str\n"
         "d) bool")
    op = input("Your answer (a/b/c/d): ").lower()
    if op == "c":
        print("Correct")
        return True
    else:
        print("Wrong")
        return False
    
def start():
    print("Can We Start the Quiz Type 'yes' ?")
    s = input().lower()
    score = 0
    if s == "yes":
        print("Starts Now")
        if first_Que(): score +=1
        if second_Que(): score +=1
        if third_Que(): score +=1
        if fourth_Que(): score +=1
        if fifth_Que(): score +=1
        if sixth_Que(): score+=1
        if seventh_Que(): score +=1
        if eighth_Que(): score +=1
        if nineth_Que(): score +=1
        if tenth_Que(): score +=1
        if eleventh_Que(): score +=1
        if twelveth_Que(): score +=1
        if thirteenth_Que(): score +=1
        if fourteenth_Que(): score +=1
        if fifteenth_Que(): score +=1
        if sixteenth_Que(): score +=1
        if seventeenth_Que(): score +=1
        if eighteenth_Que(): score +=1
        if nineteenth_Que(): score +=1
        if twenty_Que(): score +=1
        print(f"Marks You scored: {score}/20")
        if score == 20:
            return("Congratulations you scored 20/20")
        elif 15 >= score >=19 :
            return("Great Job keep trying")
        elif 11 >= score >= 14 :
            return("You Have to Improve")
        else:
            return("Need to Practice More")
    else:
        return("Exam Not Started")
    
print(Welcome())
print(start())