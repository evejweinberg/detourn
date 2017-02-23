from selenium import webdriver
import time


driver = webdriver.Firefox();
driver.set_window_size(1200,800);
driver.get('http://foxnews.com')


newTitles = 'Eve weinberg yoyoyoyoyoy'
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
elements[i].textContent = 'EVE WEINBERG'
}
'''

driver.execute_script(script)

#LETS TAKE A SCREENSHOT
time.sleep (2)
driver.save_screenshot('eve.png')

# you can embed javascript to scroll


time.sleep(2)
driver.quit()
