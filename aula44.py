# sets, utilizar s1 = set() ou s1 = {} 
l1 = [1,2,3,4,5,6,7,8,4,4,4,1,1,1]
s1 = set(l1)
# s1 = {1,2,3,4,3,3,3,1}
l2 = list(s1)
print(l1, type(l1))
print(s1, type(s1))
print(l2, type(l2))

print(7 in s1)