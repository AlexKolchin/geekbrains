# Напишите функцию, которая создаёт комбинацию двух списков таким образом:
#
# [1, 2, 3] (+) [11, 22, 33] -> [1, 11, 2, 22, 3, 33]

list1 = [3, 4, 5, 6]
list2 = [33, 44, 55, 66]
list3 = []
print('List 1 - ', list1)
print('List 2 - ', list2)
def lists(list1, list2):
    for i in range(len(list1)):
        list3.append(list1[i])
        list3.append(list2[i])
        i += 1
    return list3

print('List 3 - ', lists(list1, list2))