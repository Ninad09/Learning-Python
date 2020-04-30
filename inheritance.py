#simple inheritance
class animal:
    legs=4
    ani=""
    def __init__(self,name,color):
        self.name=name
        self.color=color

class Dog(animal):
    animal.ani="Dog"
    def sound(self):
        print("Bark")
    def description(self):
        print("\nAnimal:: ",animal.ani,"\nLegs:: ",animal.legs,"\nName:: ",self.name,"\nColor:: ",self.color)

frido=Dog("Frido","Black")
frido.sound()
frido.description()
print()

#overriding functions
class wolf:
    def sound(self):
        print("Growl")

class dog(wolf):
    def sound(self):
        print("Bark")

lone=wolf()
lone.sound()    #prints "Growl"
yamper=dog()
yamper.sound()  #prints "Bark"  Function sound() is overrided in subclass
print()

#heirarchial/indirect inheritance
class pet(dog):
    def __init__(self,name):
        self.name=name
    def sounds(self):
        print(self.name)
        self.sound()

dozer=pet("Dozer")
dozer.sounds()
print()

#Overcoming Function overriding
class barn(dog):
    def sound(self):
        print("Bark Growl") #new sound() function defined which will override previously existing two sound() functions
        super().sound()     #call to sound() function from superclass, using self.sound() will result in recursive call here

houndoom=barn()
houndoom.sound()
