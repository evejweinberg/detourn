import requests
from bs4 import BeautifulSoup
import time
# import urllib #this comes with python
#
def getTotalPages(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser')

    pageButtons = soup.select('.page-button')[-1].text
    pageButtons = pageButtons.replace(',', '')
    pageButtons = int(pageButtons)
    return pageButtons
    # print pageButtons


# pagenumber = 1
base_url = "https://www.amazon.com/Collagen-Peptides-Grass-Fed-Certified-Friendly/product-reviews/B00XQ2XGAA/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=avp_only_reviews&pageNumber="

def getReviews(url, pagenumber=1):
    html = requests.get(url + str(pagenumber)).text
    soup = BeautifulSoup(html,'html.parser')

    reviews = soup.select('span.review-text')

    for review in reviews:
        print review.text

def getTitleAndStars(url, pagenumber=1):
    html = requests.get(url + str(pagenumber)).text
    soup = BeautifulSoup(html,'html.parser')
    reviews = soup.select('.review')
    for review in reviews:
        title = review.select('.review-title')[0].text
        body = review.select('.review-text')[0].text
        stars = review.select('.review-rating')[0].text

        print title, stars
        #always returns a list, even if there is just one
        #so get the zero element


#make up a name and w for write
filedata = open('new.txt', 'w')
#its not to be a string
filedata.write('string here')

# filedata.close()

# with open('new.txt','w') as filedata:
#     filedata.write()



totalPages = getTotalPages(base_url + '1')

print totalPages

for pagenumber in range(1,totalPages):
    getTitleAndStars(base_url, pagenumber)
    # getReviews(base_url, pagenumber)
    #add a delay
    time.sleep(3)
