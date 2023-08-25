from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import os
import pandas as pd
from datetime import date

base_dir = os.path.dirname(os.path.realpath(__file__))

connection_string = "sqlite:///"+os.path.join(base_dir,'MRP_DB.db')

Base = declarative_base()

class User(Base):
    __tablename__ = "STG_UNION"

    id = Column('Id', Integer, primary_key=True, autoincrement=True)
    Union = Column('Union', String)
    Craft_Name = Column('Craft_Name', String)
    Location = Column('Location', String)
    Telephone= Column('Telephone', String)
    Fax = Column('Fax', String)
    Load_date = Column('Load_date', String)
    Backend_Table = Column('Backend_Table', String)

engine  = create_engine(connection_string, echo =True)
Base.metadata.create_all(bind=engine)


df = pd.read_csv('E:\Georgian College\MRP\sqlalchemy\inputdata\First Site Scrape.csv')

df.rename(columns={'UnionName': 'Union', 'Craftname': 'Craft_Name', 'Jurisdication': 'Location', 'Phone': 'Telephone' },inplace=True)
df.drop(columns = ['Website'],  inplace=True)
df['Load_date'] = date.today().strftime("%m/%d/%Y")
df['Backend_Table'] = 'Labor Unions'


df.to_sql(con=engine, name=User.__tablename__, if_exists='append',index=False)

