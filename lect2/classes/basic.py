
class car:
  def __init__(self,brand_name,segment,model,fuel_type,color):       #any function starts with "__" is a inbuild function
    self.brand_name = brand_name
    self.segment = segment
    self.model = model
    self.fuel_type = fuel_type
    self.color = color

  def printCar(self):
    print(self.brand_name,self.segment,self.model,self.fuel_type,self.color)

BMW_M5 = car("BMW","sedan","M5","petrol","black")
print(BMW_M5.brand_name)
print(BMW_M5.printCar())

BMW_M6 = car(brand_name="BMW",segment="sedan",model="M6",fuel_type="petrol",color="Z-black")
print(BMW_M6.model)
print(BMW_M6.printCar())

type(car)