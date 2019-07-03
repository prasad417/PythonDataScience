import requests
from bs4 import BeautifulSoup

myUrl = {
    'https://en.wikipedia.org/wiki/Venkatesh_Daggubati_filmography',
    'https://en.wikipedia.org/wiki/Chiranjeevi_filmography',
    'https://en.wikipedia.org/wiki/Akkineni_Nagarjuna_filmography',
    'https://en.wikipedia.org/wiki/Krishna_filmography',
    'https://en.wikipedia.org/wiki/Mahesh_Babu_filmography',

    'https://en.wikipedia.org/wiki/Rajinikanth_filmography',
    'https://en.wikipedia.org/wiki/Kamal_Haasan_filmography',
    'https://en.wikipedia.org/wiki/Vikram_filmography',
    'https://en.wikipedia.org/wiki/Vijay_filmography',
    'https://en.wikipedia.org/wiki/Ajith_Kumar_filmography',

    'https://en.wikipedia.org/wiki/Mammootty_filmography',
    'https://en.wikipedia.org/wiki/Mohanlal_filmography',
    'https://en.wikipedia.org/wiki/Suresh_Gopi_filmography',

    'https://en.wikipedia.org/wiki/Shah_Rukh_Khan_filmography',
    'https://en.wikipedia.org/wiki/Salman_Khan_filmography',
    'https://en.wikipedia.org/wiki/Aamir_Khan_filmography',
    'https://en.wikipedia.org/wiki/Sanjay_Dutt_filmography',
    'https://en.wikipedia.org/wiki/Akshay_Kumar_filmography',

    'https://en.wikipedia.org/wiki/Tom_Cruise_filmography',
    'https://en.wikipedia.org/wiki/Nicolas_Cage_filmography',
    'https://en.wikipedia.org/wiki/Bruce_Willis_filmography'
}

for url in myUrl:
    # To make a request
    page = requests.get(url)

    # To make our raw HTML data more prettify we need to parse our content with the help of some parsers.
    # the parsers that are quite often used are —
    #
    # lxml
    # HTML5lib
    # XML parser
    # HTML.parser

    soup = BeautifulSoup(page.text, 'html.parser')
    links = soup.select('.wikitable.sortable tbody tr i a')

    for link in links:
        with open("../webscraping.txt", "a") as myfile:
            myfile.write(f'{str(link)}\n')

