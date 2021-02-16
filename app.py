import requests

pokemon = input("Digite o nome de um pokemon: ")
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
req = requests.get(url)

try:
  poke = req.json()
  texto = f"O pokemon escolhido é o {poke['name']} e ele pesa {poke['height']}kg."
  print(texto)  
except:
  print("Pokemon não encotrado.")