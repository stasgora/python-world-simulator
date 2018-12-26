from random import randint
from creatures import Human
from creatures.animals import Antelope, CyberSheep, Fox, Sheep, Turtle, Wolf
from creatures.plants import Belladonna, Grass, Guarana, Sonchus, SosnowskyHogweed


class CreatureFactory(object):

    name_to_symbol = {"Antelope": 'A', "CyberSheep": 'X', "Fox": 'L', "Sheep": 'O',
                      "Turtle": 'Z', "Wolf": 'W', "Belladonna": 'J', "Grass": 'T',
                      "Guarana": 'G', "Sonchus": 'M', "SosnowskyHogweed": 'B', "Human": 'C'}

    @staticmethod
    def spawn_new(symbol, position, world):
        rand = -1
        if symbol == ' ':
            rand = randint(0, 10)
        elif len(symbol) > 1:
            try:
                symbol = CreatureFactory.name_to_symbol[symbol]
            except KeyError:
                return None
        if symbol == 'A' or rand == 0:
            return Antelope.Antelope(4, 4, 'A', position, world, "#8c5022")
        elif symbol == 'X' or rand == 1:
            return CyberSheep.CyberSheep(11, 4, 'X', position, world, "#4c858a")
        elif symbol == 'L' or rand == 2:
            return Fox.Fox(3, 7, 'L', position, world, "#d85819")
        elif symbol == 'O' or rand == 3:
            return Sheep.Sheep(4, 4, 'O', position, world, "#d5d4ce")
        elif symbol == 'Z' or rand == 4:
            return Turtle.Turtle(2, 1, 'Z', position, world, "#937c53")
        elif symbol == 'W' or rand == 5:
            return Wolf.Wolf(9, 5, 'W', position, world, "#909697")
        elif symbol == 'J' or rand == 6:
            return Belladonna.Belladonna(99, 0, 'J', position, world, "#163e5f")
        elif symbol == 'T' or rand == 7:
            return Grass.Grass(0, 0, 'T', position, world, "#87b50a")
        elif symbol == 'G' or rand == 8:
            return Guarana.Guarana(0, 0, 'G', position, world, "#fb2018")
        elif symbol == 'M' or rand == 9:
            return Sonchus.Sonchus(0, 0, 'M', position, world, "#eeda45")
        elif symbol == 'B' or rand == 10:
            return SosnowskyHogweed.SosnowskyHogweed(10, 0, 'B', position, world, "#435f3a")
        elif symbol == 'C':
            return Human.Human(5, 4, 'C', position, world, "#f4d8bc")
        return None
