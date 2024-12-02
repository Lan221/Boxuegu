import json
import random

# try:
#     num = int(input('please input a number:'))
#     print (f'{num} is an even number')if num % 2 == 0 else print(f'{num} is an odd number')
#
# except Exception as e:
#     print(f'please input correct number {e}.')

my_list = [random.randint (0,100)for i in range(5)]
print(my_list)
my_list.sort()
print(my_list)

with open('data.json','a',encoding ='utf-8') as f:
    json.dump(my_list,f)

