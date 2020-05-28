file=open("ninad.txt","r")
print("Previous contents of File:\n")
for line in file:
    print(line)
file=open("ninad.txt","w")
_len=file.write("Writing through Program Part 2\nTry Adding New Line")
file.close()
file=open("ninad.txt","r")
print("\nNew contents of File:\n")
for i in file:
    print(i)
print("\nCharacters in File "+str(_len))
# good practice to use try, finally statements for file operations. So that files are closed after use.
try:
    f=open("nancy.txt","w")
    f.write("Write to File\nAdding Line Breaks\nAdding Another One\nAnd Another\nAnd Another\n.\n.\n.\n...To Be Continued")
finally:
    f.close()
try:
    f=open("nancy.txt","r")
    for line in f:
        print(line)
finally:
    f.close()
#An alternative to try, finally statements we may use with ... as ... statement
with open("nancy.txt","r") as fi:
    print("\nReading through with ... as statement")
    for line in fi:
        print(line)
