tuple1 = (23, 43, 45, 34, 34)
tuple2 = (23.53, 12, 'Aryan', True)

print(tuple1)
print(tuple2)


print(tuple1[2])
print(tuple2[1:3])

#Concatination of tuples
tuple3 = tuple1 + tuple2
print(tuple3)

#Printing multiple of a tuple
print(tuple1 * 5)

#Finding the length of a tuple
print(len(tuple1))

#Packing and Unpacking
#Packing
#tuple4 = (10, 20, 30, 40)
tuple4 = (10, 20, 30)

#Unpacking
x, y, z = tuple4
print(x, y, z)
