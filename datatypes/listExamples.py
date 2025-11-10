# List is a collection of ordered elements
# syntax:
    # '[ ]'
# Allows duplicate elements and also different datatypes
# It is called heterogeneous collection
# List is a mutable datatype (Can modify the elements)


# List with empty elements
list1= [ ]
print(list1)
print(type(list1))
print(dir([ ])) # to get the methods associated to the list


# Example 1

list2 = 1,2,3,4,5,6,7,8,9
print(list2)
print(type(list2)) # produces tuple not list , here list is always [ ]

# Example 2
# Adding elements
list3= [1,2,3,4,5,6,7,8,9]
print(list3)

# Example for duplicates
list4 = [1,2,3,4,5,6,7,8,9, 9, 9, 6, 4, 3, 2, 1]
print(list4)


# Modify the list elements so it is mutable
list4 = [1,2,3]
print(list4)


# Modify using methods
list4.append(88)
print(list4)

# Modify and add a element in between adds in second position
list4.insert(2,100)
print(list4)

# Remove an element
list4.remove(100)
print(list4)


