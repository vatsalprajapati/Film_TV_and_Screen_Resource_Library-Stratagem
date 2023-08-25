from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import os

base_dir = os.path.dirname(os.path.realpath(__file__))

connection_string = "sqlite:///"+os.path.join(base_dir,'MRP_DB.db')
Base = declarative_base()

class User(Base):
    __tablename__ = "Workopolis"

    id = Column('id', Integer, primary_key=True)
    CompanyName = Column('CompanyName', String, unique=True)
    Designation = Column('Designation', String, nullable=False)
    Location = Column('Location',String)
    Description = Column('Description', String)
    Salary = Column('Salary', String)
    hyperlink = Column('Hyperlink', String)

    #  Excluded variables >>>

engine  = create_engine('sqlite:///:memory:', echo =True)
Base.metadata.create_all(bind=engine)



