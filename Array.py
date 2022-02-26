#Array and thier functions
#append, buffer info, clear, copy, count, ectend, index,insert, pop, remove, reverse, sort
from array import * # import all functions from array lib
val1 = array('i',[4,6,5,3,5,7])
val2 = array('i',[4,5,7,8,4,7])
print(val1)
print(val2)
print(type(val1))
#append:add single element to last
val1.append(7)
print(val1)
print(val1.buffer_info())# Returns the address and size of array 
cont = val1.count(7) # count number of type value returned
print(cont)