import pyodbc
import pandas as pd
import numpy as np

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=blvmes22;'
                      'Database=iqs;'
                      'Trusted_Connection=yes;')

df = pd.read_sql_query('SELECT * FROM iqs.container', conn)

print(df)
print(type(df))

#cursor = conn.cursor()
#cursor.execute('SELECT * FROM iqs.container')

#for i in cursor:
#    print(i)