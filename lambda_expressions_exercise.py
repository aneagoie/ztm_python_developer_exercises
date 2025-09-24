#Create a lambda expression to square the following:
my_list = [5,4,3]


print(list(map(lambda num: num**2, my_list)))

#Sort tuple by the second key
a = [(0,2), (4,3), (9,9), (10,-1)]

a.sort(key=lambda x: x[1])
print(a)