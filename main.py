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


    def addUser(self, login, password):
        sql = "INSERT INTO users (id, login, password) VALUES (%s, %s, %s)"
        temp = [3, login, password]
        self.cursors.execute(sql, temp)
        self.connection.commit()


def menu_prepoda():
    while True:
        print('1 - информация о студентах\n2 - получить информацию о студенте\n3 - добавть студента\n4 - добавить преподавателя\n5 - поставить оценку\n6 - изменить оценку\n0 - выход')
        type = int(input('Сделайте выбор (или 0 для выхода):'))
        if type == 1:
            print('информация о студентах')
        elif type == 2:
            print('получить информацию о студенте:')
        elif type == 3:
            print('добавть студента:')
        elif type == 4:
            print('добавить преподавателя')
        elif type == 5:
            print('поставить оценку')
        elif type == 6:
            print('изменить оценку')
        elif type == 0:
            break
        else:
            print('что-то не то нажали')

def menu_studenta():
    while True:
        print('1 - информация о себе\n2 - средний балл\n3 - номер группы\n4 - фио\n5 - информация о предметах\n0 - выход')
        type = int(input('Сделайте выбор (или 0 для выхода):'))
        if type == 1:
            print('информация о себе')
        elif type == 2:
            print('средний балл')
        elif type == 3:
            print('номер группы')
        elif type == 4:
            print('фио')
        elif type == 5:
            print('информация о предметах')
        elif type == 0:
            break
        else:
            print('что-то не то нажали')


def check_authorization(login, password):
    if login.istitle():
        res = 'prepod'
    else:
        res = 'student'
    if res == 'prepod':  # res == True
        id = 23
        return 1 # 1 - препод, 2 - студент
    if res == 'student':
        id = 18
        return 2 # 1 - препод, 2 - студент
    else:
        return False


def hide_password(password):
    hidden_password = str('*'*len(password))
    return hidden_password


def login(login, password):
    print('авторизация...')
    hidden_password = hide_password(password)
    print(login, hidden_password)
    res_auth = check_authorization(login, password)
    if not res_auth: # res_auth == False
        print('введены неверные данные, пользователя с таким паролем не существует')
    else:
        if res_auth == 1:
            print('menu prepoda')
            menu_prepoda()
        if res_auth == 2:
            print('menu studenta')
            menu_studenta()


def reg_student():
    student_name = input('введите имя:')
    student_surname = input('введите фамилию:')
    student_fakultet = input('введите факультет:')
    student_group = input('введите группу:')
    student_login = input('введите логин:')
    student_password = input('введите пароль:')
    id = 3
    DataBase.addUser(id, student_login, student_password)
    print(student_name, student_surname, student_fakultet, student_group, student_login, student_password)


def reg_prepod():
    prepod_name = input('введите имя:')
    prepod_surname = input('введите фамилию:')
    prepod_fakultet = input('введите факультет:')
    prepod_predmet = input('введите группу:')

    print(prepod_name, prepod_surname, prepod_fakultet, prepod_predmet)


def register():
    while True:
        member = input('введите данные: 1 - студент, 2 - преподаватель:')
        if int(member) == 1:
            print('vy stydent')
            reg_student()
        elif int(member) == 2:
            print('vy prepod')
            reg_prepod()
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
            a_login = input('login:')
            a_password = input('password:')
            login(a_login, a_password)
        elif type == 2:
            print('Регистрация. Введите запрашиваемые данные:')
            register()
        elif type == 0:
            break
main()
