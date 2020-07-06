import random as rm

def roll_dice():
    '''
    Returns a random roll from 1 to 6
    No parameters
    '''
    return rm.randint(1,6)

def char_select():
    '''
    Returns a random character class from "The Dragon Prince" series
    No Parameters
    '''
    return rm.choice(_characters)

def shuffle_list(lst):
    '''
    Takes a list parameter.
    Shuffles the list and returns the shuffled list
    '''
    list_new=lst
    rm.shuffle(list_new)
    return list_new

#Constant Data
numbers=[1,2,3,4,5,6,7]
_characters=('MoonShadow Elves','StarTouch Elves','SunFire Elves','Skywing Elves','EarthBlood Elves','TideBound Elves','Dragons','Human','Human Mage','DarkMage')

#Driver Function
if False:
    if __name__=='__main__':
        print('Function 1: roll_dice()...','\nRoll Dice...',roll_dice())
        print()
        print('Function 2: char_select()...','\nRandom Charcter Class...',char_select())
        print()
        print('Random even number from given range...','\nNumber...',rm.randrange(0,50,2))
        print()
        print('Function 3: Shuffle the parametered list...','\nShuffled...',shuffle_list(numbers))
        print()
        print('Random sampling from a range of population indices')
        local=int(input("Enter sample size: "))
        print('Sample List...',rm.sample(range(100),local))

#prints a random floating point between 0.0 and 1.0
print(rm.random())

#random function with start and end points
print(rm.uniform(2.4,3.15))
