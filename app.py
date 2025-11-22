import requests

API_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon(name: str) -> dict:
    url = API_URL + name.lower()
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return r.json()

def main():
    print("=== PokeAPI client ===")
    name = input("Nom du Pokémon (ex: pikachu): ").strip()

    if not name:
        print("Tu dois entrer un nom.")
        return

    try:
        data = get_pokemon(name)
        types = [t["type"]["name"] for t in data["types"]]
        print(f"\nPokémon: {data['name']}")
        print(f"Taille: {data['height']}")
        print(f"Poids: {data['weight']}")
        print("Types:", ", ".join(types))

    except requests.exceptions.HTTPError:
        print("Pokémon introuvable.")
    except requests.exceptions.RequestException as e:
        print("Erreur réseau:", e)

if __name__ == "__main__":
    main()
