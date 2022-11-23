import pyodbc
import pandas as pd
import numpy as np

conn1 = pyodbc.connect('Driver={SQL Server};'
                      'Server=brgmes02;'
                      'Database=iqs;'
                      'Trusted_Connection=yes;')

df1 = pd.read_sql_query('SELECT * FROM iqs.container', conn1)

conn2 = pyodbc.connect('Driver={SQL Server};'
                      'Server=blvmes02;'
                      'Database=iqs;'
                      'Trusted_Connection=yes;')

df2 = pd.read_sql_query('SELECT * FROM iqs.container', conn2)

df1=df1.append(df2)

print(df1)
print(type(df1))

