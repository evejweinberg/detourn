import sys
import os
from pyfiglet import Figlet
from selenium import webdriver
import time
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format


#make a temp URL and browser reference
url = "http://www.cnn.com/"
#choose some fonts
f = Figlet(font='big')
a = Figlet(font='xhelvi')


#dont look at this garbage
# script = '''
# alert('hihihih')
# '''

# driver.execute_script(script, yo);
# print 'EXECUTED!'
# driver.execute_script(script);


#start the console conversation
os.system("say hi! What is your name?")
question = "What is your name? "
print f.renderText(question)
theirName = raw_input("-------------->")

#store their answer in a variable
replacement_text = theirName

os.system("say hi "+ replacement_text)
#use cprint to make it pretty bubbleletters
cprint(figlet_format('hi ' + theirName + ' !', font='starwars'),
       'yellow', 'on_red', attrs=['bold'])


time.sleep(1)

print f.renderText(theirName+ ", Let's surf the web together. H-T-T-P-S!")
sayThis = "say " + replacement_text
os.system(sayThis + "Lets surf the web together. What is your favorite h t t p s secure website?")
destination = raw_input("-------------->")

response = destination + '???  Are you crazy? We can only go to CNN'
print a.renderText(response)
sayThis = "say " + response
os.system(sayThis)
time.sleep (1)


init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
sayThis = "say " + 'we can only go to CNN'
cprint(figlet_format(sayThis, font='starwars'),
       'yellow', 'on_red', attrs=['bold'])
os.system(sayThis)





#open the web broswer!!!
driver = webdriver.Firefox();
# driver = webdriver.PhantomJS();
driver.set_window_size(1200,4800);
driver.get(url)
os.system('say ohhhhhh, this is sad news today')

original_imgs = driver.find_elements_by_css_selector("img")

time.sleep(2)

sayThis = 'say ' + replacement_text
os.system(sayThis + '. I want to make you happy. Find an image of something happy and give it to me')
thier_image = raw_input("PASTE AN IMAGE LINK HERE-->")

temp_image = "http://www.publicdomainpictures.net/pictures/140000/velka/rainbow-1445337690d8q.jpg"



def makeHappy(thier_image):
    for i in original_imgs:
        driver.execute_script('arguments[0].src = arguments[1]', i, thier_image)

#replace all images with their image
makeHappy(thier_image)

#popup on the page and ask them to repsond in the console
#why do I get an error!!?!?!
# driver.execute_script('console.log("window.ourNameSpace.engine");')
# driver.execute_script('alert("did that make you happy? Answer me in the console");')


# driver.execute_script(script, replacement_text,replacement_text2)
time.sleep(5)

init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
addres_them = "say " + replacement_text
sayThis = addres_them + 'DID I  make you happy?'

os.system(sayThis)
cprint(figlet_format('DID I  make you happy?', font='starwars'),
       'yellow', 'on_red', attrs=['bold'])
are_they_happy = raw_input("----------->")


# if (are_they_happy == "yes"):
#     print





show_my_true_form = '''
var canv = document.createElement('canvas');
                        canv.id = 'canvasB';
                        // index++;
                        document.body.appendChild(canv); // adds the canvas to the body element
                        //retrieve context
                        var ctx = canv.getContext('2d');
                        var img = new Image();
                        img.src = 'http://itp.evejweinberg.com/a/guy2.mp4';

                        img.onload = function() {
                          console.log('loaded')
                          setInterval(function(){  processFrame()},40)
                        }


  setInterval(function(){  processFrame()},40)
			var outputCanvas = document.getElementById('output'),
				output = outputCanvas.getContext('2d'),
				bufferCanvas = document.getElementById('buffer'),
				buffer = bufferCanvas.getContext('2d'),
				video = document.getElementById('bottom-vid'),
				width = outputCanvas.width,
				height = outputCanvas.height,
				interval;
 function processFrame() {

  				buffer.drawImage(video, 0, 0);

  				// this can be done without alphaData, except in Firefox which doesn't like it when image is bigger than the canvas
  				var	image = buffer.getImageData(0, 0, width, height),
  					imageData = image.data,
  					alphaData = buffer.getImageData(0, height, width, height).data;


  				for (var i = 3, len = imageData.length; i < len; i = i + 4) {
  					imageData[i] = alphaData[i-1];
  				}

  				output.putImageData(image, 0, 0, 0, 0, width, height);



        video.style.display = 'none';
        outputCanvas.style.display = 'block';

  			}



'''


driver.execute_script(show_my_true_form)
