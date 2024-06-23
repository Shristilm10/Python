def test():
    print("this is function")


object = test()
print(object)


class test:
    a = 10


obj = test()
print(obj.a)


class test2:
    a = 5

    def testfunction(shristi):
        print("this is test2")
        print(shristi.a)

    def tf(shristi):
        print(shristi.a + 20)


obj = test2()
obj.testfunction()
obj.tf()

obj1 = test2()
obj1.a = 50
print(obj1.testfunction())
obj1.testfunction()

# at shristi we can write any variable or self
# if we dont write print(obj1.testfunction()) then result couldnot been none if we dont want none on result then we have to write obj1.testfunction()


class new:
    a = 10

    def __str__(self):
        return f"the value of a is {self.a}"

    def newfunction(self):
        return "this is function"


obj3 = new()
print(obj3)


class constructor:
    def __init__(self):
        self.a = "shristi"
        print(self.a)

    def testfunction(self):
        return self.a


obj = constructor()


class math:
    def __init__(self):
        self.num1 = 10
        self.num2 = 20

    def sum(self):
        total = self.num1 + self.num2
        return total

    def sub(self):
        total = self.num1 - self.num2
        return total

    def multi(self):
        total = self.num1 * self.num2
        return total

    def div(self):
        total = self.num1 / self.num2
        return total


object = math()

print(f"the sum is {object.sum()}")
print(f"the sub is {object.sub()}")
print(f"the multipication is {object.multi()}")
print(f"the divison is {object.div()}")


# argument a,b
class math:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def sum(self):
        total = self.num1 + self.num2
        return total

    def sub(self):
        total = self.num1 - self.num2
        return total

    def multi(self):
        total = self.num1 * self.num2
        return total

    def div(self):
        total = self.num1 / self.num2
        return total


a = int(input("enter any number"))
b = int(input("enter any number"))
object = math(a, b)

print(f"the sum is {object.sum()}")
print(f"the sub is {object.sub()}")
print(f"the multipication is {object.multi()}")
print(f"the divison is {object.div()}")


# inheritance
class parentA:
    a = 10
    b = 12


class parentB(parentA):
    c = 11


object1 = parentB()
print(object1.a)

# 
class parents():
    def __init__(self,name):
        self.name = name
class child(parents):
    def demo(self):
        text = self.name
        return text
obj = child('shristi')
print(f'parent name is {obj.demo()}')

# single level
class parentA:
    def __init__(self) -> None:
        self.a = 100
        self.b = 200

class childA(parentA):
     def __init__(self) -> None:
        self.c = 300
        parentA.__init__(self) 
        # for another of parentA.__init__(self) is super().__init__()
       
obj = childA()
print(obj.a)

# 
# class test():
#     def __init__(self,name) -> None:
#         self.name = name 
#     def name(self):
#         return self.name
#     def fullname(self):
#         return (f'{self.name()}chettri')
    
# data = input("enter your name")
# obj = test(data)
# print(obj.fullname())

# multi level
class parentA:
    def __init__(self) -> None:
        self.a = 100
        self.b = 200

class childA(parentA):
     def __init__(self) -> None:
        self.c = 300
        parentA.__init__(self) 
        # for another of parentA.__init__(self) is super().__init__()
class childB(childA):
    def testfunction(self):
        return self.a+self.b+self.c
    
obj = childB()
print(obj.a)

# polymorphism
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()

# inheritance in polymorohism
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()