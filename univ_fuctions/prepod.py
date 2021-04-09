#from univ_fuctions.pswrd import *
#from univ_fuctions.cl import *

def menu_prepoda(login):
    while True:
        print(
            '1 - информация о студентах\n2 - получить информацию о студенте\n3 - добавить студента\n4 - добавить преподавателя\n5 - поставить оценку\n6 - изменить оценку\n0 - выход')
        type = int(input('Сделайте выбор (или 0 для выхода):'))
        if type == 1:
            print('информация о студентах')
            db = DataBase()
            data = db.getUser()
            del db
            for element in data:
                print(element["id"], element["name"], element["surname"], element["fakultet"], element["group_number"])
        elif type == 2:
            students = []
            db = DataBase()
            data = db.getUser()
            del db
            for element in data:
                students.append(element["id"])
            print(students)
            id = int(input('Информация о студенте, введите id:'))
            if id in students:
                db = DataBase()
                data, data2 = db.infoStudent(id)
                del db
                for element in data:
                    print(element["name"], element["surname"], element["fakultet"],
                          element["group_number"])
                data2 = data2[0]
                for key in data2:
                    if data2[key] == None:
                        data2[key] = 'б/о'
                    print(key, ":", data2[key])
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
            del db
            print(len(data), "преподавателя(ей) можно добавить в БД:")
            if len(data) > 0:
                for element in data:
                    print(element["id"], element["name"], element["fakultet"], element["predmet"])
                    prepods_to_confirm.append(element["id"])
                print('доступные варианты:', prepods_to_confirm)
                prepod_id = int(input('введите id преподавателя для установки логина (или 0 для выхода):'))
                if prepod_id in prepods_to_confirm:
                    db = DataBase()
                    db.confirmLoginToPrepod(prepod_id)
                    print('Преподаватель добавлен. Предмет добавлен.')
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
            del db
            print('оценка поставлена')
        elif type == 6:
            number_pr = input(
                'введите номер практики [1],[2],[3] курсовую [k] или экзамен [e] (или 0 для выхода):')
            if number_pr == 'k' or number_pr == 'к':
                number_pr = 'kurs'
            elif number_pr == 'e' or number_pr == 'е':
                number_pr = 'ekzamen'
            id = input('введите id студента:')
            mark = input('поставить новую оценку:')
            db = DataBase()
            db.mark(login, number_pr, id, mark)
            del db
            print('Оценка установлена')
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
    student_password = 'temp' + student_login
    student_password = shifr_pswrd(student_password)
    db = DataBase()
    db.addUserStudent(student_login, student_password, type, name, surname, fakultet, group_number)
    del db
    print("студент <", name, surname, fakultet, group_number, student_login,
          "> добавлен, установлен временный пароль: temp[login]")