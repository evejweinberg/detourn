Python cheatsheet - detourning

In terminal —

//look for a word and make a new file
$ grep word thing.txt > new filename.txt

//connect commands together with pipe
//sort the file alphabetically, then search for whale lines and make a new file
$ sort thing.txt | grep whale >  newfile.txt

wc = word count

$ wc thing.txt
//Prints lines, words, characters
$ grep whale thing.txt | wc

//pipe as many times as you want

$ more

//make a new empty file
$ touch filename.py

Python —

Launch interactive shell
$ python

exit()

//run a python file
Python filename.py

//go to folder you want to work in
$ virtualenv env
$ source env/bin/activate
//now you see:
(Env) name: folder $

//now install beautiful soup

$ pip install beautifulsoup4
