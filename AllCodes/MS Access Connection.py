import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\db.accdb;')
cursor = conn.cursor()
cursor.execute('SELECT * FROM [as]')
   
for row in cursor.fetchall():
    print(row)