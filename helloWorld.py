user_input = input("Begin conversation by typing hello...") 
if user_input.lower().strip() == "hello" or user_input.lower().strip() == "hi": 
    computer_reply = "Hello, world!"
    print(computer_reply)
else: 
    print("No entendo")
