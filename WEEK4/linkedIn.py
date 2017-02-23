from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# import sys


# driver = webdriver.Chrome();
driver = webdriver.Firefox();
# driver = webdriver.PhantomJS();
driver.set_window_size(1200,4800);
driver.get('https://www.linkedin.com/uas/login')

#inspect the website and fin the login DOM elelent
login = driver.find_element_by_css_selector('#session_key-login')
login.send_keys('eve@neveroddoreven.tv')
password = driver.find_element_by_css_selector('#session_password-login')
password.send_keys('M8@Ug7Ehmu$J')

#hit return
password.send_keys(Keys.RETURN)

time.sleep(6)

search_term = 'police'

# search_term = 'police'
# url = 'https://www.linkedin.com/search/results/people/?keywords=' + search_term
url = "https://www.linkedin.com/vsearch/p?type=people&keywords=" + search_term

driver.get(url)

time.sleep(6)

buttons = driver.find_elements_by_css_selector('.search-result .people button')

buttons[0].click()

send_button = driver.find_elements_by_css_selector('.send-invite_actions button')[-1];

send_button.click()



# replacement_text = 'Eve weinberg yoyoyoyoyoy'
# replacement_text2 = 'SRLSLY'
#the arguments that are in the terminal command line
# replacement_text = sys.argv[1]
# in JS you would do this
# var elements = document.querySelectorAll('h1');
#live coding
# for var
# elements[i].textContent = 'LOL';

# driver.execute_script("alert('hi!')");

# instead make a variable
#a multi line string
# script = '''
# var elements = document.querySelectorAll('h1, h2, h3');
# for (var i=0; i< elements.length; i++){
# elements[i].textContent = arguments[0]
# }
# '''

# driver.execute_script(script, replacement_text,replacement_text2)
#places all next aerguments into an aray calle arguments

#LETS TAKE A SCREENSHOT
# time.sleep (2)
# driver.save_screenshot(sys.argv[1]+'_eve.png')
# driver.save_screenshot(sys.argv[1].replace(' ','_')

# you can embed javascript to scroll


# time.leep(12)
# driver.quit()
