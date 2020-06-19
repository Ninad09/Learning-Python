from datetime import datetime

lst3=[{'name':"Ninad",'date':"09 Jan 2001"},{'name':"Aarya",'date':"24 Nov 2000"},{'name':"Shruti",'date':"26 Nov 1999"},
      {'name':"Poorva",'date':"04 Jan 2000"},{'name':"Manali",'date':"29 Nov 2000"}]

for i in range(len(lst3)):
    print(lst3[i]['name'],': ',lst3[i]['date'])
print('\r')

def _ssearch(a):
    for key in range(0,len(lst3)):
        if a==lst3[key]['name']:
            return key
    return False
while True:
    name=str(input("\nEnter a name to search: "))
    if name=='exit':
        break
    nm=_ssearch(name)
    if nm!=False:
        print("Birthday::",lst3[nm]['date'])
    else:
        print("Retry with a different entry")

#sorting according to date
lst3.sort(key=lambda i:datetime.strptime(i['date'],'%d %b %Y') )

#print(lst3)
print("\nSorted by date of birth:\n")
for i in range(len(lst3)):
    print(lst3[i]['name'],': ',lst3[i]['date'])
print('\r')

while True:
    name=str(input("\nEnter a name to search: "))
    if name=='exit':
        break
    nm=_ssearch(name)
    if int(nm):
        print("Birthday::",lst3[nm]['date'])
    else:
        print("Retry with a different entry")

#===================================================
#Nothing Executed further
if False:
    lst=[21,84,51,3,0,4,7,51,82,72,40]

    #temporary sort ascending
    print(sorted(lst))
    #temporary sort descending
    print(sorted(lst,reverse=True))

    #permanent sorting
    lst.sort()
    print(lst)      #print start to end
    print(lst[::-1])#print end to start

    def myfunc(a):
        return len(a)

    lst2=['Ninad','Soniya','Bhoomika','Aarya','Poorva','Manali','Shruti','Pragat','Sahil']

    #for reverse sorting
    #lst2.sort(key=myfunc,reverse=True)

    #for normal sorting
    #lst2.sort(key=myfunc)

    lst2.sort() #this results in sorting as per letters of words
    lst2.sort(key=myfunc)

    print(lst2)
    print(lst2[::-1])
    print()
    print()

#-----------------------------------------------

    names={'Shruti':"26 Nov 1999",'Poorva':"04 Jan 2000",'Aarya':"24 Nov 2000",'Manali':"29 Nov 2000",'Ninad':"09 Jan 2001"}

    #for key in names:
    #    print(key,':',names[key])

    def _search(a):
        for key in names:
            if a==key:
                return True
        return False
    while True:
        #name=str(input("\nEnter a name to search: "))
        name="exit"
        if name=='exit':
            break
        elif _search(name):
            print("Birthday::",names[name])
        else:
            print("Retry with a different entry")
