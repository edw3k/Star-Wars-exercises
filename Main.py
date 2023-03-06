import json
from StarWars import CharacterFilms

# Read the data from the JSON file
with open('StarWars.json') as f:
    data = json.load(f)

# Create a list of CharacterFilms objects
characters = []
for item in data:
    character_data = item['fields']  # Get the dictionary containing the character data
    character = CharacterFilms(character_data['name'], character_data['created'], character_data['gender'],
                               character_data['skin_color'], character_data['hair_color'], character_data['height'],
                               character_data['eye_color'], character_data['mass'], character_data['homeworld'],
                               character_data['birth_year'])
    characters.append(character)

# Set the values for Luke Skywalker, Chewbacca, and Anakin Skywalker
for character in characters:
    if character.name == 'Luke Skywalker':
        character.set_num_of_films(6)
        character.set_first_film('Star Wars: Episode IV - A New Hope')
        character.set_alive_at_the_end(True)
    elif character.name == 'Chewbacca':
        character.set_num_of_films(9)
        character.set_first_film('Star Wars: Episode IV - A New Hope')
        character.set_alive_at_the_end(True)
    elif character.name == 'Anakin Skywalker':
        character.set_num_of_films(6)
        character.set_first_film('Star Wars: Episode I - The Phantom Menace')
        character.set_alive_at_the_end(False)

# Export the data to a new JSON file
output_data = []
for character in characters:
    output_data.append({'name': character.name,
                        'created': character.created,
                        'gender': character.gender,
                        'skin_color': character.skin_color,
                        'hair_color': character.hair_color,
                        'height': character.height,
                        'eye_color': character.eye_color,
                        'mass': character.mass,
                        'homeworld': character.homeworld,
                        'birth_year': character.birth_year,
                        'num_of_films': character.num_of_films,
                        'first_film': character.first_film,
                        'alive_at_the_end': character.alive_at_the_end})
    # export data to a new JSON file
with open('StarWars2.json', 'w') as f:
    json.dump(output_data, f, indent=4)
