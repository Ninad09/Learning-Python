if False:
    #decorators is functions taking functions as parameters and returning a combined function created from parameter functions
    #functions that modify other functions
    _text=input("Enter Statement to Decorate::")
    def decor(func):
        def temp():
            print("===============")
            func()
            print("===============")
        return temp

    def text():
        print(_text)

    print("New Variable Function")
    decorated=decor(text)
    decorated()

    #redefining original text function to contain improved text
    print("Original Function Redefined")
    text=decor(text)
    text()

    #redifining original function can be achieved by using '@' and the decorator function name/variable
    @decor
    def print_text():
        print("Hello World")

    print_text()

##Recursion##
#recursion is function calling itself

def factorial(num):
    if num==1:
        return 1
    else:
        return num * factorial(num-1)

n=int(input("Enter Factorial Base:: "))
print("Factorial of {}:: ".format(n),factorial(n))

#An unnecessarily complex Even Odd checking function
def is_even(x):
    if x==0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)

n=int(input("Enter Number:: "))
print("Is Odd:: ",is_odd(n))
print("Is Even:: ",is_even(n))

def fibo(n):
    if n==0 or n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

n=int(input("Enter Length of Fibonacci Sequence:: "))
for i in range(n):
    print(fibo(i),end=', ')
#You need to print "return" character '\r' or new line character '\n' to escape the end='' condition
print('\r')
print("Hello World")
