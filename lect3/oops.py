

class Animal():
  def __init__(self,name,sound):
    self.name = name
    self.sound = sound
  
  def speak(self):
    print(self.sound)

# inheriting parent(animal) to child(dog)
# single inheritance 
class Dog(Animal):
  def __init__(self,name,color):
    self.color = color
    super().__init__(name,"woof") #super calls the constructour function of parent class
    # sending(setting) attribute to parent class
  
  def fetch(self):
    print(self.name, "is fetching ball")

wisky_the_dog = Dog("wisky","golden brown")
wisky_the_dog.speak()           # inherited from parent(Animal)
wisky_the_dog.fetch()           # Dog class own function
print(wisky_the_dog.name,wisky_the_dog.color)

# multi-level inheritance
class Vehicle():
  def __init__(self,brand):
    self.brand = brand
  
  def printBrand(self):
    print("the brand of this vehicle is",self.brand)

# class car   -> attributes ->brand,model
class Car(Vehicle):
  def __int__(self,brand,model):
    self.model = model
    super().__init__(brand)
  
  def drive(self):
    print("driving ",self.brand,self.model)

# class electricCar(inherit Car) -> attributes -> brand,model,battery
class electricCar(Car):
  def __init__(self, brand,model,battery):
    self.battery = battery
    super().__init__(brand=brand,model=model)
  
  def charge(self):
    print(self.brand,self.model, "'s" ,self.battery," is charging")

tesla = electricCar("Tesla","model 3","TVR")
tesla.printBrand()                  # grand-parent method
tesla.drive()                       #parent method
tesla.charge()                      #child method


# multiple inheritance
class Animal():
  def __init__(self,name,sound):
    self.name = name
    self.sound = sound
  
  def speak(self):
    print(self.sound)

# inheriting parent(animal) to child(dog)
# single inheritance 
class Dog(Animal):
  def __init__(self,name,color):
    self.color = color
    super().__init__(name,"woof")       #sending(setting) attribute to parent class
  
  def fetch(self):
    print(self.name, "is fetching ball")

class Cat(Animal):
  def __init__(self, name, sound,breed):
    self.breed = breed
    super().__init__(name, sound)


# multiple inheritance -> a child can have multiple parents class
class fly():
  def __init__(self):
    print("i can fly")
  
  def canFly(self):
    print("yes")

class swim():
  def __init__(self):
    print("i can swim")

  def canSwim(self):
    print("yes")

class duck(fly,swim):
  # super will get confuse which one to call

  def __init__(self):
    super().__init__()
    print("this is duck")

mr_duck = duck()
mr_duck.canFly()
mr_duck.canSwim()