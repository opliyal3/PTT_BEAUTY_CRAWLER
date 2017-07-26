import requests
from bs4 import BeautifulSoup
import re
url = 'https://www.ptt.cc/bbs/Beauty/index.html'

reg_imgur_file = re.compile('http[s]?://i.imgur.com/\w+\.(?:jpg|png|gif)')

for round in range(3):
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    articles = soup.select('div.title a')
    paging = soup.select('div.btn-group-paging a')
    next_url = 'http://www.ptt.cc' + paging[1]['href']
    url = next_url

for article in articles :
    print(article.text,article['href'])
    res = requests.get('https://www.ptt.cc' + article['href'])
    image = reg_imgur_file.findall(res.text)
    print(image)