from DB_config import return_connection
from DB_config import use_config
from mysql.connector import Error
import dbfread as DBF

use_config()
connection = return_connection()


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


def read_dbf(file, path):
    """This method services for recognizing, reading,  copying a dbf file and entering it in the database.

        Input Arguments: dbf file, path to dbf file.
        Returns: None.

        Author: Vladimir Beketov.
    """
    if file.endswith("123B.DBF"):
        t_123b = DBF.DBF(path, encoding='cp866', load=True)
        insert_table_123b(t_123b)
    if file.endswith("123N.DBF"):
        t_123n = DBF.DBF(path, encoding='cp866', load=True)
        insert_table_123n(t_123n)
    if file.endswith("123D.DBF"):
        t_123d = DBF.DBF(path, encoding='cp866', load=True)
        insert_table_123d(t_123d)
    if file.endswith("123S.DBF") and path.find('01102017') != -1:
        t_123s = DBF.DBF(path, encoding='cp866', load=True)
        insert_table_123s_1(t_123s)
    if file.endswith("123S.DBF") and path.find('now') != -1:
        t_123s = DBF.DBF(path, encoding='cp866', load=True)
        insert_table_123s_2(t_123s)


def insert_table_123b(table):
    """This method services for inserting 123b table in the database.

        Input Arguments: table.
        Returns: None.

        Author: Maxim Ukraintsev.
    """
    connect = globals()['connection']
    for r in table:
        cursor = connect.cursor()
        query = """
        INSERT INTO `123_b` (REGN, OKATO, OKPO, OGRN, REGN_S, BIC, DT, NAME_B, ADR, PRIZ_P) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            r['REGN'], r["OKATO"], r["OKPO"], r["OGRN"], r["REGN_S"], r["BIC"], r["DT"], r["NAME_B"], r["ADR"],
            r["PRIZ_P"])
        cursor.execute(query, values)
        connect.commit()


def delete_data_from_123b():
    """This method services for deleting 123b table from the database.

        Input Arguments: None.
        Returns: None.

        Author: Vladimir Beketov.
    """
    connect = globals()['connection']
    cursor = connect.cursor()
    query = """
    DELETE FROM `123_b`
    """

    cursor.execute(query)
    connect.commit()


def insert_table_123s_2(table):
    """This method services for inserting 123s_2 table in the database.

        Input Arguments: table.
        Returns: None.

        Author: Maxim Ukraintsev.
    """
    connect = globals()['connection']
    for r in table:
        cursor = connect.cursor()
        query = """
        INSERT INTO `123_s_2` (REGN, C1_S, C2_S, C31_S, C32_S) 
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            r['REGN'], r["C1_S"], r["C2_S"], r["C31_S"], r["C32_S"])
        cursor.execute(query, values)
        connect.commit()


def delete_data_from_123s_2():
    """This method services for deleting 123s_2 table from the database.

        Input Arguments: None.
        Returns: None.

        Author: Vladimir Beketov.
    """
    connect = globals()['connection']
    cursor = connect.cursor()
    query = """
    DELETE FROM `123_s_2`
    """

    cursor.execute(query)
    connect.commit()


def insert_table_123s_1(table):
    """This method services for inserting 123s_1 table in the database.

        Input Arguments: table.
        Returns: None.

        Author: Maxim Ukraintsev.
    """
    connect = globals()['connection']
    for r in table:
        cursor = connect.cursor()
        query = """
        INSERT INTO `123s_1` (REGN, C1_S, C2_S) 
        VALUES (%s, %s, %s)
        """

        values = (
            r['REGN'], r["C1_S"], r["C2_S"])
        cursor.execute(query, values)
        connect.commit()


def delete_data_from_123s_1():
    """This method services for deleting 123s_1 table from the database.

        Input Arguments: None.
        Returns: None.

        Author: Vladimir Beketov.
    """
    connect = globals()['connection']
    cursor = connect.cursor()
    query = """
    DELETE FROM `123s_1`
    """

    cursor.execute(query)
    connect.commit()


def insert_table_123n(table):
    """This method services for inserting 123n table in the database.

        Input Arguments: table.
        Returns: None.

        Author: Maxim Ukraintsev.
    """
    connect = globals()['connection']
    for r in table:
        cursor = connect.cursor()
        query = """
        INSERT INTO `123_n` (C1, C2_1, C2_2, C2_3) 
        VALUES (%s, %s, %s, %s)
        """

        values = (r['C1'], r["C2_1"], r["C2_2"], r["C2_3"])
        cursor.execute(query, values)
        connect.commit()


def delete_data_from_123n():
    """This method services for deleting 123n table from the database.

        Input Arguments: None.
        Returns: None.

        Author: Vladimir Beketov.
    """
    connect = globals()['connection']
    cursor = connect.cursor()
    query = """
    DELETE FROM `123_n`
    """

    cursor.execute(query)
    connect.commit()


def insert_table_123d(table):
    """This method services for inserting 123n table in the database.

        Input Arguments: table.
        Returns: None.

        Author: Maxim Ukraintsev.
    """
    connect = globals()['connection']
    for r in table:
        cursor = connect.cursor()
        query = """
        INSERT INTO `123_d` (REGN, C1, C3) 
        VALUES (%s, %s, %s)
        """

        values = (r['REGN'], r["C1"], r["C3"])
        cursor.execute(query, values)
        connect.commit()


def delete_data_from_123d():
    """This method services for deleting 123d table from the database.

        Input Arguments: None.
        Returns: None.

        Author: Vladimir Beketov.
    """
    connect = globals()['connection']
    cursor = connect.cursor()
    query = """
    DELETE FROM `123_d`
    """

    cursor.execute(query)
    connect.commit()


def insert_table_123_main():
    """This method services for inserting 123 main table in the database.

        Input Arguments: None.
        Returns: None.

        Author: Maxim Ukraintsev.
    """
    connect = globals()['connection']
    cursor = connect.cursor()
    query = """
    INSERT INTO `123_main` (REGN, DT, C1, C3) 
    SELECT `123_b`.REGN, DT, C1, C3 
    FROM `123_b` 
    RIGHT JOIN `123_d` ON `123_b`.REGN = `123_d`.REGN
    """

    cursor.execute(query)
    connect.commit()


def delete_data_from_123_main():
    """This method services for deleting 123 main table from the database.

        Input Arguments: None.
        Returns: None.

        Author: Vladimir Beketov.
    """
    connect = globals()['connection']
    cursor = connect.cursor()
    query = """
    DELETE FROM `123_main`
    """

    cursor.execute(query)
    connect.commit()


def insert_table_names():
    """This method services for inserting table "names" in the database.

        Input Arguments: table.
        Returns: None.

        Author: Maxim Ukraintsev.
    """
    connect = globals()['connection']
    cursor = connect.cursor()
    query = """
    insert into  names (REGN, OKATO, OKPO, OGRN, REGN_S, BIC, NAME_B, ADR) select `123_b`.REGN, `123_b`.OKATO,
    `123_b`.OKPO, `123_b`.OGRN, `123_b`.REGN_S, `123_b`.BIC, `123_b`.NAME_B, `123_b`.ADR from `123_b` 
    where not exists (select 1 from names where names.REGN = `123_b`.REGN)
    """

    cursor.execute(query)
    connect.commit()


def delete_data_from_names():
    """This method services for deleting table "names" from the database.

        Input Arguments: None.
        Returns: None.

        Author: Vladimir Beketov.
    """
    connect = globals()['connection']
    cursor = connect.cursor()
    query = """
    DELETE FROM `names`
    """

    cursor.execute(query)
    connect.commit()


def insert_table_indicators():
    """This method services for inserting table "indicators" in the database.

        Input Arguments: table.
        Returns: None.

        Author: Maxim Ukraintsev.
    """
    connect = globals()['connection']
    cursor = connect.cursor()
    query = """
    insert into  indicators (C1, C2_1, C2_2, C2_3)  select  `123_n`.C1, `123_n`.C2_1,
    `123_n`.C2_2, `123_n`.C2_3  from `123_n`
    where not exists (select 1 from indicators where indicators.C1 = `123_n`.C1)
    """

    cursor.execute(query)
    connect.commit()


def delete_data_from_indicators():
    """This method services for deleting table "indicators" from the database.

        Input Arguments: None.
        Returns: None.

        Author: Vladimir Beketov.
    """
    connect = globals()['connection']
    cursor = connect.cursor()
    query = """
    DELETE FROM `indicators`
    """

    cursor.execute(query)
    connect.commit()
