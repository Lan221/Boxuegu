import random
my_list = []
for i in range (5):
    name = input('please input the name:')
    my_list.append(name)
print(my_list)
num=random.randint(0, 4)
while True:
    if int(input('input the number:')) == 1:
        break
    else:
        print(my_list[num],num)
        print(random.choice(my_list))
