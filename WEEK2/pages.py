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

# while pagenumber < 10:
#     getReviews(base_url, pagenumber)
#     pagenumber ++

totalPages = getTotalPages(base_url + '1')

print totalPages

for pagenumber in range(1,totalPages):
    getReviews(base_url, pagenumber)
    #add a delay
    time.sleep(3)
