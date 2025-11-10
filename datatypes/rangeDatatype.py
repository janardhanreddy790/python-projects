# range is used to generate the sequence of numbers
# range is created using below syntax:
    # range()
# range is immutable
# default starting value of range is '0'

# Examples

range1 = range(10)
print(range1)
print(type(range1))
print(dir(range))


range2 = range(10)
print(range2)

print(list(range1))

print(tuple(range1))


range3 = range(1, 20, 1) # (start , stop, step)
print(list(range3))

range4 = range(1, 20, 3) # (start , stop, step)
print(list(range4))




