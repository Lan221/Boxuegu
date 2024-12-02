import pytest


def password():
    data = input('please input the password:')
    if len(data) >= 8:
        print('correct ')
    else:
        raise Exception('the lengh password is minimum 8')

if __name__ == '__main__':
    password()
    pytest.main(['-s','_36_input_password.py'])