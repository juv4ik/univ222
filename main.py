from univ_fuctions.pswrd import *
from univ_fuctions.cl import *
#from univ_fuctions.prepod import *
#from univ_fuctions.student import *
#from univ_fuctions.reg import *

def menu_studenta(login):
    def d():
        db = DataBase()
        data = db.student_info_o_sebe(login)
        return data
    data = d()
    for element in data:
        id = element["id"]
    while True:
        print('1 - информация о себе\n2 - средний балл\n3 - номер группы\n4 - фио\n5 - информация о предметах\n9 - изменить пароль\n0 - выход')
        type = int(input('Сделайте выбор (или 0 для выхода):'))
        if type == 1:
            print('информация о', login, ':')
            #data = d()
            for element in data:
                print(element["id"], element["name"], element["surname"], element["fakultet"], element["group_number"])
        elif type == 2:
            print('средний балл')
            db = DataBase()
            data = db.student_marks(id)
            for element in data:
                print(element["prep5_1"])
        elif type == 3:
            print('номер группы')
            data = d()
            for element in data:
                print(element["group_number"])
        elif type == 4:
            print('фио')
            #data = d()
            for element in data:
                print(element["name"], element["surname"])
        elif type == 5:
            print('информация о предметах: круг круглый, а квадрат квадратный')
        elif type == 9:
            print('изменить пароль', login)
            new_password = shifr_pswrd(input('введите новый пароль (или 0 для выхода):'))
            if new_password == 'a':
                print('canceled...')
            else:
                db = DataBase()
                db.changePassword(login, new_password)
                del db
                print('пароль изменен')
        elif type == 0:
            break
        else:
            print('что-то не то нажали')

def menu_prepoda(login):
    while True:
        print(
            '1 - информация о студентах\n2 - получить информацию о студенте\n3 - добавть студента\n4 - добавить преподавателя\n5 - поставить оценку\n6 - изменить оценку\n0 - выход')
        type = int(input('Сделайте выбор (или 0 для выхода):'))
        if type == 1:
            print('информация о студентах')
            db = DataBase()
            data = db.getUser()
            for element in data:
                print(element["id"], element["name"], element["surname"], element["fakultet"], element["group_number"])
        elif type == 2:
            students = []
            db = DataBase()
            data = db.getUser()
            for element in data:
                students.append(element["id"])
            print(students)
            id = int(input('Информация о студенте, введите id:'))
            if id in students:
                db = DataBase()
                data = db.infoStudent(id)
                for element in data:
                    print(element["id"], element["name"], element["surname"], element["fakultet"],
                          element["group_number"])
            else:
                print('студента с таким id в базе нет')
        elif type == 3:
            prep_add_student()
            print('добавить студента:')
        elif type == 4:
            print('--------------добавить преподавателя')
            prepods_to_confirm = []
            db = DataBase()
            data = db.confirmPrepod()
            print(len(data), "преподавателя(ей) можно добавить в БД:")
            if len(data) > 0:
                for element in data:
                    print(element["id"], element["name"], element["fakultet"], element["predmet"])
                    prepods_to_confirm.append(element["id"])
                print('list a:', prepods_to_confirm)
                prepod_id = int(input('введите id преподавателя для установки логина (или 0 для выхода):'))
                if prepod_id in prepods_to_confirm:
                    db.confirmLoginToPrepod(prepod_id)
                elif type == 0:
                    break
                else:
                    print('введен неверный id')
            if len(data) == 0:
                print('нет преподавателей для добавления в БД')
        elif type == 5:
            number_pr = input(
                'введите номер практики [1],[2],[3] курсовую [k] или экзамен [e] (или 0 для выхода):')
            if number_pr == 'k' or number_pr == 'к':
                number_pr = 'kurs'
            elif number_pr == 'e' or number_pr == 'е':
                number_pr = 'ekzamen'
            id = input('введите id студента:')
            mark = input('поставьте оценку:')
            db = DataBase()
            db.mark(login, number_pr, id, mark)
            print('оценка поставлена')
        elif type == 6:
            print('изменить оценку')
        elif type == 0:
            break
        else:
            print('что-то не то нажали')

def prep_add_student():
    type = "s"
    name = input('введите имя:')
    surname = input('введите фамилию:')
    fakultet = input('введите факультет:')
    group_number = input('введите группу:')
    student_login = input('введите логин:')
    student_password = 'temp'+student_login
    student_password = shifr_pswrd(student_password)
    db = DataBase()
    db.addUserStudent(student_login, student_password, type, name, surname, fakultet, group_number)
    del db
    print("студент <", name, surname, fakultet, group_number, student_login, "> добавлен, установлен временный пароль: temp[login]")


def main():
    while True:
        print('========Start:========')
        print('1 - Авторизация')
        print('2 - Регистрация')
        type = int(input('Сделайте выбор (или 0 для выхода):'))
        if type == 1:
            print('Авторизация. Введите запрашиваемые данные:')
            login = input('login:')
            password = input('password:')
            db = DataBase()
            data = db.getPassword(login=login)
            for element in data:
                pass
                #print(element["password"])
            if password == deshifr_pswrd(element["password"]):
                print("...Авторизация прошла успешно,", element["name"], hide_password(password))
                if element["type"] == "s":
                    menu_studenta(login=login)
                else:
                    menu_prepoda(login=login)
            else:
                print("ne ok")
        elif type == 2:
            print('Регистрация. Введите запрашиваемые данные:')
            register()
        elif type == 0:
            break
main()
