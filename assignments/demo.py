n = int(input("Enter the number of messages:"))
data = {}
for i in range(n):
    name, message = input().split(':')
    if name in data:
        data[name].append((i,message))
    else:
        data[name] = [(i,message)]
print(data)

while True:
    print("1. Count total number of messages")
    print("2. Identify unique users in the chat")
    print("3. Count total words in the chat")
    print("4. Calculate average words per message")
    print("5. Find the longest message sent")
    print("6. Find the most active user")
    print("7. Get message count for a specific user")
    print("8. Find the most frequently used word by a specific user")
    print("9. Retrieve the first and last message sent by a user")
    print("10. Check if a user is present in the chat")
    print("11. Find commonly repeated words")
    print("12. Identify the user with the longest average message length")
    print("13. Count how many messages mention a specific user")
    print("14. Remove duplicate messages")
    print("15. Sort messages alphabetically")
    print("16. Extract all questions asked in the chat")
    print("17. Calculate the reply ratio between two users")
    print("18. Check for deleted messages")
    print("19.Exit")
    user = int(input("Enter Your Choice: "))
    if user == 9:
        user_in = ''
        if user_in in data:
            print(f"The First message of {user_in}: {data[user_in][0][1]}")
            print(f"The Last message of {user_in}: {data[user_in][-1][1]}")
        
