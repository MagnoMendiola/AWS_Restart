#--Ejercicio 1
myString = "This is a string"
print(myString)

print(type(myString))

print(myString+ " is of the data type "+str(type(myString)))

print(myString ,'is of the data type',str(type(myString)))

#--Ejercicio 2

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)


#--Ejercicio 3
name = input("What is your name? ")
print(name)

#--Ejercicio 4

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

print("{}, you like a {} {}!".format(name,color,animal))
