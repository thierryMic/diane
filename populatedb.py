from flask import url_for
from db.base import Base

import os
import re

from shutil import copy
from random import randint

from db.database import session, Member, Gallery, Painting, getTable, engine

gal = {"StillLife":1, "Wildlife":2, "Landscape":3}

def addMember(email, name, image, usergroup):
    member = Member(email=email, name=name, image=image, usergroup=usergroup)
    session.add(member)
    session.commit()


def addGallery(name, image):
    gallery = Gallery(name=name, image=image)
    session.add(gallery)
    session.commit()


def addGalleries():
    addGallery(name="Still life", image="img/Gallery StillLife")
    addGallery(name="Wildlife", image="img/Gallery Wildlife")
    addGallery(name="Landscapes", image="img/Gallery Landscapes")



def addPainting(title, galleryid, paintingdate="1/1/2008", medium="Oil on canvas",
                memberId="thierry.michel@hotmail.com", image="", height=122,
                width=99, sold=True, price=5000):


    painting = Painting(title=title, galleryId=galleryid, paintingDate=paintingdate,
                        memberId=memberId, image=image, medium=medium, height=height, width=width,
                        sold=sold, price=price)

    session.add(painting)
    session.commit()


def addPaintings():
    path = r"static/imgSrc"
    paintings =  os.listdir(path)
    y = 0
    for painting in paintings:
        x = re.search(r"(\w*)\s(.*)\.(\w*)", painting)
        if hasattr(x, 'group') and x.group(1) in gal:
            y = y + 1
            print y
            print "Filename: " + painting
            print "Gallery: " +  x.group(1)
            print "Painting: " + x.group(2)
            print "Extendion: " +x.group(3)
            print "\n"

            addPainting(title=x.group(2), galleryid=gal[x.group(1)], image=x.group(1) + " " + x.group(2))



if __name__ == '__main__':

    #drop tables
    Painting.__table__.drop(engine, checkfirst=False)
    Gallery.__table__.drop(engine, checkfirst=False)
    Member.__table__.drop(engine, checkfirst=False)

    Base.metadata.create_all(engine)

    addMember("thierry.michel@hotmail.com", "Thierry Michel", "", "admin")
    addGalleries()
    addPaintings()






