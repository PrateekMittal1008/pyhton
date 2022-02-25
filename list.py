#list and their functions
# sorting,append, entend, reverse, remove, insert, copy, count, index, pop, clear 
lst = [45,77,55,35,45,33]
lst2 = [45,56,32]
#sorting forward
lst.sort()
print(lst)
#sorting reverse
lst.sort(reverse=True)
print(lst)
#Append add single element to last
lst.append(43)
print(lst)
#extend multiple elements to last
lst.extend(lst2)
print(lst)
#list reversing
lst.reverse()
print(lst)
#remove an element
lst.remove(56)
print(lst)
#insert and element with specified space
lst.insert(2, 56)
print(lst)
#count Occurance of elements in list
count=lst.count(56)
print(count)
#index value retrun
ind=lst.index(56)
print(ind)
#pop
lst.pop(2)
print(lst)
#end of code