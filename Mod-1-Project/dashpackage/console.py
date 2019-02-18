from models import Base, Concert, Artist, Genre, Venue
from ticketmasterapi import TicketMasterAPI, TicketmasterEventsParser, TicketmasterConcertBuilder
from ticketwebscraper import TicketWebParser
from eventbriteapi import EventbriteAPI, EventbriteEventsParser, EventbriteConcertBuilder
from bs4 import BeautifulSoup
import sqlalchemy
from queries import *
engine = sqlalchemy.create_engine('sqlite:///nycconcertdatabase.db', echo=True)

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
