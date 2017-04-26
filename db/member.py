from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, sessionmaker
from database import Base
import database as db

class Member(Base):
    __tablename__ = 'member'

    email = Column(String(60), primary_key=True)
    name = Column(String(250), nullable=False)
    image = Column(String(250), nullable=True)
    usergroup = Column(String(10), nullable=False)



    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.email,
            'name': self.name,
            'image': self.image
        }


    @staticmethod
    def save(user):
        try:
            db.session.add(user)
            db.session.commit()
            return True
        except:
            return False

