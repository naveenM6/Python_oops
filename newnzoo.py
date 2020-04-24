class Animals:
    sound = "Buck Buck"
    add_food = 2
    name = 'Deer'
    def __init__(self, breed, required_food_in_kgs,age_in_months=1):
        if age_in_months > 1:
            raise ValueError(f"Invalid value for field age_in_months: {age_in_months}")
        self._age_in_months = age_in_months
        self._breed = breed
        if required_food_in_kgs <= 0:
            raise ValueError(f"Invalid value for field required_food_in_kgs: {required_food_in_kgs}")
        self._required_food_in_kgs = required_food_in_kgs
        
    def __str__(self):
        return self.name
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += self.add_food
        
    @classmethod    
    def make_sound(cls):
        print(cls.sound)
        
    @property
    def age_in_months(self):
        return self._age_in_months
        
    @property
    def breed(self):
        return self._breed
        
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
 
class Carnivores:
    hunt_animal = 'Deer'
    h_animal = 'deers'
    def hunt(self,zoo):
        if zoo._animal_li[self.hunt_animal] == 0:
            print(f'No {self.h_animal} to hunt')
        else:
            zoo._animal_li[self.hunt_animal] -= 1
            zoo.animal_count -= 1
            
class LandAnimals:
    breath = "Breathe in air"
    @classmethod   
    def breathe(cls):
        print(cls.breath)
        
class WaterAnimals:
    breath = "Breathe oxygen from water"
    @classmethod   
    def breathe(cls):
        print(cls.breath)

class Deer(Animals,LandAnimals):
    pass

class Lion(Animals,Carnivores,LandAnimals):
    sound = "Roar Roar"
    add_food = 4
    name = 'Lion'
    
class Shark(Animals,Carnivores,WaterAnimals):
    sound = "Shark Sound"
    add_food = 8
    name = 'Shark'
    hunt_animal = 'GoldFish'
    h_animal = 'GoldFish'
    
class GoldFish(Animals,WaterAnimals):
    sound = "Hum Hum"
    add_food = 0.2
    name = 'GoldFish'
    
class Snake(Animals,Carnivores,LandAnimals):
    sound = "Hiss Hiss"
    add_food = 0.5
    name = 'Snake'
    
class Zoo():
    count_animals_in_all = 0
    def __init__(self):
        self._reserved_food_in_kgs = 0
        self.animal_count = 0
        self._animal_li = {'Deer': 0,'Lion':0,'Shark':0,'GoldFish':0,'Snake':0}
        
    def add_food_to_reserve(self,weight):
        self._reserved_food_in_kgs += weight
        
    def count_animals(self):
        return self.animal_count
        
    def add_animal(self,animal):
        self.animal_count += 1
        li = ['Lion','Shark','Snake','GoldFish','Deer']
        if str(animal) in li:
            self._animal_li[str(animal)] += 1
        Zoo.count_animals_in_all += 1
        
    def feed(self,animal):
        if self._reserved_food_in_kgs != 0:
            self._reserved_food_in_kgs -= animal.required_food_in_kgs
            animal.grow()
        
    @staticmethod
    def count_animals_in_given_zoos(list):
        count = 0
        for i in list:
            count += i.animal_count
        return count
        
    @classmethod
    def count_animals_in_all_zoos(cls):
        return Zoo.count_animals_in_all
        
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
        
    @property
    def animal_li(self):
        return self._animal_li
