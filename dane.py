import sqlite3
#   https://git-scm.com/book/pl/v2
#   http://python101.readthedocs.io/pl/latest/env/index.html#

conn = sqlite3.connect("D:\ASKiT\DataBase\Komputery.db")
c = conn.cursor()
#c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
#c.execute("INSERT INTO stocks VALUES ('2006-02-05','BUY','RHAT',100,35.14)")

# Never do this -- insecure!
symbol = 'RHAT'
c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

# Do this instead
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchone())
print()
# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
#c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
for row in c.execute('SELECT * FROM Komputery ORDER BY IP'):
#   print(row)
    print(row[0], row[1], row[3], row[5])

for row in c.execute('SELECT * FROM Awarie ORDER BY 1'):
    print(row)
    print(row[0], row[1], row[3], row[5])

#c.execute("SELECT * FROM Komputery ORDER BY IP")
#print(c.fetchone())

#for row in cursor:
 #  print()

conn.commit()
conn.close()
##https://kivy.org/#download
##http://www.stuartellis.name/articles/python-development-windows/
## http://zetcode.com/db/sqlitepythontutorial/
###    https://www.tutorialspoint.com/sqlite/sqlite_python.htm
#### https://www.pythoncentral.io/introduction-to-sqlite-in-python/
#####   http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
####### http://www.sqlitetutorial.net/sqlite-python/
#####http://www.cosc.canterbury.ac.nz/greg.ewing/python_gui/
### https://www.wykop.pl/link/4210575/jak-sie-uczyc-pythona-mirek-radzi-edycja-2018/