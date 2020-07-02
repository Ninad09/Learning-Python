#Have the function BinaryReversal(str) take the str parameter being passed, which will be a positive integer, take its binary representation
#(padded to the nearest N * 8 bits), reverse that string of bits, and then finally return the new reversed string in decimal form.
#For example: if str is "47" then the binary version of this integer is 101111 but we pad it to be 00101111.
#Your program should reverse this binary string which then becomes: 11110100 and then finally return the decimal version of this string, which is 244.
from math import ceil
def tobinary(number):
    """
    takes an integer number as an argument
    returns a string of binary characters rounded of to 8 bits
    """
    n=number
    string=""
    while not n==0:
        string=str(n%2)+string
        n=n//2
    #Round of to nearest 8 multiple
    mul8=ceil(len(string)/8)*8
    offset=mul8-len(string)
    for i in range(offset):
        string='0'+string
    print(len(string),' bit representation...')
    return string

def reversebinary(binary):
    """
    Take in a binary number as a string
    Reverses the bits of the binary number
    Returns the reversed binary as a string
    """
    joiner=""
    binary=list(binary)
    for i in range(len(binary)):
        if binary[i]=='1':
            binary[i]='0'
        else:
            binary[i]='1'
    return joiner.join(binary)

def tointeger(binary):
    """
    Takes in binary number as a string
    Converts to integer and returns the integer
    """
    integer=0
    binary=binary[::-1]
    for i in range(len(binary)):
        integer+=int(binary[i])*(2**i)
    return integer

#Driver Code
if __name__=='__main__':
    numb=int(input("Enter Number--"))
    bi=tobinary(numb)
    print("Binary rep :: ",bi)
    rev_bi=reversebinary(bi)
    print("Reversed binary rep :: ",rev_bi)
    print("Reversed Binary Integer :: ",tointeger(rev_bi))
