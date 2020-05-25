#dictioning 1
#NULL substituted by "None" in Pyhton
var=None
print(var)
print(None)
#Dictionaries: key-value pairs
lst={"n":1,'i':2,'a':3,'d':3}
print(lst['n'])
print(lst['d'])
bi={"one":[0,0,1],"two":[0,1,0],"three":[0,1,1]}
print("Binary representation of three: "+str(bi["three"]))
#This cannot be done
#lst={[1,2,3]:"one two three",[0,0,2]:"zero zero two"}
ls={12:14,15:17,32:12}
print(ls[12])   #This doesnot cause a KeyError
#print(ls[14])  This causes KeyError
#Key-Value pair is always ordered as___Key:Order___
print(ls[32])
#dictioning 2
dic={1:5,2:25,3:"error"}
print(dic)
dic[3]=625          #reassigning different value to existing key
dic[4]=625*5        #adding additional keys to dic
dic[5]=dic[4]*5     #adding additional keys to dic
print(dic)
#searching for keys using 'in' and 'not in'
#only works for keys and not values
print(2 in dic)     #true
print(625 in dic)   #false because no "625" key
print(7 in dic)     #false
#dictionary.get()
#dic[None]="default statement"   #inserting default key to the dictionary, given by 'None:"Value"'
#default value need not be inserted explicitly
print(dic.get(4))
print(dic.get(6,dic[5]*5))  #Temporarily inserting new element pair and displaying value
print(dic.get(45))          #default value will be called
print(dic)
