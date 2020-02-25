import random
for i in range(5):
    var=random.randint(0,10)
    print(var)
from math import sqrt,pi
print(pi)
print(sqrt(pi))
def area(rad):
    """
    Calculate area of circle for given radius
    """
    ar=float(pi*rad*rad)
    return ar
r=float(input("\nEnter Radius of Circle: "))
print("\nThe Area of Circle is "+str(area(r)))
