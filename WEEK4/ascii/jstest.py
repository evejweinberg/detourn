import sys
import os
from selenium import webdriver
import time


#open the web broswer!!!
driver = webdriver.Firefox();
driver.set_window_size(1200,4800);
url = "http://www.cnn.com/"
driver.get(url)


show_my_true_form = '''
var canv = document.createElement('canvas');
                        canv.id = 'canvasB';
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

# why does this work, but alery does not??
driver.execute_script('console.log("window.ourNameSpace.engine");')
# driver.execute_script('alert("did that make you happy? Answer me in the console");')

#why does this NOT work??
# driver.execute_script(show_my_true_form)
