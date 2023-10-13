import re

def validate_ph_num(ph_num):
    pattern =("\(\d{3}\)-\d{3}-\d{4}")
    if re.match(pattern, ph_num):
        return True
    else:
        return False

ph_num = input("Enter a phone number (in the format (555)-555-5555): ")

if validate_ph_num(ph_num):
    print(f"The phone number '{ph_num}' is valid.")
else:
    print(f"The phone number '{ph_num}' is not valid.")

#Output
'''
Enter a phone number (in the format (555)-555-5555): (333)-222-3334
The phone number '(333)-222-3334' is valid.
'''    