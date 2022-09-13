#This is a cheatsheet for common string methods in python


#string notation
a = "Test"
a = 'Test'

#print string
print(a)


#convert to string
b = str(100)

#loop trough a string
for chars in a:
    print(chars)


#reverse a string
a = a[::-1]
print(a)

#.find Method, finds a sustring in a string, returns -1 if not found, returns position of first letter of the substring
x = a.find("T")
print(x)

#.count, counts how often a substring appears in a string
fizz = "Ababababa"
print(fizz.count("a"))


#input method
name = input("Bitte gib deinen Namen ein!")


#string insertion
print("Hallo, {name}")

#more string insertion
item = 7
print("%s is carrying %d items"%(name, item))

#string addition
print(name+a)

#string multiplication
print(7*"a")

#string seperation
print("b",a)#Standard seperator = " "
print("b",a,sep="TEST")#customizing seperator


string = "Various string methods"
string2 = " investment in learning "

#lowercase
print(string.lower())

#uppercase
print(string.upper())

#is lowercase
print(string.islower())

#is highercase
print(string.isupper())

#startswith
print(string.startswith("Var"))

#endswith
print(string.endswith("el"))

#link with array
print('-->'.join(['various', 'strings', 'methods']))

#String in array splitten
print(string.split())

#add chars, the word is on the left
print("hello".ljust(15, '*'))

#add chars, the word is on the right side
print("hello".rjust(15, '*'))

#center the word in the middle
print("welcome".center(20, '*'))

#remove spaces on both sides
print(string2.strip())

#remove spaces on left side only
print(string2.lstrip())

#remove spaces on right side only
print(string2.rstrip())


#find index of a substring
string = "object oriented programming"
print("index of 'r' in:'", string, "':", string.index('r'))

#replace method
print("replacing 'e' with '3' :", string.replace('e', '3'))




