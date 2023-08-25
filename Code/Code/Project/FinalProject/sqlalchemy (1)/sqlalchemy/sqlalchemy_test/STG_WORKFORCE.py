from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import os
import pandas as pd
from datetime import date

base_dir = os.path.dirname(os.path.realpath(__file__))

connection_string = "sqlite:///"+os.path.join(base_dir,'MRP_DB.db')
Base = declarative_base()

class User(Base):
    __tablename__ = "STG_WORKFORCE"

    Id = Column('Id', Integer, primary_key=True,autoincrement=True)
    Title = Column('Title', String)
    Name = Column('Name', String)
    Location = Column('Location', String)
    Telephone = Column('Telephone', String)
    Email = Column('Email', String)
    Currertly_Working = Column('Currertly_Working', String)
    Availability = Column('Availability', String)
    # Comments = Column('Comments', String)
    Load_date = Column('Load_date', String)
    Backend_Table = Column('Backend_Table', String)


engine  = create_engine(connection_string, echo =True)
Base.metadata.create_all(bind=engine)


df_dgcv = pd.read_csv('E:\Georgian College\MRP\sqlalchemy\inputdata\DGCv6.csv')
df_dgcv.rename(columns = {'Contact':'Telephone','Availibility': 'Availability', 'Currently Working':'Currertly_Working'},inplace=True)
df_dgcv['Location'] = ''
df_dgcv['Load_date'] = date.today().strftime("%m/%d/%Y")
df_dgcv['Backend_Table'] = 'DGCv6'
new_col_lst = ['Title', 'Name', 'Location', 'Telephone', 'Email', 'Currertly_Working', 'Availability',  'Load_date', 'Backend_Table']
df_dgcv = df_dgcv[new_col_lst]


df_dgcv.to_sql(con=engine, name=User.__tablename__, if_exists='append',index=False)





