# import selenium
from selenium import webdriver
import time
source = 'ddg'


url= "http://codepen.io/animeshk874/pen/WRgMdv"
searchterm = ".CodeMirror-code"
filename = 'codepen.txt'


driver = webdriver.Firefox()


#selenium lets you control other browsers, we can open websites
#finds all, without the s on elelments it returns only the first
#make up a name and w for write
filedata = open(filename, 'w')




def get_page():
    time.sleep(.5)
    titles = driver.find_elements_by_css_selector(searchterm)
    print titles

    for title in titles:
        # print title.text

        #its got to be a string
        filedata.write(title.text)
        filedata.write("\n")

    # driver.find_element_by_css_selector('a.next').click()

    # get_page()


driver.get(url)
get_page()

#to close the browser
driver.quit()





filedata.close()

# with open('new.txt','w') as filedata:
#     filedata.write()
