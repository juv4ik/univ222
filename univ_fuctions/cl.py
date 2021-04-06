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
        sql2 = "SELECT * FROM marks WHERE id = %s"
        self.cursors.execute(sql2, [id])
        data2 = self.cursors.fetchall()
        return data, data2

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