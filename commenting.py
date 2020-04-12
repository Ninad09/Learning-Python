def name():
    #printing name
    print("Ninad Deshpande")
#This should not be printed
"""
This should cause an error
This does not cause an error
Python program does not have a way of commenting multiple lines
This triple quoes method although not executed creates a string
"""

def age():
    #printing age
    print(str(2020-2001))
name()
age()
func1=name
func2=age
#assigning new names
def func():
    print("Reassigned Function Names:")
    func1()
    func2()
func()
