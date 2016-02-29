class Dog:
  # Object that is returned by concrete factory
  
  def speak(self):
    return "Woof!"

  def __str__(self):
    return "Dog"

class DogFactory:
  # Concrete factory

  def get_pet(self):
    # Returns a Dog object
    return Dog()

  def get_food(self):
    # Returns a Dog Food object (a simple string)
    return "Dog food!"

class PetStore:
  # Houses our abstract factory

  def __init__(self, pet_factory=None):
    # pet_factory is our abstract factory

    self._pet_factory = pet_factory

  def show_pet(self):
    # Utility which displays details of objects returned by the DogFactory

    pet = self._pet_factory.get_pet()
    pet_food = self._pet_factory.get_food()

    print("Our pet is '{}'".format(pet))
    print("Our pet says hello by '{}'".format(pet.speak()))
    print("Its food is '{}'".format(pet_food))

# Create a concrete factory
factory = DogFactory()

# Create a PetStore housing our Abstract Factory
shop = PetStore(factory)
shop.show_pet()
