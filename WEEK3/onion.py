
# import selenium
from selenium import webdriver
import time
from time import gmtime, strftime



url= "http://www.theonion.com/"
# searchterm = ".most-popular a"
searchterm = ".most-popular .inner header .headline a"
filename = 'OnionMostPopular.txt'


driver = webdriver.Firefox()


#selenium lets you control other browsers, we can open websites
#finds all, without the s on elelments it returns only the first
#make up a name and w for write
filedata = open(filename, 'a')
# f = open(filename, 'a').write(what)
# filedata = codecs.open('medium.txt', 'r', 'utf-8')
filedata.write('\n')
filedata.write('\n')
filedata.write(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
filedata.write('\n')


def get_page():
    time.sleep(.5)
    titles = driver.find_elements_by_css_selector(searchterm)

    for title in titles:
        # print title.text.encode("utf8")

        #its got to be a string


        filedata.write(title.text.encode("utf8"))
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
