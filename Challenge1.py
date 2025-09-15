
def encode_message(message):
    encoded_message = ""
    for index,item in enumerate(message,start=1):
        index = index%len(item)
        encoded_message += item[-index:] + item[:-index] + " "
    return encoded_message

def decode_message(message):
    decoded_message = ""
    for index,item in enumerate(message,start=1):
        index = index%len(item)
        decoded_message += item[index:] + item[:index] + " "
    return decoded_message

while True:
    try:
        choice = int(input("1. Encode 2. Decode 3.Exit:"))
        if choice == 1:
            user_input = list(input("Enter the message:").split())
            print(encode_message(user_input))
        elif choice == 2:
            print(decode_message(list(encode_message(user_input).split())))
        elif choice == 3:
            break
        else:
            print("Invalid choice")
    except:
        print("Invalid value entered, please enter correctly")
    else:
        continue



