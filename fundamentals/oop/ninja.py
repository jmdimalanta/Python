from pets import Pet


class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self, pet):
        print(f"{self.first_name} walked {pet.name}")
    
    def feed(self, pet):
        print(f"{self.first_name} fed {pet.name} some treats")

    def bathe(self, pet):
        print(f"{self.first_name} gave {pet.name} a bath")

class Cat(Pet):
    def display(self):
        print("I am a subclass.")


class Fish(Pet):
    def display2(self):
        print("I am also a subclass.")


# scorpion = Ninja("Hanzo", "Hasashi", "Milk Bone", "Dog Food", "Dog")
# print(scorpion.pet)

# bruce = pets.Pet("Bruce", "Dog", "fetch")

# scorpion.feed(bruce)
# scorpion.walk(bruce)
