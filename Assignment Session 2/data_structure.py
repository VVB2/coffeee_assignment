#Note each block is one Assignment Question
from array import *

#Array

array_num = array('i', [1,3,5,3,7,3,9])
for i in array_num:
    print(i)
print("Access first three items individually")
print(array_num[0])
print(array_num[1])
print(array_num[2])

array_num.reverse()
print(array_num)

print(array_num.count(3))

array_num.remove(3)
print(array_num)

#Dictionary

