from fastapi import FastAPI
import requests

app = FastAPI()

ANILIST_URL = "https://graphql.anilist.co"
KITSU_URL = "https://kitsu.io/api/edge/anime"


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

    response = requests.post(ANILIST_URL, json={'query': query, 'variables': variables})
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

@app.get("/episodes/")
def get_anime_episodes(nome: str, contar_ovas: bool = False):
    
    episodios = buscar_anime(nome)

    if not episodios:
        return {"erro": "Anime não encontrado"}

    
    ovas = []
    if contar_ovas:
        ovas = buscar_ovas(nome)

    
    return {
        "nome": nome,
        "episodios": episodios,
        "ovas": sum(ovas) if ovas else 0  
    }
