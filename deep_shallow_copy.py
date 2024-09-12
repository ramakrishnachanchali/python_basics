import copy
l1 = [1,2,3,[4,5],6]

l1[3].append(7)
l2 = copy.copy(l1)
l2[3].append(8)
print(l1)
print(l2)

l3 = [1,2,3,[4,5],6]

l3[3].append(7)
l4 = copy.deepcopy(l3)
l4[3].append(8)
print(l3)
print(l4)
