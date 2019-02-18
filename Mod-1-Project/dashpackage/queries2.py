#average price per genre
session.query(Genre.name, sqlalchemy.func.avg(Concert.minimum_price)).join(Concert).group_by(Genre.name).all()


#number of concerts per genre
session.query(Genre.name, sqlalchemy.func.count(Concert.name)).join(Concert).group_by(Genre.name).all()

#Genre per neighborhood
session.query(Venue.neighborhood, sqlalchemy.func.count(Genre.name)).join(Concert).join(Genre).group_by(Venue.neighborhood).all()

#number of concerts per borough
session.query(Venue.borough, sqlalchemy.func.count(Concert.name)).join(Concert).group_by(Venue.borough).all()

#average price per borough
session.query(Venue.borough, sqlalchemy.func.avg(Concert.minimum_price)).join(Concert).group_by(Venue.borough).all()


#number of genres per Queens borough
def genres_per_borough(borough):
    return session.query(Genre.name, sqlalchemy.func.count(Genre.name).join(Concert).join(Venue).filter(Venue.borough == 'borough').group_by(Genre.name).all()

# #Query by date, needs to import datetime
# def after_date(year, month, day):
#     return session.query(Concert.name, Concert.date).filter(Concert.date > datetime.date(year, month, day)).all()


def concerts_at_price(price):
    return session.query(Venue.borough, sqlalchemy.func.count(Concert.name)).join(Concert).group_by(Venue.borough).filter(Concert.minimum_price == price).all()

def concerts_with_price_between(price1, price2):
    return session.query(Venue.borough, sqlalchemy.func.count(Concert.name)).join(Concert).group_by(Venue.borough).filter(Concert.minimum_price >= price1 <= price2).all()
