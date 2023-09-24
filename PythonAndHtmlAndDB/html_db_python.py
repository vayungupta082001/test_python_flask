# import os
import pandas as pd
import mysql.connector

# Database
mydb = mysql.connector.connect(
    host="sql12.freesqldatabase.com",
    user="sql12648490",
    password="IRvMwntPKw",
    port=3306,
    database="sql12648490"
)

# Get Data
sqlScript = "select * from user_login"
cursor=mydb.cursor()
cursor.execute(sqlScript)
results=cursor.fetchall()
# print (results)

# do something
df=pd.DataFrame()
for x in results:
    df2=pd.DataFrame(list(x)).T
    df=pd.concat([df, df2])

df.to_html("PythonAndHtmlAndDB/templates/index.html")