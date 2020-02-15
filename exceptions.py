try:
    n1=float(input("Enter Number: "))
    n2=float(input("Enter Number: "))
    if n2<0:
        raise ValueError("Denominator is Negative")
    n3=n1/n2
    print("Hello")
    print(n3)
except ZeroDivisionError:
    print("Division by Zero is not Allowed")
    raise
except TypeError:
    print("Error in Types")
    raise
finally:
    print("Always Printed")
