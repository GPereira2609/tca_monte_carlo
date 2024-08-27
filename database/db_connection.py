import psycopg2 
from contextlib import contextmanager
from config.settings import USER, PASSWORD, HOST, PORT, DRIVER, URL, DB_NAME


def get_db_properties():
    db_properties = {
        "user": USER,
        "password": PASSWORD,
        "driver": DRIVER
    }
    url = URL
    return url, db_properties


def get_db_connection():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )
    return conn

class DBConnection:


    def __init__(self, db_name, host, user, password, port=5432):
        self._db_name = db_name
        self._host = host
        self._user = user
        self._password = password
        self._port = port
        self._test_connection()


    def _create_connection(self):
        connection = None
        try:
            connection = psycopg2.connect(dbname=self.db_name,
                                          user=self.user,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port)
            # print("Postgres Database connection successful")
        except psycopg2.Error as err:
            print(f"Error: '{err}'")
        return connection
    
    def _test_connection(self):
        self._create_connection()


    @contextmanager
    def connection(self):
        """
        with connection() as connect:
            cursor = connect.cursor()
            ...

        :return:
        """
        connection = self._create_connection()
        try:
            yield connection
        finally:
            if connection and not connection.closed:
                connection.close()


    @property
    def db_name(self):
        return self._db_name


    @property
    def host(self):
        return self._host


    @property
    def user(self):
        return self._user


    @property
    def password(self):
        return self._password


    @property
    def port(self):
        return self._port

    # def __del__(self):
    #     self.db.close()

    def query(self, sql_query: str):
        with self.connection() as connect:
            try:
                print(sql_query)
                cursor = connect.cursor()
                cursor.execute(sql_query)
                connect.commit()
                query_result = cursor.fetchall()
                cursor.close()
                return query_result
            except psycopg2.Error as err:
                print(f"Error: '{err}'")
