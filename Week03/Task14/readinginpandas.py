import pandas as pd
import sqlite3

# create a connection object
conn = sqlite3.connect('Sample-SQL-File-10rows.db')



# Read the data from the file
# CSV files are comma separated values

df = pd.read_csv('addresses.csv')
print(df)

# Print the first 5 rows of the data
print(df.head())


#reading from a json file
df_json = pd.read_json('example.json')
print(df_json)

# reading from an excel file, use additional library openpyxl
df_excel = pd.read_excel('FinancialSample.xlsx')
print(df_excel)

# reading from a sql database

df = pd.DataFrame({'id': [1, 2, 3, 4, 5], 
'name': ['John', 'Paul', 'George', 'Ringo', 'Pete'], 
'salary': [10000, 20000, 30000, 40000, 50000]
})

# insert data into a database
df.to_sql('user_details', conn, if_exists='replace', index=False)
print(df)

# read data from a database
df = pd.read_sql_query('SELECT * FROM user_details', conn)
print(df)
