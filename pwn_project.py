file = open("dane.txt", "r") #otwiera w trybie do odczytu

#oblicz liczbę studentów / count number of students
count = 0
for line in file:
    count += 1
print("Studentów jest " + str(count) + ".")

#imiona i miasta studentów / all names and cities
file.seek(0) #powrót do początku pliku
print("Imiona i miasta studetów:")
for line in file:
    lista = line.strip().split(";")
    print(lista[0], lista[2])

#ilu studentów jest w Warszawie, Szczecinie, Bydgoszczy / number of students in Warsaw, Szczecin and Bydgoszcz
file.seek(0)
slownik = {"Warszawa":0, "Szczecin":0, "Bydgoszcz":0}
for line in file:
    lista = line.strip().split(";")
    if (lista[2] in slownik):
        miasto = lista[2]
        ile = slownik[miasto]
        ile += 1
        slownik[miasto] = ile
print(slownik)  #na warsztatach
print("W Warszawie jest " + str(slownik["Warszawa"]) + " studentów, w Szczecinie " \
+ str(slownik["Szczecin"]) + " a w Bydgoszczy " + str(slownik["Bydgoszcz"]) + ".") #moje rozwiazanie

#z jakich miast pochodzą studenci / cities
file.seek(0)
zbior = set() #zbiór ma niepowtarzalne wartosci
for line in file:
    lista = line.strip().split(";")
    miasto = lista[2]
    zbior.add(miasto)
print(zbior) #na warsztatach
print("Miasta z których pochodzą studenci to: " + ", ".join(zbior) + ".")  #moje rozwiązanie

#samodzielnie wykonane zadania / additional tasks performed independently
# średnia w poszczególnych miastach / average grade for each city
file.seek(0)
print("Miasto i suma ocen:") #cities and grades totalled up
dict = {'Katowice':0, 'Szczecin':0, 'Warszawa':0, 'Bydgoszcz':0, 'Pozna�': 0, '��d�':0, 'Krak�w':0, 'Wroc�aw':0, 'Gda�sk': 0}
for line in file:
    lista = line.strip().split(";")
    if (lista[2] in dict):
        miasto = lista[2]
        suma = dict[miasto]
        suma += float(lista[1])
        dict[miasto] = suma
print(dict)

file.seek(0) #liczba studentow z kazdego miasta tym razem / cities and their number of students
print("Miasto i liczba studentow:")
slownik_2 = {'Katowice':0, 'Szczecin':0, 'Warszawa':0, 'Bydgoszcz':0, 'Pozna�': 0, '��d�':0, 'Krak�w':0, 'Wroc�aw':0, 'Gda�sk': 0}
for line in file:
    lista = line.strip().split(";")
    if (lista[2] in slownik_2):
        miasto = lista[2]
        ile = slownik_2[miasto]
        ile += 1
        slownik_2[miasto] = ile
print(slownik_2)

new_dict = {} #średnia ocen w poszczegolnych miastach / final calculation of average grade
for city in dict:
    new_dict[city] = dict[city] / slownik_2[city]
print("Miasto i jego średnia ocen: ", new_dict)

print("Miasta i średnia od najmniejszej do największej średniej:", sorted(new_dict.items(), key=lambda x:x[1])) #uporzadkowanie wynikow miasto i srednia wg sredniej
#cities and their average grade sorted out from the smallest to the biggest result

print("Miasta w ktrych średnia jest najwyższa to:") #cities with the highest average grade
print(list(sorted(new_dict.items(), key=lambda x:x[1]))[-1])
print(list(sorted(new_dict.items(), key=lambda x:x[1]))[-2])
print(list(sorted(new_dict.items(), key=lambda x:x[1]))[-3])

#studenci ze średnią wyższą od ogolnej / students with grades above average
suma_srednich_miast = 0
for city in new_dict:
    suma_srednich_miast += float(new_dict[city])
print("To suma ocen miast: ", suma_srednich_miast) #suma ocen miast

srednia_miast = suma_srednich_miast / len(zbior)
print("To liczba miast: ", len(zbior)) #number of cities
print("To srednia ocen ze wszystkich miast: ", srednia_miast) #srednia ocen miast / average grade for each city

file.seek(0)
print("Studenci ze średnią wyższą od ogólnej:") #students above average
for line in file:
    lista = line.strip().split(";")
    student = lista[0]
    ocena_st = lista[1]
    if float(ocena_st) > float(srednia_miast):
        print(student)
#najlepsi studenci z kazdego miasta / the best students from each city (1 example, even when more students have the same result)
#uwaga - czasem takie same wyniki ma wiecej osob najlepszych, ale w zadaniu prosba tylko o jednego studenta wiec podaje jednego
file.seek(0)
dict_wwa = {} #wwa
for line in file:
    lista = line.strip().split(";")
    if lista[2] == "Warszawa":
      dict_wwa[lista[0]]=lista[1]
print(dict_wwa)

print(sorted(dict_wwa.items(), key=lambda x:x[1])[-1])
print("W Warszawie najwyższą średnią ma: ", sorted(dict_wwa.items(), key=lambda x:x[1])[-1]) #the best student in Warsaw is...

file.seek(0)
dict_kato = {} #katowice
for line in file:
    lista = line.strip().split(";")
    if lista[2] == "Katowice":
      dict_kato[lista[0]]=lista[1]
print(dict_kato)

print("W Katowicach najwyższą średnią ma: ", sorted(dict_kato.items(), key=lambda x:x[1])[-1])


file.seek(0)
dict_krk = {} #krakow
for line in file:
    lista = line.strip().split(";")
    if lista[2] == "Krak�w":
      dict_krk[lista[0]]=lista[1]
print(dict_krk)

print("W Krakowie najwyższą średnią ma: ", sorted(dict_krk.items(), key=lambda x:x[1])[-1])

file.seek(0)
dict_gd = {} #gdansk
for line in file:
    lista = line.strip().split(";")
    if lista[2] == "Gda�sk":
      dict_gd[lista[0]]=lista[1]
print(dict_gd)

print("W Gdańsku najwyższą średnią ma: ", sorted(dict_gd.items(), key=lambda x:x[1])[-1])

file.seek(0)
dict_ld = {} #chyba lodz
for line in file:
    lista = line.strip().split(";")
    if lista[2] == "��d�":
      dict_ld[lista[0]]=lista[1]
print(dict_ld)

print("W Łodzi najwyższą średnią ma: ", sorted(dict_ld.items(), key=lambda x:x[1])[-1])

file.seek(0)
dict_bd = {} #Bydgoszcz
for line in file:
    lista = line.strip().split(";")
    if lista[2] == "Bydgoszcz":
      dict_bd[lista[0]]=lista[1]
print(dict_bd)

print("W Bydgoszczy najwyższą średnią ma: ", sorted(dict_bd.items(), key=lambda x:x[1])[-1])

file.seek(0)
dict_sz = {} #Szczecin
for line in file:
    lista = line.strip().split(";")
    if lista[2] == "Szczecin":
      dict_sz[lista[0]]=lista[1]
print(dict_sz)

print("W Szczecinie najwyższą średnią ma: ", sorted(dict_sz.items(), key=lambda x:x[1])[-1])

file.seek(0)
dict_wr = {} #Wrocław
for line in file:
    lista = line.strip().split(";")
    if lista[2] == "Wroc�aw":
      dict_wr[lista[0]]=lista[1]
print(dict_wr)

print("We Wrocławiu najwyższą średnią ma: ", sorted(dict_wr.items(), key=lambda x:x[1])[-1])

file.seek(0)
dict_pn = {} #Poznań
for line in file:
    lista = line.strip().split(";")
    if lista[2] == "Pozna�":
      dict_pn[lista[0]]=lista[1]
print(dict_pn)

print("We Wrocławiu najwyższą średnią ma: ", sorted(dict_pn.items(), key=lambda x:x[1])[-1])

file.close()
