# import selenium
from selenium import webdriver
import time

driver = webdriver.Firefox()
url = ""

#selenium lets you control other browsers, we can open websites
#finds all, without the s on elelments it returns only the first




def get_page():
    time.sleep(.5)
    titles = driver.find_elements_by_css_selector('.result__title')

    for title in titles:
        print title.text

    # driver.find_element_by_css_selector('a.next').click()

    # get_page()


driver.get('https://duckduckgo.com/?q=facebook+data+article&ia=news')
get_page()

#to close the browser
driver.quit()
