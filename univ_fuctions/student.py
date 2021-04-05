def menu_studenta(login):
    def d():
        db = DataBase()
        data = db.student_info_o_sebe(login)
        return data
    while True:
        print('1 - информация о себе\n2 - средний балл\n3 - номер группы\n4 - фио\n5 - информация о предметах\n9 - изменить пароль\n0 - выход')
        type = int(input('Сделайте выбор (или 0 для выхода):'))
        if type == 1:
            print('информация о', login, ':')
            data = d()
            for element in data:
                print(element["id"], element["name"], element["surname"], element["fakultet"], element["group_number"])
        elif type == 2:
            print('средний балл')
        elif type == 3:
            print('номер группы')
            data = d()
            for element in data:
                print(element["group_number"])
        elif type == 4:
            print('фио')
            data = d()
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