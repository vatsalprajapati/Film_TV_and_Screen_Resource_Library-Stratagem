from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import os
import pandas as pd

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
    Salary = Column('Salary', String)
    Availability = Column('Availability', String)
    Comments = Column('Comments', String)
    HyperLink = Column('HyperLink', String)
    Backend_Table = Column('Backend_Table', String)


engine  = create_engine(connection_string, echo =True)
Base.metadata.create_all(bind=engine)


df = pd.read_csv('E:\Georgian College\MRP\sqlalchemy\inputdata\workopolis.csv')
df.rename(columns = {'Role':'Title', 'Company':'Name', 'Description':'Comments'},inplace=True)
df['hyperlink'] = 'Change your code- remove this line'
df['Backend_Table'] = 'workopolis'
df['Email'] = ''
df['Telephone'] = ''
df['Availability'] = ''
new_col_lst = ['Title', 'Name', 'Location', 'Telephone', 'Email', 'Salary', 'Availability', 'Comments', 'hyperlink', 'Backend_Table']
df = df[new_col_lst]



df_dgcv = pd.read_csv('E:\Georgian College\MRP\sqlalchemy\inputdata\DGCv6.csv')
df_dgcv.rename(columns = {'Contact':'Telephone','Availibility': 'Availability'},inplace=True)
df_dgcv['Location'] = ''
df_dgcv['Salary'] = ''
df_dgcv['Comments'] = ''
df_dgcv['hyperlink'] = 'Change your code- remove this line'
df_dgcv['Backend_Table'] = 'DGCv6'
df_dgcv = df_dgcv[new_col_lst]


df.to_sql(con=engine, name=User.__tablename__, if_exists='append',index=False)
df_dgcv.to_sql(con=engine, name=User.__tablename__, if_exists='append',index=False)





