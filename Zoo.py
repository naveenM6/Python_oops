class Deer:
    sound = "Buck Buck"
    breath = "Breathe in air"
    def __init__(self, breed, required_food_in_kgs,age_in_months=1):
        if age_in_months > 1:
            raise ValueError(f"Invalid value for field age_in_months: {age_in_months}")
        self._age_in_months = age_in_months
        self._breed = breed
        if required_food_in_kgs <= 0:
            raise ValueError(f"Invalid value for field required_food_in_kgs: {required_food_in_kgs}")
        self._required_food_in_kgs = required_food_in_kgs
        self._add_food = 2
        
    def __str__(self):
        return 'Deer'
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += self._add_food
    
    @classmethod    
    def make_sound(cls):
        print(cls.sound)
    
    @classmethod   
    def breathe(cls):
        print(cls.breath)
        
    @property
    def age_in_months(self):
        return self._age_in_months
    
    @property
    def breed(self):
        return self._breed
    
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs

    @property
    def add_food(self):
        return self._add_food
        
class Lion(Deer):
    sound = "Roar Roar"
    def __init__(self, breed, required_food_in_kgs,age_in_months=1):
        super().__init__(breed, required_food_in_kgs,age_in_months)
        self._add_food = 4
    
    def __str__(self):
        return 'Lion'
        
    def hunt(self,zoo):
        if zoo._animal_list['deer'] == 0:
            print('No deers to hunt')
        else:
            zoo._animal_list['deer'] -= 1
            zoo.animal_count -= 1
        
class Shark(Deer):
    breath = "Breathe oxygen from water"
    sound = "Shark Sound"
    def __init__(self,breed, required_food_in_kgs,age_in_months=1):
        super().__init__(breed, required_food_in_kgs,age_in_months)
        self._add_food = 8
    
    def __str__(self):
        return 'Shark'
        
    def hunt(self,zoo):
        if zoo._animal_list['deer'] == 0:
            print('No GoldFish to hunt')
        else:
            zoo._animal_list['gold_fish'] -= 1
            zoo.animal_count -= 1
        
class GoldFish(Deer):
    breath = "Breathe oxygen from water"
    sound = "Hum Hum"
    def __init__(self,breed, required_food_in_kgs,age_in_months=1):
        super().__init__(breed, required_food_in_kgs,age_in_months)
        self._add_food = 0.2
    
    def __str__(self):
        return 'GoldFish'
    
class Snake(Deer):
    sound = "Hiss Hiss"
    def __init__(self,breed, required_food_in_kgs,age_in_months=1):
        super().__init__(breed, required_food_in_kgs,age_in_months)
        self._add_food = 0.5
    
    def __str__(self):
        return 'Snake'
        
    def hunt(self,zoo):
        if zoo._animal_list['deer'] == 0:
            print('No deers to hunt')
        else:
            zoo._animal_list['deer'] -= 1
            zoo.animal_count -= 1
        
class Zoo:
    count_animals_in_all = 0
    def __init__(self):
        self._reserved_food_in_kgs = 0
        self.animal_count = 0
        self._animal_list = {'deer': 0,'lion':0,'shark':0,'gold_fish':0,'snake':0}
        
    def add_food_to_reserve(self,weight):
        self._reserved_food_in_kgs += weight
        
    def count_animals(self):
        return self.animal_count
        
    def add_animal(self,animal):
        self.animal_count += 1
        if str(animal) == 'Lion':
            self._animal_list['lion'] += 1
        if str(animal) == 'Deer':
            self._animal_list['deer'] += 1
        if str(animal) == 'Shark':
            self._animal_list['shark'] += 1
        if str(animal) == 'GoldFish':
            self._animal_list['gold_fish'] += 1
        if str(animal) == 'Snake':
            self._animal_list['snake'] += 1
            
        Zoo.count_animals_in_all += 1
     
        
    def feed(self,animal):
        if self._reserved_food_in_kgs == 0:
            return
        self._reserved_food_in_kgs -= animal.required_food_in_kgs
        animal.grow()
        return self._reserved_food_in_kgs
        
    @classmethod
    def count_animals_in_given_zoos(cls,list):
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
    def animal_list(self):
        return self._animal_list
        
        
zoo = Zoo()
shark = Shark(age_in_months=1, breed="Hunter Shark", required_food_in_kgs=10)
gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=0.5)
deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
zoo.add_animal(deer)
zoo.add_animal(shark)
zoo.add_animal(gold_fish)
shark.hunt(zoo)
print(zoo.animal_count)
