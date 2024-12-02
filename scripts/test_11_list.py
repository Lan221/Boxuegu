import random
my_list = []
for i in range(10):
    num = random.randint(1,20)
    my_list.append(num)
print(my_list)
print('number 8 appears:',my_list.count(8))
my_list.pop(2)
print('new list:',my_list)
my_list.sort()
print('after sorting:',my_list)
my_list.sort(reverse=True)
print('2nd time sorting:',my_list)
