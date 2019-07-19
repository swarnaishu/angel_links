from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///table.db',echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Angel(Base):
    __tablename__='angel'

    id = Column(Integer, primary_key=True)
    links = Column(String)
    description = Column(String)
    
    def __init__(self,links, description):
        self.links = links
        self.description = description

    def dic(self):
        return {
            'id': self.id,
            'links': self.links,
            'description': self.description
        }
    
    def save_to_db(self):
        session.add(self)
        session.commit()

    def remove(self):
        session.delete(self)
        session.commit()
    


Base.metadata.create_all(engine)

def insert(data):
    for link in data:
        obj = Angel(links=link[0],description=link[1])
        obj.save_to_db()

links=[
        ['https://angel.co/company/nextorbit-1/jobs','Intelligent demand planning & adaptive pricing'],

        ]
    
insert(links)