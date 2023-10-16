from bs4 import BeautifulSoup
import requests

url="https://www.amazon.in/Samsung-Galaxy-Ultra-Green-Storage/dp/B0BTYWFXKC/ref=sr_1_2?crid=2CA400WPO9BUA&keywords=samsung+s23+ultra+5g&nsdOptOutParam=true&qid=1697476609&sprefix=sa%2Caps%2C238&sr=8-2"
HEADERS=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0','Accept-Language':'en-US,en;q=0.5'})
webpage=requests.get(url,headers=HEADERS)
soup=BeautifulSoup(webpage.content,"html.parser")
headings = soup.find_all(class_="a-size-large a-spacing-none")
h_list=[]
for i in headings:
    h_list.append(i.getText())
price = soup.find(class_="a-price-whole")
p_list=[]
for i in price:
    p_list.append(i.getText())
print(f"The Price of {h_list[0]} is Rs {p_list[0]}")