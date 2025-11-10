# str is a group of characters or sequence of characters.
# Usage:
    # str can be created by using '', "", ''', """
    # mutable: We cant change the value once assigned
    # immutable: Can re assign the value
    # str is immutable
#Examples:
stringVar = 'Hello Python'
print(stringVar)
print(stringVar.lower())
print(stringVar.upper())
print(stringVar.title())
print(type(stringVar))



# '''
# Mostly used for multiple lines

stringVar1 = '''Hello Python'''
print(stringVar1)
print(stringVar1.lower())
print(stringVar1.upper())
print(stringVar1.title())
print(type(stringVar1))

# '''
# Mostly used for multiple lines

stringVar2 = '''Hello Python
Welcome to the learning 
you can learn more about Python'''
print(stringVar2)
print(stringVar2.lower())
print(stringVar2)
print(stringVar2.lower())
print(stringVar2.upper())
print(stringVar2.title())
print(type(stringVar2))


stringVar3 = 'Citie\'s'
print(stringVar3)
print(stringVar3.lower())
print(stringVar3)
print(stringVar3.lower())
print(stringVar3.upper())
print(stringVar3.title())
print(type(stringVar3))


stringVar4 = "Citie's"
print(stringVar4)
print(stringVar4.lower())
print(stringVar4)
print(stringVar4.lower())
print(stringVar4.upper())
print(stringVar4.title())
print(type(stringVar4))



# string methods
print(dir(str))


# to get the help to use the string
help(str)

# Immutable

stringReplace = 'Hello Python'
print(stringReplace)

stringReplace.replace("Python", "Java")
print(stringReplace)

# instead this will create a new string
newString = stringReplace.replace("Python", "Java")
print(newString)

# ALso  this creates a new string
print(stringReplace.replace("Python", "json"))

