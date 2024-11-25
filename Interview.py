###
# Q: 12345*
# Output:
#   12345*
#   1234*5
#   123*45
#   12*345
#   1*2345
#   *12345 ###

#Method:1
l=[1,2,3,4,5]
lenth = len(l)
index = lenth
for i in range(lenth+1):
    newlist=l.copy()
    newlist.insert(index,"*")
    print(newlist)
    index -= 1

Method:2
numbers = [1, 2, 3, 4, 5]
number_str = ''.join(map(str, numbers))
for i in range(len(number_str)):
    print(number_str[:len(number_str)-i-1] + '*' + number_str[len(number_str)-i-1:])

