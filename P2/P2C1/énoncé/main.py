# Ecrivez votre code ici !
nombre1 = input("Donnez un premier nombre")
nombre2 = input("Donnez un deuxième nombre")

if nombre1.isnumeric() and nombre2.isnumeric():
    nombre2 = int(nombre2) 
    nombre1 = int(nombre1)
else:
    raise SystemExit("Fin du programme")

operation = input("Quelle opération voulez-vous effectuer ? (+, -, *, /)")
if operation == "+":
    resultat = nombre1 + nombre2
elif operation == "-":
    resultat = nombre1 - nombre2
elif operation == "*":
    resultat = nombre1 * nombre2
elif operation == "/": 
    if nombre2 == 0:
        raise SystemExit("Erreur: impossible de diviser par zéro")
    resultat = round(nombre1 / nombre2)

print(f"Le résultat est {resultat}")