from bs4 import BeautifulSoup
with open("index.html", 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

title = soup.title.string
print("titre:", title)

all_products = dict()

products = soup.find_all("li")
for product in products:
    nom = product.find('h2').string.strip()
    prix = product.find("p", class_="price").string.strip()
    description = product.find_all("p")[-1].string.strip()
    all_products[nom] =    {"prix": prix}
     
    all_products[nom]["description"] = {
        "prix": prix,
        "description": description
    } 

print("Produits:", all_products)
