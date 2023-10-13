import re

url = input("Enter the URL: ")
pattern = r'^https?://(www\.)?([\w.-]+)'

match = re.match(pattern, url)
if match:
    domain = match.group(2)
    print(f"Domain: {domain}")
else:
    print("No match")

#Output
'''
Enter the URL: https://bard.google.com
Domain: bard.google.com
'''