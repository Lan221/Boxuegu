my_list=['test','goods','table','pink','like']
my_new_list = []
for i in my_list:
    if i[-1]=='s' or i[-1]=='e':
        my_new_list.append(i)
print('my_new_list:',my_new_list)
