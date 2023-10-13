import re

def extract_numbers(text):
    return re.findall(r'\d+', text)

user_input = input("Please enter a text containing numbers: ")

numbers = extract_numbers(user_input)
print(numbers)

#Output
'''
Please enter a text containing numbers: The price of the product is $20.50 and the quantity is 3. There are 10 items in stock.
['20', '50', '3', '10']
'''