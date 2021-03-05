import re
import csv
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


CSV_PATH = 'starbucks_menu'

if not os.path.exists(CSV_PATH):
    os.mkdir(CSV_PATH)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.starbucks.co.kr/menu/drink_list.do')

# get category names
category_name_elems = driver.find_elements_by_xpath('//li/label[starts-with(@for, product_)]')

category_names = list()
for i in category_name_elems:
    category_names.append(i.text)
category_names.pop(0)

# get product names
products_under_category = driver.find_elements_by_xpath('//ul[starts-with(@class, "product_")]')

products_list = list()
for i in products_under_category:
    product_names = i.find_elements_by_tag_name('dd')

    products_by_category = list()  
    for name in product_names:
        products_by_category.append(name.text)
    products_list.append(products_by_category)


category_product_set = list()
for i, products in enumerate(products_list):
    category_product_set.append((category_names[i], products))

# save data to csv file
with open('starbucks_menu/menu.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(category_product_set)

driver.quit()