#This is a cheatsheet for common string methods in python


#string notation
a = "Test"
a = 'Test'

#string ausgeben
print(a)


#integer / float in string konvertieren
b = str(100)

#Durch string loopen, chars ist hierbei der Buchstabe
for chars in a:
    print(chars)


#string umkehren
a = a[::-1]
print(a)

#.find Method, findet Position des Buchstaben, -1 wenn nicht gefunden
x = a.find("T")
print(x)

#.count, zählt wie oft ein substring vorkommt
fizz = "Ababababa"
print(fizz.count("a"))


#input method
name = input("Bitte gib deinen Namen ein!")


#string insertion
print("Hallo, {name}")

#more string insertion
item = 7
print("%s is carrying %d items"%(name, item))

#string Addition
print(name+a)

#string Multiplikation
print(7*"a")

#string seperation
print("b",a)#Standard seperator = " "
print("b",a,sep="TEST")#customizinh seperator


string = "Various string methods"
string2 = " investment in learning "

print(string.lower())#in Kleinbuchstaben

print(string.upper())#in Großbuchstaben

print(string.islower())#Ist kleingeschrieben

print(string.isupper())#Ist großgeschrieben

print(string.startswith("Var"))#Beginnt mit

print(string.endswith("el"))#Ended mit

print('-->'.join(['various', 'strings', 'methods']))#mit array verknüpfen

print(string.split())#String in array splitten

print("hello".ljust(15, '*'))#Zeichen hinzufügen, Wort links

print("hello".rjust(15, '*'))#Zeichen hinzufügen, Wort rechts

print("welcome".center(20, '*'))#Wort zentriert in der Mitte

print(string2.strip())#Leerzeichen links und rechts entfernen

print(string2.lstrip())#Leerzeichen links entfernen

print(string2.rstrip())#Leerzeichen rechts entfernen


string = "object oriented programming"
print("index of 'r' in:'", string, "':", string.index('r'))#Index eines substrings heruasfinden

print("replacing 'e' with '3' :", string.replace('e', '3'))#String ersetzen




