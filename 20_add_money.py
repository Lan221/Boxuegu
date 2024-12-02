# money_list =[{'id': 1, 'money':10},
#             {'id': 2, 'money':20},
#             {'id': 3, 'money':30},
#             {'id': 4, 'money':40},
#             {'id': 5, 'money':50},]
# for i in money_list:
#     if i.get('id')%2 == 0:
#         i['money'] += 10
#     else:
#         i['money'] += 20
#
# print(money_list)

my_string = input('请输入字符串：')
my_dict = {}
for i in my_string:
    my_dict[i]=my_string.count(i)

    print(my_dict)




