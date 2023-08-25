from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import os

base_dir = os.path.dirname(os.path.realpath(__file__))

connection_string = "sqlite:///"+os.path.join(base_dir,'MRP_DB.db')
Base = declarative_base()

class User(Base):
    __tablename__ = "DGCv6"

    id = Column('id', Integer, primary_key=True)
    Name = Column('Name', String, unique=True)
    Email = Column('Email', String)
    Availability = Column('Availability', String)
    hyperlink = Column('Hyperlink', String)

    #  Excluded variables >>>  Currently Working


#engine  = create_engine('sqlite:///:memory:', echo =True)
engine  = create_engine(connection_string, echo =True)
Base.metadata.create_all(bind=engine)



