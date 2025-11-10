import sys

list1=[1,2,3,4,5,6,7,8,9]
tuple1=(1,2,3,4,5,6,7,8,9)

print(list1)
print(tuple1)

print(sys.getsizeof(list1))  # list uses more memory than tuple and faster and performance is slow due to dynamic behaviour
print(sys.getsizeof(tuple1)) # tuple is better in terms of memory and slower and performance is high due to fixed set of elements


# Fixed set of elements use tuple
# When the elements are dynamic then go for list


