import itertools

#count(int) counts up from parameter to infinity
#cycle()    iterates infinitely through a iterable (list, string, ...)
#repeat()   repeats an objects either infinitely or a specific number of times

#count()
print("Count Up from 6::",end=' ')
for i in itertools.count(6):    #count(arg1,arg2) second argument defines jump
    print(i,end=' ')
    if i>15:
        break
print()
#cycle()
cycl,i=itertools.cycle("Ninad "),0    # count(list or string) repeats indefinitely
for value in cycl:
    print(value,end='')
    i+=1
    if i>59:
        break
print()
# repeat()
rep=itertools.repeat("Shruti ",5)
print(''.join(list(rep)))

#accumulate()
#adds all elements of list and returns the value
nums=list(itertools.accumulate(range(8)))
print(nums)

#takewhile()
#returns value as long as a conditon is True
less10=list(itertools.takewhile(lambda v:v<10,nums))
print(less10)
#stops returning values after the first time the condition is false

#product()
#works like cartesian product of sets (2 or more)
prod=list(itertools.product(nums,less10,range(2)))
#all arguments need to be a list
#product of list with itself can be obtained using repeat=x as the second argument
#lst=list(itertools.product(nums,repeat=1)) list nums is taken twice i.e. repeated once
print(prod)

#permutations
perm=list(itertools.permutations(nums,2))
#perm=list(itertools.permutations(nums))
#no second argument gives all possible permuations of length eaual to length of the list
#specifying second argument (int) gives length of required permutations
print(perm)
