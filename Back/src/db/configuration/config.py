from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__host = os.environ['DATABASE_CONFIG_HOST']
        self.__port = os.environ['DATABASE_CONFIG_PORT']
        self.__user = os.environ['DATABASE_CONFIG_USER']
        self.__password = os.environ['DATABASE_CONFIG_PASSWORD']
        self.__database = os.environ['DATABASE_CONFIG_DATABASE']
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = psycopg2.connect(
            host=self.__host,
            port=self.__port,
            user=self.__user,
            password=self.__password,
            database=self.__database,
        )
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.close()
