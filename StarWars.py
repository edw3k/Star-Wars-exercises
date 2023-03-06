import json


class StarWars:
    def __init__(self, name, created, gender, skin_color, hair_color, height, eye_color, mass, homeworld, birth_year):
        self.name = name
        self.created = created
        self.gender = gender
        self.skin_color = skin_color
        self.hair_color = hair_color
        self.height = height
        self.eye_color = eye_color
        self.mass = mass
        self.homeworld = homeworld
        self.birth_year = birth_year

    def getter(self):
        print("The name of the character is: ", self.name, "its gender is " + self.gender, "belongs to the home "
                                                                                           "world of " +
              self.homeworld + " and was born in " + self.birth_year)


class CharacterFilms(StarWars):
    def __init__(self, name, created, gender, skin_color, hair_color, height, eye_color, mass, homeworld, birth_year):
        super().__init__(name, created, gender, skin_color, hair_color, height, eye_color, mass, homeworld, birth_year)
        self.num_of_films = None
        self.first_film = None
        self.alive_at_the_end = None

    def set_num_of_films(self, num):
        self.num_of_films = num

    def set_first_film(self, film):
        self.first_film = film

    def set_alive_at_the_end(self, status):
        self.alive_at_the_end = status

