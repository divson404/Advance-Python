# a = int(input("1st number: "))
# b = int(input("2nd number: "))


# def mod(x, y):
#     z = x%y
#     return z

# print(mod(a, b))
# def factorial():
#     i = int(input("input a number: "))
#     for z in range(i):
#         print(z)
# factorial()

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)

# print(factorial(12))


# class Phone:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

#     def description(self):
#         return f"The name of my car is {self.name} is color {self.color}"

# class Wifi:
#     def __init__(self, name, password, security, bandwidth, price, date):
#         self.name = name
#         self.password = password
#         self.security = security
#         self.bandwidth = bandwidth
#         self.price = price
#         self.date = date
    
#     def description(self):
#         return f"This are the property of the wifi, the name is {self.name} and the password is {self.password} with {self.security} and a bandwidth of {self.bandwidth}."

# device = Wifi("starlink 1000", "wert234rt45", "WPA3-Personal", "2.4GHz band", "$1000", "20th March")    
# print()
# device.description()

# class Wifi2:
#     def __init__(self, name, password, security, bandwidth, price, date):
#         self.name = name
#         self.password = password
#         self.security = security
#         self.bandwidth = bandwidth
#         self.price = price
#         self.date = date

#     def description1(self):
#         return f"This are the property of the wifi, the name is {self.name} and the password is {self.password} with {self.security} and a bandwidth of {self.bandwidth}."

# device = Wifi2("starlink 2000", "qwertghnjk", "WPA2/WPA3-Personal", "5/2.4GHz band", "$2500", "20th March" )
# print()
# device.description1()    

# def launch():
#         return f"{Wifi.name} will be launching with a starting price of {Wifi.price} while {Wifi2.name} will 
#         launching with a starting price of {Wifi2.price} and both will be available for pre-order on {Wifi2.date}"


# device.launch()

# class Animal:
#         def __init__(self):
#             self.name = "Bingo"

#         def sound(self):
#             pass

# class Dog (Animal):
#      def sound(self):
#           return "woof"

# class Cat (Animal):
#      def sound(self):
#           return "meow"
     
# dog = Dog("Buddy")
# cat = Cat("Whiskers")

# print(dog.name)
# print(cat.name)

# print(dog.sound())
# print(cat.sound())

# class Parent:
#      def parent_method(self):
#           print("Parent Method")

# class Child(Parent):
#      def child_method(self):
#           print("Child Method")

# obj = Child()
# obj.parent_method()

# class Animal:
#     def __init__(self):
#         self.limb = 4
#         self.eye = 2
#         self.stomach = 1
#         self.ear = 2

#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         print("Woof")

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow")

# def animal_sound(animal):
#     animal.make_sound()

# dog = Dog()
# cat = Cat()


# animal_sound(dog) 
# animal_sound(cat) 

# class ParentClass:
#     def method(self):
#         print("Parent Method")

# class ChildClass(ParentClass):
#     def method(self):
#         pass

# obj = ChildClass()
# obj.method()
class TempConverter:
    def __init__(self, temp: float, b_unit: float, d_unit: float):
        self.temp=temp
        self.b_unit=b_unit
        self.d_unit=d_unit

    def Covert(self):
        if self.b_unit =='C' and self.d_unit == 'K':
            return self.temp + 273
        elif self.b_unit == 'K'and self.d_unit == 'C':
            return self.temp - 273
        
        
var = TempConverter(73.89, "C", "K")
print(var.Covert())

#create a class that checks if a tweet on twitter is recent?