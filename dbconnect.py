import pyodbc
import pandas as pd
import numpy as np


#define a dict
dict1=dict({'Site':['Ballyragget', 'Belview','Drogheda','Ballitore','Wexford','loughegish','Virginia','Gooding'], 'No of Containers':[0,0,0,0,0,0,0,0]})
#create a dataframe from dict
df=pd.DataFrame.from_dict(dict1).set_index('Site')


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=brgmes02;'
                      'Database=iqs;'
                      'Trusted_Connection=yes;')


df1=pd.read_sql_query('SELECT count(*) FROM iqs.container', conn)
df.loc['Ballyragget']=df1.loc[0].values


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=blvmes02;'
                      'Database=iqs;'
                      'Trusted_Connection=yes;')

df1=pd.read_sql_query('SELECT count(*) FROM iqs.container', conn)
df.loc['Belview']=df1.loc[0].values


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=drgmes02;'
                      'Database=iqs;'
                      'Trusted_Connection=yes;')

df1=pd.read_sql_query('SELECT count(*) FROM iqs.container', conn)
df.loc['Drogheda']=df1.loc[0].values

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=bltmes02;'
                      'Database=iqs;'
                      'Trusted_Connection=yes;')

df1=pd.read_sql_query('SELECT count(*) FROM iqs.container', conn)
df.loc['Ballitore']=df1.loc[0].values

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=wxcmes02;'
                      'Database=iqs;'
                      'Trusted_Connection=yes;')

df1=pd.read_sql_query('SELECT count(*) FROM iqs.container', conn)
df.loc['Wexford']=df1.loc[0].values

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=mgnmes02;'
                      'Database=iqs;'
                      'Trusted_Connection=yes;')

df1=pd.read_sql_query('SELECT count(*) FROM iqs.container', conn)
df.loc['loughegish']=df1.loc[0].values

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=virmes02;'
                      'Database=iqs;'
                      'Trusted_Connection=yes;')

df1=pd.read_sql_query('SELECT count(*) FROM iqs.container', conn)
df.loc['Virginia']=df1.loc[0].values

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=gdpmes12;'
                      'Database=iqs;'
                      'Trusted_Connection=yes;')

df1=pd.read_sql_query('SELECT count(*) FROM iqs.container', conn)
df.loc['Gooding']=df1.loc[0].values


print(df)
#print(type(df1))

