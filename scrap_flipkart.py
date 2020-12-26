import pandas as pd

import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.flipkart.com/search?q=apple+iphone+11&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_1_10_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_1_10_na_na_ps&as-pos=1&as-type=HISTORY&suggestionId=apple+iphone+11&requestId=1fa6f894-d110-4357-a75e-db21ac7c84d0 '
website = requests.get(url)

soup = bs(website.content, 'html.parser')
pritty_html = soup.prettify()

phones = soup.find_all(class_='_4rR01T')
ratings = soup.find_all(class_='_3LWZlK')
price = soup.find_all(class_='_30jeq3 _1_WHN1')

custom_list = []
custom_ratings = []
custom_price = []

for i in range(len(phones)):
    custom_list.append(phones[i].get_text())
    custom_ratings.append(ratings[i].get_text())
    custom_price.append(price[i].get_text())

df = pd.DataFrame({'Product Name': custom_list, 'Price': custom_price, 'Rating': custom_ratings})
df.to_csv('Apple.csv', index=False, encoding='utf-8')

url = 'https://www.flipkart.com/search?q=realme&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_3_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_3_na_na_ps&as-pos=2&as-type=RECENT&suggestionId=realme%7CMobiles&requestId=d034370a-5a90-4dfd-a0ce-0eb6215a71a3&as-backfill=on'
website = requests.get(url)

soup = bs(website.content, 'html.parser')
pritty_html = soup.prettify()

phones = soup.find_all(class_='_4rR01T')
ratings = soup.find_all(class_='_3LWZlK')
price = soup.find_all(class_='_30jeq3 _1_WHN1')

custom_list = []
custom_ratings = []
custom_price = []

for i in range(len(phones)):
    custom_list.append(phones[i].get_text())
    custom_ratings.append(ratings[i].get_text())
    custom_price.append(price[i].get_text())

df = pd.DataFrame({'Product Name': custom_list, 'Price': custom_price, 'Rating': custom_ratings})
df.to_csv('Realme.csv', index=False, encoding='utf-8')

url = 'https://www.flipkart.com/search?q=mi&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
website = requests.get(url)

soup = bs(website.content, 'html.parser')
pritty_html = soup.prettify()

phones = soup.find_all(class_='_4rR01T')
ratings = soup.find_all(class_='_3LWZlK')
price = soup.find_all(class_='_30jeq3 _1_WHN1')

custom_list = []
custom_ratings = []
custom_price = []

for i in range(len(phones)):
    custom_list.append(phones[i].get_text())
    custom_ratings.append(ratings[i].get_text())
    custom_price.append(price[i].get_text())

df = pd.DataFrame({'Product Name': custom_list, 'Price': custom_price, 'Rating': custom_ratings})
df.to_csv('Mi.csv', index=False, encoding='utf-8')

url = 'https://www.flipkart.com/search?q=samsung+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=samsung+mobiles%7CMobiles&requestId=d794d684-730c-4f83-85c6-dee727ab2508&as-backfill=on'
website = requests.get(url)

soup = bs(website.content, 'html.parser')
pritty_html = soup.prettify()

phones = soup.find_all(class_='_4rR01T')
ratings = soup.find_all(class_='_3LWZlK')
price = soup.find_all(class_='_30jeq3 _1_WHN1')

custom_list = []
custom_ratings = []
custom_price = []

for i in range(len(phones)):
    custom_list.append(phones[i].get_text())
    custom_ratings.append(ratings[i].get_text())
    custom_price.append(price[i].get_text())

df = pd.DataFrame({'Product Name': custom_list, 'Price': custom_price, 'Rating': custom_ratings})
df.to_csv('Samsung.csv', index=False, encoding='utf-8')

url = 'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.serviceability%5B%5D%3Dfalse&p%5B%5D=facets.brand%255B%255D%3DVivo&otracker=nmenu_sub_Electronics_0_Vivo'
website = requests.get(url)

soup = bs(website.content, 'html.parser')
pritty_html = soup.prettify()

phones = soup.find_all(class_='_4rR01T')
ratings = soup.find_all(class_='_3LWZlK')
price = soup.find_all(class_='_30jeq3 _1_WHN1')

custom_list = []
custom_ratings = []
custom_price = []

for i in range(len(phones)):
    custom_list.append(phones[i].get_text())
    custom_ratings.append(ratings[i].get_text())
    custom_price.append(price[i].get_text())

df = pd.DataFrame({'Product Name': custom_list, 'Price': custom_price, 'Rating': custom_ratings})
df.to_csv('Vivo.csv', index=False, encoding='utf-8')

url = 'https://www.flipkart.com/search?p[]=facets.brand%255B%255D%3DHonor&sid=tyy%2F4io&otracker=CLP_filters&otracker=nmenu_sub_Electronics_0_Honor'
website = requests.get(url)

soup = bs(website.content, 'html.parser')
pritty_html = soup.prettify()

phones = soup.find_all(class_='_4rR01T')
ratings = soup.find_all(class_='_3LWZlK')
price = soup.find_all(class_='_30jeq3 _1_WHN1')

custom_list = []
custom_ratings = []
custom_price = []

for i in range(len(phones)):
    custom_list.append(phones[i].get_text())
    custom_ratings.append(ratings[i].get_text())
    custom_price.append(price[i].get_text())

df = pd.DataFrame({'Product Name': custom_list, 'Price': custom_price, 'Rating': custom_ratings})
df.to_csv('Honor.csv', index=False, encoding='utf-8')

url = 'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DAsus&otracker=nmenu_sub_Electronics_0_Asus'
website = requests.get(url)

soup = bs(website.content, 'html.parser')
pritty_html = soup.prettify()

phones = soup.find_all(class_='_4rR01T')
ratings = soup.find_all(class_='_3LWZlK')
price = soup.find_all(class_='_30jeq3 _1_WHN1')

custom_list = []
custom_ratings = []
custom_price = []

for i in range(len(phones)):
    custom_list.append(phones[i].get_text())
    custom_ratings.append(ratings[i].get_text())
    custom_price.append(price[i].get_text())

df = pd.DataFrame({'Product Name': custom_list, 'Price': custom_price, 'Rating': custom_ratings})
df.to_csv('Honor.csv', index=False, encoding='utf-8')
