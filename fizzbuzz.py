#Quick Method 1
if False:
    for num in range (1,101):
        if num%3==0 and num%5==0:
            print("FizzBuzz")
        elif num%3==0:
            print("Fizz")
        elif num%5==0:
            print("Buzz")
        else:
            print(num)

#method 2
    for num in range(1,101):
        output=""
        if num%3==0:
            output+="Fizz"
        if num%5==0:
            output+="Buzz"
        #if num%7==0:
            #output+="Fuzz"
        if output=="":
            output=num
        print(output)

#for adding extra comparisons only add if statements before the output check
