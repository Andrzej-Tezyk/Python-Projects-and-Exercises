nested_list = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
print(nested_list)

print(len(nested_list))
print(len(nested_list[1]))
print(len(nested_list[-1]))

print(nested_list[1][1])

print(nested_list[3][2])
print(nested_list[-1][2])
print(nested_list[3][-2])
print(nested_list[-1][-2])

for inner_list in nested_list:
    print(inner_list)

for inner_list in nested_list:
    for number in inner_list:
        print(number)