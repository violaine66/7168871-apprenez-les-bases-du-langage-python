# Ecrivez votre code ici
def salaire_mensuel(salaire_annuel):
   salaire_mensuel = salaire_annuel / 12
   return salaire_mensuel

def salaire_hebdomadaire(salaire_mensuel):
    salaire_hebdomadaire = salaire_mensuel / 4
    return salaire_hebdomadaire

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    salaire_horaire = salaire_hebdomadaire / heures_travaillees
    return salaire_horaire

salaire_annuel_string=input("Saisissez votre salaire annuel : ")
salaire_annuel = float(salaire_annuel_string)
heures_travaillees_string=input("Saisissez le nombre d'heures travaillées par semaine : ")
heures_travaillees = float(heures_travaillees_string)

mensuel = salaire_mensuel(salaire_annuel)
hebdomadaire = salaire_hebdomadaire(mensuel)
horaire = salaire_horaire(hebdomadaire, heures_travaillees)
print("votre salaire horaire est de ", horaire)
