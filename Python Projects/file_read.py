file=input("Enter File Name:: ")
with open(file) as f:
    text=f.read()
print(text)

def count_char(txt,char):
    cnt=0
    for c in txt:
        if c==char.lower() or c==char.upper():
            cnt+=1
    return cnt

#print('\r',"\nNumber of Occurences of 'M':: ",count_char(text,'m'))
print("\n\nPercentage of all letters:")
for ch in "abcdefghijklmnopqrstuvwxyz":
    percent=round(100*count_char(text,ch)/len(text),2)
    print("{}::{}%".format(ch,percent))
