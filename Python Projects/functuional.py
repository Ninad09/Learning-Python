#normal Functions (def Functions)
#Functions are assigned to variables

#Pure Functions
#return Values depends only on member inside the function
def square(x):
    return x*x

num=int(input("Number to Square:: "))
print("Square:: ",square(num))

#Impure Functions
#return values may depend on external members to the function
if False:
    lst=[]
    def str_append(st):
        lst.append(st)
        print(' '.join(lst))
        
    n=input("number of appends:: ")
    for i in range(int(n)):
        string=input("Enter string to append:: ")
        str_append(string)

#Lambdas
#Anonymous Functions

#finding fourth power of input number
print("Lambda Direct\nFourth Power:: ",(lambda x:x**4)(num))

def twice(func,n):
    return func(func(n))

print("Lambda Indirect\nFourth Multiple:: ",twice((lambda x:2*x),num))
