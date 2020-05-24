#Weakly Private

#variables starting with a single underscore are marked as private
#These can be accessed from outside the class in the same program
#variables marked private are not loaded when using a program in "import * "

class QUeue:
    def __init__(self,st):
        self._qu=list(st)
    def push(self,value):
        self._qu.insert(0,value)
    def pop(self):
        return self._qu.pop(-1)
    def __repr__(self):
        return "Queue: {}".format(self._qu)

queue1=QUeue([0,1,2,4,5])
print(queue1)
print()
queue1.push(24)
queue1.pop()
queue1.pop()
print(queue1)
print()

#Strongly Private

#They cannot be accessed directly from outside the class
#Can be accessed by using class methods or using "object._classname__privatemethod"
class Class:
    def __init__(sold,value):
        sold.__privalue=value
    def print_val(self):
        print("Private Value:: ",self.__privalue)

obj=Class(input("Enter Value:: "))
print()
obj.print_val()
print(obj._Class__prival)
#print(obj.__prival)     #causes an error
#class denies the existence of attribute
#...There is no war in Ba Sing Se...
