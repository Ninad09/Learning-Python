#Map
#takes function and iterable as arguments
#Takes the list elements one by one and applies the function to the elements and creates a new list

lst=[21,84,652,7,3,41,54,81,34,20,94,37]
print("Original list:: ",lst)
res1=list(map(lambda x:x*2.5,lst))
print("Original list x2.5:: ",res1)

#Filter
#Takes function(boolean return) and iterable as arguments
#Iterates through all list elements and only returns elements that satisfy the condition given by the function

res2=list(filter(lambda x:x%2==0,lst))
print("Even numbers in list:: ",res2)

#The result has to be explicitly converted to a list if you want to print it, for both map and filter

#Generators
#Types of iterators, do not allow fixed indexing
#Creted using functions and keyword yield

#a function that behaves like an iterator, and therefore can be used in a for loop
def generator():
    for i in range(5):
        yield i

#Can be iterated through using function name
for i in generator():
    print(i)

if False:
    #generators don't have memory restrictions as they generate items one by one
    #they can therefore be infinite
    def infini():
        while True:
            yield 5

    #Creates an infinite iterable where all elements are 5
    for i in infini():
        print(i)

def user_generate(n):
    for i in range(n):
        yield i
#generator on the fly using user inputs
num=int(input("Enter Number:: "))
print(list(user_generate(num)))
