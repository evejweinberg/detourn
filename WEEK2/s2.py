# import selenium
from selenium import webdriver
import time

driver = webdriver.Firefox()
# driver = webdriver.Chrome()

url = "http://skymall.com/collections/health-beauty"

#selenium lets you control other browsers, we can open websites
#finds all, without the s on elelments it returns only the first



driver.get(url)



products = driver.find_elements_by_css_selector('.product')

for product in products:
    title = product.find_element_by_css_selector('product_title').text
    price = product.find_element_by_css_selector('price-box').text


    print title,price


#to close the browser
driver.quit()
