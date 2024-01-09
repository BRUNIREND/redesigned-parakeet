from mysql.connector import connect, Error
from getpass import getpass
import pymysql

class MYSQL:
    def __init__(self):
        try:
            self.connection = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                database="online_movie_rating",
                password='Abcd268377',
                cursorclass=pymysql.cursors.DictCursor
            )
            create_db_query = "CREATE DATABASE IF NOT EXISTS  online_movie_rating"
            with self.connection.cursor() as cursor:
                cursor.execute(create_db_query)
                print("successfully connected...")
                print("#" * 20)

        except Exception as ex:
            print("Connection refused...")
            print(ex)
    def create_table_Movies(self):
        with self.connection.cursor() as cursor:
            sql_query = """
                        CREATE TABLE IF NOT EXISTS movies(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            title VARCHAR(100),
                            release_year YEAR(4),
                            genre VARCHAR(100),
                            collection_in_mil INT
                        )
                        """
            cursor.execute(sql_query)

    def create_table_Reviewers(self):
        with self.connection.cursor() as cursor:
            sql_query = """
                        CREATE TABLE IF NOT EXISTS reviewers (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            first_name VARCHAR(100),
                            last_name VARCHAR(100)
                        )
                        """
            cursor.execute(sql_query)
    def create_table_Ratings(self):
        with self.connection.cursor() as cursor:
            sql_query = """
                        CREATE TABLE IF NOT EXISTS ratings (
                            movie_id INT,
                            reviewer_id INT,
                            rating DECIMAL(2,1),
                            FOREIGN KEY(movie_id) REFERENCES movies(id),
                            FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
                            PRIMARY KEY(movie_id, reviewer_id)
                        )
                        """
            cursor.execute(sql_query)

    def delete_data_from_table(self):
        with self.connection.cursor() as cursor:
            cursor.execute("Delete from movies")
            cursor.execute("Delete from ratings")
            cursor.execute("Delete from reviewers")
            self.connection.commit()

    def create_new_Schema(self):
        self.create_table_Movies()
        self.create_table_Reviewers()
        self.create_table_Ratings()
