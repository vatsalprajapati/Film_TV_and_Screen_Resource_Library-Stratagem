from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import os
import pandas as pd
from datetime import date

base_dir = os.path.dirname(os.path.realpath(__file__))

connection_string = "sqlite:///"+os.path.join(base_dir,'MRP_DB.db')

Base = declarative_base()

class User(Base):
    __tablename__ = "STG_PRODUCTION_UNITS"

    id = Column('Id', Integer, primary_key=True, autoincrement=True)
    Name = Column('Name', String)
    Min_Project_Size = Column('Min_Project_Size', String)
    Location = Column('Location', String)
    Wage= Column('Wage', String)
    Team_size = Column('Team_size', String)
    Description = Column('Description', String)
    Load_date = Column('Load_date', String)
    Backend_Table = Column('Backend_Table', String)

engine  = create_engine(connection_string, echo =True)
Base.metadata.create_all(bind=engine)

# Clutch- Second site scrape
df = pd.read_csv('E:\Georgian College\MRP\sqlalchemy\inputdata\Second Site Scrape.csv')

df.rename(columns={'MinProjectSize': 'Min_Project_Size', 'Team-Size': 'Team_size'},inplace=True)
df.drop(columns = ['Website'],  inplace=True)
df['Description'] = ''
df['Load_date'] = date.today().strftime("%m/%d/%Y")
df['Backend_Table'] = 'Clutch'


# Cion- Third site scrape
df_cion = pd.read_csv('E:\Georgian College\MRP\sqlalchemy\inputdata\Third Site Scrape.csv')

df_cion.rename(columns={'Production House': 'Name'},inplace=True)
df_cion.drop(columns = ['Title', 'Type'],  inplace=True)
df_cion['Min_Project_Size'] = ''
df_cion['Location'] = ''
df_cion['Wage'] = ''
df_cion['Team_size'] = ''
df_cion['Load_date'] = date.today().strftime("%m/%d/%Y")
df_cion['Backend_Table'] = 'Cion'


df.to_sql(con=engine, name=User.__tablename__, if_exists='append',index=False)
df_cion.to_sql(con=engine, name=User.__tablename__, if_exists='append',index=False)

