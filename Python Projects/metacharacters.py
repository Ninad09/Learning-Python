import re
raw=r"\r\a\w string"
#no escape functions called
print(raw)

#meta 1
line=r"num.er$"  #. matches any charcter except the new line character
if re.match(line,"number"):
    print("match 1")
if re.match(line,"numzer"):
    print("match 2")
if re.match(line,"num\ter"):
    print("match 3")
#match() checks for string length first
if re.match(line,"mean numper"):
    print("match 4")
#^ start
#$ end

#character classes
cls=r"[t,r,i,a,d]"
if re.search(cls,"ninad"):
    print("match 1")
#returns true for any charcter of character class present in string
if re.search(cls,"mirage"):
    print("match 2")
if re.search(cls,"Neevu"):
    print("match 3")

#[A-Z] any uppercase character from A to Z
#[a-z] any lowercase character from a to z
#combine [A-Za-z] any charcter of any case

#[4-9] any number from 4 to 9, extremes included
#[a-z][A-Z][3-8] string length:3 characters and order specified

#[^A-Z] matches all charcter except the mentioned in character class
line1=r"[^a-z]"
if re.search(line1,"ALL UPPERCASE"):
    print("Match 1")
if re.search(line1,"Some Uppercase and number 012893"):
    print("Match 2")
if re.search(line1,"all lowercase will match for empty spaces"):
    print("Match 3")
if re.search(line1,"nouppercase"):
    print("Match 4")
