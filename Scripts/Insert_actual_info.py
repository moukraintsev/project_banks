import Insert_tables as it
from os import path
import time
import os

parent_dir = path.dirname(path.abspath(__file__))
parent_dir = str(parent_dir).replace('\\Scripts', '\\Data\\Rar\\')

path_for_download_rar_01022016 = parent_dir + 'form_until_01022016'
path_for_download_rar_01102017 = parent_dir + 'form_until_01102017'
path_for_download_rar_now = parent_dir + 'form_until_now'

path_for_download_dbf_01022016 = parent_dir + 'DBF_until_01022016'
path_for_download_dbf_01102017 = parent_dir + 'DBF_until_01102017'
path_for_download_dbf_now = parent_dir + 'DBF_until_now'


def fill_main_table_4tab(path_dir, date_for_down):
    """This method translating missing data from downloaded files to auxiliary tables and filling in the main table.

        Input Arguments: path to the file directory, date for downloading.
        Returns: None.

        Author: Vladimir Beketov.
    """
    counter = 0

    for d, dirs, directory in os.walk(path_dir):
        for file in directory:
            if file.endswith(date_for_down, 0, 6):
                if counter < 4:
                    start_time = time.time()
                    path_local = os.path.join(d, file)
                    print(file, 'in Process...')
                    it.read_dbf(file, path_local)
                    print(file, 'loaded by %s seconds' % (time.time() - start_time), '\n')
                    counter += 1
                if counter == 4:
                    start_time = time.time()
                    print("Inserting main table in Process...")
                    it.insert_table_123_main()
                    print('Main table inserted by %s seconds' % (time.time() - start_time), '\n')
                    it.insert_table_names()
                    it.insert_table_indicators()
                    it.delete_data_from_123b()
                    it.delete_data_from_123n()
                    it.delete_data_from_123d()
                    it.delete_data_from_123s_1()
                    it.delete_data_from_123s_2()
                    counter = 0


def insert_actual(list_for_download, list_for_check_download, downloaded_dates):
    """This method translating missing data from downloaded files to auxiliary tables and filling in the main table.

        Input Arguments: list for download, list for check download, downloaded dates.
        Returns: None.

        Author: Maxim Ukraintsev.
    """

    it.delete_data_from_123b()
    it.delete_data_from_123n()
    it.delete_data_from_123d()
    it.delete_data_from_123s_1()
    it.delete_data_from_123s_2()

    for i in range(0, len(list_for_download)):
        flag = True
        for j in range(0, len(downloaded_dates)):
            if str(list_for_check_download[i]) == str(downloaded_dates[j]):
                flag = False
                break
        if (list_for_download[i].find('2014') != -1 or list_for_download[i].find('2015') != -1) and flag:
            counter = 0
            for d, dirs, directory in os.walk(path_for_download_dbf_01022016):
                for file in directory:
                    if file.endswith(list_for_download[i], 0, 6):
                        if counter < 3:
                            start_time_download = time.time()
                            path_local = os.path.join(d, file)
                            print(file, 'in Process...')
                            it.read_dbf(file, path_local)
                            print(file, 'loaded by %s seconds' % (time.time() - start_time_download), '\n')
                            counter += 1
                        if counter == 3:
                            start_time = time.time()
                            print("Inserting main table in Process...")
                            it.insert_table_123_main()
                            print('Main table inserted by %s seconds' % (time.time() - start_time), '\n')
                            it.insert_table_names()
                            it.insert_table_indicators()
                            it.delete_data_from_123b()
                            it.delete_data_from_123n()
                            it.delete_data_from_123d()
                            counter = 0
        elif (list_for_download[i].find('2016') != -1 or (
                list_for_download[i].find('2017') != 1 and list_for_download[i].find('092017') == -1 and
                list_for_download[i].find('102017') == -1 and list_for_download[i].find('112017') == -1 and
                list_for_download[i].find('122017') == -1)) and flag:
            fill_main_table_4tab(path_for_download_dbf_01102017, list_for_download[i])
        elif flag:
            fill_main_table_4tab(path_for_download_dbf_now, list_for_download[i])
