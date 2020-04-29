if False:
    class animal:
        def __init__(self,color,legs):
            self.color=color
            self.legs=legs
        def print_animal(self,mal):
            print("Color of {}:: ".format(mal),self.color,"\nLegs of {}:: ".format(mal),self.legs)

    dog=animal("Black",4)
    #print("\nColor of Dog:: ",dog.color,"\nNumber of legs:: ",dog.legs)
    dog.print_animal("Dog")

class rectangle:
    sides=4
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def attributes(leaf):
        print("Rectangle Attributes:\nSides:: ",leaf.sides,"\nLength:: ",leaf.length,"\nBreadth:: ",leaf.breadth)
    def calc_perimeter(self):
        peri=2*(self.breadth+self.length)
        print("Perimeter of this rectangle:: {} m.".format(peri))
    def calc_area(self):
        area=self.breadth*self.length
        print("Area of this rectangle:: {} sq.m.".format(area))

rect1=rectangle(42,14)
rect1.attributes()
print()
rect1.calc_perimeter()
print()
rect1.calc_area()
