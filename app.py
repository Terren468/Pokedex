import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
moves = open("./moves.json", encoding="utf8")
data2 = json.load(moves)

for pokemon in data:
  print(pokemon['name']['english'])

def pokemon_printer():
  while True:
    language = input("Choose a language (English,Chinese,Japanese,French): ").lower()
    if language in data[0]['name']:
      break
    else:
      print(f"Language not found. Please try again.")
  while True:
    try:
      id = int(input("Enter the pokemon id (1 - 809): "))
      if 1 <= id <= 809:
        print (data[id - 1]['name'][language])
        break
      else:
        print("Id not found. Please try again.")
    except ValueError:
      print("Invalid id. Please enter a number.")
pokemon_printer()

def pokemon_type():
  while True:
    type = input("Enter a pokemon type: ").capitalize()
    found = False
    for pokemon in data:
      if type in pokemon['type']:
        print(pokemon['name']['english'])
        found = True
    if found:
      break
    else:
      print(f"No pokemon found for that type. Please try again.")
pokemon_type()

def pokemon_searcher():
  while True:
    search = input("Enter a pokemon name: ").lower()
    found = False
    for pokemon in data:
      if search in pokemon['name']['english'].lower():
        print(pokemon['name']['english'])
        found = True
    if found:
      break
    else:
      print("No pokemon found for this name. Plese try again.")
pokemon_searcher()

def pokemon_moves():
  while True:
    moves = input("Enter a pokemon name to see their moves: ").lower()
    found = False
    for pokemon in data:
      if pokemon['name']['english'].lower() == moves:
        found = True
        for move in data2:
          if move['type'] in pokemon ['type']:
            print(f"{move['ename']} ({move['type']}) - Power: {move['power']}, Accuracy: {move['accuracy']}, PP: {move['pp']}")
if found:
      break
    else:
      print("No pokemon found for that name. Please try again.")
pokemon_moves()
