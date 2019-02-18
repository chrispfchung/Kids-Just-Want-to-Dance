import requests
from models import *
import requests
import json


#goc = "get one or create" queries databse to check to make sure object has not already been initialized
#will use this function in Ticketmaster and Eventbrite ConcertBuilder
from sqlalchemy.orm.exc import NoResultFound
def goc(session, model,**kwargs):
   try:
       return session.query(model).filter_by(**kwargs).one()
   except NoResultFound:
       return model(**kwargs)


#ConcertBuilder class will use output from ticketmasterapi function
#and parsing functions from EventsParser class to output
#sqlalchemy objects


class TicketmasterConcertBuilder:
    def __init__(self, url):
        self.url = url

    def run(self):
        all_concerts = []
        tm = TicketMasterAPI(self.url)
        for i in tm.data_pull():
            parser = TicketmasterEventsParser(i)
            concert = Concert(name=parser.concert_name(),
            date=parser.concert_date(), minimum_price=parser.concert_minimum_price(),
            maximumum_price=parser.concert_maximum_price(), url=parser.concert_url(),
            artists=goc(session, Artist, name=parser.concert_artist()),
            genres=goc(session, Genre, name=parser.concert_genre()),
            venues=goc(session, Venue,name=parser.concert_venue_name(), city=parser.concert_venue_city(),
            address=parser.concert_venue_address(), latitude=parser.concert_venue_latitude(),
            longitude=parser.concert_venue_longitude()))
            session.add(concert)
            session.commit()

# Ticketmaster API addresses
# page0 = 'https://app.ticketmaster.com/discovery/v2/events.json?latlong=40.754900,-73.984000&radius=8&unit=miles&source=ticketmaster&classificationName=music&startDateTime=2018-11-09T14:00:00Z&page=0&size=200&sort=relevance,desc&apikey=rah2o9AS2HbqU4x2DwAbsRZA35MutNT4'
# page1 = 'https://app.ticketmaster.com/discovery/v2/events.json?latlong=40.754900,-73.984000&radius=8&unit=miles&source=ticketmaster&classificationName=music&startDateTime=2018-11-09T14:00:00Z&page=1&size=200&sort=relevance,desc&apikey=rah2o9AS2HbqU4x2DwAbsRZA35MutNT4'
# page2 = 'https://app.ticketmaster.com/discovery/v2/events.json?latlong=40.754900,-73.984000&radius=8&unit=miles&source=ticketmaster&classificationName=music&startDateTime=2018-11-09T14:00:00Z&page=2&size=200&sort=relevance,desc&apikey=rah2o9AS2HbqU4x2DwAbsRZA35MutNT4'
# page3 = 'https://app.ticketmaster.com/discovery/v2/events.json?latlong=40.754900,-73.984000&radius=8&unit=miles&source=ticketmaster&classificationName=music&startDateTime=2018-11-09T14:00:00Z&page=3&size=200&sort=relevance,desc&apikey=rah2o9AS2HbqU4x2DwAbsRZA35MutNT4'
# page4 = 'https://app.ticketmaster.com/discovery/v2/events.json?latlong=40.754900,-73.984000&radius=8&unit=miles&source=ticketmaster&classificationName=music&startDateTime=2018-11-09T14:00:00Z&page=4&size=200&sort=relevance,desc&apikey=rah2o9AS2HbqU4x2DwAbsRZA35MutNT4'
# page5 = 'https://app.ticketmaster.com/discovery/v2/events.json?latlong=40.754900,-73.984000&radius=8&unit=miles&source=ticketmaster&classificationName=music&startDateTime=2018-11-09T14:00:00Z&page=0&size=200&sort=relevance,asc&apikey=rah2o9AS2HbqU4x2DwAbsRZA35MutNT4'



#class function to pull in json event data from ticketmaster API
#output will be a list of events

class TicketMasterAPI:

    def __init__(self, url):
        self.url = url

    def data_pull(self):
        r = requests.get(self.url)
        concert_data_dictionary = r.json()
        concert_list = concert_data_dictionary['_embedded']['events']
        return concert_list


#class to define parsing functions
class TicketmasterEventsParser:
    def __init__(self, individual_concert_data):
        self.individual_concert_data = individual_concert_data

    #retrieves concert name
    def concert_name(self):
        return self.individual_concert_data['name']

    #retrieves concert Date
    def concert_date(self):
        return self.individual_concert_data['dates']['start']['localDate']

    #retrieves minimum price
    def concert_minimum_price(self):
        try:
            return self.individual_concert_data['priceRanges'][0]['min']
        except:
            pass

    #retrieves maximumum_price
    def concert_maximum_price(self):
        try:
            return self.individual_concert_data['priceRanges'][0]['max']
        except:
            pass

    #retrieves concert URL
    def concert_url(self):
        return self.individual_concert_data['url']

    #retrieve concert artist/artists
    def concert_artist(self):
        try:
            return self.individual_concert_data['_embedded']['attractions'][0]['name']
        except:
            pass

    #retrieves genre
    def concert_genre(self):
        try:
            return self.individual_concert_data['classifications'][0]['genre']['name']
        except:
            pass

    #retrieves venue_name
    def concert_venue_name(self):
        return self.individual_concert_data['_embedded']['venues'][0]['name']

    #retrieves venue city
    def concert_venue_city(self):
        return self.individual_concert_data['_embedded']['venues'][0]['city']['name']

    #retrieves concert venue address
    def concert_venue_address(self):
        try:
            return self.individual_concert_data['_embedded']['venues'][0]['address']['line1']
        except:
            pass

    #retrieves concert latitude
    def concert_venue_latitude(self):
        return self.individual_concert_data['_embedded']['venues'][0]['location']['latitude']

    #retrieves concert longitude
    def concert_venue_longitude(self):
        return self.individual_concert_data['_embedded']['venues'][0]['location']['longitude']



#function to scrape and add ticketweb prices
def add_ticket_web_prices():
    concerts = session.query(Concert).filter(Concert.minimum_price == None).all()
    for concert in concerts:
        if "ticketweb" in concert.url:
            try:
                parser = TicketWebParser(concert.url)
                concert.minimum_price = parser.get_price()
                session.add(concert)
                session.commit()
            except:
                pass
