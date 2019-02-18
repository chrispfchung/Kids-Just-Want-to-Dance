from dashpackage import db


#creating concert class/table
class Concert(db.Model):
    __tablename__ = 'concerts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    date = db.Column(db.Date)
    minimum_price = db.Column(db.Float)
    maximumum_price = db.Column(db.Float)
    url = db.Column(db.Text)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'))
    artists = db.relationship('Artist', back_populates ='concerts')
    genres = db.relationship('Genre', back_populates='concerts')
    venues = db.relationship('Venue', back_populates='concerts')

#creating artist class/table
class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    genre_id = db.Column(db.Text, db.ForeignKey('genres.id'))
    concerts = db.relationship('Concert', back_populates='artists')
    genres = db.relationship('Genre', back_populates='artists')



#creating genre class/table
class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    artists = db.relationship('Artist', back_populates='genres')
    concerts = db.relationship('Concert', back_populates='genres')
    venues = db.relationship('Venue', back_populates='genres')

#creating venue class/table
class Venue(db.Model):
    __tablename__ = 'venues'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    city = db.Column(db.Text)
    address = db.Column(db.Text)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    zip = db.Column(db.Integer)
    neighborhood = db.Column(db.Text)
    borough = db.Column(db.Text)
    concerts = db.relationship('Concert', back_populates='venues')
    genres = db.relationship('Genre', back_populates='venues')
