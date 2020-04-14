#string formatting:
n=[45,81,72]
ms="Numbers: {1} {2} {0}".format(n[0],n[1],n[2])
#numbers in {} denote position in 'format()'
#no numbers in {} follow normal sequencing 0,1,2,3,...
print(ms)

msg="Variable values:: x:{x} y:{y}".format(x=23,y=37)
#variable formatting ignores position in format()
print(msg)

msg1="\nName:: {name}\nAge:: {age}\nRoll No.: {}".format(10,name="Ninad Deshpande",age=19)
#values in {} with no value need to be placed first in format()
print(msg1)

if False:
    #List Comprehensions
    #Set Builder formatting for lists

    #sqaures of numbers from 0 to 9
    sqs=[i**2 for i in range(10)]
    print("Squares using set builder:\n",sqs)

    import math

    #factorial function
    def factorial(num):
        #factorial of 0 and 1 is 1
        if num==0 or num==1:
            return 1
        elif num>1:
            fact=1
            for i in range(1,num+1):
                fact=fact*i
            return fact

    #print factorials
    facts2=[math.factorial(m) for m in range(10)]
    print("Factorials using import function:\n",facts2)
    facts1=[factorial(i) for i in range(10)]
    print("Factorials using user defined function:\n",facts1)

    #powers of 2 from 0 to 9
    powers=[2**i for i in range(10)]
    print("Powers of 2 from 0 to 9:\n",powers)

    #print only even squares from 0 to 15
    evensq=[n**2 for n in range(16) if n**2%2==0]
    print("Even squares from 0 to 15:\n",evensq)

    #print only odd squares from 0 to 15
    oddsq=[n**2 for n in range(16) if n**2%2==1]
    print("Odd sqaures from 0 to 15:\n",oddsq)

    #print squareroots of odd numbers from 50 to 60
    sqroots=[round(math.sqrt(b),2) for b in range(50,61)]
    print("Square roots from 50 to 60:\n",sqroots)
