import sys

import MySQLDBBase
from random import randint
import os


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mda = MySQLDBBase.MYSQL()
    mda.create_new_Schema()

    user_input1 = int(input("Добро пожаловать в систему оценки кинофильмов\n "
                        "Выберите действие:\n6: Вывести все фильмы\n7: Вывести всех пользователей\n"
                        "1: Создать 1000 записей\n"
                        "2: Оставить отзыв\n"
                        "3: Вывести все оценки\n"
                        "4: Добавить фильм\n"
                        "5: Очистить записи из БД\n"
                        "0: Выйти из системы\n"))

    title = ["3 idiots", "Casablanca", "John Wick", "The Godfather", "Deadpool"]
    release_date = [1994,1993,1992,2004,2003,2005,2006]
    genre = ["Horror", "Thriller", "Dramma", "Fantasy", "Action"]
    names = ['Иван', 'Катя', 'Август', 'Августин', 'Авраам', 'Aврора', 'Агата', 'Агафон', 'Агнесса', 'Агния', 'Ада',
             'Аделаида', 'Аделина', 'Адонис', 'Акайо', 'Акулина', 'Алан', 'Алевтина', 'Александр', 'Александра',
             'Алексей', 'Алена', 'Алина', 'Алиса', 'Алла', 'Алсу', 'Альберт', 'Альбина', 'Альфия', 'Альфред', 'Амалия',
             'Амелия', 'Анастасий', 'Анастасия', 'Анатоли', 'Ангелина', 'Андрей', 'Анна', 'Антон', 'Арсений', 'Артем']
    last_name = ["Агафьев", 'Прокофьев', "Северов", "Семенов", "Суриков"]
    while True:
        match user_input1:
            case 1:
                for i in range(1000):
                    sql_query = (f"""INSERT INTO movies (title, release_year, genre, collection_in_mil) 
                                values ("{title[randint(0, len(title) - 1)]}", {int(release_date[randint(0, len(release_date) - 1)])} , "{genre[randint(0, len(genre) - 1)]}", {int(randint(1, 1000))})
                    """)
                    # sql_query = ("INSERT INTO movies (title, release_year, genre, collection_in_ml)"
                    #              "VALUES ( " + str(title[randint(0, len(title) - 1)]) + ", "
                    #              " " + str(release_date[randint(0, len(release_date) - 1)]) +","
                    #              " " + str(genre[randint(0, len(genre) - 1)]) + ", "
                    #              " " + str(randint(1, 1000)) + " ")

                    with mda.connection.cursor() as cursor:
                        cursor.execute(sql_query)
                        mda.connection.commit()

                    sql_query = f""" INSERT INTO reviewers(first_name, last_name) VALUES ("{names[randint(0, len(names) - 1)]}" , "{last_name[randint(0, len(last_name) - 1)]}")
                    """
                    with mda.connection.cursor() as cursor:
                        cursor.execute(sql_query)
                        mda.connection.commit()
                print("insert was complete!")
            case 5:
                mda.delete_data_from_table()
                print("Data was sacasfully deleted")
            case 6:
                sql_query = "Select * from movies LIMIT 10"
                with (mda.connection.cursor() as cursor):
                    cursor.execute(sql_query)
                    result = cursor.fetchall()
                    print("|ID|\t|Title|\t|release year|\t|genre|\t|collection in million|")
                    for i in result:
                        print(i['id'], i['title'], i['release_year'], i['genre'], i['collection_in_mil'])
            case 7:
                sql_query = "Select * from reviewers LIMIT 10"
                print("|ID|\t|First name|\t|Last name|")
                with (mda.connection.cursor() as cursor):
                    cursor.execute(sql_query)
                    result = cursor.fetchall()
                    for i in result:
                        print(i["id"], i["first_name"], i["last_name"])


            case 2:
                user_input_movie_id = int(input("Введите ID фильма: "))
                user_input_reviwier_id = int(input("Введите ID пользователя: "))
                user_input_score = float(input("Введите оценку фильма: "))
                sql_query = f"""INSERT INTO ratings(movie_id,reviewer_id,rating) values ({user_input_movie_id}, {user_input_reviwier_id}, {user_input_score})
                """
                with mda.connection.cursor() as cursor:
                    cursor.execute(sql_query)
                    mda.connection.commit()
                print(f"Пользователь под номером {user_input_reviwier_id} оставил оценку на фильм {user_input_movie_id} с баллом {user_input_score}.")
            case 3:
                sql_query = "Select * from ratings"
                with (mda.connection.cursor() as cursor):
                    cursor.execute(sql_query)
                    result = cursor.fetchall()
                    for i in result:
                        print(i)
            case 4:
                user_input_movie_name = input("Введите название фильма: ")
                user_input_release_year = input("Введите год создания фильма: ")
                user_input_genre = input("Введите жанр фильма: ")
                user_input_collection_in_ml = input("Введите количество продаж в миллионах фильма: ")

                sql_query = (f"""INSERT INTO movies (title, release_year, genre, collection_in_mil) 
                                                    values ("{user_input_movie_name}", {int(user_input_release_year)} , "{user_input_genre}", {int(user_input_collection_in_ml)})
                                        """)

                with mda.connection.cursor() as cursor:
                    cursor.execute(sql_query)
                    mda.connection.commit()
            case 0:
                sys.exit()


        user_input1 = int(input("Выберите действие:\n6: Вывести все фильмы\n7: Вывести всех пользователей\n"
                        "1: Создать 1000 записей\n"
                        "2: Оставить отзыв\n"
                        "3: Вывести все оценки\n"
                        "4: Добавить фильм\n"
                        "5: Очистить записи из БД\n"
                        "0: Выйти из системы\n"))
    # with mda.connection.cursor() as cursor:
    #     sql_query = "DESCRIBE movies"
    #     result = cursor.execute(sql_query)
    #     for i in cursor.fetchall():
    #         print(i)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
