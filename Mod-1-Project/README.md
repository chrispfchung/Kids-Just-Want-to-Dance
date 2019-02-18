# Module 1 Project
![alt text](https://github.com/briansrebrenik/Mod-1-Project/blob/master/screenshots/Screen%20Shot%202018-11-19%20at%201.23.52%20PM.png?raw=true)

What we used:

1. Python
2. SQL
3. SQLAlchemy
4. Flask
5. Dash
6. Ticketmaster API
7. Eventbrite API
8. BeautifulSoup
9. Mapbox 


## OVERVIEW
The purpose of our project was to determine the affordability and genre variety of the live music scene in New York City. In order to compile concert data, we used the Ticketmaster API. The data available included concert data up to a year in advance of show date and
consisted of information like name, genre, location, start/end date, price, and venue. To create an even fuller database,
we also pulled from Eventbrite’s API. This contained very similar information to
Ticketmaster’s. In total, we have 2,224 clean, usable events. Armed with this data, we could answer the following key questions : “What type of music is popular in NYC? What’s the affordability of music in NYC?
Average entry price by genre? Per neighborhood? and Where are the free concerts located?”

Our SQL Database Schema consisted of building relationships centered around Concert.
The other classes are Venue, Genre, and Artist. The Venue class contains the most properties
as it provided location information which was very important to our project. We were able to get
city, borough and eventually created zipcode-to-neighborhood functions that added event’s neighborhood
into our database based on its zipcode. This allowed us to answer more questions regarding concert location.
We narrowed down the amount of genres because of inconsistent genre format, e.g. Hip/Hop vs Hip-Hop.
We also grouped genres <10 events with similar genres to prevent too much scattered info.

One of the early issues we ran into was that many of the prices could not connect into our database because Ticketmaster API pulled
from other ticket sales websites. A few of these websites did not allow us to scrape its site as it thought
we were bots and others contained event information that was inconsistent and missing data.Thankfully Ticketweb.com,
the most occurring website by far, allowed us to freely scrape for data. Another issue was that
much of the artist information on the Ticketmaster API was able to connect easily into our database.
However because of Eventbrite’s inconsistent event pages’ formatting, its artists were unable to pull through.
Although artists could’ve been potentially helpful to our project, this was not a major issue because other data could answer much more questions.

## Plotting the Data Collected

![alt text](https://github.com/briansrebrenik/Mod-1-Project/blob/master/screenshots/Screen%20Shot%202018-11-19%20at%203.33.41%20PM.png)
![alt text](https://github.com/briansrebrenik/Mod-1-Project/blob/master/screenshots/Screen%20Shot%202018-11-19%20at%203.34.05%20PM.png)
![alt text](https://github.com/briansrebrenik/Mod-1-Project/blob/master/screenshots/Screen%20Shot%202018-11-19%20at%203.34.36%20PM.png)
![alt text](https://github.com/briansrebrenik/Mod-1-Project/blob/master/screenshots/Screen%20Shot%202018-11-19%20at%203.34.53%20PM.png)
![alt text](https://github.com/briansrebrenik/Mod-1-Project/blob/master/screenshots/Screen%20Shot%202018-11-19%20at%203.35.22%20PM.png)
![alt text](https://github.com/briansrebrenik/Mod-1-Project/blob/master/screenshots/Screen%20Shot%202018-11-19%20at%203.35.36%20PM.png)
![alt text](https://github.com/briansrebrenik/Mod-1-Project/blob/master/screenshots/Screen%20Shot%202018-11-19%20at%203.35.50%20PM.png)
