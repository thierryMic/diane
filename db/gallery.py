from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, sessionmaker
from database import Base


class Gallery(Base):
    __tablename__ = 'gallery'

    galleryId = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    image = Column(String(60), nullable=False)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.galleryId,
            'name': self.name,
            'image': self.image,
        }
