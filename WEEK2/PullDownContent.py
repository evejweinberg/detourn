import bs4
import urllib

url2 = "https://news.ycombinator.com/item?id=13520891"
url3="http://wagesforfacebook.com/"

#download html
#send it to beautiful soup
html = urllib.urlopen(url3).read()

#create an object that parses the html content
soup = bs4.BeautifulSoup(html, "html.parser")

# print soup.text

# a querySelector
titles = soup.select('.main-text')

# print titles
#remove white space with strip() too. like JS's trim()

for thing in titles:
    if "struggling" in thing.text:
        print thing.text.strip()
        print ('\n')
