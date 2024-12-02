# age = int(input('please enter your age:'))
# if age >= 65:
#     print('you may retire now')
# else:
#     print('you have to continue to work')

while True:

    user_name = input('please input your user name:')
    user_pwd = input('please input your password:')
    user_code = input('please input the verify code:')

    if user_code == 'qwer':
        if user_name == 'lan' and user_pwd == '1234':
            print ('login in successful')
            break
        elif user_name == 'exit':
            break
        else:
            print ('user name or password is incorrect')

    else:
        print('please input correct verify code')
        break

