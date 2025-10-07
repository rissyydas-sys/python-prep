def is_password_strong(password):
    upper = False
    lower = False
    digit = False
    special_char = False
    if len(password) >=8 :
        for char in password:
            if char.isupper():
                upper = True
            if char.islower():
                lower = True
            if char.isdigit():
                digit = True
            if char.isalnum():
                special_char = True

    if upper and lower and digit and special_char:
        print("Strong password")
    else:
        print("Weak password")

password = input("Enter password:")
is_password_strong(password)