# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2, 4 : 3}

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

# re-declaring a variable works
myint="Vishnu"
print(myint)
myfloat=False
print(myfloat)


# to access a member of a sequence type, use []
print(mylist[0])
print(mylist[1])
print(mylist[4])


# use slices to get parts of a sequence
print(mylist[1:3])
print(mylist[2:3])
print(mylist[1:5:2])

# you can use slices to reverse a sequence
print(mylist[::-1])

# dictionaries are accessed via keys
print(mydict[4])
print(mydict["one"])
print(mydict["two"])

# ERROR: variables of different types cannot be combined
print(6+myfloat+True+True)
print("Vishnu "+str(456))
print("Appu "+"123")

# Global vs. local variables in functions
def NewFunction():
    global mystr 
    mystr= "ABC"
    print(mystr)
    
NewFunction()
print(mystr)

