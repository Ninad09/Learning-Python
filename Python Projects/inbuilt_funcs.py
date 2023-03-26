#String Functions
msg="Hello World"

#makes all letters uppercase
up=msg.upper()
print(up)
#makes all letters lowercase
down=msg.lower()
print(down)

#replace specific word or group with other
rep=msg.replace("World","Trade Towers")
print(rep)

#join elements of list using set of characters as joiners
numbers=['1','2','3','4','5','6']
print(" {} ".format(msg).join(numbers))

#split string into list elements by specific set of characters
spl="My name is XYZ".split('is')
print(spl)
#split does not include the characters used to seperate the string

#confirming whether string start or end with a specific set of characters
print(msg.startswith("Hell") and msg.endswith("ld"))

#--------------------
#numeric Functions
num=[21,-25,84,93,-12,34,-82]

print("Maximum Value in list:: ",max(num))
print("Minimum Value in list:: ",min(num))
print("Absolute Values of all numbers in list")
for i in range(len(num)):
    print(abs(num[i]))
print("Sum of all Values in list:: ",sum(num))

#collective "and" for a list:: "all"
#returns True or False
print(all(int(i) for i in num))
#int() / str() and similar functions return True or False depending on the argument data types

#collective "or" for a list:: "any"
#returns True of False
print(any(i<0 for i in num))

#enumerate provides index and value pair at output
for enum in enumerate(num):
    print(enum)
