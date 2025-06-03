# Ecrivez votre code ici !
nombres = input("Saisissez une liste de nombres séparés par des virgules : ")
liste = nombres.split(',')

liste_entiers = []
for n in liste:   
    nombre_entier = int(n)
    liste_entiers.append(nombre_entier)

somme = 0
for n in liste_entiers:
   somme += n 
print(somme)

moyenne = somme / len(liste_entiers)
print(moyenne)

nombre_au_dessus_moyenne = 0
for n in liste_entiers:
    if n > moyenne:
       nombre_au_dessus_moyenne += 1
print(nombre_au_dessus_moyenne)