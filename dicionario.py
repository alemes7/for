import os

paises = {
    "Brasil": "Brasilia",
    "Italia": "Roma",
    "Japao": "Toquio",
}

pais = input("Digite um pais:")

if pais in paises:
    capital = paises[pais]
    print("A capital de", pais, "é", capital)
else:
    print("Pais não encontrado")


os.system("pause")