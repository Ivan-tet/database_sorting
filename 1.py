import pyodbc

lis = [...]


conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\48575\Desktop\zadanie 5\orders1.accdb;')

                    
cursor = conn.cursor()
cursor.execute('select * from Orders')

for row in cursor.fetchall():
        for i in lis:
                if row[1] == i:
                    print(row[2])
