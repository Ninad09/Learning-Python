n=int(input("Size of Square:: "))
# 2-D array with all slots set to 0
magicSquare=[[0 for x in range(n)] for y in range(n)]
def generateSquare(n):
    # initialize position of 1 
    i=n/2
    j=n-1
    num=1
    # Fill the magic square with remaining values
    while num<=(n*n):
        if i==-1 and j==n: # Jump Condition 3
            j=n-2
            i=0
        else: 
            # next number goes out of right bound of square
            if j==n: 
                j=0
            # next number goes out of upper bound of square 
            if i<0:
                i=n-1  
        if magicSquare[int(i)][int(j)]: # Jump Condition 2
            j=j-2
            i=i+1
            continue
        else: 
            magicSquare[int(i)][int(j)]=num 
            num=num+1
        j=j+1
        i=i-1 # Jump Condition 1
# Printing magic square
def printSquare():
    print ("Magic Squre for n =",n,'\n')
    for i in range(0, n): 
        for j in range(0, n):
            # print(magicSquare[i][j],end='')
            print('%3d ' % (magicSquare[i][j]),end = '')
            # To display output in matrix form 
            if j==n-1:
                print()
    print ("\nSum of each row or column",n*(n**2+1)/2,"\n")
# Driver Code
generateSquare(n)
printSquare()
