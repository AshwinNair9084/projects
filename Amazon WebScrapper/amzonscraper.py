from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd

url= "https://www.amazon.in/s?k=tshirt&crid=2WI5BNKO4I0VB&sprefix=tshirt%2Caps%2C263&ref=nb_sb_noss_2"

session = HTMLSession()
r = session.get(url)
r.html.render(sleep=5)

soup = BeautifulSoup(r.html.raw_html, "html.parser")

# Extracting all the brand titles
brand_title  = soup.find_all('span', class_="a-size-base-plus a-color-base")
brand_type = []
for product in brand_title: brand_type.append(product.text)

# Extracting all the product titles
product_title = soup.find_all('span', class_="a-size-base-plus a-color-base a-text-normal")
product_type = []
for product in product_title: product_type.append(product.text)

# Extracting all the price titles
price_title = soup.find_all('span', class_="a-price-whole")
price_type = []
for product in price_title: price_type.append("Rs. " + product.text)

# Extracting all the Reviews titles
review_title = soup.find_all('span', class_="a-icon-alt")
review_type = []
for product in review_title: review_type.append(product.text)


# Making the csv file
print (len(brand_type))
print (len(product_type))
print (len(price_type[:len(brand_type)]))
print (len(review_type[:len(brand_type)]))
 
# dictionary of lists
dict = {'Brand Name': brand_type, 'Product Name': product_type, 'Price': price_type[:len(brand_type)], 'Stars': review_type[:len(brand_type)]}
     
df = pd.DataFrame(dict)
 
print(df.head())
df.to_csv('WebAmazon_tshirt_scrapper.csv')
