from flask import flash, current_app, url_for
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric, Boolean
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql import func

import datetime

from database import Base, Member, Gallery
import database as db
import images

class Painting(Base):

    """Represents an item object"""

    __tablename__ = 'painting'

    paintingId = Column(Integer, primary_key=True)
    title = Column(String(60), nullable=False)
    description = Column(String(500), nullable=True)
    galleryId = Column(Integer, ForeignKey('gallery.galleryId'))
    gallery = relationship(Gallery)
    paintingDate = Column(Date)
    memberId = Column(String(60), ForeignKey('member.email'))
    member = relationship(Member)
    image = Column(String(), nullable=True)
    medium = Column(String(), nullable=True)
    height = Column(Numeric(), nullable=True)
    width = Column(Numeric(), nullable=True)
    sold = Column(Boolean(), nullable=False)
    price = Column(Numeric(), nullable=True)



    # def __init__(self, name='', description='', category=None, user=None,
    #              image='default.jpg'):
    #     self.title = name
    #     self.description = description
    #     self.gallery = category
    #     self.member = user
    #     self.image = image



    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'paintingId': str(self.paintingId),
            'title': self.title,
            'description': self.description,
            'galleryId': str(self.galleryId),
            'paintingDate': self.paintingDate.strftime("%B %Y"),
            # 'memberId': self.memberId,
            'image': url_for('static', filename="img/%s" % self.image),
            'medium': self.medium,
            'height': str(self.height),
            'width': str(self.width),
            'sold': str(self.sold),
            'price': str(self.price),
        }


    # @staticmethod
    # def validParams(params, image):
    #     if params['name'] == '':
    #         flash('You entered an invalid value for the name field')
    #         return False

    #     if not images.validName(image.filename.lower()):
    #         flash('You selected an invalid picture to upload')
    #         return False
    #     return True



    # @staticmethod
    # def save(item, params, image, userId):
    #     if Item.validParams(params, image):
    #         item.name = params['name']
    #         # item.categoryId = int(params['category'])
    #         item.category = db.getOne(Category, "id", params['category'])
    #         item.description = params['description'].strip()
    #         # item.userId = userId
    #         item.user = db.getOne(User, "email", userId)

    #         db.session.add(item)
    #         db.session.flush()

    #         url = images.save(image, item)
    #         if url:
    #             item.image = url

    #         db.session.commit()
    #         flash("%s has been saved" % item.name)
    #         return True
    #     return False


    # @staticmethod
    # def delete(item):
    #     try:
    #         images.delete(item.image)
    #         db.session.delete(item)
    #         db.session.commit()
    #         flash('Item %s has been deleted' % item.name)
    #         return True
    #     except:
    #         flash('An error occured and Item %s not deleted. Please try again' % item.name)
    #         return False