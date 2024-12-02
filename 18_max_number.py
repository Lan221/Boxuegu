my_list = [1,3,4,9,7,4,5]
max_value = my_list[0]
max_index = 0

for index,value in enumerate(my_list):
    if max_value < value:
        max_value = value
        max_index = index

print(f'max number is:', max_value,'the index is:',max_index)
