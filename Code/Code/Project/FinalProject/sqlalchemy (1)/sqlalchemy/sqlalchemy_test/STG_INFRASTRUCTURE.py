from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import os
import pandas as pd
from datetime import date

base_dir = os.path.dirname(os.path.realpath(__file__))

connection_string = "sqlite:///"+os.path.join(base_dir,'MRP_DB.db')

Base = declarative_base()

class User(Base):
    __tablename__ = "STG_INFRASTRUCTURE"

    id = Column('Id', Integer, primary_key=True, autoincrement=True)
    company = Column('Company', String)
    location = Column('Location', String)
    Comments = Column('Comments', String)
    hyperlink= Column('Hyperlink', String)
    Load_date = Column('Load_date', String)
    Backend_Table = Column('Backend_Table', String)

engine  = create_engine(connection_string, echo =True)
Base.metadata.create_all(bind=engine)


df = pd.read_csv('E:\Georgian College\MRP\sqlalchemy\inputdata\productionhub1_Rentals1.csv')

df.rename(columns={'CompanyName': 'company', 'Description': 'Comments'},inplace=True)
df['Load_date'] = date.today().strftime("%m/%d/%Y")
df['Backend_Table'] = 'productionhub1_Rentals1'


df.to_sql(con=engine, name=User.__tablename__, if_exists='append',index=False)

