import requests
from bs4 import BeautifulSoup
import json

myUrl = {
    # 'https://en.wikipedia.org/wiki/Venkatesh_Daggubati_filmography',
    # 'https://en.wikipedia.org/wiki/Chiranjeevi_filmography',
    # 'https://en.wikipedia.org/wiki/Akkineni_Nagarjuna_filmography',
    # 'https://en.wikipedia.org/wiki/Krishna_filmography',
    # 'https://en.wikipedia.org/wiki/Mahesh_Babu_filmography',
    'https://en.wikipedia.org/wiki/Vijay_Deverakonda'
    #
    # 'https://en.wikipedia.org/wiki/Rajinikanth_filmography',
    # 'https://en.wikipedia.org/wiki/Kamal_Haasan_filmography',
    # 'https://en.wikipedia.org/wiki/Vikram_filmography',
    # 'https://en.wikipedia.org/wiki/Vijay_filmography',
    # 'https://en.wikipedia.org/wiki/Ajith_Kumar_filmography',
    #
    # 'https://en.wikipedia.org/wiki/Mammootty_filmography',
    # 'https://en.wikipedia.org/wiki/Mohanlal_filmography',
    # 'https://en.wikipedia.org/wiki/Suresh_Gopi_filmography',
    #
    # 'https://en.wikipedia.org/wiki/Shah_Rukh_Khan_filmography',
    # 'https://en.wikipedia.org/wiki/Salman_Khan_filmography',
    # 'https://en.wikipedia.org/wiki/Aamir_Khan_filmography',
    # 'https://en.wikipedia.org/wiki/Sanjay_Dutt_filmography',
    # 'https://en.wikipedia.org/wiki/Akshay_Kumar_filmography',
    #
    # 'https://en.wikipedia.org/wiki/Tom_Cruise_filmography',
    # 'https://en.wikipedia.org/wiki/Nicolas_Cage_filmography',
    #'https://en.wikipedia.org/wiki/Bruce_Willis_filmography'
}

movies = {}
moviesLinks = set()
wikiUrl = 'https://en.wikipedia.org'


def get_response(page_url):
    return requests.get(page_url)


for url in myUrl:
    # To make a request
    page = get_response(url)

    # To make our raw HTML data more prettify we need to parse our content with the help of some parsers.
    # the parsers that are quite often used are —
    #
    # lxml
    # HTML5lib
    # XML parser
    # HTML.parser

    soupParser = BeautifulSoup(page.text, 'lxml')
    rows = soupParser.select('.wikitable.sortable tbody tr')

    for tr in rows:
        links = tr.select('td i a')
        for a in links:
            if (str(a['title']).find('page does not exist') < 0) and (len(str(a['href'])) > 0):
                movieUrl = wikiUrl + a['href']
                movies[a['title']] = movieUrl
                moviesLinks.add(movieUrl)                
json_string = json.dumps(movies, indent=4)
print(json_string)
print(moviesLinks)

for movieLink in movieLinks:
    page = get_response(wikiUrl+href)
    soup = BeautifulSoup(page.text, 'html.parser')
    movieInfo = soup.select('.infobox.vevent tr', 'html.parser')
    print()
