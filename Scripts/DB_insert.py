import os
import Insert_tables as it
import time


path_for_download_dbf_01022016 = '../Data/Rar/DBF_until_01022016'
path_for_download_dbf_01102017 = '../Data/Rar/DBF_until_01102017'
path_for_download_dbf_now = '../Data/Rar/DBF_until_now'


def fill_main_table_3tab():
    """This method fill the main table of database.

        Input Arguments: None.
        Returns: None.

        Author: Maxim Ukraintsev.
    """
    counter = 0
    for d, dirs, directory in os.walk(path_for_download_dbf_01022016):
        for file in directory:
            if counter == 3:
                it.insert_table_123_main()
                it.insert_table_names()
                it.insert_table_indicators()
                it.delete_data_from_123b()
                it.delete_data_from_123n()
                it.delete_data_from_123d()
                counter = 0
            if counter < 3:
                start_time = time.time()
                path_local = os.path.join(d, file)
                print(file, 'in Process...')
                it.read_dbf(file, path_local)
                print(file, 'loaded by %s seconds' % (time.time() - start_time), '\n')
                counter += 1


def fill_main_table_4tab(path):
    """This method fill the main table of database.

        Input Arguments: path to directory.
        Returns: None.

        Author: Vladimir Beketov.
    """
    counter = 0
    for d, dirs, directory in os.walk(path):
        for file in directory:
            if counter == 4:
                it.insert_table_123_main()
                it.insert_table_names()
                it.insert_table_indicators()
                it.delete_data_from_123b()
                it.delete_data_from_123n()
                it.delete_data_from_123d()
                it.delete_data_from_123s_1()
                it.delete_data_from_123s_2()
                counter = 0
            if counter < 4:
                start_time = time.time()
                path_local = os.path.join(d, file)
                print(file, 'in Process...')
                it.read_dbf(file, path_local)
                print(file, 'loaded by %s seconds' % (time.time() - start_time), '\n')
                counter += 1


fill_main_table_3tab()
