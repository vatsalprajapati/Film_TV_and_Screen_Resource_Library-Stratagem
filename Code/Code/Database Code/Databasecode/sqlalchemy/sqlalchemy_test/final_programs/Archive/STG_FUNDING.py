from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import os
import pandas as pd
from datetime import date

base_dir = os.path.dirname(os.path.realpath(__file__))

connection_string = "sqlite:///"+os.path.join(base_dir,'MRP_DB.db')
Base = declarative_base()

class User(Base):
    __tablename__ = "STG_FUNDING"

    Id = Column('Id', Integer, primary_key=True, autoincrement=True)
    Project = Column('Project', String)
    Company = Column('Company', String)
    Year = Column('Year', String)
    Content_Type = Column('Content_Type', String)
    Fund = Column('Fund', String)
    Activity = Column('Activity', String)
    Genre = Column('Genre', String)
    Delivery_Method = Column('Delivery_Method', String)
    Region = Column('Region', String)
    Program = Column('Program', String)
    Status = Column('Status',String)
    Language = Column('Language', String)
    Load_date = Column('Load_date', String)
    Backend_Table = Column('Backend_Table', String)



engine  = create_engine(connection_string, echo =True)
Base.metadata.create_all(bind=engine)


df = pd.read_csv('E:\Georgian College\MRP\sqlalchemy\inputdata\canadamediafund.csv')


df.drop(columns = ['Broadcaster', 'Round', 'Selection Round'],  inplace=True)
df.rename(columns={'Commitment': 'Fund', 'Delivery Method': 'Delivery_Method'},inplace=True)
df['Load_date'] = date.today().strftime("%m/%d/%Y")
df['Backend_Table'] = 'canadamediafund'


df.to_sql(con=engine, name=User.__tablename__, if_exists='append',index=False)



