names=[ "Luffy" , "Zoro" , "Nami" , "Sanji"]
favourite_colour=["Red" , "Blue" , "Green" , "Orange"]

nColour = input("Whats your favourite colour? ")
favourite_colour.append(nColour)

nName = input("Whats your name? ")
names.append(nName)

print(names)
print(favourite_colour)

Delete = input("Choose a colour to remove from the list ")
if Delete in favourite_colour:
    print(Delete + " found in list")
    ID = favourite_colour.index(Delete)
    names.pop(ID)
    favourite_colour.remove(Delete)
    print(favourite_colour)
    print(names)
