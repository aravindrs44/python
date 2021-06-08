
class Pet:
    def __init__(self, name, types, tricks, health = 50, energy = 50):
        self.name = name
        self.type = types
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print("BORF")

chiaro = Pet("Chiaro", "dog", "butt wiggle")