def add(n1,n2):
    print("Result: "+str(n1+n2))
def sub(n1,n2):
    print("Result: "+str(n1-n2))
def mul(n1,n2):
    print("Result: "+str(n1*n2))
def div(n1,n2):
    print("Result: "+str(n1/n2))
def mod(n1,n2):
    print("Result: "+str(n1%n2))
while 1:
    print("\nOperations:\nAdd\nSubtract\nMultiply\nDivide\nModulus\nexit\n")
    op=input("Enter Operation: ")
    if op=="exit":
        break
    else:
        num1=float(input("\nEnter First Number: "))
        num2=float(input("Enter Second Number: "))
        if op=='Add':
            add(num1,num2)
        elif op=='Subtract':
            sub(num1,num2)
        elif op=='Multiply':
            mul(num1,num2)
        elif op=='Divide':
            div(num1,num2)
        elif op=='Modulus':
            mod(num1,num2)
