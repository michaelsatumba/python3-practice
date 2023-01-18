
import bs4

import requests

res = requests.get('https://automatetheboringstuff.com/2e/chapter12/')

res.raise_for_status

soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('#calibre_link-372 > strong')
print(elems[0].text.strip())
