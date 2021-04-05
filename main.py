import pymysql
from pymysql.cursors import DictCursor
from univ_fuctions.pswrd import *
from univ_fuctions.prepod import *
from univ_fuctions.student import *
from univ_fuctions.reg import *


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

    def changePassword(self, login, new_password):
        sql = "UPDATE usrs SET password = %s WHERE login = %s"
        temp = [new_password, login]
        self.cursors.execute(sql, temp)
        self.connection.commit()


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
