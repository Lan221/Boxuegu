2#age = int (input('please input your age'))
#if age >= 18:
#    print('you could enter')
#    print('you could not enter')
# name = input('please input your name:')
# if name == 'admin' or name == 'test':
#     print(f'welcome {name}')
# else:
#     print('do not have this person')

import random
while True:
    computer = random.randint(1,3)
    manuel_input = int(input('please input a number:'))
    if manuel_input == 0:
        print('welcome to play this game next time')
        break
    if manuel_input !=1 and manuel_input !=2 and manuel_input !=3:
        print('input correct number')
        continue
    if computer > manuel_input:
        print(f' computer {computer},manuel {manuel_input}, computer wins')
    elif computer < manuel_input:
        print(f'computer {computer},manuel {manuel_input},manuel wins')
    else:
        print('it is equal')






