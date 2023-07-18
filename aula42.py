import copy
d1 = {
    'c1': 1,
    'c2': 2,
    'c3': 3,
    'l1': [0,1,2,3,4]
}

d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2['l1'][2] = 99999

print(d1)
print(d2)