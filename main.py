import pymysql
from pymysql.cursors import DictCursor
from univ_fuctions.pswrd import *
#from univ_fuctions.prepod import *
#from univ_fuctions.student import *
#from univ_fuctions.reg import *


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
        sql2 ="INSERT INTO marks (id) SELECT id FROM usrs WHERE login=%s"
        temp2 = [login]
        self.cursors.execute(sql2, temp2)
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
        #creating tables
        sql1 = "ALTER TABLE marks ADD COLUMN " + login + "_1 INT (2)"
        sql2 = "ALTER TABLE marks ADD COLUMN " + login + "_2 INT (2)"
        sql3 = "ALTER TABLE marks ADD COLUMN " + login + "_3 INT (2)"
        sql4 = "ALTER TABLE marks ADD COLUMN " + login + "_kurs INT (2)"
        sql5 = "ALTER TABLE marks ADD COLUMN " + login + "_ekzamen INT (2)"
        self.cursors.execute(sql1)
        self.cursors.execute(sql2)
        self.cursors.execute(sql3)
        self.cursors.execute(sql4)
        self.cursors.execute(sql5)
        self.connection.commit()

    def infoStudent(self, id):
        sql = "SELECT * FROM usrs WHERE id = %s"
        self.cursors.execute(sql, [id])
        data = self.cursors.fetchall()
        return data

    def student_marks(self, id):
        sql = "SELECT * FROM marks WHERE id = %s"
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

    def changePassword(self, login, new_password):
        sql = "UPDATE usrs SET password = %s WHERE login = %s"
        temp = [new_password, login]
        self.cursors.execute(sql, temp)
        self.connection.commit()

    def mark(self, login, number_pr, id, mark):
        sql = "UPDATE marks SET "+login+"_"+number_pr+" = %s WHERE id = %s"
        temp = [mark, id]
        self.cursors.execute(sql, temp)
        self.connection.commit()
        print(login, number_pr)


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
            print(data[0].values())
        elif type == 3:
            print('номер группы')
            #data = d()
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
            print('оценка поставлена?')
        elif type == 6:
            print('изменить оценку')
        elif type == 0:
            break
        else:
            print('что-то не то нажали')

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
