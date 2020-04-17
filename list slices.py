lst=[21,32,54,81,37,6,2,4,8,5]
#print from index 2 to index 4
print(lst[2:5])
#print index 4 to end
print(lst[4:])
#print start to 6
print(lst[:7])
#print every other element
print(lst[::2])
#print start to third last element
print(lst[:-2])
#print reverse list
print(lst[::-1])
print(sorted(lst))
print(lst[::-1])
#sorted() function does not imply permanent sorting of list
#sorted(lst)

#for permanent sorting
lst.sort()
print(lst)
print(lst[::-1])
