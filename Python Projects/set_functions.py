#intersection
def set_intersect(set1,set2):
    """
    Parameters: Set_one, Set_two
    Returns the intersection of the two sets as a set
    '---' if no intersect found
    """
    tset=set()
    for i in set1:
        if i in set2:
            tset.add(i)
    if tset=={}:
        return '---'
    return tset

#-----------
#CoderByte
if False:
    def FindIntersection(strArr):
      # code goes here
      temp=list(set(strArr[0].split(', '))&set(strArr[1].split(', ')))
      output=sorted(int(x) for x in temp)
      return ','.join(map(str,output))

    # keep this function call here 
    print(FindIntersection(input()))

#-----------

def set_union(set1,set2):
    """
    Parameters: Set_one, Set_two
    Returns the union of the two sets as a set
    """
    tset=set()
    for i in set1:
        if i not in tset:
            tset.add(i)
    for j in set2:
        if j not in tset:
            tset.add(j)
    return tset

def set_difference(set1,set2):
    """
    Parameters: Set_one, Set_two
    Subtracts the sets: return_Set = Set_one - Set_two
    """
    tset=set1-set2
    return tset

if __name__=='__main__':
    set_one=set(input("Enter Set -- ").split(','))
    set_two=set(input("Enter Set -- ").split(','))
    print("Intersection:\n",set_intersect(set_one,set_two))
    print("Union:\n",set_union(set_one,set_two))
    print("Difference:\n",set_difference(set_one,set_two))
    print(set_one.difference(set_two))
    print(set_one,set_two)
