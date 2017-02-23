


# import selenium
from selenium import webdriver
import time



url= "https://www.youtube.com/watch?v=tO0hffeA2iE"
searchterm = ".comment-renderer-text-content"
filename = 'YTcomments.txt'


driver = webdriver.Firefox()


#selenium lets you control other browsers, we can open websites
#finds all, without the s on elelments it returns only the first
#make up a name and w for write
filedata = open(filename, 'w')




def get_page():
    time.sleep(.5)
    titles = driver.find_elements_by_css_selector(searchterm)

    for title in titles:

        if ("fuck" in title.text) or ("ass" in title.text) or ("bitch" in title.text):
            print title.text.strip()
            print ('\n')

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
