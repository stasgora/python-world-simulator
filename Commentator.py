class Commentator(object):

    @staticmethod
    def report_death(lives, dies):
        return type(lives).__name__ + " at " + str(lives.get_position()) + " killed " + type(dies).__name__ + " at " + str(dies.get_position()) + "\n"

    @staticmethod
    def report_birth(born):
        return type(born).__name__ + " was born at " + str(born.get_position()) + "\n"

    @staticmethod
    def report_ability_use(human):
        return "Human drank his magic potion. Strength = " + str(human.get_strength()) + "\n"

    @staticmethod
    def report_eating_guarana(creature, guarana):
        return type(creature).__name__ + " at " + str(creature.get_position()) + " ate Guarana at " \
               + str(guarana.get_position()) + ". Strength = " + str(creature.get_strength()) + "\n"

    @staticmethod
    def report_file_saving_error():
        return "Could not save world state.\n"

    @staticmethod
    def report_file_loading_error():
        return "Could not load world state.\n"
