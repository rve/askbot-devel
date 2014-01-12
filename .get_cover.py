import re
import urllib2
from bs4 import BeautifulSoup as bs

url="http://api.douban.com/book/subject/1220562"
result = urllib2.urlopen(url).read()
soup = bs(result)
cover = soup.find(rel="image").get('href')
print cover

