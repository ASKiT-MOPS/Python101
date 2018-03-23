lista = ["Polak", "Rosjanin", "Niemiec"]
if 2+2==5:
	print ("tego raczej nie wydrukujemy")
elif 2+2==4:
	print ("")
def wypelnij_liste(lista):
	lista = ["czyzby","kotek","zginal"]
	print("lista wewnątrz")
	print (lista)
lista = ["ala","ma","kotka"]
wypelnij_liste(lista)
print (lista) 

#!/usr/bin/env python
# Powyzej standardowy poczatek skryptów w Pythonie w systemach typu Unix
# definiujemy klase ̨ Kwadrat:
class Kwadrat:
  bok = 0  
# do tego metode ̨ podajaca wartosc boku
  def podaj_bok(self):
    return self.bok
  def podaj_pole(self):
    return self.bok ** 2
class Szescian(Kwadrat):
  def podaj_pole(self):
    return Kwadrat.podaj_pole(self) * 6
kw = Kwadrat()
sz = Szescian()
kw.bok = sz.bok = 10
print (kw.podaj_bok())
print(kw.podaj_pole())
print("teraz sześcian")
print (sz.podaj_bok())
print (sz.podaj_pole())