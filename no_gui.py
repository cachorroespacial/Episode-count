import requests

anime = input("Enter the name of the anime: ")
contar_ovas = input("Do you want to count OVAs too? (y/n): ").lower() == 'y'

response = requests.get(
    "http://127.0.0.1:8000/episodes/",
    params={"nome": anime, "contar_ovas": contar_ovas}
)

data = response.json()

if "erro" in data:
    print("Anime not found.")
else:
    print(f"Name: {data['nome']}")
    print(f"Episodes: {data['episodios']}")
    print(f"OVAs: {data['ovas']}")
