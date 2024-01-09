import os
import sqlite3

class SQLITE:

    def __init__(self):
        #if os.path.isfile("lite.db"):
        self.connection = sqlite3.connect("../../Downloads/lite.db")
        self.cursor = self.connection.cursor()


    def CreateTable_User(self):
        self.cursor.execute("""
                              CREATE TABLE IF NOT EXISTS User
                              (id_user INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                              telephone TEXT,
                              address TEXT,
                              login TEXT,
                              password TEXT,
                              email TEXT);
                            """)

    def CreateTable_Order(self):
        self.cursor.execute("""
                              CREATE TABLE IF NOT EXISTS 'Order'
                              (id_order INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                              date_create TEXT,
                              date_update TEXT,
                              status INTEGER,
                              id_user INTEGER NOT NULL REFERENCES User(id_user)); -- Внешний ключ
                            """)

    def CreateTable_Product(self):
        self.cursor.execute("""
                              CREATE TABLE IF NOT EXISTS Product
                              (id_product INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                              name TEXT,
                              description TEXT,
                              date_create TEXT,
                              date_update TEXT,
                              price REAL,
                              count INTEGER);
                            """)

    def CreateTable_Order_row(self):
        self.cursor.execute("""
                              CREATE TABLE IF NOT EXISTS Order_row
                              (id_order INTEGER NOT NULL REFERENCES 'Order'(id_order), -- Внешний ключ
                              id_product INTEGER NOT NULL REFERENCES Product(id_product)) -- Внешний ключ
                            """)

    def CreateScheme(self):
        self.CreateTable_User()
        self.CreateTable_Product()
        self.CreateTable_Order()
        self.CreateTable_Order_row()

if __name__ == "__main__":
    db = SQLITE()
    db.CreateScheme()

    # INSERT одной записи
    #db.cursor.execute("""
    #                    INSERT INTO User ('telephone', 'address', 'login', 'password', 'email')
    #                    VALUES ('89456547898', 'Москва, ул. Киренского 26Б', 'nonick2', '123', 'nonick2@mail.ru')
    #                  """)

    # INSERT коллекции записей
    #dataCollections = (['11111111', 'Красноярск', 'petya', '123', 'petya@mail.ru'],
    #                   ['22222222', 'Москва', 'vanya', '321', 'vanya@mail.ru'],
    #                   ['33333333', 'Казань', 'masha', '123456', 'masha@mail.ru'])
    #db.cursor.executemany("INSERT INTO User ('telephone', 'address', 'login', 'password', 'email') VALUES (?, ?, ?, ?, ?)", dataCollections)
    #db.connection.commit()

    # SELECT всех записей
    #"""
    db.cursor.execute("SELECT * FROM User")
    result = db.cursor.fetchall()
    print(result)
    for row in result:
        print(row)
        print(row[5])
    #"""

"""
1. свойство lastrowid - идентификатор последний добавленной записи
2. Проверить запросом существует ли таблица:
SELECT name FROM sqlite_master WHERE type = 'table' AND name = '{table_name}';

3. Просмотр БД в PyCharm:
    1. View->Tool Windows->Database
    2. перетянуть свою базу или нажать на + указать файл с базой.
    3. если в первый раз, то придется устанавливать Driver Sqlite (Xerial)
"""
'''
cursor.execute("""
    CREATE TABLE IF NOT EXISTS `mdl_assignment` (
      `id` bigint(10) unsigned NOT NULL AUTO_INCREMENT,
      `course` bigint(10) unsigned NOT NULL DEFAULT '0',
      `name` varchar(255) NOT NULL DEFAULT '',
      `intro` text NOT NULL,
      `introformat` smallint(4) unsigned NOT NULL DEFAULT '0',
      `assignmenttype` varchar(50) NOT NULL DEFAULT '',
      `resubmit` tinyint(2) unsigned NOT NULL DEFAULT '0',
      `preventlate` tinyint(2) unsigned NOT NULL DEFAULT '0',
      `emailteachers` tinyint(2) unsigned NOT NULL DEFAULT '0',
      `var1` bigint(10) DEFAULT '0',
      `maxbytes` bigint(10) unsigned NOT NULL DEFAULT '100000',
      `timedue` bigint(10) unsigned NOT NULL DEFAULT '0',
      `timeavailable` bigint(10) unsigned NOT NULL DEFAULT '0',
      `grade` bigint(10) NOT NULL DEFAULT '0',
      `timemodified` bigint(10) unsigned NOT NULL DEFAULT '0',
      PRIMARY KEY (`id`),
      KEY `mdl_assi_cou_ix` (`course`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Defines assignments' AUTO_INCREMENT=1 ;
    """)
'''