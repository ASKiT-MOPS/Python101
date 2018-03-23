import sqlite3
conn = sqlite3.connect("D:\ASKiT\DataBase\Komputery.db")
c = conn.cursor()
#c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
#c.execute("INSERT INTO stocks VALUES ('2006-02-05','BUY','RHAT',100,35.14)")
c.execute("SELECT * FROM Komputery")	
print(c.fetchone())		 
			 
conn.commit()
conn.close()
			 
plik = 0
try:
  try:
    plik = open("pliki.py",'r')
    for count in range (50):
      s = plik.readline()
      print (count+1,s)
  finally:
    if plik:
      plik.close()
except:
  print("zz")
  print ("Nastapił bład podczas czytania pliku")
    # ostatnia linia    