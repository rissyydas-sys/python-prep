# Function to find the factorial of a number.
def factorial(num):
    if num ==1 or num == 0:
        return 1
    return num*factorial(num-1)

# Function to check the number is strong number or not.
def IsStrongNumber(num):
    number = num
    n=0
    sum_num = 0
    while num >0:
        n = num%10
        sum_num += factorial(n)
        num = num//10
    if sum_num == number:
        print(f"{number} is a Strong Number")
    else:
        print(f"{number} is not a Strong Number")

user_input = int(input("Enter the number:"))
IsStrongNumber(user_input)