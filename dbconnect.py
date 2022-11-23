import pyodbc
import pandas as pd
import numpy as np
from fpdf import FPDF

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


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




alternating_colors = [['white'] * len(df.columns), ['lightgray'] * len(df.columns)] * len(df)
alternating_colors = alternating_colors[:len(df)]

#https://stackoverflow.com/questions/32137396/how-do-i-plot-only-a-table-in-matplotlib
fig, ax =plt.subplots(figsize=(12,4))
ax.axis('tight')
ax.axis('off')
the_table = ax.table(cellText=df.values,rowLabels=df.index,colLabels=df.columns,rowColours=['lightblue']*len(df),
                        colColours=['lightblue']*len(df.columns),
                        cellColours=alternating_colors,loc='center')


#https://stackoverflow.com/questions/4042192/reduce-left-and-right-margins-in-matplotlib-plot
pp = PdfPages("report.pdf")
pp.savefig(fig, bbox_inches='tight')
pp.close()

#print(df.values)
#print (df.columns)
#print(type(df1))

