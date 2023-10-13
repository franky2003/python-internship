import re

def remove(input_string):
    pattern = r'<[^>]+>'
    text = re.sub(pattern, '', input_string)
    return text

html_string = input("Enter a string with HTML tags: ")
text = remove(html_string)
print(text)

#Output
'''
Enter a string with HTML tags: <p>This is new<p>
This is new
'''