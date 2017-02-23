
# import selenium
from selenium import webdriver
import time
from time import gmtime, strftime


# BLANK WINDOW
driver = webdriver.Firefox()
#//print hi (fade on or type on)
filename = 'termArt.txt'

# WORDS = ['what','do','you','want', 'from', 'me','?']
#go to a wikipedia page and look for WORDS

#Terminal window
# osascript -e 'tell application \"System Events\"' -e 'keystroke \"f\" using { command down, control down }' -e 'activate' -e 'end tell'
# os.system( [shell command here i think  )
#//go full screen, hit command enter on itself
#//use applescript


#//make 10 pop-ups default UI that read:
# ASK = ['how','was','your','day','?']


#//make Ascii art in the terminal

#//then ask:



filedata = open(filename, 'a')
# f = open(filename, 'a').write(what)
# filedata = codecs.open('medium.txt', 'r', 'utf-8')
filedata.write('\n')
filedata.write('\n')
filedata.write(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
filedata.write('\n')


# def get_page():
#     time.sleep(.5)
#     titles = driver.find_elements_by_css_selector(searchterm)
#
#     for title in titles:
#         filedata.write(title.text.encode("utf8"))
#         filedata.write("\n")



driver.get()
# get_page()
driver.quit()





filedata.close()

# with open('new.txt','w') as filedata:
#     filedata.write()
