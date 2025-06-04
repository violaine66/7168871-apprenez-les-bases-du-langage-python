# Écrivez votre code ici !
import csv

def extract(file="input.csv"):
    data = []
    with open(file, "r") as fichier_csv:
        script = csv.DictReader(fichier_csv, delimiter=",")
        for ligne in script:
            data.append(ligne)
    return data 

def transform(data):
    transformed = []
    for ligne in data
        nom = ligne["nom"]
        heures = float(ligne['heures_travaillees'])
        salaire = heures*20
        transformed.append({"nom": nom, "salaire": round(salaire, 2)})
    return transformed

def load(data, file="output.csv"):
   headers = ["nom", "salaire"]
    with open(file, "w", newline='') as fichier_csv:
        writer = csv.DictWriter(fichier_csv, fieldnames=headers delimiter=",")
        writer.writeheader()
        writer.writerows(data)

def main():
    data_extraites = extract("input.csv")
    data_transformees = transform(data_extraites)
    load(data_transformees, "output.csv")
# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()
