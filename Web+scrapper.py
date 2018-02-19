
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup as soup

#Target finds and downloads the html page
target = requests.get('https://www.newegg.com/global/in/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphic+card&N=-1&isNodeId=1')

#It parses the data 
html_content = soup(target.content,'html.parser')

# grabs each product
container = html_content.find_all('div',{'class':'item-container'})

filename = 'web.csv'
headers = 'Brand , Product , Shipping , \n'
f=open(filename,'w')
f.write(headers)

for container in container:
    
    brand = container.div.div.a.img['title']
    
    title = container.findAll('a',{'class':'item-title'})
    
    product_name = title[0].text
    
    shipping_container = container.findAll('li',{'class':'price-ship'})
    shipping = shipping_container[0].text.strip()
    
    pricing = container.findAll('li',{'class':'price-current'})
    
    
    print ('brand: '+brand)
    print ('Product: '+product_name)
    print ('Shipping: '+shipping)
    
    f.write(brand + ',' + product_name.replace(',','|') + ',' + shipping+ '\n')
    
f.close()

