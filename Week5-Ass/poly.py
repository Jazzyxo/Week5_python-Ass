# Base class: Animal
class Animal:
    def move(self):
        return "This animal moves in its own way."

# Subclass: Bird
class Bird(Animal):
    def move(self):
        return "Flying in the sky! 🐦"

# Subclass: Fish
class Fish(Animal):
    def move(self):
        return "Swimming in the water! 🐟"

# Subclass: Snake
class Snake(Animal):
    def move(self):
        return "Slithering on the ground! 🐍"

# Create objects for each subclass
bird = Bird()
fish = Fish()
snake = Snake()

# Polymorphism in action
animals = [bird, fish, snake]
for animal in animals:
    print(animal.move())
