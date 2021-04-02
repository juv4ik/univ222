import pymysql
from pymysql.cursors import DictCursor


class DataBase:
    def __init__(self):
        self.connection = self.connect()
        self.cursors = self.connection.cursor()

    def connect(self):
        connection = pymysql.connect(
            host='localhost',
            user='admin',
            password='admin',
            db='un',
            charset='utf8mb4',
            cursorclass=DictCursor
        )
        return connection

    def __del__(self):
        self.connection.close()
        print('connection closed')


    def addUserStudent(self, login, password, type, name, surname, fakultet, group_number):
        sql = "INSERT INTO usrs (id, login, password, type, name, surname, fakultet, group_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        temp = ["NULL", login, password, type, name, surname, fakultet, group_number]
        self.cursors.execute(sql, temp)
        self.connection.commit()

    def addUserPrepod(self, password, type, name, surname, fakultet, predmet):
        sql = "INSERT INTO usrs (id, password, type, name, surname, fakultet, predmet) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        temp = ["NULL", password, type, name, surname, fakultet, predmet]
        self.cursors.execute(sql, temp)
        self.connection.commit()

    def getUser(self):
        sql = "SELECT * FROM usrs WHERE type = 's'"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        return data
        # [{'login': 'sfsf', 'password': 'fksanks'}, {}]

    def confirmPrepod(self):
        sql = "SELECT * FROM usrs WHERE type = 'p' AND login = ''"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        return data

    def confirmLoginToPrepod(self, id):
        login = "prep"+str(id)
        sql = "UPDATE usrs SET login = %s WHERE id = %s"
        temp = [login, id]
        self.cursors.execute(sql, temp)
        self.connection.commit()

    def infoStudent(self, id):
        sql = "SELECT * FROM usrs WHERE id = %s"
        self.cursors.execute(sql, [id])
        data = self.cursors.fetchall()
        return data

    def getPassword(self, login):
        login = login
        sql = "SELECT * FROM usrs WHERE login = %s"
        self.cursors.execute(sql, [login])
        data = self.cursors.fetchall()
        return data

    def student_info_o_sebe(self, login):
        sql = "SELECT * FROM usrs WHERE login = %s"
        self.cursors.execute(sql, [login])
        data = self.cursors.fetchall()
        return data


def shifr(password):
    password = password.replace('a', 2)
    return password

def deshifr(password):
    password = password.replace(2, 'a')
    return password


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
            id = int(input('Информация о студенте, введите id:'))
            db = DataBase()
            data = db.infoStudent(id)
            for element in data:
                print(element["id"], element["name"], element["surname"], element["fakultet"], element["group_number"])
        elif type == 3:
            print('добавть студента:')
        elif type == 4:
            print('--------------добавить преподавателя')
            db = DataBase()
            data = db.confirmPrepod()
            print(len(data), "преподавателя(ей) можно добавить в БД:")
            if len(data) > 0:
                for element in data:
                    print(element["id"], element["name"], element["fakultet"], element["predmet"])
                prepod_id = int(input('введите id преподавателя для установки логина:'))
                db.confirmLoginToPrepod(prepod_id)
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

def menu_studenta(login):
    def d():
        db = DataBase()
        data = db.student_info_o_sebe(login)
        return data
    while True:
        print('1 - информация о себе\n2 - средний балл\n3 - номер группы\n4 - фио\n5 - информация о предметах\n0 - выход')
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
            print('информация о предметах')
        elif type == 0:
            break
        else:
            print('что-то не то нажали')


def hide_password(password):
    hidden_password = str('*'*len(password))
    return hidden_password


def reg_student():
    type = "s"
    name = input('введите имя:')
    surname = input('введите фамилию:')
    fakultet = input('введите факультет:')
    group_number = input('введите группу:')
    student_login = input('введите логин:')
    student_password = input('введите пароль:')
    db = DataBase()
    db.addUserStudent(student_login, student_password, type, name, surname, fakultet, group_number)
    del db
    print("студент <", name, surname, fakultet, group_number, student_login, student_password, "> добавлен")



def reg_prepod():
    type = "p"
    password = input('введите пароль:')
    name = input('введите имя:')
    surname = input('введите фамилию:')
    fakultet = input('введите факультет:')
    predmet = input('введите предмет:')
    db = DataBase()
    db.addUserPrepod(password, type, name, surname, fakultet, predmet)
    del db
    print("преподаватель", password, name, surname, fakultet, predmet, "добавлен.\nЛогин установит главный преподаватель.")


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
                print(element["password"])
            if password == element["password"]:
                print("...Авторизация прошла успешно,", element["name"])
                if element["type"] == "s":
                    menu_studenta(login=login)
                else:
                    menu_prepoda()
            else:
                print("ne ok")
        elif type == 2:
            print('Регистрация. Введите запрашиваемые данные:')
            register()
        elif type == 3:
            print("меню препода")
            menu_prepoda()
        elif type ==4:
            print("меню студента")
            menu_studenta()
        elif type == 0:
            break
main()
'''
#--------------

def check_authorization(login, password):
    if login.istitle():
        res = 'prepod'
    else:
        res = 'student'
    if res == 'prepod':  # res == True
        id = 23
        return 1  # 1 - препод, 2 - студент
    if res == 'student':
        id = 18
        return 2  # 1 - препод, 2 - студент
    else:
        return False

#--------------


def login(login, password):
    print('авторизация...')
    hidden_password = hide_password(password)
    print(login, hidden_password)
    res_auth = DataBase.check_authorization(login, password)
    if not res_auth: # res_auth == False
        print('введены неверные данные, пользователя с таким паролем не существует')
    else:
        if res_auth == 1:
            print('menu prepoda')
            menu_prepoda()
        elif res_auth == 2:
            print('menu studenta')
            menu_studenta()
        else: print('ооо, сложна!!!!!!!!!!!!!!!')
'''