if False:
    class rectangle:
        def __init__(self,length,width):
            self.length=length
            self.width=width
        def calc_area(self):
            return self.length*self.width

        #Class Method, called directly by class, no instance object is required
        @classmethod
        def square(cls,side):
            return cls(side,side)
    #Class Methods recieve additional argument "Self" parameter

    rect=rectangle(int(input("Length: ")),int(input("Width: ")))
    print("\nArea of said rectangle:: ",rect.calc_area())
    print()
    sq=rectangle.square(int(input("Side of Square: ")))
    print("\nArea of said Square:: ",sq.calc_area())

    #Static methods do not recieve any additional arguments, No "Slef" parameter
    class polygon:
        def __init__(self,sides):
            self.sides=sides
        @staticmethod
        def isSquare(side):
            if side<3:
                print("Not a Polygon")
                return False
            elif side==4:
                return True
            else:
                return False

    poly=input("Enter sides of Polygons: ").split()
    print(poly)
    for side in poly:
        print(side,end=" : ")
        if polygon.isSquare(int(side)):
            print("Is a Square")
        else:
            print("Not a Square")

    #Properties
    #Use @property, it is accessed when a class instance is called with the name of the function, no parenthesis needed
    #obj.prop_name
    class polygnon:
        def __init__(self,sides):
            self.sides=sides
        @property
        def isEnclosed(self):
            print("Polygnon is always an enclosed figure")

    obj=polygnon(5)
    print("Property of class Polygnon:: ")
    obj.isEnclosed
    #properties cannot be changed for object to object
    #obj.isEnclosed="Not Always"
    #This causes an error

#Property setter
#@prop_name.setter
class password:
    def __init__(self,name):
        self.name=name
        self.access=False
    @property
    def accessgrant(self):
        #return self.access
        if self.access:
            return "Granted"
        else:
            return "Denied"
    @accessgrant.setter
    def accessgrant(self,value):
        pass_=input("Enter Password for {}: ".format(self.name))
        if pass_=="Nancy901346":
            self.access=value
        else:
            print("Access Denied")

pass1=password("Ninad Comp")
print("Access ",pass1.accessgrant)
pass1.accessgrant=True
print("Access ",pass1.accessgrant)
