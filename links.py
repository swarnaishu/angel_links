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
        ['https://angel.co/company/coindcxindia/jobs','Indias top Bitcoin & Cryptocurrency Exchange'],
        ['https://angel.co/company/uptime-1/jobs','Predictive maintenance for building systems'],
        ['https://angel.co/company/village-technologies/jobs','An AI-powered platform to help parents become aware of their childs development'],
        ['https://angel.co/company/datil/jobs','Real Automation for Small Businesses'],
        ['https://angel.co/company/meesho/jobs','Indias Biggest E-Commerce Reseller Network (YC S16)'],
        ['https://angel.co/company/knowdis-data-science/jobs','Machine Learning for E-commerce, Finance and Pharma'],
        ['https://angel.co/company/yelp/jobs','Connecting people with great local businesses'],
        ['https://angel.co/company/act-md/jobs','Act together. Make health happen.'],
        ['https://angel.co/company/akridata/jobs','Edge to Core AI data pipelines'],
        ['https://angel.co/company/marco-29/jobs','A simple way to plan trips with friends'],
        ['https://angel.co/company/doorhopper/jobs','virtual access of city market with same access as offline market'],
        ['https://angel.co/company/twf/jobs','Premium Wheat Flours'],
        ['https://angel.co/company/autosoul/jobs','Automotive Social Media Platform'],
        ['https://angel.co/company/chain-of-demand/jobs','Predictive Analytics for the Fashion Industry'],
        ['https://angel.co/company/warby-parker/jobs','Find the perfect frames at an affordable price'],
        ['https://angel.co/company/hellocore/jobs','Meditation you can feel.'],
        ['https://angel.co/company/greyamp-consulting/jobs','Enabling Digital Transformation for Business'],
        ['https://angel.co/company/eiyamx/jobs','Shipping and Fulfillment for Ecommerce Businesses'],
        ['https://angel.co/company/goshare/jobs','Your Friend With A Truck'],
        ['https://angel.co/company/velotio-technologies/jobs','Software & product engineering partner for startups & enterprises'],
        ['https://angel.co/company/patch-d/jobs','Predictive Diagnostics to solve the problem of sepsis in the at home patient'],
        ['https://angel.co/company/promptcloud/jobs','Web scraping service provider, catering to the big data requirements of enterprises'],
        ['https://angel.co/company/adaptilab/jobs','B2B SaaS to help companies grow machine learning teams from hiring to productivity'],
        ['https://angel.co/company/socialcore-1/jobs','A.I. powered video analytics platform'],
        ['https://angel.co/company/biotrillion/jobs',"Data from Life. Data for Life.”],
        ['https://angel.co/company/awiros/jobs','Video Intelligence']
        ['https://angel.co/company/xten-av/jobs','Worlds First AV Design Platform head quartered in Silicon valley california'],
        ['https://angel.co/company/gridle/jobs','A family of Engineers, Designers and Product folks building Superior Digital Experiences!'],
        ['https://angel.co/company/accrualify/jobs','spend management system'],
        ['https://angel.co/company/catchafire-1/jobs','Skills-based volunteer marketplace'],
        ['https://angel.co/company/relimetrics/jobs','Industry 4.0 software for smart quality audit in manufacturing and assembly'],
        ['https://angel.co/company/enlitic/jobs','Enlitic uses deep learning to make doctors faster and more accurate'],
        ['https://angel.co/company/lentil-ai/jobs','AI and Productivity'],
        ['https://angel.co/company/billin-1/jobs','Mobile First Bill Management Service'],
        ['https://angel.co/company/vida/jobs','Eradicating chronic disease'],
        ['https://angel.co/company/maritime-data-systems/jobs','MDS builds maritime online Startups'],
        ['https://angel.co/company/musixmatch/jobs','The Music AI Platform featuring the worlds Largest Lyrics DB'],
        ['https://angel.co/company/piktochart/jobs','Stories from Data. Infographics Creator.'],
        ['https://angel.co/company/summit-securities-group-1/jobs','Tech, math, and trading - start-up ethos meets Wall Street.'],
        ['https://angel.co/company/stream/jobs','Stream is an API for building and scaling activity feeds and chat'],
        ['https://angel.co/company/bison/jobs','Changing how you see private equity'],
        ['https://angel.co/company/opsani/jobs','Continuous Optimization for Cloud-based apps'],
        ['https://angel.co/company/pitstop/jobs','Predictive Maintenance for Automotive '],
        ['https://angel.co/company/cruise-automation/jobs','AI enable agri-food quality assessment'],
        ['https://angel.co/company/imagoai/jobs','I enable agri-food quality assessment'],
        ['https://angel.co/company/purestake/jobs','Secure and Reliable Blockchain Infrastructure-as-a-Service'],
        ['https://angel.co/company/ocrolus/jobs','https://angel.co/company/ocrolus/jobs'],
        ['https://angel.co/company/apostrophe/jobs','Dermatology Crafted to You and Delivered to Your Door'],
        ['https://angel.co/company/shipthis-1/jobs','Technology based International Freight Forwarder and Customs Broker']
        ]
    
insert(links)