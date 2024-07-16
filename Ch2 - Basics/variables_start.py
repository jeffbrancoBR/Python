# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
# modified by Juan Rodriguez on 07/16/2024
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2, "three" : 3}

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

# re-declaring a variable works
myint = "abc"
print(myint)

# to access a member of a sequence type, use []
print(mylist[4])
print(mytuple[0])

# use slices to get parts of a sequence
print(mylist[1:5])
print(mylist[1:5:2])

# you can use slices to reverse a sequence

print(mylist[::-1])

# dictionaries are accessed via keys

print(mydict["three"])

# ERROR: variables of different types cannot be combined

print("This is a string" + str(123)) #this works due to the str() function

# Global vs. local variables in functions

def myFunction():
    global mystr
    mystr = "hello"
    print(mystr)

myFunction() # this will print the local variable mystr see function for this
print(mystr) # this will print the global variable mystr
del mystr # this will delete the global variable mystr
print(mystr) # this will cause an error because mystr is no longer defined