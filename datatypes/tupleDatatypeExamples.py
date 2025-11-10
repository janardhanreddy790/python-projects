# Tuple is also ordered collection
# syntax:
    # () also can be created without parenthesis
# Allows duplicate elements
# Allows different types are allowed
# It is a mutable datatype meaning it cannot be modified once created.
# one can create a tuple with a single element with a comma (,) after the element
    # (1,)
# Examples:

# declaration
tuple1 = ()
print(tuple1)
print(type(tuple1))

# single element
tuple2 = (100,)
print(tuple2)
print(type(tuple2))

# multiple elements
tuple3 = (100,200,300)
print(tuple3)

# Different datatypes
#tuple4(10) = (100,200,300, "Hey", 10.2, True) # Allows different data types in a tuple
#print(tuple4)

# tuple methods
print(dir(()))

# tuple cannot be indexed as below
tuple5 = (100)


# In terms of memory tuple is better than list where performance wise list is better uses more memory

