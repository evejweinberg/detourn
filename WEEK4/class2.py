from selenium import webdriver
import time
import sys


# driver = webdriver.Firefox();
driver = webdriver.PhantomJS();
driver.set_window_size(1200,4800);
driver.get('http://foxnews.com')


replacement_text = 'Eve weinberg yoyoyoyoyoy'
replacement_text2 = 'SRLSLY'
replacement_text = sys.argv[1]
# in JS you would do this
# var elements = document.querySelectorAll('h1');
#live coding
# for var
# elements[i].textContent = 'LOL';

# driver.execute_script("alert('hi!')");

# instead make a variable
#a multi line string
script = '''
var elements = document.querySelectorAll('h1, h2, h3');
for (var i=0; i< elements.length; i++){
elements[i].textContent = arguments[0]
}
'''

driver.execute_script(script, replacement_text,replacement_text2)
#places all next aerguments into an aray calle arguments

#LETS TAKE A SCREENSHOT
time.sleep (2)
driver.save_screenshot(sys.argv[1]+'_eve.png')
# driver.save_screenshot(sys.argv[1].replace(' ','_')

# you can embed javascript to scroll


time.sleep(2)
driver.quit()
