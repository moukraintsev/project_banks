import matplotlib
from DB_config import return_connection
import datetime
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandastable import Table
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Radiobutton
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import filedialog as fd
import Insert_actual_info
import Check_files

connection = return_connection()
global table


def place_main_table():
    """This method outputs the main table.

        Input Arguments: None.
        Returns: link to the main table.

        Author: Vladimir Beketov
    """
    global table
    table = LabelFrame(window, text='База данных', width=1920, height=540)
    table.pack(fill="both", side="top", padx=25, pady=10)
    print("Database is downloading. Please stand by...")
    df_main = pd.read_sql(
        "SELECT * FROM `123_main` WHERE C3 != '0' ORDER BY DT", globals()['connection'])
    Frame.table = pt = Table(table, dataframe=df_main,
                             showtoolbar=False, showstatusbar=True)
    pt.show()
    return table


def export_frame():
    """This method service for creating MS Excel export frame in interface.

        Input Arguments: None.
        Returns: None.

        Author: Maxim Ukraintsev.
    """
    exp_frame = LabelFrame(window, text='Экспортировать в MS Excel', width=960, height=270)
    exp_frame.place(x=25, y=450)

    btn_1 = Button(exp_frame, text="Все банки по месяцам", background="#555", foreground="#ccc",
                   padx="15", pady="6", font="15", command=choice_month)
    btn_1.pack(expand=True, fill=BOTH)

    btn_2 = Button(exp_frame, text="Панель данных", background="#555", foreground="#ccc",
                   padx="15", pady="6", font="15", command=choice_bank)
    btn_2.pack(expand=True, fill=BOTH)

    return


def build_graph_frame():
    """This method service for creating graph frame in interface.

        Input Arguments: None.
        Returns: None.

        Author: Maxim Ukraintsev.
    """
    graph_frame = LabelFrame(window, text='Построить график', width=960, height=270)
    graph_frame.place(x=350, y=450)

    btn_1 = Button(graph_frame, text="Выбрать показатель", background="#555", foreground="#ccc",
                   padx="15", pady="6", font="15", command=choice_par)
    btn_1.pack(expand=True, fill=BOTH)

    return


def click_export_a(year, month):
    """This method exports the file when user click on the "all banks by month" button».

        Input Arguments: year, month.
        Returns: MS Excel file.

        Author: Maxim Ukraintsev.
    """
    date = str(year) + '-' + month
    df = pd.read_sql("SELECT * FROM `123_main` WHERE DT='{}'".format(date), globals()['connection'])
    export_file_path = fd.asksaveasfilename(defaultextension='.xlsx')
    df.to_excel(export_file_path, index=False, header=True)


def choice_month():
    """This method serves for selecting the month to export the table.

        Input Arguments: None.
        Returns: None.

        Author: Vladimir Beketov.
    """
    sub = tk.Toplevel(window)
    sub.transient(window)
    sub.title('Все банки по месяцам')
    sub.minsize(405, 405)
    sub.maxsize(405, 405)
    export_button = Button(sub, text='Экспортировать', command=lambda: click_export_a(year.get(), month.get()))
    export_button.pack(side='bottom')

    year = IntVar()
    month = StringVar()
    year.set(0)
    month.set(0)

    frame_year = LabelFrame(sub, text='Выберите год', width=250, height=405)
    frame_year.pack(side='right', fill='y', padx=25, pady=10)

    for i in range(2014, 2021):
        tk.Radiobutton(frame_year, text='%i' % i, value=i, variable=year).pack()

    frame_month = LabelFrame(sub, text='Выберите месяц', width=250, height=405)
    frame_month.pack(side='left', fill='y', padx=25, pady=10)

    rb_jan = Radiobutton(frame_month, text="Январь", value='01-01', variable=month)
    rb_jan.grid(row=1, column=0, sticky=W)

    rb_feb = Radiobutton(frame_month, text="Февраль", value='02-01', variable=month)
    rb_feb.grid(row=2, column=0, sticky=W)

    rb_mar = Radiobutton(frame_month, text="Март", value='03-01', variable=month)
    rb_mar.grid(row=3, column=0, sticky=W)

    rb_apr = Radiobutton(frame_month, text="Апрель", value='04-01', variable=month)
    rb_apr.grid(row=4, column=0, sticky=W)

    rb_may = Radiobutton(frame_month, text="Май", value='05-01', variable=month)
    rb_may.grid(row=5, column=0, sticky=W)

    rb_jun = Radiobutton(frame_month, text="Июнь", value='06-01', variable=month)
    rb_jun.grid(row=6, column=0, sticky=W)

    rb_jul = Radiobutton(frame_month, text="Июль", value='07-01', variable=month)
    rb_jul.grid(row=7, column=0, sticky=W)

    rb_aug = Radiobutton(frame_month, text="Август", value='08-01', variable=month)
    rb_aug.grid(row=8, column=0, sticky=W)

    rb_sep = Radiobutton(frame_month, text="Сентябрь", value='09-01', variable=month)
    rb_sep.grid(row=9, column=0, sticky=W)

    rb_oct = Radiobutton(frame_month, text="Октябрь", value='10-01', variable=month)
    rb_oct.grid(row=10, column=0, sticky=W)

    rb_nov = Radiobutton(frame_month, text="Ноябрь", value='11-01', variable=month)
    rb_nov.grid(row=11, column=0, sticky=W)

    rb_dec = Radiobutton(frame_month, text="Декабрь", value='12-01', variable=month)
    rb_dec.grid(row=12, column=0, sticky=W)


def click_export_b(regn):
    """This method exports the file when user click on the "all banks by month" button».

        Input Arguments: registration number.
        Returns: MS Excel file.

        Author: Maxim Ukraintsev.
    """
    df = pd.read_sql("SELECT * FROM `123_main` WHERE REGN='{}'".format(regn), globals()['connection'])
    export_file_path = fd.asksaveasfilename(defaultextension='.xlsx')
    df.to_excel(export_file_path, index=False, header=True)


def choice_bank():
    """This method serves for selecting the bank to export the table.

        Input Arguments: None.
        Returns: None.

        Author: Vladimir Beketov.
    """
    sub = tk.Toplevel(window)
    sub.transient(window)
    sub.title('Панель данных')
    sub.minsize(810, 540)
    sub.maxsize(810, 540)

    table_sub = LabelFrame(sub, text='Список банков', width=303, height=303)
    table_sub.pack(fill="both", side="top", padx=25, pady=10)
    df = pd.read_sql("SELECT * FROM names", globals()['connection'])
    Frame.table = pt = Table(table_sub, dataframe=df, columns=2,
                             showtoolbar=False, showstatusbar=False)
    pt.show()

    message = LabelFrame(sub, text='Введите регистрационный номер (REGN) банка', width=303, height=303)
    message.pack(fill="both", side="top", padx=25, pady=10)
    mess = StringVar()
    message_entry = Entry(message, textvariable=mess)
    message_entry.pack(padx=25, pady=0, side='left')

    message_button = Button(message, text="Экспортировать", command=lambda: click_export_b(mess.get()))
    message_button.pack(side='bottom')


def build_graph(regn, c1):
    """This method service for processing a user's request to build a graph.

        Input Arguments: registration number, indicator.
        Returns: None.

        Author: Maxim Ukraintsev.
    """
    matplotlib.use('TkAgg')
    sub = tk.Toplevel(window)
    sub.transient(window)
    sub.title('График')
    sub.minsize(960, 810)
    sub.maxsize(960, 810)

    fig = plt.figure(1, figsize=(25, 25))

    canvas = FigureCanvasTkAgg(fig, master=sub)

    plot_widget = canvas.get_tk_widget()

    df = pd.read_sql("SELECT DT, C3 FROM `123_main` WHERE REGN={} and C1={} ORDER BY DT".format(regn, c1),
                     globals()['connection'])

    df.C3 = pd.to_numeric(df.C3)

    plt.plot(df.DT, df.C3, color='red', label='Значения показателя')

    plot_widget.pack(side='top')


def choice_par():
    """This method service for creating a dialog box for plotting a graph.

        Input Arguments: None.
        Returns: None.

        Author: Maxim Ukraintsev.
    """
    sub = tk.Toplevel(window)
    sub.transient(window)
    sub.title('Выбор параметра')
    sub.minsize(1920, 810)
    sub.maxsize(1920, 810)

    table_par = LabelFrame(sub, text='Список параметров', width=960, height=540)
    table_par.pack(fill="both", side="right", padx=25, pady=10)
    df = pd.read_sql("SELECT * FROM `indicators`", globals()['connection'])
    Frame.table = pt = Table(table_par, dataframe=df, columns=2,
                             showtoolbar=False, showstatusbar=False)
    pt.show()

    table_sub = LabelFrame(sub, text='Список банков', width=960, height=540)
    table_sub.pack(fill="both", side="left", padx=25, pady=10)
    df = pd.read_sql("SELECT * FROM names", globals()['connection'])
    Frame.table = pt = Table(table_sub, dataframe=df, columns=2,
                             showtoolbar=False, showstatusbar=False)
    pt.show()

    message_1 = LabelFrame(sub, text='Введите регистрационный номер (REGN) банка', width=303, height=303)
    message_1.pack(fill="both", side="top", padx=25, pady=10)
    mess_1 = StringVar()
    message_entry_1 = Entry(message_1, textvariable=mess_1)
    message_entry_1.pack(padx=25, pady=0, side='left')

    message_2 = LabelFrame(sub, text='Введите параметр', width=303, height=303)
    message_2.pack(fill="both", side="top", padx=25, pady=10)
    mess_2 = StringVar()
    message_entry_2 = Entry(message_2, textvariable=mess_2)
    message_entry_2.pack(padx=25, pady=0, side='left')

    button_l = Label(sub, width=303, height=303)
    button_l.pack(fill="both", side="top", padx=25, pady=1)
    button = Button(button_l, text='Построить график', command=lambda: build_graph(mess_1.get(), mess_2.get()))
    button.pack(expand=True)


def check_new():
    """This method checks for relevance of database.

        Input Arguments: None.
        Returns: None.

        Author: Vladimir Beketov
    """
    choice_month_act()


def check_files():
    """This method serves for "Проверить целостность файлов" button click processing.

        Input Arguments: None.
        Returns: None.

        Author: Vladimir Beketov.
    """
    messagebox.showinfo('Проверка целостности файлов',
                        'Выполняется проверка и дозагрузка файлов с сайта ЦБ.\nЭто может занять какое-то время.')
    Check_files.check_all()
    messagebox.showinfo('Проверка целостности файлов', 'Проверка целостности файлов завершена.')


def click_download(jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec, year, widget, downloaded_dates):
    """This method serves for "Загрузить месяцы" button click processing.

        Input Arguments:
            jan - dec - take the state of the checkbuttons.
            year - take the state of the radoibuttons.
            widget - link to the verification window.
            downloaded-dates - list of the stored in the DB dates
        Returns: None.

        Author: Vladimir Beketov.
    """
    list_for_download = []
    list_for_check_download = []

    if jan == 1:
        list_for_download.append('01' + str(year))
        list_for_check_download.append(str(year) + '-02-01')
    if feb == 1:
        list_for_download.append('02' + str(year))
        list_for_check_download.append(str(year) + '-03-01')
    if mar == 1:
        list_for_download.append('03' + str(year))
        list_for_check_download.append(str(year) + '-04-01')
    if apr == 1:
        list_for_download.append('04' + str(year))
        list_for_check_download.append(str(year) + '-05-01')
    if may == 1:
        list_for_download.append('05' + str(year))
        list_for_check_download.append(str(year) + '-06-01')
    if jun == 1:
        list_for_download.append('06' + str(year))
        list_for_check_download.append(str(year) + '-07-01')
    if jul == 1:
        list_for_download.append('07' + str(year))
        list_for_check_download.append(str(year) + '-08-01')
    if aug == 1:
        list_for_download.append('08' + str(year))
        list_for_check_download.append(str(year) + '-09-01')
    if sep == 1:
        list_for_download.append('09' + str(year))
        list_for_check_download.append(str(year) + '-10-01')
    if oct == 1:
        list_for_download.append('10' + str(year))
        list_for_check_download.append(str(year) + '-11-01')
    if nov == 1:
        list_for_download.append('11' + str(year))
        list_for_check_download.append(str(year) + '-12-01')
    if dec == 1:
        list_for_download.append('12' + str(year))
        list_for_check_download.append(str(year + 1) + '-01-01')

    widget.destroy()

    global table

    if len(list_for_download) != 0:
        print('Выполняется проверка целостности файлов...')
        Check_files.check_all()
        print('Проверка завершена.')

        messagebox.showinfo('Загрузка актуальной БД',
                            'Это может занять прололжительное время.\nОставшееся время примерно ' + str(
                                20 * len(list_for_download)) + ' минут')
        Insert_actual_info.insert_actual(list_for_download, list_for_check_download, downloaded_dates)
        table.destroy()
        table = place_main_table()


def click_download_all(downloaded_dates, widget):
    """This method serves for "Загрузить все" button click processing.

        Input Arguments: downloaded dates.
        Returns: None.

        Author: Maxim Ukraintsev.
    """
    all_dates_list = []
    all_dates_check_list = []

    now = datetime.date.today()
    i = 2014
    while i <= now.year:
        if i == now.year:
            j = 1
            while j < now.month:
                if j < 10:
                    all_dates_list.append('0' + str(j) + str(i))
                    all_dates_check_list.append(str(i) + '-0' + str(j) + '-01')
                else:
                    all_dates_list.append(str(j) + str(i))
                    all_dates_check_list.append(str(i) + '-' + str(j) + '-01')
                j += 1
        else:
            j = 1
            while j < 13:
                if j < 10:
                    all_dates_list.append('0' + str(j) + str(i))
                    if i == 2014 and j == 1:
                        print()
                    else:
                        all_dates_check_list.append(str(i) + '-0' + str(j) + '-01')
                else:
                    all_dates_list.append(str(j) + str(i))
                    all_dates_check_list.append(str(i) + '-' + str(j) + '-01')
                j += 1
        i += 1
    widget.destroy()

    global table
    Insert_actual_info.insert_actual(all_dates_list, all_dates_check_list, downloaded_dates)
    table.destroy()
    table = place_main_table()


def choice_month_act():
    """This method serves for selecting the month to check the actuality.

        Input Arguments: None.
        Returns: None.

        Author: Maxim Ukraintsev.
    """
    sub = tk.Toplevel(window)
    sub.transient(window)
    sub.title('Дозагрузка БД (Проверка актуальности базы)')
    sub.minsize(607, 500)
    sub.maxsize(607, 500)
    export_button = Button(sub, text='Загрузить месяцы',
                           command=lambda: click_download(month_jan.get(), month_feb.get(), month_mar.get(),
                                                          month_apr.get(), month_may.get(), month_jun.get(),
                                                          month_jul.get(), month_aug.get(), month_sep.get(),
                                                          month_oct.get(), month_nov.get(), month_dec.get(),
                                                          year.get(), sub, list_dates))
    export_button.pack(side='bottom')

    export_all_button = Button(sub, text='Загрузить все', command=lambda: click_download_all(list_dates, sub))
    export_all_button.pack(side='bottom')

    year = IntVar()
    month_jan = IntVar()
    month_feb = IntVar()
    month_mar = IntVar()
    month_apr = IntVar()
    month_may = IntVar()
    month_jun = IntVar()
    month_jul = IntVar()
    month_aug = IntVar()
    month_sep = IntVar()
    month_oct = IntVar()
    month_nov = IntVar()
    month_dec = IntVar()

    year.set(0)
    month_jan.set(0)
    month_feb.set(0)
    month_mar.set(0)
    month_apr.set(0)
    month_may.set(0)
    month_jun.set(0)
    month_jul.set(0)
    month_aug.set(0)
    month_sep.set(0)
    month_oct.set(0)
    month_nov.set(0)
    month_dec.set(0)

    frame_year = LabelFrame(sub, text='Выберите год', width=250, height=500)
    frame_year.pack(side='right', fill='y', padx=25, pady=10)

    for i in range(2014, 2021):
        tk.Radiobutton(frame_year, text='%i' % i, value=i, variable=year).pack()

    frame_month = LabelFrame(sub, text='Выберите месяц', width=250, height=500)
    frame_month.pack(side='left', fill='y', padx=25, pady=10)

    rb_jan = Checkbutton(frame_month, text="Январь", variable=month_jan)
    rb_jan.grid(row=1, column=0, sticky=W)

    rb_feb = Checkbutton(frame_month, text="Февраль", variable=month_feb)
    rb_feb.grid(row=2, column=0, sticky=W)

    rb_mar = Checkbutton(frame_month, text="Март", variable=month_mar)
    rb_mar.grid(row=3, column=0, sticky=W)

    rb_apr = Checkbutton(frame_month, text="Апрель", variable=month_apr)
    rb_apr.grid(row=4, column=0, sticky=W)

    rb_may = Checkbutton(frame_month, text="Май", variable=month_may)
    rb_may.grid(row=5, column=0, sticky=W)

    rb_jun = Checkbutton(frame_month, text="Июнь", variable=month_jun)
    rb_jun.grid(row=6, column=0, sticky=W)

    rb_jul = Checkbutton(frame_month, text="Июль", variable=month_jul)
    rb_jul.grid(row=7, column=0, sticky=W)

    rb_aug = Checkbutton(frame_month, text="Август", variable=month_aug)
    rb_aug.grid(row=8, column=0, sticky=W)

    rb_sep = Checkbutton(frame_month, text="Сентябрь", variable=month_sep)
    rb_sep.grid(row=9, column=0, sticky=W)

    rb_oct = Checkbutton(frame_month, text="Октябрь", variable=month_oct)
    rb_oct.grid(row=10, column=0, sticky=W)

    rb_nov = Checkbutton(frame_month, text="Ноябрь", variable=month_nov)
    rb_nov.grid(row=11, column=0, sticky=W)

    rb_dec = Checkbutton(frame_month, text="Декабрь", variable=month_dec)
    rb_dec.grid(row=12, column=0, sticky=W)

    connect = globals()['connection']
    cursor = connect.cursor()

    query = """
            SELECT distinct  DT from `123_main`  order by DT
            """
    cursor.execute(query)
    rows = cursor.fetchall()

    frame_export = LabelFrame(sub, text='Актуальные месяцы', width=250, height=500)
    frame_export.pack(side='right', fill='y', padx=25, pady=10)

    txt = scrolledtext.ScrolledText(frame_export, width=250, height=500)
    txt.pack(fill='x', padx=25, pady=10)

    list_dates = []

    for row in rows:
        for i in row:
            list_dates.append(i)
            txt.insert(INSERT, str(i) + '\n')


if __name__ == '__main__':
    start_time = time.time()

    window = Tk()
    window.title("Индивидуальный проект")
    window.geometry('1920x1080')

    menu = Menu(window)
    new_item = Menu(menu)
    new_item.add_command(label='Проверить актуальность', command=check_new)
    new_item.add_command(label='Проверить целостность файлов', command=check_files)
    menu.add_cascade(label='База данных', menu=new_item)
    window.config(menu=menu)

    table = place_main_table()
    export_frame()
    build_graph_frame()

    window.mainloop()

    print('\n', "Program finished in %s seconds ---" % (time.time() - start_time))
