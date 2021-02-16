import requests as rq

pokemon = input('Digite o nome do pokemon: ')
url =f'https://pokeapi.co/api/v2/pokemon/{pokemon}'

try:
  req = rq.get(url)
  poke_info = req.json()
  habilidades = []

  for i in poke_info['abilities']:
    habilidades.append(i['ability']['name'])

  habilidades = ', '.join(habilidades)

  texto = f'Pokemon: {poke_info["name"]}\nHabilidades: {habilidades}\nPeso: {poke_info["height"]}kg'

  print(texto)
except:
  print('Pokemon não encontrado!')