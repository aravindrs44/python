import pets

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet(name, types, tricks, health, energy)

    def walk(self):
        self.pet.walk()
        print(f"{self.pet.name}'s health ↑ by 5!")
    
    def feed(self):
        self.pet.eat()
        print(f"{self.pet.name}'s Health ↑ by 5")
        print(f"{self.pet.name}'s Energy ↑ by 10")

    def bathe(self):
        self.pet.noise()

senlair = Ninja("Sen", "Lair", "hot cheetos", "takis")