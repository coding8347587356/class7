list1 = [2, "abc", True, 12.56]
tuple1 = (2, "abc", True, 12.56)

#list1[0] = 5
#tuple1[0] = 5

print(tuple1)

#tuple packing
address = ('244', 'Brickfiled Shelters','Banglore', 'Karnataka', '562107')

houseNo, streetName, city, state, zipCode = address

print('House Number', houseNo)
print('Street name', streetName)
print(city)
print(state)
print(zipCode)

tuple2 = 3,4, "abc", 12.45
print(tuple2)

tuple3 = ("abc", [8,4,6], [1,2,3])

print(tuple3[2][1])

tuple4 = (1,2,3,4,5,6,7,8,9,10)
print(tuple4[0:4])
print(tuple4[3:])
print(tuple4[:4])
print(tuple4[:])