import datetime
import requests
from bs4 import BeautifulSoup as bs
import wget
import rarfile
import os
from os import path

parent_dir = path.dirname(path.abspath(__file__))
parent_dir = str(parent_dir).replace('\\Scripts', '\\Data\\Rar\\')

path_for_download_rar_01022016 = parent_dir + 'form_until_01022016'
path_for_download_rar_01102017 = parent_dir + 'form_until_01102017'
path_for_download_rar_now = parent_dir + 'form_until_now'

path_for_download_dbf_01022016 = parent_dir + 'DBF_until_01022016'
path_for_download_dbf_01102017 = parent_dir + 'DBF_until_01102017'
path_for_download_dbf_now = parent_dir + 'DBF_until_now'

form_until_01022016 = {'href': []}
form_until_01102017 = {'href': []}
form_until_now = {'href': []}


def count_files_in_dir(dir_path):
    """This method counts the number of files in the directory.

        Input Arguments: path to directory.
        Returns: quantity.

        Author: Maxim Ukraintsev.
    """
    counter = 0
    for d, dirs, files in os.walk(dir_path):
        for _ in files:
            counter += 1
    return counter


def download_rar(list_rar, path_dist_rar):
    """This method downloads archives from the Central Bank of the Russian Federation website.

        Input Arguments: list of downloaded archives, path to the save directory.
        Returns: None.

        Author: Vladimir Beketov.
    """
    i = 0
    while i < len(list_rar):
        wget.download(list_rar[i], path_dist_rar)
        i += 1
    print(len(list_rar), "\tRAR files was download in\t", path_dist_rar)


def download_dbf(path_dist_rar, path_dist_dbf):
    """This method counts the number of files in the directory.

        Input Arguments: path to the rar-files directory, path to the dbf-files directory.
        Returns: None.

        Author: Maxim Ukraintsev.
    """
    counter = 0
    for d, dirs, files in os.walk(path_dist_rar):
        for file in files:
            path_local = os.path.join(d, file)
            rf = rarfile.RarFile(path_local)
            for f in rf.infolist():
                rf.extract(f, path_dist_dbf)
                counter += 1
    print(counter, "\tDBF files was download in\t", path_dist_dbf)


def check_files_01022016():
    """This method checks the integrity of saved files and loads them if they are missing (till 01.02.2016).

        Input Arguments: None.
        Returns: None.

        Author: Maxim Ukraintsev.
    """
    for d, dirs, files in os.walk(path_for_download_rar_01022016):
        if len(files) != 24:
            folder = path_for_download_rar_01022016
            for the_file in os.listdir(folder):
                file_path = os.path.join(folder, the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(e)
            download_rar(form_until_01022016['href'], path_for_download_rar_01022016)
    for d, dirs, files in os.walk(path_for_download_dbf_01022016):
        if len(files) != 72:
            folder = path_for_download_dbf_01022016
            for the_file in os.listdir(folder):
                file_path = os.path.join(folder, the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(e)
            download_dbf(path_for_download_rar_01022016, path_for_download_dbf_01022016)


def check_files_01102017():
    """This method checks the integrity of saved files and loads them if they are missing (till 01.10.2017).

        Input Arguments: None.
        Returns: None.

        Author: Vladimir Beketov.
    """
    for d, dirs, files in os.walk(path_for_download_rar_01102017):
        if len(files) != 20:
            folder = path_for_download_rar_01102017
            for the_file in os.listdir(folder):
                file_path = os.path.join(folder, the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(e)
            download_rar(form_until_01102017['href'], path_for_download_rar_01102017)
    for d, dirs, files in os.walk(path_for_download_dbf_01102017):
        if len(files) != 80:
            folder = path_for_download_dbf_01102017
            for the_file in os.listdir(folder):
                file_path = os.path.join(folder, the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(e)
            download_dbf(path_for_download_rar_01102017, path_for_download_dbf_01102017)


def check_files_now():
    """This method checks the integrity of saved files and loads them if they are missing (till now).

        Input Arguments: None.
        Returns: None.

        Author: Maxim Ukraintsev.
    """
    now = datetime.date.today()
    number = (now.year - 2018) * 12 + 2 + now.month
    for d, dirs, files in os.walk(path_for_download_rar_now):
        if len(files) != number:
            folder = path_for_download_rar_now
            for the_file in os.listdir(folder):
                file_path = os.path.join(folder, the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(e)
            download_rar(form_until_now['href'], path_for_download_rar_now)
    for d, dirs, files in os.walk(path_for_download_dbf_now):
        if len(files) != 4 * number:
            folder = path_for_download_dbf_now
            for the_file in os.listdir(folder):
                file_path = os.path.join(folder, the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(e)
            download_dbf(path_for_download_rar_now, path_for_download_dbf_now)


def check_all():
    """This method checks the integrity of saved files and loads them if they are missing.

        Input Arguments: None.
        Returns: None.

        Author: Maxim Ukraintsev.
    """
    rarfile.UNRAR_TOOL = "Unrar/UnRAR.exe"
    url = "http://www.cbr.ru/banking_sector/otchetnost-kreditnykh-organizaciy/"

    r = requests.get(url)

    if r.status_code != 200:
        print("\nError with the connection to the website\n")
    else:
        print("\nConnection with the website is successful\n")

    soup = bs(r.text, "html.parser")
    months = soup.find_all('a', class_='versions_item')

    for month in months:
        if month['href'].find('123', 18, 21) != -1:
            if month['href'].find('2014') != -1 or month['href'].find('2015') != -1 or month['href'].find(
                    '201601') != -1:
                form_until_01022016['href'].append('https://www.cbr.ru' + month['href'])

            elif month['href'].find('2016') != -1 and month['href'].find('201601') == -1:
                form_until_01102017['href'].append('https://www.cbr.ru' + month['href'])

            elif month['href'].find('2017') != -1 and month['href'].find('201710') == -1 and month['href'].find(
                    '201711') == -1 and month['href'].find('201712') == -1:
                form_until_01102017['href'].append('https://www.cbr.ru' + month['href'])

            else:
                form_until_now['href'].append('https://www.cbr.ru' + month['href'])
