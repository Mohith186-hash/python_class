import my_programs as mp

function_map = {
    1: mp.Student_progress,
    2: mp.basic_calendar,
    3: mp.validate_email,
    4: mp.count_words,
    5: mp.largest_in_list,
    6: mp.miss_numb,
    7: mp.star_pyramid,
    8: mp.area_of_triangle,
    9: mp.count_occurance,
    10:mp.stopwatch
} 

while True:
    print('''
--------Progam Menu----
1. Student Progress Caluculation
2. Basic Calendar Display
3. Validate Email Address
4. Count Words in Sentence
5. Largest in List
6. Missing Number in Range
7. Star Pyraid
8. Calculate Area of Triangle
9. Count Occurrence of Each Element in List
10.Simple Stopwatch using time module
0. Exit
------------''')
    choice = int(input("Enter Your Choice: "))
    if choice  > 0 and choice <= len(function_map):
        function_map[choice]()
    elif choice == 0:
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")