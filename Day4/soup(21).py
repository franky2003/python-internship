from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
contents = response.text
soup = BeautifulSoup(contents, "html.parser")
headings = soup.find_all(class_="title")
h_list=[]
s_list=[]
l_list=[]
for i in headings:
    h_list.append(i.getText())
    if i.a:
        heading_link = i.a['href']
        l_list.append(heading_link)
    else:
        l_list.append(None)   
print(h_list)
print(l_list)
scores = soup.find_all(class_="score")
for j in scores:
    s_list.append(j.getText())
print(s_list)    