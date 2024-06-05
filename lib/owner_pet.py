class Pet:
    all = []
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird','reptile', 'exotic']
    def __init__(self,name,pet_type,Owner=None):
        self.name = name
        if pet_type not in self.PET_TYPES:
            raise ValueError(f"Invalid pet_type: {pet_type}. Valid pet types are {self.PET_TYPES}.")
        self.pet_type = pet_type
        self.owner = Owner
        self.all.append(self)
        
    pass

class Owner:
    
    def __init__(self,name):
        self.name = name
        
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    def add_pet(self, pet):
      if type(pet) is not Pet:
        raise Exception("Input object is not of type Pet")
      pet.owner = self
          

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)

    

        pass
