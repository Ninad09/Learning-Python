#Domain specific languages are highly specialized mini programming languages.
#Regular expressions are a popular example, and SQL (for database manipulation) is another.
import re
pat=r"ninad"
#r"" raw string, there are no escape characters
if re.match(pat,"Ninad Deshpande"):
#re.match checks for match in the beginning of the string
    print("Match")
else:
    print("No Match")
#re.match() is case sensitive

#re.search() finds occurence of first parameter string anywhere in the second parameter
st="shruti"
girls="poorva gogate shruti govande aarya rao manali chavan shruti govande"
match=re.search(st,girls)
print(match)
#group(), start(), end(), span()
if match:
    print("Group: ",match.group())
    print("Start: ",match.start())
    print("End: ",match.end())
    print("Span: ",match.span())
#re.match and re.search return 'Match Objects' or 'None'

#re.findall locates all occurences and returns a list of them
print("FindAll: ",re.findall(st,girls))

#re.finditer returns iterator
for word in re.finditer(st,girls):
    print(word)
    #match objects

#re.sub()
#substitutes all occurences of first parameter string with second paramater string  in third parameter string
newgirls=re.sub(st,"-shruti-",girls)
print(newgirls)
