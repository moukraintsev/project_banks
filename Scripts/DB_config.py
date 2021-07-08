import re
from os import path
import DB_connect
from DB_connect import build_widget
import mysql
from mysql.connector import Error, OperationalError, ProgrammingError

global connection_


def execute_query(query):
    """This method processing a database request.

        Input Arguments: query.
        Returns: None.

        Author: Maxim Ukraintsev.
    """
    connect = globals()['connection']
    cursor = connect.cursor()
    try:
        cursor.execute(query)
        connect.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(query):
    """This method read a database request.

        Input Arguments: query.
        Returns: None.

        Author: Maxim Ukraintsev.
    """
    connect = globals()['connection']
    cursor = connect.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def create_database():
    """This method rebuilds database schema.

        Input Arguments: None.
        Returns: None.

        Author: Vladimir Beketov.
    """
    connect = globals()['connection_']
    cursor = connect.cursor()
    query = """
        CREATE DATABASE IF NOT EXISTS `banks_f123`
    """
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


global new_connection


def create_connection_with_db():
    global new_connection
    try:
        new_connection = mysql.connector.connect(
            host=DB_connect.main_user_host,
            user=DB_connect.main_user_name,
            passwd=DB_connect.main_user_password,
            database='banks_f123',
            auth_plugin='mysql_native_password'
        )
        print("DB Connection: ", DB_connect.main_user_host, DB_connect.main_user_name, DB_connect.main_user_password)
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return new_connection


def execute_scripts_from_file(filename):
    connect = globals()['connection_']
    cursor = connect.cursor()

    statement = ""

    parent_dir = path.dirname(path.abspath(__file__))
    parent_dir = str(parent_dir).replace('\\Scripts', '')

    for line in open(path.join(parent_dir, 'Data\\', filename), encoding='utf8'):

        if re.match(r'--', line):  # ignore sql comment lines
            continue

        if not re.search(r'[^-;]+;', line):  # keep appending lines that don't end in ';'
            statement = statement + line

        else:  # when you get a line ending in ';' then exec statement and reset for next statement
            statement = statement + line
            # print "\n\n[DEBUG] Executing SQL statement:\n%s" % (statement)
            try:
                cursor.execute(statement)
            except (OperationalError, ProgrammingError) as e:
                print("\n[WARN] MySQLError during execute statement \n\tArgs: '%s'" % (str(e.args)))

            statement = ""


def use_config():
    build_widget()
    global connection_
    connection_ = DB_connect.connection
    create_database()
    connection_ = create_connection_with_db()
    print("Your new connection:", connection_)
    execute_scripts_from_file('bd_config.sql')


def return_connection():
    global connection_
    return connection_

