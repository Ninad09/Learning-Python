#dunders
#magic methods
#special functions that have double undescores '__' at the start and end of the function name
#eg.: __init__
#operator overloading using dunders __add__ for +
class numb:
    def __init__(self,x,y):
        self.x,self.y=x,y
    def __add__(obj1,obj2):     #Overloaded addition of two objects
        return numb(obj1.x+obj2.x,obj1.y+obj2.y)
    def __sub__(obj1,obj2):     #Overloaded subtraction of two objects
        return numb(obj1.x-obj2.x,obj1.y-obj2.y)
#__new__() is called before __init__()
print("Object1::")
x1,y1=int(input("Enter X: ")),int(input("Enter Y: "))
ob1=numb(x1,y1)
print("Object2::")
x2,y2=int(input("Enter X: ")),int(input("Enter Y: "))
ob2=numb(x2,y2)
print()
print("Overloaded Addition of ojects")
obj=ob1+ob2
print("Values of X and Y in new object:: {} {}".format(obj.x,obj.y))
print()
print("Overloaded Subtraction of ojects")
obj=ob1-ob2
print("Values of X and Y in new object:: {} {}".format(obj.x,obj.y))

#dunders for most common operations
#__add__ for +
#__sub__ for -
#__mul__ for *
#__truediv__ for /
#__floordiv__ for //
#__mod__ for %
#__pow__ for **
#__and__ for &
#__xor__ for ^
#__or__ for |

#dunders for comparison operators
#__lt__ for <
#__le__ for <=
#__eq__ for ==
#__ne__ for !=
#__gt__ for >
#__ge__ for >=

#dunders for objects to be acted on as containers
#__len__ for len()
#__getitem__ for indexing
#__setitem__ for assigning to indexed values
#__delitem__ for deleting indexed values
#__iter__ for iteration over objects (e.g., in for loops)
#__contains__ for in
