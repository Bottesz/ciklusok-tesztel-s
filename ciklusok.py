# bizonyos muveletek ismetlesere valo
# ciklus valtozo - szamlalja hogy hanyszor futott le a ciklus
# ciklus mag - ismetlendo utasitasok
# cilusfeltel - itt adjuk hogy meddig fusson a ciklus
def szamlalos_ciklus1():
    cv:int = 1

    while (cv <= 10):
        print(f" {cv} Többé nem kések mert lemaradok fontos információkról!")
        cv += 1

    print( cv, "A ciklus után")

"""
def elolteszteos_ciklus():
## kerjunk be egy szamot 10-nal nagyobbszamt a felhasznalotol
szam:int = int(input("Adjon meg egy 10-nél nagyobb számot! "))
while szam < 10:
    print("10nél nagyobb számot")
    szam:int = int(input("Adjon meg egy 10-nél nagyobb számot! "))

print("Hurrá végre sikerült egy 10 nagyobb számot megadni")


# készíts külön eljárást
#1. ird ki a számokat 1 - 10 a képernyőre egymás mellé
#2. ird ki a számokat 20 - 30 a képernyőre egymás
#3. ird ki a 15 - 25 közötti páros számokat
#4. ird ki  a számokat egyesével 12 - 30 között fordított sorrendbe

print("valami", end=", ")
print("vége")
"""


#1 feladat
szamkiiras:int = 1

while (szamkiiras <=10):
    print(f"{szamkiiras}",end=", ")
    szamkiiras += 1
print("\n")



#2.feladat
szamkiiras:int = 20

while (szamkiiras <=30):
    print(f"{szamkiiras}",end=", ")
    szamkiiras += 1
print("\n")


#3.feladat
szamkiiras:int = 15
while (szamkiiras <=25):
    if szamkiiras % 2 == 0:
        print(f"{szamkiiras}", end=", ")
    szamkiiras += 2
print("\n")



#4.feladat
szamkiiras:int = 30
while (szamkiiras>= 12):
    print(f"{szamkiiras}", end=", ")
    szamkiiras -= 1
print("\n")
