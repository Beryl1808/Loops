#Input a word or a sentence
string=input("Please enter your string:")

string2=("")

for i in string:
    string2= i + string2

print("\nThe Original string =",string)
print("The Reversed string =",string2)