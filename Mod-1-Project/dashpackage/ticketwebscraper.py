#parser for tickets that did not have prices in the Ticketmaster API
import requests
from bs4 import BeautifulSoup


class TicketWebParser:
    def __init__(self, url):
        self.url = url

    def get_price(self):
        r = requests.get(self.url)
        c = r.content
        soup = BeautifulSoup(c, 'html.parser')
        data = soup.findAll('span', {'class': 'price theme-secondary-color small'})
        price = float(data[0].text.replace('$', ""))
        return price
