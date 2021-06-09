
class Pet:
    def __init__(self, name, types, tricks, health = 50, energy = 50):
        self.name = name
        self.type = types
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25

    def eat(self):
        self.energy += 5
        self.health += 10

    def play(self):
        self.health += 5

    def noise(self):
        print("BORF")