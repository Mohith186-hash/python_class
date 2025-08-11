def Student_progress():
    print('''"Student Report Card Generator"
      
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

sub1 = float(input("Enter marks in Math: "))
sub2 = float(input("Enter marks in Science: "))
sub3 = float(input("Enter marks in English: "))

total = sub1 + sub2 + sub3
percentage = total / 3

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== STUDENT REPORT CARD =====")
print(f"Name       : {name}")
print(f"Roll No    : {roll_no}")
print(f"Math       : {sub1}")
print(f"Science    : {sub2}")
print(f"English    : {sub3}")
print(f"Total      : {total}")
print(f"Percentage : {percentage:.2f}%")
print(f"Grade      : {grade}")
print("================================"))
    
print("Test cases: ")
          
print(Input: Enter student name: Mohith
Enter roll number: 22
Enter marks in Math: 56
Enter marks in Science: 56
Enter marks in English: 25

===== STUDENT REPORT CARD =====
Name       : Mohith
Roll No    : 22
Math       : 56.0
Science    : 56.0
English    : 25.0
Total      : 137.0
Percentage : 45.67%
Grade      : F ) 
          
print(Test case2 :
Enter student name: tarak
Enter roll number: 85
Enter marks in Math: 90
Enter marks in Science: 82
Enter marks in English: 99

===== STUDENT REPORT CARD =====
Name       : tarak
Roll No    : 85
Math       : 90.0
Science    : 82.0
English    : 99.0
Total      : 271.0
Percentage : 90.33%
Grade      : A+
          
print"Explanation:* This program takes a student’s details and marks, 
        * Calculates the total , Percentage, and grade, 
        * Then displays a formatted report card.''')
    
def basic_calendar():
    print('''"Basic Calendar Display"
          
import calendar:
          
year = int(input("Enter Year: ")) 
month = int(input("Enter the MOnth (1-12):))
          
print("\n",calendar.month(year, month)
    
print("Test Case: ")
print("Test Case 1: )          

print("Enter year: 2024
Enter month (1-12): 11

    November 2024
Mo Tu We Th Fr Sa Su
            1  2  3
4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30     
          
print("Test Case: 2")
Enter year: 2023
Enter month (1-12): 5

       May 2023
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
          
print("Explanation: This program uses Python’s built-in calendar module to display a month or full year’s calendar based on user input."''')

def validate_email():
    print(''' "Program For Email Address"

email = input("Enter your email address: ")

if "@" in email and "." in email and email.index("@") > 0 and email.index("@") < email.rindex("."):
    print("✅ Valid Email Address")
else:
    print("❌ Invalid Email Address")
          
print("Test Cases: ")
print("Test Case1: " )

print("Enter your email address: mohith@gmail.com
✅ Valid Email Address")

print("Test Case 2: ")

print("Enter your email address: mohith@
❌ Invalid Email Address")
Explanation: This program checks if the entered email contains “@” and “.” in the correct order to determine if it’s valid.''')

def count_words():
    print(''' "Program for count Words"

sentence = input("Enter a sentence: ")

word_count = len(sentence.split())

print(f"Number of words: {word_count}")

print("Test Case: ")
print("Test Case 1: " )
print("Enter a sentence: Python is easy to learn"
"Number of words: 5")

print("Test Case2 : ")
print("Enter a sentence: my name is Mohith"
"Number of words: 4")
Explanation: This program splits the input sentence into words and counts them using len().''')

def largest_in_list():
    print(''' "Program for Largest word in list"
          
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

largest = max(numbers)

print(f"The largest number is: {largest}")
          
print("Test Case: ")
print("Test Case 1: " )
print("Enter numbers separated by space: 5 12 7 3 19 8
The largest number is: 19")

print("Test Case2 : ")
print("Enter numbers separated by space: 55 24 45 72 36 32 26 
The largest number is: 72''')
    
def miss_numb():
    print(''' "Find Missing Number in Range"

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
n = len(numbers) + 1
total_sum = n * (n + 1) // 2
missing = total_sum - sum(numbers)

print(f"The missing number is: {missing}")
          
print("Test Cases: ")
print("Test Case 1: ")
print("Enter numbers separated by space: 1 2 4 5
The missing number is: 3 ")
          
print("Test Case2: ")
print("Enter numbers separated by space: 11 13 14 15
The missing number is: 12 ")''')
    
def star_pyramid():
    print('''Star Pyramid formation
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print("  " * (rows - i), end="")  
    
    for j in range(i):
        print("*", end="  ")
    
    print()
print(Test Cases:)
print(Test Case1: )
Enter number of rows: 5
        *  
      *  *  
    *  *  *  
  *  *  *  *  
*  *  *  *  *  
print(Test Case2:
Enter number of rows: 6
          *  
        *  *
      *  *  *
    *  *  *  *
  *  *  *  *  *
*  *  *  *  *  *''')
    
def area_of_triangle():

    print('''Area of Triangle
          
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = 0.5 * base * height

print(f"The area of the triangle is: {area}")

print("Test Cases: " )
print("Test Case1: ")
Enter the base of the triangle: 10
Enter the height of the triangle: 5
The area of the triangle is: 25.0

print("Test Case2: ")
Enter the base of the triangle: 15
Enter the height of the triangle: 10
The area of the triangle is: 75.0''')

def count_occurance():
    print('''Count Occurrence of Each Element in List
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
occurrences = {}
for num in numbers:
    occurrences[num] = occurrences.get(num, 0) + 1


print("Element occurrences:")
for key, value in occurrences.items():
    print(f"{key} : {value}")
print(Test Cases:)
print(Test Case1: )
Enter numbers separated by space: 2 3 2 5 3 2
Element occurrences:
2 : 3
3 : 2
5 : 1
print(Test Case2 :
Enter numbers separated by space: 2 3 3 5 5 6 4 6 1 2 2
Element occurrences:
2 : 3
3 : 2
5 : 2
6 : 2
4 : 1
1 : 1)
print("Explanation : This program counts how many times each element appears in a list using a dictionary.")''')

def stopwatch():
    print('''Simple stopwatch using time module

import time
print("Press Enter to start the stopwatch")
input()
start_time = time.time()

print("Stopwatch started... Press Enter to stop")
input()
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")
print("Test Cases :
print("Test case1: ")
Press Enter to start the stopwatch

Stopwatch started... Press Enter to stop

Elapsed time: 4.53 seconds
          
print(Test case2: )
Press Enter to start the stopwatch

Stopwatch started... Press Enter to stop

Elapsed time: 0.99 seconds
Explanation: This program measures the time between two Enter key presses using the `time` module.''')