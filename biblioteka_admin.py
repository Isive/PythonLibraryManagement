import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter.messagebox import showinfo
from getpass import getpass
from subprocess import call

#import os
import mysql.connector
conn = mysql.connector.connect(user='root',password='',host='localhost',
database='biblioteka', auth_plugin='mysql_native_password')
query='SELECT * FROM ksiazki'
cursor=conn.cursor()
cursor.execute(query)
zalogowany = 0
login_window = tk.Tk()
for (id_k, Tytul, Autor, ksiazki) in cursor:
    print(f'{id_k} - {Tytul} - {Autor}')
#for k in cursor.execute('SELECT * FROM ksiazki'):
   # print(k)
    #ks = cursor.fetchall()
    #for k in cursor.execute(
    #    print(k['id_k'], k['Tytul'], k['Autor'], k['Rok_wydania'])
    #print()
query2='SELECT * FROM uzytkownicy'
cursor2=conn.cursor()
cursor2.execute(query2)
for (id, Imie, Nazwisko, Email, uzytkownicy) in cursor2:
    print(f'{id} - {Imie} - {Nazwisko} - {Email}')
#frame = Frame(openLoginWindow.login_window)
#user_window = tk.Tk()
#login_window.geometry("400x500")
#login_window.configure(bg='#88BDCC')

insertQuery="INSERT INFO users(Tytul, Autor, Rok_wydania) VALUES(%(Tytul)s,(%(Autor)s, (%(Rok_wydania)s)"
insertData = {
    'Tutul' : 'Dziady',
    'Autor' : 'Adam Mickiewicz',
    'Rok_wydania' : '1822'
}
#cursor.execute(insertQuery, insertData)
#conn.commit()
conn.close()

def logout():

    zalogowany=""
    openLoginWindow()

def Open():
    login_window.destroy()
    call(["python", "biblioteka1.py"])

def openLoginWindow():
    #login_window = tk.Tk()
    frame = Frame(login_window)
    frame.pack()
    login_window.geometry("400x500")
    login_window.configure(bg='#88BDCC')

    title = Label(login_window,
                  text = "Biblioteka Online",font=("Arial", 25))
    title.pack(pady=10)
    user_name = Label(login_window,
                  text = "Nazwa użytkownika")
    user_name.pack(pady=10,padx=10)
    #user_name.place(x=25, y=100)
    user_name_input_area = Entry(login_window,
                                width = 30)
    user_name_input_area.pack(pady=10)
    #password = getpass()
    password = Label(login_window,
                    text = "Hasło")
    password.pack(pady=10,padx=10)
    password_input_area = Entry(login_window,
                                width = 30, show="*")
    password_input_area.pack(pady=10,padx=10)
    input_login = user_name_input_area.get()
    input_pass = password_input_area.get()
    def zaloguj():
        conn = mysql.connector.connect(user='root', password='', host='localhost',
                                       database='biblioteka', auth_plugin='mysql_native_password')
        query2 = 'SELECT * FROM administracja'
        cursor2 = conn.cursor()
        cursor2.execute(query2)
        input_login = user_name_input_area.get()
        input_pass = password_input_area.get()
        global zalogowany
        for (id_a, login, haslo) in cursor2:
            if(input_login==login and input_pass==haslo):
                openAdminWindow(), login_input(), login_button.pack_forget(), user_name.pack_forget(), user_name_input_area.pack_forget(), title.pack_forget(), #register_label.pack_forget(),register_button.pack_forget(), \
                password.pack_forget(), password_input_area.pack_forget(),user_button.pack_forget()
                zalogowany = id_a
    login_button = Button(login_window,
                        text = "Zaloguj",width=30,height=2,bg='#33DD11',command =lambda:[zaloguj()])
    login_button.pack(pady=10,padx=10)

    user_button = Button(login_window, text="Użytkownik", width=20, height=1, command=Open)
    user_button.pack(pady=10, padx=10)
   # register_label = Label(login_window,
   #                 text = "Jeśli nie masz konta, to zarejestruj")
   # register_label.pack(pady=10,padx=10)
   # register_button = Button(login_window,
   #                     text = "Rejestracja",width=20,height=1,bg='#33DD11',command = lambda:[openRegisterWindow(),login_button.pack_forget(),user_name.pack_forget(),user_name_input_area.pack_forget(), title.pack_forget(),register_label.pack_forget(),
   #                                                                                      register_button.pack_forget(),password.pack_forget(),password_input_area.pack_forget()])
   # register_button.pack(pady=10,padx=10)
    frame.pack_forget()

    def login_input():
        inputValue=user_name_input_area.get()
        print(inputValue)
        inputValue2 = password_input_area.get()
        print(inputValue2)

def delete():
    login_window.login_button.destroy()

def destroyRegisterWindow(login_window):
    login_window.destroy()

def destroyUsersWindow(login_window):
    login_window.destroy()

def destroyBooksWindow(login_window):
    login_window.destroy()

def destroyBookAddWindow(login_window):
    login_window.destroy()

def destroyUserAddWindow(login_window):
    login_window.destroy()

def openRegisterWindow():
    #register_window = tk.Tk()
    login_window.clipboard_clear()
    login_window.geometry("400x500")
    login_window.configure(bg='#88BDCC')
    #login_window.destroy()
    title = Label(login_window,
                  text = "Rejestracja",font=("Arial", 25))
    title.pack(pady=10)
    user_name = Label(login_window,
                  text = "Imię")
    user_name.pack(pady=5)
    user_name_input_area = Entry(login_window,
                             width = 30)
    user_name_input_area.pack(pady=5)
    user_name2 = Label(login_window,
                       text="Nazwisko")
    user_name2.pack(pady=5)
    user_name_input_area2 = Entry(login_window,
                                  width=30)
    user_name_input_area2.pack(pady=5)
    email = Label(login_window,
                  text = "Email")
    email.pack(pady=5)
    email_input_area = Entry(login_window,
                             width = 30)
    email_input_area.pack(pady=5)
    password = Label(login_window,
                  text = "Hasło")
    password.pack(pady=5)
    password_input_area = Entry(login_window,
                             width = 30,show="*")
    password_input_area.pack(pady=5)
    re_password = Label(login_window,
                  text = "Powtórz hasło")
    re_password.pack(pady=5)
    re_password_input_area = Entry(login_window,
                             width = 30,show="*")
    re_password_input_area.pack(pady=5)
    register_button = Button(login_window,
                       text = "Zarejestruj",width=30,height=2,bg='#33DD11',command=lambda:[registerUser()])
    register_button.pack(pady=10)
    return_button = Button(login_window,
                       text = "Wróć do logowania",width=30,height=2,bg='#33DD11',command=lambda:[openLoginWindow(), title.pack_forget(),user_name.pack_forget(),user_name_input_area.pack_forget(),user_name2.pack_forget(),user_name_input_area2.pack_forget(),
                                                                                                 email.pack_forget(),email_input_area.pack_forget(),password.pack_forget(),
                                                                                                 password_input_area.pack_forget(),re_password.pack_forget(),re_password_input_area.pack_forget(),
                                                                                                 register_button.pack_forget(),return_button.pack_forget()])
    return_button.pack(pady=10)
    def registerUser():
        conn = mysql.connector.connect(user='root', password='', host='localhost',
                                       database='biblioteka', auth_plugin='mysql_native_password')
        cursor2 = conn.cursor(buffered=True)
        input_user = user_name_input_area.get()
        input_user2 = user_name_input_area2.get()
        input_pass = password_input_area.get()
        input_pass2 = re_password_input_area.get()
        input_email= email_input_area.get()
        if(input_pass==input_pass2):
            queryw = 'INSERT INTO uzytkownicy (Imie,Nazwisko,Email,Haslo) VALUES (%s, %s, %s, %s)'
            val = (input_user, input_user2, input_email, input_pass)
            cursor2.execute(queryw, val)
            conn.commit()
            print(cursor2.rowcount, "record inserted.")
        openLoginWindow(), title.pack_forget(), user_name.pack_forget(), user_name_input_area.pack_forget(),user_name2.pack_forget(), user_name_input_area2.pack_forget(),
        email.pack_forget(), email_input_area.pack_forget(), password.pack_forget(),
        password_input_area.pack_forget(), re_password.pack_forget(), re_password_input_area.pack_forget(),
        register_button.pack_forget(), return_button.pack_forget()




def openAdminWindow():   
    #admin_window = tk.Tk()
    login_window.geometry("700x600")
    login_window.configure(bg='#88BDCC')
    #login_window.destroy()
    title = Label(login_window,
                  text = "Biblioteka Online Panel Administratora",font=("Arial", 25))
    title.pack(pady=10)
    password = Label(login_window,
                  text = "Zmień Hasło")
    password.pack(pady=10)
    password_input_area = Entry(login_window,
                             width = 30,show="*")
    password_input_area.pack(pady=10)
    password2 = Label(login_window,
                  text = "Potwierdź Hasło")
    password2.pack(pady=10)
    password2_input_area = Entry(login_window,
                             width = 30,show="*")
    password2_input_area.pack(pady=10)
    input_pass = password_input_area.get()
    input_pass2 = password2_input_area.get()

    def adminEdit():
        conn = mysql.connector.connect(user='root', password='', host='localhost',
                                       database='biblioteka', auth_plugin='mysql_native_password')
        query2 = 'SELECT * FROM administracja'
        cursor2 = conn.cursor()
        cursor2.execute(query2)
        input_pass = password_input_area.get()
        input_pass2 = password2_input_area.get()
        global zalogowany
        idz=zalogowany
        for (id_a, login, haslo) in cursor2:
            if(id_a==zalogowany and input_pass==input_pass2):
                conn = mysql.connector.connect(user='root', password='', host='localhost',
                                               database='biblioteka', auth_plugin='mysql_native_password')
                cursor2 = conn.cursor()
                queryw = 'UPDATE administracja SET haslo = %s WHERE id_a = %s'
                val = (input_pass,zalogowany)
                cursor2.execute(queryw,val)
                conn.commit()
                print(cursor2.rowcount, "record update.")

    zatwierdz_button = Button(login_window,
                             text="Zatwierdź", width=20, height=1, bg='#FF5566',command =lambda:[adminEdit()])
    zatwierdz_button.pack(pady=10)
    book_add_button = Button(login_window,
                             text="Dodaj książkę", width=20, height=1, bg='#FF5566',
                             command=lambda: [openBookAddWindow(), title.pack_forget(), password.pack_forget(),
                                              password_input_area.pack_forget(), password2.pack_forget(),
                                              password2_input_area.pack_forget(),
                                              zatwierdz_button.pack_forget(), book_add_button.pack_forget(),
                                              user_add_button.pack_forget(), book_show_button.pack_forget(),
                                              user_show_button.pack_forget(),
                                              book_find_button.pack_forget(), user_find_button.pack_forget(),
                                              logout_button.pack_forget()])
    book_add_button.pack(pady=10)
    user_add_button = Button(login_window,
                             text="Dodaj Użytkownika", width=20, height=1, bg='#FF5566',
                             command=lambda: [openUserAddWindow(), title.pack_forget(), password.pack_forget(),
                                              password_input_area.pack_forget(), password2.pack_forget(),
                                              password2_input_area.pack_forget(),
                                              zatwierdz_button.pack_forget(), book_add_button.pack_forget(),
                                              user_add_button.pack_forget(), book_show_button.pack_forget(),
                                              user_show_button.pack_forget(),
                                              book_find_button.pack_forget(), user_find_button.pack_forget(),
                                              logout_button.pack_forget()])
    user_add_button.pack(pady=10)
    book_show_button = Button(login_window,
                              text="Pokaż listę książek", width=20, height=1, bg='#FF5566',
                              command=lambda: [openBooksWindow()])
    book_show_button.pack(pady=10)
    user_show_button = Button(login_window,
                              text="Pokaż listę użytkowników", width=20, height=1, bg='#FF5566',
                              command=lambda: [openUsersWindow()])
    user_show_button.pack(pady=10)
    book_find_button = Button(login_window,
                              text="Wyszukaj książkę", width=20, height=1, bg='#FF5566',
                              command=lambda: [openBookShowWindow(), title.pack_forget(), password.pack_forget(),
                                               password_input_area.pack_forget(), password2.pack_forget(),
                                               password2_input_area.pack_forget(),
                                               zatwierdz_button.pack_forget(), book_add_button.pack_forget(),
                                               user_add_button.pack_forget(), book_show_button.pack_forget(),
                                               user_show_button.pack_forget(),
                                               book_find_button.pack_forget(), user_find_button.pack_forget(),
                                               logout_button.pack_forget(), logout_button.pack_forget()])
    book_find_button.pack(pady=10)
    user_find_button = Button(login_window,
                              text="Wyszukaj użytkownika", width=20, height=1, bg='#FF5566',
                              command=lambda: [openUserShowWindow(), title.pack_forget(), password.pack_forget(),
                                               password_input_area.pack_forget(), password2.pack_forget(),
                                               password2_input_area.pack_forget(),
                                               zatwierdz_button.pack_forget(), book_add_button.pack_forget(),
                                               user_add_button.pack_forget(), book_show_button.pack_forget(),
                                               user_show_button.pack_forget(),
                                               book_find_button.pack_forget(), user_find_button.pack_forget(),
                                               logout_button.pack_forget()])
    user_find_button.pack(pady=10)
    logout_button = Button(login_window,
                           text="Wyloguj", width=20, height=1, bg='#FF5566',
                           command=lambda: [openLoginWindow(), title.pack_forget(), password.pack_forget(),
                                            password_input_area.pack_forget(), password2.pack_forget(),
                                            password2_input_area.pack_forget(),
                                            zatwierdz_button.pack_forget(), book_add_button.pack_forget(),
                                            user_add_button.pack_forget(), book_show_button.pack_forget(),
                                            user_show_button.pack_forget(),
                                            book_find_button.pack_forget(), user_find_button.pack_forget(),
                                            logout_button.pack_forget()])
    logout_button.pack(pady=10)

def openUserWindow():
    title = Label(login_window,
                  text = "Biblioteka Online Panel Użytkownika",font=("Arial", 25)).place(x = 80,
                                           y = 20) 

def openBooksWindow():   
    books_window = tk.Tk()
    books_window.geometry("820x600")
    books_window.configure(bg='#88BDCC')
    title = Label(books_window,
                  text = "Książki",font=("Arial", 25)).place(x = 280,
                                           y = 20)
    conn = mysql.connector.connect(user='root', password='', host='localhost',
                                   database='biblioteka', auth_plugin='mysql_native_password')
    query = 'SELECT * FROM ksiazki'
    cursor2 = conn.cursor()
    cursor2.execute(query)
    #id=0;
    """
    for (id_k, Tytul, Autor, ksiazki) in cursor:
        id=id+1;
        tekst=(f'{id_k} - {Tytul} - {Autor}')
        title2 = Label(books_window,
            text=tekst, font=("Arial", 15)).place(x=80,y=40 + id * 40)
            """
    columns = ('id', 'Tytul', 'Autor', 'Rok')
    tree = ttk.Treeview(books_window, columns=columns, show='headings')

        # define headings
    tree.heading('id', text='Id')
    tree.heading('Tytul', text='Tytuł')
    tree.heading('Autor', text='Autor')
    tree.heading('Rok', text='Rok wydania')

        # generate sample data
    #query2 = 'SELECT * FROM ksiazki'
    #cursor2 = conn.cursor()
    #cursor2.execute(query2)
    contacts = []
    for (id, Tytul, Autor, Rok_wydania) in cursor2:
       # contacts.append((f'{id} - {Imie} - {Nazwisko} - {Email}'))
       contacts.append((id, Tytul, Autor, Rok_wydania))
            # add data to the treeview
    for contact in contacts:
        tree.insert('', tk.END, values=contact)

    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
                    # show a message
            showinfo(title='Information', message=','.join(record))

    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=0, column=0, sticky='nsew')

            # add a scrollbar
    scrollbar = ttk.Scrollbar(books_window, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

def openUsersWindow():   
    users_window = tk.Tk()
    users_window.geometry("820x600")
    users_window.configure(bg='#88BDCC')
    title = Label(users_window,
                  text = "Użytkownicy",font=("Arial", 25)).place(x = 250,
                                           y = 20)
    conn = mysql.connector.connect(user='root', password='', host='localhost',
                                   database='biblioteka', auth_plugin='mysql_native_password')
    query2 = 'SELECT * FROM uzytkownicy'
    cursor2 = conn.cursor()
    cursor2.execute(query2)
    idu = 0;
    """
    for (id, Imie, Nazwisko, Email, uzytkownicy) in cursor2:
        idu = idu+1;
        tekst=(f'{id} - {Imie} - {Nazwisko} - {Email}')
        title2 = Label( users_window,
                  text = tekst,font=("Arial", 15)).place(x = 80,
                                           y = 40+idu*40)
        """

    columns = ('id', 'Imie', 'Nazwisko', 'Email')
    tree = ttk.Treeview(users_window, columns=columns, show='headings')

        # define headings
    tree.heading('id', text='Id')
    tree.heading('Imie', text='Imie')
    tree.heading('Nazwisko', text='Nazwisko')
    tree.heading('Email', text='Email')

        # generate sample data
   # query2 = 'SELECT * FROM uzytkownicy'
    #cursor2 = conn.cursor()
    #cursor2.execute(query2)
    contacts = []
    for (id, Imie, Nazwisko, Email, uzytkownicy) in cursor2:
       # contacts.append((f'{id} - {Imie} - {Nazwisko} - {Email}'))
       contacts.append((id, Imie, Nazwisko, Email))
            # add data to the treeview
    for contact in contacts:
        tree.insert('', tk.END, values=contact)

    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
                    # show a message
            showinfo(title='Information', message=','.join(record))

    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=0, column=0, sticky='nsew')

            # add a scrollbar
    scrollbar = ttk.Scrollbar(users_window, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')
   # return_button = Button(users_window,
    #                    text = "Powrót do panelu administratora",width=30,height=1,bg='#FF5566',command = destroyUsersWindow(users_window)
      #                     ).place(x = 100,
       #                                         y = 700)

def openUserAddWindow():   
    #user_add_window = tk.Tk()
    login_window.geometry("700x800")
    login_window.configure(bg='#88BDCC')
    usert = tk.StringVar()
    usert2 = tk.StringVar()
    emailt = tk.StringVar()
    passt = tk.StringVar()
    title = Label(login_window,
                  text = "Dodaj użytkownika",font=("Arial", 25))
    title.pack(pady=5)
    user_name = Label(login_window,
                      text="Imię")
    user_name.pack(pady=5)
    user_name_input_area = Entry(login_window,textvariable=usert,
                                 width=30)
    user_name_input_area.pack(pady=5)
    user_name2 = Label(login_window,
                      text="Nazwisko")
    user_name2.pack(pady=5)
    user_name_input_area2 = Entry(login_window, textvariable=usert2,
                                 width=30)
    user_name_input_area2.pack(pady=5)
    email = Label(login_window,
                  text="Email")
    email.pack(pady=5)
    email_input_area = Entry(login_window,textvariable=emailt,
                             width=30)
    email_input_area.pack(pady=5)
    password = Label(login_window,
                     text="Hasło")
    password.pack(pady=5)
    password_input_area = Entry(login_window,textvariable=passt,
                                width=30,show="*")
    password_input_area.pack(pady=5)
    re_password = Label(login_window,
                        text="Powtórz hasło")
    re_password.pack(pady=5)
    re_password_input_area = Entry(login_window,
                                   width=30,show="*")
    re_password_input_area.pack(pady=5)
    #user_name_input_area="x"
    #user_name_input_area(usert).pack()
    #print(s)
    print(usert)
    print(usert.get())
    def addUser():
        #entryString = user_name_input_area.get()
        #name = (user_name_input_area.get())
        #print(name)
        #print(usert)
        #print(usert.get())
        conn = mysql.connector.connect(user='root', password='', host='localhost',
                                       database='biblioteka', auth_plugin='mysql_native_password')
        cursor2 = conn.cursor(buffered=True)
        input_user = user_name_input_area.get()
        input_user2 = user_name_input_area2.get()
        input_pass = password_input_area.get()
        input_pass2 = re_password_input_area.get()
        input_email= email_input_area.get()
        if(input_pass==input_pass2):
            queryw = 'INSERT INTO uzytkownicy (Imie,Nazwisko,Email,Haslo) VALUES (%s, %s, %s, %s)'
            val = (input_user, input_user2, input_email, input_pass)
            cursor2.execute(queryw, val)
            conn.commit()
            print(cursor2.rowcount, "record inserted.")

        #VALUES(NULL, "x", "b", "a", "password")
        #cursor3 = conn.cursor()
        #cursor3.execute(queryw)
        #print(id, Imie, Nazwisko, Email, uzytkownicy)
    user_add_button = Button(login_window,
                        text = "Dodaj Użytkownika",width=20,height=1,bg='#FF5566',command =addUser)
    user_add_button.pack(pady=10)
    return_button = Button(login_window,
                        text = "Powrót do panelu administratora",width=30,height=1,bg='#FF5566',command=lambda:[openAdminWindow(),title.pack_forget(),user_name.pack_forget(),user_name_input_area.pack_forget(),
                                                                                                                user_name2.pack_forget(),user_name_input_area2.pack_forget(),email.pack_forget(),email_input_area.pack_forget(),
                                                                                                                password.pack_forget(),password_input_area.pack_forget(),re_password.pack_forget(),re_password_input_area.pack_forget(),
                                                                                                                user_add_button.pack_forget(),return_button.pack_forget()])

    return_button.pack(pady=10)

def openBookAddWindow():   
    #book_add_window = tk.Tk()
    login_window.geometry("700x500")
    login_window.configure(bg='#88BDCC')
    title = Label(login_window,
                  text = "Dodaj książkę",font=("Arial", 25))
    title.pack(pady=10)
    tytul = Label(login_window,
                      text="Tytuł")
    tytul.pack(pady=10)
    tytul_input_area = Entry(login_window,
                                 width=30)
    tytul_input_area.pack(pady=10)
    autor = Label(login_window,
                  text="Autor")
    autor.pack(pady=10)
    autor_input_area = Entry(login_window,
                             width=30)
    autor_input_area.pack(pady=10)
    rok = Label(login_window,
                  text="Rok wydania")
    rok.pack(pady=10)
    rok_input_area = Entry(login_window,
                             width=30)
    rok_input_area.pack(pady=10)

    def addBook():

        conn = mysql.connector.connect(user='root', password='', host='localhost',
                                       database='biblioteka', auth_plugin='mysql_native_password')
        cursor2 = conn.cursor(buffered=True)
        input_tytul = tytul_input_area.get()
        input_autor = autor_input_area.get()
        input_rok = rok_input_area.get()
        queryw = 'INSERT INTO ksiazki (Tytul,Autor,Rok_wydania) VALUES ( %s, %s, %s)'
        val = (input_tytul, input_autor, input_rok)
        cursor2.execute(queryw, val)
        conn.commit()
        print(cursor2.rowcount, "record inserted.")
    book_add_button = Button(login_window,
                        text = "Dodaj książkę",width=20,height=1,bg='#FF5566',command =addBook)
    book_add_button.pack(pady=10)
    return_button = Button(login_window,
                        text = "Powrót do panelu administratora",width=30,height=1,bg='#FF5566',command=lambda:[openAdminWindow(),title.pack_forget(),tytul.pack_forget(),tytul_input_area.pack_forget(),autor.pack_forget(),autor_input_area.pack_forget(),
                                                                                                                rok.pack_forget(),rok_input_area.pack_forget(),book_add_button.pack_forget(),return_button.pack_forget()])

    return_button.pack(pady=10)

def openUserShowWindow():
    login_window.geometry("600x700")
    login_window.configure(bg='#88BDCC')
    userid = tk.StringVar()
    usert = tk.StringVar()
    usert2 = tk.StringVar()
    emailt = tk.StringVar()
    emailt_new = tk.StringVar()
    passt = tk.StringVar()
    usert_new = tk.StringVar()
    title = Label(login_window,
                  text="Wyszukaj użytkownika", font=("Arial", 25))
    title.pack(pady=5)
    user_id = Label(login_window,
                      text="Id")
    user_id.pack(pady=5)
    user_id_input_area = Entry(login_window, textvariable=userid,
                                 width=30)
    user_id_input_area.pack(pady=5)
    user_name = Label(login_window,
                      text="Imię")
    user_name.pack(pady=5)
    user_name_input_area = Entry(login_window, textvariable=usert,
                                 width=30)
    user_name_input_area.pack(pady=5)
    user_name2 = Label(login_window,
                      text="Nazwisko")
    user_name2.pack(pady=5)
    user_name_input_area2 = Entry(login_window, textvariable=usert2,
                                 width=30)
    user_name_input_area2.pack(pady=5)
    email = Label(login_window,
                  text="Email")
    email.pack(pady=5)
    email_input_area = Entry(login_window, textvariable=emailt,
                             width=30)
    email_input_area.pack(pady=5)
    # user_name_input_area="x"
    # user_name_input_area(usert).pack()
    # print(s)
    print(usert)
    print(usert.get())

    def showUser():
        users_window = tk.Tk()
        users_window.geometry("820x500")
        users_window.configure(bg='#88BDCC')
        conn = mysql.connector.connect(user='root', password='', host='localhost',
                                       database='biblioteka', auth_plugin='mysql_native_password')
        cursor = conn.cursor(buffered=True)
        input_id = user_id_input_area.get()
        input_imie = user_name_input_area.get()
        input_nazwisko = user_name_input_area2.get()
        input_email = email_input_area.get()
        query2 = "select * from uzytkownicy where Id LIKE \"%"+input_id+"%\" AND Imie LIKE \"%"+input_imie+"%\" AND Nazwisko LIKE \"%"+input_nazwisko+"%\" AND Email LIKE \"%"+input_email+"%\" "
        cursor2 = conn.cursor()
        cursor2.execute(query2)


        columns = ('id', 'Imie', 'Nazwisko', 'Email')
        tree = ttk.Treeview(users_window, columns=columns, show='headings')
        # define headings
        tree.heading('id', text='Id')
        tree.heading('Imie', text='Imie')
        tree.heading('Nazwisko', text='Nazwisko')
        tree.heading('Email', text='Email')

        contacts = []
        for (id, Imie, Nazwisko, Email, uzytkownicy) in cursor2:
            #if (int(input_id) == int(id) or input_imie == Imie or input_nazwisko == Nazwisko or input_email == Email):

            contacts.append((id, Imie, Nazwisko, Email))
        for contact in contacts:
            tree.insert('', tk.END, values=contact)

        def item_selected(event):
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']
                # show a message
                showinfo(title='Information', message=','.join(record))

        tree.bind('<<TreeviewSelect>>', item_selected)

        tree.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar
        scrollbar = ttk.Scrollbar(users_window, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

    def editUser():
        conn = mysql.connector.connect(user='root', password='', host='localhost',
                                       database='biblioteka', auth_plugin='mysql_native_password')
        cursor = conn.cursor(buffered=True)
        query2 = 'SELECT * FROM uzytkownicy'
        cursor2 = conn.cursor()
        cursor2.execute(query2)
        input_id = user_id_input_area.get()
        input_imie = user_name_input_area.get()
        input_nazwisko = user_name_input_area2.get()
        input_email = email_input_area.get()
        input_nazwisko_new = user_name_new_input_area.get()
        input_email_new = email_new_input_area.get()
        for (id, Imie, Nazwisko, Email, uzytkownicy) in cursor2:
            # tekst = (f'{id} - {Imie} - {Nazwisko} - {Email}')
            if (int(input_id) == int(id) or input_imie == Imie or input_nazwisko == Nazwisko or input_email == Email):
                conn = mysql.connector.connect(user='root', password='', host='localhost',
                                               database='biblioteka', auth_plugin='mysql_native_password')
                cursor2 = conn.cursor()
                if(input_nazwisko_new != ""):
                    queryw = 'UPDATE uzytkownicy SET Nazwisko =%s WHERE id= %s OR Imie = %s OR Nazwisko = %s OR Email = %s'
                    val = (input_nazwisko_new, input_id, input_imie, input_nazwisko, input_email)
                    cursor2.execute(queryw, val)
                    conn.commit()
                    print(cursor2.rowcount, "record edited.")
                if(input_email_new != ""):
                    queryw = 'UPDATE uzytkownicy SET Email =%s WHERE id= %s OR Imie = %s OR Nazwisko = %s OR Email = %s'
                    val = (input_email_new, input_id, input_imie, input_nazwisko, input_email)
                    cursor2.execute(queryw, val)
                    conn.commit()
                    print(cursor2.rowcount, "record edited.")

    def removeUser():
        conn = mysql.connector.connect(user='root', password='', host='localhost',
                                       database='biblioteka', auth_plugin='mysql_native_password')
        cursor = conn.cursor(buffered=True)
        query2 = 'SELECT * FROM uzytkownicy'
        cursor2 = conn.cursor()
        cursor2.execute(query2)
        input_id = user_id_input_area.get()
        input_imie = user_name_input_area.get()
        input_nazwisko = user_name_input_area2.get()
        input_email = email_input_area.get()
        for (id, Imie, Nazwisko, Email, uzytkownicy) in cursor2:
            #tekst = (f'{id} - {Imie} - {Nazwisko} - {Email}')
            if (input_id == id or input_imie == Imie or input_nazwisko == Nazwisko or input_email == Email):
                conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                   database='biblioteka', auth_plugin='mysql_native_password')
                cursor2 = conn.cursor()
                queryw = 'DELETE FROM uzytkownicy WHERE id= %s OR Imie = %s OR Nazwisko = %s OR Email = %s'
                val = (input_id, input_imie, input_nazwisko,input_email)
                cursor2.execute(queryw, val)
                conn.commit()
                print(cursor2.rowcount, "record delete.")
    user_add_button = Button(login_window,
                             text="Pokaż Użytkownika", width=20, height=1, bg='#FF5566', command=showUser)
    user_add_button.pack(pady=5)
    title2 = Label(login_window,
                  text="Nowe dane edycja użytkownika", font=("Arial", 15))
    title2.pack(pady=5)
    user_name_new = Label(login_window,
                       text="Nazwisko")
    user_name_new.pack(pady=5)
    user_name_new_input_area = Entry(login_window, textvariable=usert_new,
                                  width=30)
    user_name_new_input_area.pack(pady=5)
    email_new = Label(login_window,
                  text="Email")
    email_new.pack(pady=5)
    email_new_input_area = Entry(login_window, textvariable=emailt_new,
                             width=30)
    email_new_input_area.pack(pady=5)
    user_edit_button = Button(login_window,
                             text="Edytuj dane Użytkownika", width=20, height=1, bg='#FF5566', command=editUser)
    user_edit_button.pack(pady=5)
    user_remove_button = Button(login_window,
                             text="Usuń Użytkownika", width=20, height=1, bg='#FF5566', command=removeUser)
    user_remove_button.pack(pady=5)
    return_button = Button(login_window,
                           text="Powrót do panelu administratora", width=30, height=1, bg='#FF5566',
                           command=lambda: [openAdminWindow(), title.pack_forget(), title2.pack_forget(),
                                            user_name.pack_forget(), user_name_input_area.pack_forget(),
                                            user_id.pack_forget(), user_id_input_area.pack_forget(),
                                            user_name2.pack_forget(), user_name_input_area2.pack_forget(),
                                            user_name_new.pack_forget(), user_name_new_input_area.pack_forget(),
                                            email.pack_forget(), email_input_area.pack_forget(),
                                            email_new.pack_forget(), email_new_input_area.pack_forget(),
                                            user_add_button.pack_forget(), user_edit_button.pack_forget(),
                                            user_remove_button.pack_forget(), return_button.pack_forget()])

    return_button.pack(pady=10)

def openBookShowWindow():
    login_window.geometry("700x600")
    login_window.configure(bg='#88BDCC')
    title = Label(login_window,
                  text="Wyszukaj książkę", font=("Arial", 25))
    title.pack(pady=10)
    tytul = Label(login_window,
                  text="Tytuł")
    tytul.pack(pady=10)
    tytul_input_area = Entry(login_window,
                             width=30)
    tytul_input_area.pack(pady=10)
    autor = Label(login_window,
                  text="Autor")
    autor.pack(pady=10)
    autor_input_area = Entry(login_window,
                             width=30)
    autor_input_area.pack(pady=10)
    rok = Label(login_window,
                text="Rok wydania")
    rok.pack(pady=10)
    rok_input_area = Entry(login_window,
                           width=30)
    rok_input_area.pack(pady=10)
    def showBook():
        books_window = tk.Tk()
        books_window.geometry("820x700")
        books_window.configure(bg='#88BDCC')
        conn = mysql.connector.connect(user='root', password='', host='localhost',
                                       database='biblioteka', auth_plugin='mysql_native_password')
        cursor2 = conn.cursor(buffered=True)
        input_tytul = tytul_input_area.get()
        input_autor = autor_input_area.get()
        input_rok = rok_input_area.get()
        query = "select * from ksiazki where Tytul LIKE \"%"+input_tytul+"%\" AND Autor LIKE \"%"+input_autor+"%\" AND Rok_wydania LIKE \"%"+input_rok+"%\" "
        cursor2 = conn.cursor()
        cursor2.execute(query)
        # id=0;
        columns = ('id', 'Tytul', 'Autor', 'Rok')
        tree = ttk.Treeview(books_window, columns=columns, show='headings')

        # define headings
        tree.heading('id', text='Id')
        tree.heading('Tytul', text='Tytuł')
        tree.heading('Autor', text='Autor')
        tree.heading('Rok', text='Rok wydania')

        contacts = []
        for (id, Tytul, Autor, Rok_wydania) in cursor2:
            # contacts.append((f'{id} - {Imie} - {Nazwisko} - {Email}'))
            if (input_tytul == Tytul or input_autor == Autor or input_rok == Rok_wydania):
                contacts.append((id, Tytul, Autor, Rok_wydania))
            # add data to the treeview
        for contact in contacts:
            tree.insert('', tk.END, values=contact)

        def item_selected(event):
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']
                # show a message
                showinfo(title='Information', message=','.join(record))

        tree.bind('<<TreeviewSelect>>', item_selected)

        tree.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar
        scrollbar = ttk.Scrollbar(books_window, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

    def removeBook():
        conn = mysql.connector.connect(user='root', password='', host='localhost',
                                       database='biblioteka', auth_plugin='mysql_native_password')
        cursor = conn.cursor(buffered=True)
        query2 = 'SELECT * FROM ksiazki'
        cursor2 = conn.cursor()
        cursor2.execute(query2)
        input_tytul = tytul_input_area.get()
        input_autor = autor_input_area.get()
        input_rok = rok_input_area.get()
        print("test1")
        for (id_k, Tytul, Autor, Rok_wydania) in cursor2:
            tekst = (f'{id_k} - {Tytul} - {Autor} - {Rok_wydania}')
            print("test2")
            if (input_tytul == Tytul or input_autor == Autor or input_rok == Rok_wydania):
                conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                   database='biblioteka', auth_plugin='mysql_native_password')
                cursor2 = conn.cursor()
                print("test3")
                queryw = 'DELETE FROM ksiazki WHERE Tytul = %s OR Autor = %s OR Rok_wydania = %s'
                val = (input_tytul, input_autor, input_rok)
                cursor2.execute(queryw, val)
                print("test4")
                conn.commit()
                print(cursor2.rowcount, "record delete.")
    book_add_button = Button(login_window,
                        text = "Pokaż książkę",width=20,height=1,bg='#FF5566',command =showBook)
    book_add_button.pack(pady=10)
    book_remove_button = Button(login_window,
                             text="Usuń książkę", width=20, height=1, bg='#FF5566', command=removeBook)
    book_remove_button.pack(pady=10)
    return_button = Button(login_window,
                        text = "Powrót do panelu administratora",width=30,height=1,bg='#FF5566',command=lambda:[openAdminWindow(),title.pack_forget(),tytul.pack_forget(),tytul_input_area.pack_forget(),autor.pack_forget(),autor_input_area.pack_forget(),
                                                                                                                rok.pack_forget(),rok_input_area.pack_forget(),book_add_button.pack_forget(),book_remove_button.pack_forget(),return_button.pack_forget()])

    return_button.pack(pady=10)


def openUserWindow():
    #openUserWindow.user_window.destroy()
    #openUserWindow.user_window = Tk()
    login_window.geometry("900x700")

    browse = Frame(openUserWindow.user_window)
    borrowed = Frame(openUserWindow.user_window)
    borrow_book = Frame(openUserWindow.user_window)
    return_book = Frame(openUserWindow.user_window)
    edit_account = Frame(openUserWindow.user_window)

    def change_to_browse():
        browse.pack(fill='both', expand=1)
        borrowed.pack_forget()
        borrow_book.forget()
        edit_account.pack_forget()
        return_book.pack_forget()

    def change_to_borrowed():
        borrowed.pack(fill='both', expand=1)
        browse.pack_forget()
        borrow_book.forget()
        edit_account.pack_forget()
        return_book.pack_forget()

    def change_to_borrow_book():
        borrow_book.pack(fill='both', expand=1)
        browse.pack_forget()
        borrowed.pack_forget()
        edit_account.pack_forget()
        return_book.pack_forget()

    def change_to_return_book():
        return_book.pack(fill='both', expand=1)
        browse.pack_forget()
        borrowed.pack_forget()
        borrow_book.pack_forget()
        edit_account.pack_forget()

    def change_to_edit_account():
        edit_account.pack(fill='both', expand=1)
        browse.pack_forget()
        borrowed.pack_forget()
        borrow_book.pack_forget()
        return_book.pack_forget()

    font1 = font.Font(family='Georgia', size='22', weight='bold')
    font2 = font.Font(family='Aerial', size='12')

    label1 = Label(browse, text="Przeglądaj", foreground="green3", font=font1)
    label1.pack(pady=300)

    label2 = Label(borrowed, text="Wypożyczenia", foreground="green3", font=font1)
    label2.pack(pady=300)

    label3 = Label(borrow_book, text="Wypożycz książkę", foreground="green3", font=font1)
    label3.pack(pady=300)

    label4 = Label(return_book, text="Zwróć książkę", foreground="green3", font=font1)
    label4.pack(pady=300)

    label5 = Label(edit_account, text="Edytuj konto", foreground="green3", font=font1)
    label5.pack(pady=300)

    title = Label(openUserWindow.login_window,
                  text="Biblioteka Online", foreground="green3", font=font1).place(x=300,
                                                                                   y=0)

    opcja_1 = Button(openUserWindow.login_window,
                     text="Przeglądaj", width=20, height=2, bg='#FF0011', command=change_to_browse).place(x=0,
                                                                                                          y=80)
    opcja_2 = Button(openUserWindow.login_window,
                     text="Wypożyczone", width=20, height=2, bg='#FF0011', command=change_to_borrowed).place(x=150,
                                                                                                             y=80)
    opcja_3 = Button(openUserWindow.login_window,
                     text="Wypożycz", width=20, height=2, bg='#FF0011', command=change_to_borrow_book).place(x=300,
                                                                                                             y=80)
    opcja_4 = Button(openUserWindow.login_window,
                     text="Zwróć", width=20, height=2, bg='#FF0011', command=change_to_return_book).place(x=450,
                                                                                                          y=80)
    opcja_5 = Button(openUserWindow.login_window,
                     text="Edytuj konto", width=20, height=2, bg='#FF0011', command=change_to_edit_account).place(x=600,
                                                                                                                  y=80)
    opcja_6 = Button(openUserWindow.login_window,
                     text="Wyloguj", width=20, height=2, bg='#FF0011',
                     command=lambda: [openLoginWindow(), openUserWindow.login_window.destroy()]).place(x=750,
                                                                                                      y=80)


openLoginWindow()
#openUserWindow()
#user_window.mainloop()
login_window.mainloop()
#admin_window.mainloop()