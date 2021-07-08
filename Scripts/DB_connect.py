from tkinter import *
import mysql.connector

main_user_name = ''
main_user_password = ''
main_user_host = ''
connection = ''


def authorization(user_name, user_password, user_host, widget):
    """
    Цель: Проверка соединения с существующей базой данных
    Вход: authuser – пользовательские данные, authpassword –
    пользовательские данные, authhost  - пользовательские данные, widget – элемент интерфейса приложения
    Выход: Exception.
    """
    try:
        # Python_is_the_BEST

        global main_user_name, main_user_password, main_user_host, connection

        main_user_name = user_name
        main_user_password = user_password
        main_user_host = 'localhost'

        connection = mysql.connector.connect(
            host=main_user_host,
            user=user_name,
            password=main_user_password,
            auth_plugin='mysql_native_password'
        )

        widget.destroy()
        print("Authorization complete")
        print("Your connection: ", connection)

    except Exception as e:
        print("Authorization failed")
        return e


def confirm_auth(password, usr, hst, widget):
    """
    Цель: Получение и проверка корректности данных, введенных пользователем
    Вход: pswrd – пользовательские данные,
    usr – пользовательские данные, hst – пользовательские данные, widget – элемент интерфейса приложения
    Выход: Нет.
    """
    if usr.get():
        user_name = usr.get()
    else:
        user_name = ''
        print("Некорректный username")

    if password.get():
        user_password = password.get()
    else:
        user_password = ''
        print("Некорректный пароль")

    if hst.get():
        user_host = hst.get()
    else:
        user_host = 'localhost'

    authorization(user_name, user_password, user_host, widget)


def build_widget():
    """
    Цель: Формирование диалогового окна для авторизации
    Вход: Нет.
    Выход: Нет
    """
    widget = Tk()
    widget.title("Authorization")
    widget.geometry("480x135")

    # LABELS
    label1 = Label(widget, text="Username(по умолчанию 'root')")
    label1.grid(row=0, column=0, sticky=W)
    label2 = Label(widget, text="Password")
    label2.grid(row=1, column=0, sticky=W)

    # ENTRIES
    getting_username = StringVar()
    username = Entry(widget, textvariable=getting_username, width=25)
    username.grid(row=0, column=1, sticky=W)

    getting_password = StringVar()
    password = Entry(widget, textvariable=getting_password, width=25)
    password.grid(row=1, column=1, sticky=W)

    getting_host = StringVar()

    b = Button(widget, text="Подтвердить",
               command=lambda: confirm_auth(getting_password, getting_username, getting_host, widget))
    b.grid(row=3, column=0, sticky=W)

    widget.resizable(False, False)
    widget.overrideredirect(0)
    widget.mainloop()
