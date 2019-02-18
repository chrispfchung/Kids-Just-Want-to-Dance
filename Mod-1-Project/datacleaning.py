#fixing hiphop / rap genre
def hiphop():
    concerts = session.query(Concert).join(Genre).filter(Genre.name == "Hip Hop / Rap")
    hiphop_genre = session.query(Genre).filter(Genre.name == "Hip-Hop/Rap").first()
    for concert in concerts:
        concert.genres = hiphop_genre
        session.add(concert)
        session.commit()

#fixing jazz genre
def jazz():
    concerts = session.query(Concert).join(Genre).filter(Genre.name == "Jazz")
    jazz_genre = session.query(Genre).filter(Genre.name == "Blues & Jazz").first()
    for concert in concerts:
        concert.genres = jazz_genre
        session.add(concert)
        session.commit()

#fixing religious genre
def religious():
    concerts = session.query(Concert).join(Genre).filter(Genre.name == "Religious/Spiritual")
    jazz_genre = session.query(Genre).filter(Genre.name == "Religious").first()
    for concert in concerts:
        concert.genres = jazz_genre
        session.add(concert)
        session.commit()


#fixing other genre
def other():
    concerts = session.query(Concert).join(Genre).filter(Genre.name == "Undefined")
    other_genre = session.query(Genre).filter(Genre.name == "Other").first()
    for concert in concerts:
        concert.genres = other_genre
        session.add(concert)
        session.commit()


#fixing electronic genre
def electronic():
    concerts = session.query(Concert).join(Genre).filter(Genre.name == "EDM / Electronic")
    electronic_genre = session.query(Genre).filter(Genre.name == "Dance/Electronic").first()
    for concert in concerts:
        concert.genres = electronic_genre
        session.add(concert)
        session.commit()

#fixing pop genre
def pop():
    concerts = session.query(Concert).join(Genre).filter(Genre.name == "Top 40")
    pop_genre = session.query(Genre).filter(Genre.name == "Pop").first()
    for concert in concerts:
        concert.genres = pop_genre
        session.add(concert)
        session.commit()
