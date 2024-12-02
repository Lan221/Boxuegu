
# def input_student_info():
#     name = input("please input student's name:")
#     age = int(input("please input the student's age:"))
#     student_dict = {'name':name, 'age':age}
#     return student_dict


# for i in range(3):
#     student_dict = input_student_info()
#     student_info.append(student_dict)
# print(student_info)
student_info = [{'name': 'Yuhan', 'age': 9}, {'name': 'Marco', 'age': 10}, {'name': 'Sergio', 'age': 10}]

def select_student():
    name_search = input ('please input name you would like to search:')
    for i in student_info:
        if i['name'] == name_search:
            print(f'name:{name_search},age:{i['age']}')
            return
    else:
        print(f'{name_search} can not find the list.')

def student_total_num():
    return len(student_info)

print('----- student info-------')

if __name__ == "__main__":
    num = 1
    for student in student_info:

        print(f"{num} \t {student['name']} \t {student['age']}")
        num += 1

    print('total student is: ',student_total_num())
    # Search for a student
    select_student()