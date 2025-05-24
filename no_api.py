import requests

def buscar_anime(nome: str):
    
    query = '''
    query ($search: String) {
      Media(search: $search, type: ANIME) {
        title {
          romaji
        }
        episodes
      }
    }
    '''
    variables = {"search": nome}

    response = requests.post("https://graphql.anilist.co", json={'query': query, 'variables': variables})
    data = response.json()

    if "data" in data and data["data"]["Media"]:
        anime = data["data"]["Media"]
        return anime["episodes"]
    else:
        return None


def buscar_ovas(nome: str):
    
    url = f"https://kitsu.io/api/edge/anime?filter[text]={nome}&filter[subtype]=ova"
    response = requests.get(url)
    data = response.json()

    ovas = []
    for entry in data['data']:
        ovas.append(entry['attributes']['episodeCount'])

    return ovas


def main():
    anime = input("Enter the name of the anime: ")
    contar_ovas = input("Do you want to count OVAs too? (y/n): ").lower() == 'y'

    
    episodios = buscar_anime(anime)

    if not episodios:
        print("Anime not found.")
        return

    ovas = []
    if contar_ovas:
        ovas = buscar_ovas(anime)

    print(f"Name: {anime}")
    print(f"Episodes: {episodios}")
    print(f"OVAs: {sum(ovas) if ovas else 0}")


if __name__ == "__main__":
    main()
