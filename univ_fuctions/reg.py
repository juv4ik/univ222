from univ_fuctions.pswrd import *
from univ_fuctions.cl import *

def reg_student():
    type = "s"
    name = input('введите имя:')
    surname = input('введите фамилию:')
    fakultet = input('введите факультет:')
    group_number = input('введите группу:')
    student_login = input('введите логин:')
    student_password = input('введите пароль:')
    student_password = shifr_pswrd(student_password)
    db = DataBase()
    db.addUserStudent(student_login, student_password, type, name, surname, fakultet, group_number)
    del db
    print("студент <", name, surname, fakultet, group_number, student_login, "> добавлен")


def reg_prepod():
    type = "p"
    password = input('введите пароль:')
    name = input('введите имя:')
    surname = input('введите фамилию:')
    fakultet = input('введите факультет:')
    predmet = input('введите предмет:')
    password = shifr_pswrd(password)
    db = DataBase()
    db.addUserPrepod(password, type, name, surname, fakultet, predmet)
    del db
    print("преподаватель", name, surname, fakultet, predmet, "добавлен.\nПосле проверки логин установит главный преподаватель.")


def register():
    while True:
        member = input('введите данные: 1 - студент, 2 - преподаватель:')
        if int(member) == 1:
            print('регистрация студента')
            reg_student()
        elif int(member) == 2:
            print('регистрация преподавателя')
            reg_prepod()
        elif int(member) == 0:
            break
        else:
            print('вы ввели неверные данные')