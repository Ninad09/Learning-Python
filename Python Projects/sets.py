set_num={1,2,3,4,5,6}
names={"Ninad","Poorva","Manali","Aarya","Shruti"}

#check for presence of terms in sets using keyword 'in'
print("5 in set_num ",5 in set_num)
print("Set of Names:: ",names)
print("'Poorva' not in names ","Poorva" not in names)

#for empty set use set(), {} curly brackets creates an empty dictionary
print(set())

#sets cannot contain duplicates
_set={2,1,5,2,3,9,4}
print(_set)

#sets are automatically ordered for ascending and duplicates removed
#set_name.add() to add/append elements to existing set
#set_name.remove() to remove elements from existing set
_set.add(21)
_set.add(-4)
print(_set)
#does not immediately sort after appending or removing elements ina set
_set.remove(3)
_set.remove(-4)
print(_set)
#set_name.pop() removes an element from arbitrary location (front)
_set.pop()
print("First Set:: ",_set)
#len() functions works for sets and gives length of set after deleting duplicates
print("Length of First:: ",len(_set))

print("Second Set:: ",set_num)
print("Length of Second:: ",len(set_num))

#set arithmetics
#'|' for union/or function between two sets
#'&' for intersection/and function between two sets
#'-' for difference function (first-second)
#'^' for ExOR, first or second but not both
print("First OR Second:: ",set_num|_set)
print("First AND Second:: ",set_num&_set)
print("First - Second:: ",_set-set_num)
print("Second - First:: ",set_num-_set)
print("First ExOR Second:: ",_set^set_num)
