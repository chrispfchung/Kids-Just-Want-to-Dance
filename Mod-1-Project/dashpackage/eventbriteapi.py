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



#ConcertBuilder class will use output from eventbriteapi function
#and parsing functions from EventsParser class to output
#sqlalchemy objects

class EventbriteConcertBuilder:
    def __init__(self, url):
        self.url = url

    def run(self):
        all_concerts = []
        tm = EventbriteAPI(self.url)
        for i in tm.data_pull():
            parser = EventbriteEventsParser(i)
            concert = Concert(name=parser.concert_name(),
            date=parser.concert_date(), minimum_price=parser.concert_minimum_price(),
            maximumum_price=parser.concert_maximum_price(), url=parser.concert_url(),
            genres=goc(session, Genre, name=parser.concert_genre()),
            venues=goc(session, Venue,name=parser.concert_venue_name(), city=parser.concert_venue_city(),
            address=parser.concert_venue_address(), latitude=parser.concert_venue_latitude(),
            longitude=parser.concert_venue_longitude()))
            session.add(concert)
            session.commit()



#function to cycle through all eventbrite addresses and add data to database
def parse_through_apis():
    for i in range(1, 28):
        url = f"https://www.eventbriteapi.com/v3/events/search/?page={i}&categories=103&start_date.range_start=2018-11-08T00:00:00Z&price=paid&location.latitude=40.7549&location.longitude=-73.9840&location.within=8mi&expand=venue,subcategory,ticket_availability&token=XZYQ3WKQV5AWJJSDWP5L"
        builder = EventbriteConcertBuilder(url)
        builder.run()





#class function to pull in json event data from eventbrite API
#output will be a list of events

class EventbriteAPI:

    def __init__(self, url):
        self.url = url

    def data_pull(self):
        r = requests.get(self.url)
        concert_data_dictionary = r.json()
        concert_list = concert_data_dictionary['events']
        return concert_list

#class to define parsing functions
class EventbriteEventsParser:

    def __init__(self, individual_concert_data):
        self.individual_concert_data = individual_concert_data


    #retrieves concert name
    def concert_name(self):
        return self.individual_concert_data['name']['text']

    #retrieves concert Date
    def concert_date(self):
        return self.individual_concert_data['start']['local'][:10]

    #retrieves minimum price
    def concert_minimum_price(self):
        try:
            return float(self.individual_concert_data['ticket_availability']['minimum_ticket_price']['major_value'])
        except:
            pass

    #retrieves maximumum_price
    def concert_maximum_price(self):
        try:
            return float(self.individual_concert_data['ticket_availability']['maximum_ticket_price']['major_value'])
        except:
            pass

    #retrieves concert URL
    def concert_url(self):
        return self.individual_concert_data['url']

    #retrieve concert artist/artists
    def concert_artist(self):
        try:
            pass
        except:
            pass

    #retrieves genre
    def concert_genre(self):
        try:
            return self.individual_concert_data['subcategory']['name']
        except:
            pass

    #retrieves venue_name
    def concert_venue_name(self):
        return self.individual_concert_data['venue']['name']

    #retrieves venue city
    def concert_venue_city(self):
        return self.individual_concert_data['venue']['address']['city']

    #retrieves concert venue address
    def concert_venue_address(self):
        try:
            return self.individual_concert_data['venue']['address']['address_1']
        except:
            pass

    #retrieves concert latitude
    def concert_venue_latitude(self):
        return self.individual_concert_data['venue']['latitude']

    #retrieves concert longitude
    def concert_venue_longitude(self):
        return self.individual_concert_data['venue']['longitude']
