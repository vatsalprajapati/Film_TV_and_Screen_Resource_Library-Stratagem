from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import os
import pandas as pd
from datetime import date

base_dir = os.path.dirname(os.path.realpath(__file__))

connection_string = "sqlite:///"+os.path.join(base_dir,'MRP_DB.db')

Base = declarative_base()

class User(Base):
    __tablename__ = "STG_LINKS_TO_PDF"

    id = Column('Id', Integer, primary_key=True, autoincrement=True)
    Title = Column('Title', String)
    Description = Column('Description', String)
    LinkToPdf = Column('LinkToPdf', String)
    Load_date = Column('Load_date', String)
    Backend_Table = Column('Backend_Table', String)

engine  = create_engine(connection_string, echo =True)
Base.metadata.create_all(bind=engine)

# Fourth Site Scrape *** cmpa
df = pd.read_csv('E:\Georgian College\MRP\sqlalchemy\inputdata\Fourth Site Scrape.csv')

df.rename(columns={'Pdf Link': 'LinkToPdf'},inplace=True)
df['Load_date'] = date.today().strftime("%m/%d/%Y")
df['Title'] = df['Title'].str.replace("�", "")
df['Description'] = df['Description'].str.replace("�", "")
df['Backend_Table'] = 'cmpa'

# Site5 *** OntarioCreates
df_OC = pd.read_csv('E:\Georgian College\MRP\sqlalchemy\inputdata\Site5.csv')

df_OC.rename(columns={'PDFLink': 'LinkToPdf','PDF Keyword': 'Description'},inplace=True)
df_OC['Title'] = df_OC['Title'].str.replace("�", "")
df_OC['Description'] = df_OC['Description'].str.replace("�", "")
df_OC['Load_date'] = date.today().strftime("%m/%d/%Y")
df_OC['Backend_Table'] = 'OntarioCreates'

# Site 6 *** StatisticsCanada
df_SC = pd.read_csv('E:\Georgian College\MRP\sqlalchemy\inputdata\Site 6.csv')

df_SC.rename(columns={'link': 'LinkToPdf'},inplace=True)
df_SC['Title'] = df_SC['Title'].str.replace("�", "")
df_SC['Description'] = df_SC['Description'].str.replace("�", "")
df_SC['Load_date'] = date.today().strftime("%m/%d/%Y")
df_SC['Backend_Table'] = 'StatisticsCanada'



df.to_sql(con=engine, name=User.__tablename__, if_exists='append',index=False)
df_OC.to_sql(con=engine, name=User.__tablename__, if_exists='append',index=False)
df_SC.to_sql(con=engine, name=User.__tablename__, if_exists='append',index=False)

