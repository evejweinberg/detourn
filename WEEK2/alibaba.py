import bs4
import urllib

#download html
#send it to beautiful soup
#tell bs4 what to search for
# import http://www.alibaba.com//Agrochemicals_pid100003949?spm=a2700.7848340.1997230041.7.an3PUG
#inside h2 with class title

url2 = "https://news.ycombinator.com/item?id=13520891"
url = "http://www.alibaba.com//Agrochemicals_pid100003949?spm=a2700.7848340.1997230041.7.an3PUG"

html = urllib.urlopen(url2).read()

# print html

# you can run this file with a pointer to save it
# $ python alibaba.py > newfile.html

#create an object that parses the html content
soup = bs4.BeautifulSoup(html, "html.parser")

#like a querySelector
titles = soup.select('.comment')

# print titles

for thing in titles:
    if thing.find("http") == 1:
    print thing.text.strip()

#lets remove white space with strip() too. like JS's trim()

#next time == multiple pages!!
