
import random

class OrangeTree():
    def __init__(self):
        self.age = 1
        self.height = 2 # feet
        self.oranges = []
        self.number_of_oranges = 0

    def grow(self):
        self.age += 1
        self.height += 2
        if self.age > 3:
            self.number_of_oranges = random.randint(0,5)
            for i in range(0, self.number_of_oranges):
                self.oranges.append(float(random.randrange(500, 1500))/100)

    def alive(self):
        if self.age > 10:
            return False
        else:
            return True

    def has_oranges(self):
        if len(self.oranges) > 0:
            return True

    def pick_orange(self):
        if len(self.oranges) > 0:
            return self.oranges.pop(0)
        else:
            pass

tree = OrangeTree()

while not tree.has_oranges():
  tree.grow()
  print(f"Tree is {tree.age} years old and {tree.height} feet tall")

while tree.alive():
  basket = []

  while tree.has_oranges():
    basket.append(tree.pick_orange())

  avg_diameter = sum(basket)/len(basket)

  print(f"Year {tree.age} Report")
  print(f"Tree Height: {tree.height} feet")
  print(f"Harvest: {len(basket)} oranges with an average diameter of {avg_diameter} inches")
  print(" ")

  tree.grow()

print('Alas, the tree, she is dead!')


