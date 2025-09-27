class Stack():
    # Stack implementation. 
    def __init__(self):
        self.stack = []

    def push(self,value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None 
    
    def is_empty(self):
        return len(self.stack) == 0
    
# Function to check the string is balanced or not.
def is_balanced(str):
    stack = Stack()
    bracket_map = {')':'(',']':'[','}':'{'}

    for char in str:
        if char in bracket_map.values():
            stack.push(char)
        elif char in bracket_map:
            top_item = stack.pop()
            if top_item != bracket_map[char]:
                return False 
    return stack.is_empty()

print("Enter 'Exit' to exit the Program")
while True:
    user_input = input("Enter the string:")
    if user_input == "Exit":
        print("Program Exits!!")
        break
    elif is_balanced(user_input):
        print("Balanced")
    else:
        print("Not Balanced")