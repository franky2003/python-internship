import re

def find_urls(text):
    url_pattern = r'https?://\S+|www\.\S+'
    return re.findall(url_pattern, text)

user_input = input("Please enter a text with URLs: ")

urls = find_urls(user_input)
print(urls)

#Output
'''
Please enter a text with URLs: Here are some example URLs: https://www.example.com http://example.com/page www.test.com
['https://www.example.com', 'http://example.com/page', 'www.test.com']
'''