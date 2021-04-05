def menu_prepoda():
    while True:
        print('1 - информация о студентах\n2 - получить информацию о студенте\n3 - добавть студента\n4 - добавить преподавателя\n5 - поставить оценку\n6 - изменить оценку\n0 - выход')
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
                    print(element["id"], element["name"], element["surname"], element["fakultet"], element["group_number"])
            else: print('студента с таким id в базе нет')
        elif type == 3:
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
            print('поставить оценку')
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
    student_password = input('введите пароль:')
    student_password = shifr_pswrd(student_password)
    db = DataBase()
    db.addUserStudent(student_login, student_password, type, name, surname, fakultet, group_number)
    del db
    print("студент <", name, surname, fakultet, group_number, student_login, "> добавлен")