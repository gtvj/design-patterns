class Dog:

  def __init__(self, name):
    self._name = name

  def speak(self):
    return "I'm a dog and my name is {0}. Woof!".format(self._name)

class Cat:

  def __init__(self, name):
    self._name = name

  def speak(self):
    return "I'm a cat and my name is {0}. Meow!".format(self._name)

def get_animal(type="dog"):

  # The factory method

  animals = dict(dog=Dog("Fido"), cat=Cat("Garfield"))

  return animals[type]

# In action

d = get_animal('dog')
print(d.speak())

c = get_animal('cat')
print(c.speak())
