from bs4 import BeautifulSoup
import re
import urllib2

#function to find links within a given link
def myscrape(url, case):

    #makes sure the url is a string
    newu  = str(url)
    #add url components to the given case
    newc = 'http://' + str(case) + '/'
    page = urllib2.urlopen(newu).read()

    soup = BeautifulSoup(page, 'lxml')
    soup.prettify()
    links = set()

    for link in soup.findAll('a',href=re.compile(newc)):
        links.add(link['href'])

    return links

if __name__=="__main__":

    url = raw_input("Enter url: ")
    case = raw_input("Enter a case: ")
    work = myscrape(url,case)

    for data in work:
        print data
