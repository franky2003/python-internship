import re

def check_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*\d).{8,}$'
    
    if re.match(pattern, password):
        return True
    else:
        return False
password = input("Enter a password: ")

if check_password(password):
    print("Password is strong")
else:
    print("Format Invalid")

#Output
'''
Enter a password: fet3eE@34$
Password is strong
'''