import re

def validate(date):
    pattern = r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$'
    match = re.match(pattern, date)
    return bool(match)


date_input = input("Enter a date (MM/DD/YYYY format): ")

if validate(date_input):
    print(f"{date_input} is a valid date.")
else:
    print(f"{date_input} is not a valid date.")

#Output
'''
Enter a date (MM/DD/YYYY format): 01/11/2023
01/11/2023 is a valid date.
'''