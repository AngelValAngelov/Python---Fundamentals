class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = list()
        self.fish = list()
        self.birds = list()

    def add_animal(self, s, n):
        if s == "mammal":
            self.mammals.append(n)
        elif s == "fish":
            self.fish.append(n)
        elif s == "bird":
            self.birds.append(n)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            print(f"Mammals in {self.name}: {', '.join(self.mammals)}")
        elif species == "fish":
            print(f"Fishes in {self.name}: {', '.join(self.fish)}")
        elif species == "bird":
            print(f"Birds in {self.name}: {', '.join(self.birds)}")
        print(f"Total animals: {zoo.__animals}")


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())

for _ in range(count):
    animals = input().split(" ")
    species = animals[0]
    name = animals[1]
    zoo.add_animal(species, name)


info = input()
zoo.get_info(info)



