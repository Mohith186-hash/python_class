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
    # Count total number of messages
    if user == 1:
        print(f"The total number of messages: {n}")
    # Identify unique users in the chat
    elif user == 2:
        print(f"Unique users: {list(data.keys())}")
    # Count total words in the chat
    elif user == 3:
        total_words = 0
        for name in data.keys():
            for idx,msg in data[name]:
                total_words += len(msg.split())
        print(f"The total words in the chat: {total_words}")
    # Calculate average words per message
    elif user == 4:
        total_number_of_words = 0
        for name in data:
            for idx, msg in data[name]:
                total_words += len(msg.split())
        print(f"The average words in chat: {total_number_of_words/n}")
    # Find the longest message sent
    elif user == 5:
        long_message = ''
        for name in data:
            for idx, msg in data[name]:
                if len(long_message) < len(msg):
                    long_message = msg
                    user = name
        print(f"The Maximum Length of Message: {long_message}")
    # Find the most active user
    elif user == 6:
        max_count = 0
        most_active_user = ""
        for name in data:
            if max_count < len(data[name]):
                max_count = len(data[name])
                most_active_user = name
        print(f"Most active user: {most_active_user} ({max_count} messages)")
    # Get message count for a specific user
    elif user == 7:
        user_name = input("Enter user name: ")
        if user_name in data:
            message_count = len(data[user_name])
            print(f"{user_name} has sent {message_count} messages.")
    # For most frequently used word by specific user
    elif user == 8:
        user_in = input()
        w ={}
        if user_in in data:
            for ind, msg in data[user_in]:
                for words in msg.split():
                    if words in w:
                        w[words]= w[words]+1
                    else:
                        w[words] = 1
            print(f"Most frequent word used by {user_in}: {max(w, key=w.get)}")
        else:
            print(f"{user_in} not in present in chat")
    # Retrieve the first and last message sent by a user
    elif user == 9:
        user_in = input()
        if user_in in data:
            print(f'First message by {user_in}: "{user_in}: {data[user_in][0][1]}"')
            print(f'Last message by {user_in}: "{user_in}: {data[user_in][-1][1]}"')
        else:
            print(f"{user_in} not in present in chat")
    # Check if a user is present in the chat
    elif user == 10:
        user_name = ''
        if user_name in data:
            print(f"User {user_name} found in the chat")
        else:
            print(f"User {user_name} not found in chat")
    # Find commonly repeated words
    elif user == 11:
        d= {}
        repeated_words = []
        for name in data:
            for ind, msg in data[name]:
                for words in msg.split():
                    if words in d:
                        d[words] = d[words]+1
                    else:
                        d[words] = 1
            for word in d:
                if d[word] >= 2:
                    repeated_words.append(word)
        print(f'Common repeated words: {repeated_words}')
    # Identify the user with the longest average message length
    elif user == 12:
        max_avg = 0
        user = ''
        for name in data:
            total_words = 0
            total_msgs = len(data[name])
            for idx, msg in data[name]:
                total_words += len(msg.split())
                avg = total_words / total_msgs
            if avg > max_avg:
                max_avg = avg
                user = name
        print(f"User with longest average message: {user} (avg {max_avg} words)")
    # Count how many messages mention a specific user
    elif user == 13:
        u_in = input()
        count = 0
        if u_in in data:
            for name in data:
                for idx, msg in data[name]:
                    for word in msg.split():
                        if u_in == word:
                            count += 1
            print(f"Messages mentioning {u_in}: {count}")
        else:
            print(f"User '{u_in}' not found in the chat.")
    # Remove duplicate messages
    elif user == 14:
        mess = []
        count = 0
        for name in data:
            for idx, msg in data[name]:
                if msg not in mess:
                    mess.append(msg)
                    count += 1
        print(f"Unique messages count: {count}")
    # Sort messages alphabetically
    elif user == 15:
        sort_msg = []
        for name in data:
            for idx, msg in data[name]:
                sort_msg.append(msg)
        print(f"All messages sorted A-Z: {sorted(sort_msg)}")
    # Extract all questions asked in the chat
    elif user == 16:
        lis_qus =[]
        for name in data:
            for idx, msg in data[name]:
                if '?' in msg:
                    lis_qus.append(msg)
        print(f"List of messages ending with or containing ?: {lis_qus}")
    # Calculate the reply ratio between two users
    elif user == 17:
        u_in = input().split('and')
        u1=0
        u2=0
        if u_in in data:
            for name in data[u_in]:
                u1 = len(data[u_in[0]])
                u2 = len(data[u_in[1]])
        print(f"Reply ratio from {u_in[0]} to {u_in[1]}: {u1//u2}")
    # Check for deleted messages
    elif user == 18:
        cou = 0
        for name in data:
            for idx, msg in data[name]:
                if msg == "This message was deleted":
                    cou += 1
        print(f"Deleted messages found: {cou}")
    # Exit
    elif user == 19:
        break