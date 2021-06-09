from pets import Pet

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        print(f"{self.pet.name}'s health UP by 5!")
        return self
    
    def feed(self):
        self.pet.eat()
        print(f"{self.pet.name}'s Health UP by 5")
        print(f"{self.pet.name}'s Energy UP by 10")
        return self

    def bathe(self):
        self.pet.noise()
        return self


chiaro = Pet("Chiaro", "dog", "butt wiggle")
senlair = Ninja("Aravind", "Sripada", "hot cheetos", "takis", chiaro)
senlair.feed().walk().bathe()
print(chiaro.health)