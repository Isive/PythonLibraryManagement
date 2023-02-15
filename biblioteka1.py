from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector
import re
from datetime import date
from subprocess import call

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

db = mysql.connector.connect(host="localhost",user="root",passwd="",database="biblioteka")
mycur = db.cursor()


def Open():
    login_window.destroy()
    call(["python", "biblioteka_admin.py"])


def check(email):

    if(re.search(regex,email)):
        return 1
    else:
        return 0

def error_destroy():
    err.destroy()

def succ_destroy():
    succ.destroy()
    register_window.destroy()
    openLoginWindow()

def succ_destroy1():
    succ.destroy()

def error():
    global err
    err = Toplevel(register_window)
    err.title("Error")
    err.geometry("400x100")
    Label(err,text="Wszystkie pola są wymagane",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="grey",width=8,height=1,command=error_destroy).pack()

def error2():
    global err
    err = Toplevel(register_window)
    err.title("Error")
    err.geometry("400x100")
    Label(err,text="Hasła muszą się zgadzać!",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="grey",width=8,height=1,command=error_destroy).pack()

def error3():
    global err
    err = Toplevel(register_window)
    err.title("Error")
    err.geometry("400x100")
    Label(err,text="Niepoprawny email!",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="grey",width=8,height=1,command=error_destroy).pack()

def error4():
    global err
    err = Toplevel(register_window)
    err.title("Error")
    err.geometry("400x100")
    Label(err,text="Email jest już użyty!",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="grey",width=8,height=1,command=error_destroy).pack()

def error5():
    global err
    err = Toplevel(register_window)
    err.title("Error")
    err.geometry("600x100")
    Label(err,text="Imie i/lub nazwisko musi składać się z przynajmniej 2 znaków!",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="grey",width=8,height=1,command=error_destroy).pack()

def error6():
    global err
    err = Toplevel(register_window)
    err.title("Error")
    err.geometry("600x100")
    Label(err,text="Hasło musi składać się z przynajmniej 5 znaków!",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="grey",width=8,height=1,command=error_destroy).pack()

def error7():
    global err
    err = Toplevel(login_window)
    err.title("Error")
    err.geometry("500x100")
    Label(err,text="Brak konta z podanymi danymi!",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="grey",width=8,height=1,command=error_destroy).pack()

def error8():
    global err
    err = Toplevel(login_window)
    err.title("Error")
    err.geometry("500x100")
    Label(err,text="Wszystkie pola są wymagane",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="grey",width=8,height=1,command=error_destroy).pack()

def error9():
    global err
    err = Toplevel(user_window)
    err.title("Error")
    err.geometry("400x100")
    Label(err,text="Brak książki o podanym ID",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="grey",width=8,height=1,command=error_destroy).pack()

def error10():
    global err
    err = Toplevel(user_window)
    err.title("Error")
    err.geometry("400x100")
    Label(err,text="Książka jest wypożyczona",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="grey",width=8,height=1,command=error_destroy).pack()

def error11():
    global err
    err = Toplevel(user_window)
    err.title("Error")
    err.geometry("500x100")
    Label(err,text="Nowe hasło musi różnić się od starego",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="grey",width=8,height=1,command=error_destroy).pack()

def error12():
    global err
    err = Toplevel(user_window)
    err.title("Error")
    err.geometry("400x100")
    Label(err,text="Hasła muszą się zgadzać!",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="grey",width=8,height=1,command=error_destroy).pack()

def error13():
    global err
    err = Toplevel(user_window)
    err.title("Error")
    err.geometry("600x100")
    Label(err,text="Hasło musi składać się z przynajmniej 5 znaków!",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="grey",width=8,height=1,command=error_destroy).pack()

def error14():
    global err
    err = Toplevel(user_window)
    err.title("Error")
    err.geometry("600x100")
    Label(err,text="Imie i/lub nazwisko musi składać się z przynajmniej 2 znaków!",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="grey",width=8,height=1,command=error_destroy).pack()
def success():
    global succ
    succ = Toplevel(register_window)
    succ.title("Success")
    succ.geometry("400x100")
    Label(succ, text="Zarejestrowano pomyślnie", fg="green", font="bold").pack()
    Label(succ, text="").pack()
    Button(succ, text="Ok", bg="grey", width=8, height=1, command=succ_destroy).pack()


def success1():
    global succ
    succ = Toplevel(user_window)
    succ.title("Success")
    succ.geometry("400x100")
    Label(succ, text="Pomyślnie wypożyczono", fg="green", font="bold").pack()
    Label(succ, text="").pack()
    Button(succ, text="Ok", bg="grey", width=8, height=1, command=succ_destroy1).pack()

def success2():
    global succ
    succ = Toplevel(user_window)
    succ.title("Success")
    succ.geometry("400x100")
    Label(succ, text="Pomyślnie zwrócono", fg="green", font="bold").pack()
    Label(succ, text="").pack()
    Button(succ, text="Ok", bg="grey", width=8, height=1, command=succ_destroy1).pack()

def success3():
    global succ
    succ = Toplevel(user_window)
    succ.title("Success")
    succ.geometry("400x100")
    Label(succ, text="Pomyślnie zaktualizowano", fg="green", font="bold").pack()
    Label(succ, text="").pack()
    Button(succ, text="Ok", bg="grey", width=8, height=1, command=succ_destroy1).pack()

def login_user():
     global email_info
     email_info = email_input_area.get()
     global password_info
     password_info = password_input_area.get()

     global id_u
     global firstname
     global lastname
     global email
     global password

     sql2 = """select COUNT(*) from uzytkownicy where Email = %s AND Haslo = %s"""
     t2 = (email_info,password_info)
     mycur.execute(sql2,t2)

     rows=mycur.fetchone()



     found = rows[0]

     sql3 = """select * from uzytkownicy where Email = %s AND Haslo = %s"""
     t3 = (email_info,password_info)
     mycur.execute(sql3,t3)
     rows2=mycur.fetchone()

     if found == 0:
         error7()
     elif email_info == "":
        error8()
     elif password_info == "":
        error8()
     else:
        id_u = rows2[0]
        firstname = rows2[1]
        lastname = rows2[2]
        email = rows2[3]
        password = rows2[4]
        openUserWindow()

def logout():

    email_info=""
    password_info=""
    user_window.destroy()
    openLoginWindow()

def loginReturn():

    register_window.destroy()
    openLoginWindow()

def openLoginWindow():

    global email_input_area
    global password_input_area

    global login_window

    login_window = tk.Tk()
    login_window.geometry("400x500")
    login_window.resizable(False, False)
    email_input_area = tk.StringVar()
    password_input_area = tk.StringVar()

    Label(login_window, text = "Biblioteka Online",font=("Arial", 25)).place(x = 80,y = 20)
    Label(login_window, text = "Email").place(x = 40, y = 120)
    Entry(login_window,textvariable=email_input_area,width = 30).place(x = 160,y = 120)
    Label(login_window, text = "Hasło").place(x = 40,y = 160)
    Entry(login_window,textvariable=password_input_area, show="*",width = 30).place(x = 160,y = 160)
    Button(login_window, text = "Zaloguj",width=30,height=2,bg='#e0e0de',command = login_user).place(x = 100,y = 200)
    Label(login_window, text = "Jeśli nie masz konta, to zarejestruj").place(x = 120,y = 270)
    Button(login_window, text = "Rejestracja",width=20,height=1,bg='#e0e0de',command = openRegisterWindow).place(x = 130, y = 300)
    Label(login_window, text="Panel administratora").place(x=120, y=360)
    Button(login_window,text="Administrator", width=20, height=1,bg='#e0e0de', command=Open).place(x=130,y=390)
    login_window.mainloop()

def register_user():
     firstname_info = firstname_input_area.get()
     lastname_info = lastname_input_area.get()
     email_info = email_input_area.get()
     password_info = password_input_area.get()
     repassword_info = repassword_input_area.get()

     sql1 = """select COUNT(*) from uzytkownicy where Email = %s"""
     t1 = (email_info,)
     mycur.execute(sql1,t1)

     rows=mycur.fetchone()
     found = rows[0]

     if found != 0:
         error4()
     elif len(firstname_info)<2:
         error5()
     elif len(lastname_info)<2:
         error5()
     elif firstname_info == "":
        error()
     elif lastname_info == "":
        error()
     elif email_info == "":
        error()
     elif len(password_info)<5:
        error6()
     elif password_info == "":
        error()
     elif password_info != repassword_info:
         error2()
     elif check(email_info) == 0:
         error3()

     else:
        sql = "insert into uzytkownicy (Imie,Nazwisko,Email,Haslo) values(%s,%s,%s,%s)"
        t = (firstname_info,lastname_info,email_info, password_info)
        mycur.execute(sql, t)
        db.commit()
        Label(register_window, text="").pack()
        success()


def openRegisterWindow():


    global firstname_input_area
    global lastname_input_area
    global email_input_area
    global password_input_area
    global repassword_input_area

    global register_window

    login_window.destroy()
    register_window = tk.Tk()
    register_window.geometry("400x500")
    register_window.resizable(False, False)

    firstname_input_area = tk.StringVar()
    lastname_input_area = tk.StringVar()
    email_input_area = tk.StringVar()
    password_input_area = tk.StringVar()
    repassword_input_area = tk.StringVar()
    Label(register_window,text = "Rejestracja",font=("Arial", 25)).place(x = 80,y = 20)
    Label(register_window,text = "Imię",).place(x = 40,y = 120)
    Entry(register_window,textvariable=firstname_input_area,width = 30).place(x = 160,y = 120)
    Label(register_window,text = "Nazwisko").place(x = 40,y = 160)
    Entry(register_window,textvariable=lastname_input_area,width = 30).place(x = 160,y = 160)
    Label(register_window,text = "Email").place(x = 40,y = 200)
    Entry(register_window,textvariable=email_input_area,width = 30).place(x = 160,y = 200)
    Label(register_window,text = "Hasło").place(x = 40,y = 240)
    Entry(register_window,show="*",textvariable=password_input_area,width = 30).place(x = 160,y = 240)
    Label(register_window,text = "Powtórz hasło").place(x = 40,y = 280)
    Entry(register_window,show="*",textvariable=repassword_input_area,width = 30).place(x = 160,y = 280)
    Button(register_window,text = "Zarejestruj",width=30,height=2,bg='#e0e0de',command=register_user).place(x = 100,y = 320)
    Button(register_window,text = "Wróć",width=20,height=2,bg='#e0e0de',command=loginReturn).place(x = 140,y = 360)

def openUserWindow():

    def raise_frame(frame):
        frame.tkraise()

    global user_window
    global id_w_ksiazki
    global id_z_ksiazki
    global tytul
    global autor
    global rok_wydania

    login_window.destroy()
    user_window = tk.Tk()
    user_window.geometry("1050x700")
    user_window.resizable(False, False)

    browse = Frame(user_window,highlightbackground="grey", highlightthickness=3)
    borrowed = Frame(user_window,highlightbackground="grey", highlightthickness=3)
    borrow_book = Frame(user_window,highlightbackground="grey", highlightthickness=3)
    return_book = Frame(user_window,highlightbackground="grey", highlightthickness=3)
    edit_account = Frame(user_window,highlightbackground="grey", highlightthickness=3)
    search_book = Frame(user_window,highlightbackground="grey", highlightthickness=3)
    menu = Frame(user_window, highlightbackground="grey", highlightthickness=3)
    footer = Frame(user_window, highlightbackground="grey", highlightthickness=3)

    browse.config(bg='#e0e0de')
    borrowed.config(bg='#e0e0de')
    borrow_book.config(bg='#e0e0de')
    return_book.config(bg='#e0e0de')
    edit_account.config(bg='#e0e0de')
    search_book.config(bg='#e0e0de')

    browse.grid_columnconfigure(0, weight=1)
    browse.grid_columnconfigure(1, weight=1)
    browse.grid_columnconfigure(2, weight=1)

    borrowed.grid_columnconfigure(0, weight=1)
    borrowed.grid_columnconfigure(1, weight=1)
    borrowed.grid_columnconfigure(2, weight=1)

    search_book.grid_columnconfigure(0, weight=1)
    search_book.grid_columnconfigure(1, weight=1)
    search_book.grid_columnconfigure(2, weight=1)

    browse.place(x=0, y=75, width=1050, height=550)
    borrowed.place(x=0, y=75, width=1050, height=550)
    borrow_book.place(x=0, y=75, width=1050, height=550)
    return_book.place(x=0, y=75, width=1050, height=550)
    edit_account.place(x=0, y=75, width=1050, height=550)
    search_book.place(x=0, y=75, width=1050, height=550)
    menu.place(x=0, y=0, width=1050, height=75)
    footer.place(x=0,y=625,width=1050, height= 75)

    Button(menu, text = "Przeglądaj",width=20,height=2,bg='#e0e0de',command=lambda:[raise_frame(browse),show1()]).grid(row=0,column=1)
    Button(menu, text = "Wypożyczone",width=20,height=2,bg='#e0e0de',command=lambda:[show2(),raise_frame(borrowed)]).grid(row=0,column=2)
    Button(menu, text = "Wypożycz",width=20,height=2,bg='#e0e0de',command=lambda:raise_frame(borrow_book)).grid(row=0,column=3)
    Button(menu, text = "Zwróć",width=20,height=2,bg='#e0e0de',command=lambda:raise_frame(return_book)).grid(row=0,column=4)
    Button(menu, text = "Edytuj konto",width=20,height=2,bg='#e0e0de',command=lambda:raise_frame(edit_account)).grid(row=0,column=5)
    Button(menu, text="Szukaj", width=20, height=2, bg='#e0e0de',command=lambda: raise_frame(search_book)).grid(row=0, column=6)
    Button(menu, text = "Wyloguj",width=20,height=2,bg='#e0e0de',command=logout).grid(row=0,column=7)

    id_w_ksiazki = tk.StringVar()
    id_z_ksiazki = tk.StringVar()
    tytul = tk.StringVar()
    autor = tk.StringVar()
    rok_wydania = tk.StringVar()

    def show1():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="biblioteka")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT * FROM ksiazki")
        records = mycursor.fetchall()
        print(len(records))
        cols1 = ('id_k','Tytul', 'Autor','Rok_wydania')
        listBox1 = ttk.Treeview(browse, columns=cols1, show='headings',height=20)

        for i, (id_k,Tytul, Autor,Rok_wydania) in enumerate(records, start=1):
            listBox1.insert("", "end", values=(id_k,Tytul, Autor,Rok_wydania))
            mysqldb.close()

        for col in cols1:
            listBox1.heading(col, text=col)
            listBox1.grid(row=1, columnspan=3,pady=(30,0))


    def show2():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="biblioteka")
        mycursor = mysqldb.cursor()
        borrowed_list = """SELECT w.id_ksiazki, k.Tytul,k.Autor, w.data_wypozyczenia FROM wypozyczenia w JOIN ksiazki k ON w.id_ksiazki=k.id_k JOIN uzytkownicy u ON w.id_uzytkownika=u.id WHERE u.id= %s"""
        t5 = (id_u,)
        mycursor.execute(borrowed_list,t5)
        records = mycursor.fetchall()
        cols2 = ('ID książki','Tytuł', 'Autor','Data wypozycznia')
        listBox2 = ttk.Treeview(borrowed, columns=cols2, show='headings',height=20)
        print(records)

        for i, (id_ksiazki, Tytul,Autor, data_wypozyczenia) in enumerate(records, start=1):
            listBox2.insert("", "end", values=(id_ksiazki, Tytul,Autor, data_wypozyczenia))
            mysqldb.close()

        for col in cols2:
            listBox2.heading(col, text=col)
            listBox2.grid(row=1, columnspan=3,pady=(30,0))

    def borrow():
        wypozycz = id_w_ksiazki.get()
        sql_borrow = """select COUNT(*) from wypozyczenia where id_ksiazki = %s and id_uzytkownika = %s"""
        sql_search = """select COUNT(*) from ksiazki where id_k = %s"""
        t_borrow1 = (wypozycz,id_u)
        t_borrow2 = (wypozycz,)
        mycur.execute(sql_borrow,t_borrow1)
        rows=mycur.fetchone()

        mycur.execute(sql_search,t_borrow2)
        rows1=mycur.fetchone()

        found = rows1[0]
        if found == 0:
            error9()
        elif rows[0] >= 1:
            error10()
        else:
            sql_insert =  "insert into wypozyczenia (id_uzytkownika,id_ksiazki,data_wypozyczenia) values(%s,%s,%s)"
            today = date.today()
            d1 = today.strftime("%Y-%m-%d")
            t_insert = (id_u,wypozycz,d1)
            mycur.execute(sql_insert, t_insert)
            db.commit()
            success1()

    def returnb():
        zwroc = id_z_ksiazki.get()
        sql_return = """select COUNT(*) from wypozyczenia where id_ksiazki = %s"""

        t_return = (zwroc,)

        mycur.execute(sql_return,t_return)
        rows=mycur.fetchone()

        found = rows[0]
        if found == 0:
            error9()
        else:
            sql_delete =  "delete from wypozyczenia where id_ksiazki = %s and id_uzytkownika = %s"

            t_delete = (zwroc,id_u)
            mycur.execute(sql_delete, t_delete)
            db.commit()
            success2()

    def update_password():
            global psw_info
            psw_info = text_psw.get()
            global rpsw_info
            rpsw_info = text_rpsw.get()

            if len(psw_info)<5:
                error13()
            elif psw_info == password:
                error11()
            elif psw_info != rpsw_info:
                error12()
            else:
                sql_update = "update uzytkownicy set Haslo = %s where id = %s"
                t_update = (psw_info,id_u)
                mycur.execute(sql_update,t_update)
                db.commit()
                success3()

    def update_user():
         global fName_info
         fName_info = text_fn.get()
         global lName_info
         lName_info = text_ln.get()

         if len(fName_info)<2:
             error14()
         elif len(lName_info)<2:
             error14()
         else:
             sql_update = "update uzytkownicy set Imie = %s, Nazwisko = %s where id = %s"
             t_update = (fName_info,lName_info,id_u)
             mycur.execute(sql_update,t_update)
             db.commit()
             success3()

    def search():
        tytul_k = tytul.get()
        autor_k = autor.get()
        rok_wydania_k = rok_wydania.get()

        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="biblioteka")
        mycursor = mysqldb.cursor()



       # sql_search1 = "select * from ksiazki where Tytul LIKE \"%"+tytul_k+"%\" OR Autor LIKE \"%"+autor_k+"%\" OR Rok_wydania LIKE \"%"+rok_wydania_k+"%\" "
       # t_search1 = (tytul_k,autor_k,rok_wydania_k)
        mycursor.execute("select * from ksiazki where Tytul LIKE \"%"+tytul_k+"%\" AND Autor LIKE \"%"+autor_k+"%\" AND Rok_wydania LIKE \"%"+rok_wydania_k+"%\" ")

        cols3 = ('ID książki', 'Tytuł', 'Autor', 'Rok wydania')
        listBox3 = ttk.Treeview(search_book, columns=cols3, show='headings', height=15)

        records = mycursor.fetchall()

        for i, (id_k, Tytul, Autor, Rok_wydania) in enumerate(records, start=1):
            listBox3.insert("", "end", values=(id_k, Tytul, Autor, Rok_wydania))
            mysqldb.close()

        for col in cols3:
            listBox3.heading(col, text=col)
            listBox3.column(col,minwidth=50)
            listBox3.grid(row=4, columnspan=4,pady=(30,0))

    Label(browse, text="Książki",fg='white', bg='#9c9797',width=1050, font=("Arial",30)).grid(row=0, columnspan=3)
    Label(borrowed, text="Wypożyczenia",fg='white', bg='#9c9797',width=1050, font=("Arial",30)).grid(row=0, columnspan=3)



    Label(borrow_book, text="Wypożycz",fg='white', bg='#9c9797',width=1050, font=("Arial",30)).grid(row=0,columnspan=4)
    Label(borrow_book, text="ID książki",bg='#e0e0de', font=("Arial",15)).grid(row=1, column=1,pady=(30, 0))
    Entry(borrow_book,textvariable=id_w_ksiazki).grid(row=1,column=2, pady=(30, 0))
    Button(borrow_book,width=30, text = "Wypożycz",font=("Arial", 12),fg='white', bg='#9c9797', command=borrow).grid(row=2,columnspan=4)

    borrow_book.grid_columnconfigure(0, weight=5)
    borrow_book.grid_columnconfigure(3, weight=5)

    Label(return_book, text="Zwróć",fg='white', bg='#9c9797',width=1050, font=("Arial",30)).grid(row=0, columnspan=4)
    Label(return_book, text="ID książki",bg='#e0e0de', font=("Arial", 15)).grid(row=1, column=1,pady=(30,0))
    Entry(return_book,textvariable=id_z_ksiazki).grid(row=1, column=2,pady=(30,0))
    Button(return_book,width=30, text = "Zwróć",font=("Arial", 12),fg='white', bg='#9c9797', command=returnb).grid(row=2,columnspan=4)

    return_book.grid_columnconfigure(0, weight=5)
    return_book.grid_columnconfigure(3, weight=5)

    Label(search_book, text="Szukaj książki", fg='white', bg='#9c9797', width=1050, font=("Arial", 30)).grid(row=0,columnspan=4)
    Label(search_book, text="Tytuł",bg='#e0e0de', font=("Arial", 15)).grid(row=1, column=0)
    Label(search_book, text="Autor",bg='#e0e0de', font=("Arial", 15)).grid(row=1, column=1)
    Label(search_book, text="Rok wydania",bg='#e0e0de', font=("Arial", 15)).grid(row=1, column=2)
    Label(search_book, text="",bg='#e0e0de', font=("Arial", 15)).grid(row=1, column=4)
    Entry(search_book, textvariable=tytul,width=55).grid(row=2, column=0)
    Entry(search_book, textvariable=autor,width=55).grid(row=2, column=1)
    Entry(search_book, textvariable=rok_wydania,width=55).grid(row=2, column=2)
    Label(search_book, text="", font=("Arial", 15)).grid(row=2, column=4)
    Button(search_book, width=145, text="Szukaj",command=search,font=("Arial", 15),fg='white', bg='#9c9797').grid(row=3, columnspan=4)

    text_id = tk.StringVar()
    text_id.set(id_u)

    text_fn = tk.StringVar()
    text_fn.set(firstname)
    text_ln = tk.StringVar()
    text_ln.set(lastname)
    text_em = tk.StringVar()
    text_em.set(email)

    text_psw = tk.StringVar()
    text_rpsw = tk.StringVar()

    Label(edit_account, text="Edytuj konto",fg='white', bg='#9c9797',width=1050, font=("Arial",30)).grid(row=0, columnspan=4)
    Label(edit_account, text="ID użytkownika",bg='#e0e0de', font=("Arial",15)).grid(row=2, column=1,pady=(30,0))
    Entry(edit_account,textvariable = text_id,state=DISABLED).grid(row=2,column=2,pady=(30,0))
    Label(edit_account, text="Imie",bg='#e0e0de', font=("Arial",15)).grid(row=3, column=1)
    Entry(edit_account,textvariable = text_fn,).grid(row=3,column=2)
    Label(edit_account, text="Nazwisko",bg='#e0e0de', font=("Arial",15)).grid(row=4, column=1)
    Entry(edit_account,textvariable = text_ln).grid(row=4,column=2)
    Label(edit_account, text="Email",bg='#e0e0de', font=("Arial",15)).grid(row=5, column=1)
    Entry(edit_account,textvariable = text_em,state=DISABLED).grid(row=5,column=2)
    Button(edit_account,width=40, text = "Edytuj",font=("Arial", 12),fg='white', bg='#9c9797',command=update_user).grid(row=6,columnspan=4)

    Label(edit_account, text="Hasło",bg='#e0e0de', font=("Arial",15)).grid(row=7, column=1,pady=(50,0))
    Entry(edit_account,textvariable = text_psw, show="*").grid(row=7,column=2,pady=(50,0))
    Label(edit_account, text="Powtórz hasło",bg='#e0e0de', font=("Arial",15)).grid(row=8, column=1)
    Entry(edit_account,textvariable = text_rpsw, show="*").grid(row=8,column=2)
    Button(edit_account,width=40, text = "Zmień hasło",font=("Arial", 12),fg='white', bg='#9c9797',command=update_password).grid(row=9,columnspan=4)

    edit_account.grid_columnconfigure(0, weight=5)
    edit_account.grid_columnconfigure(3, weight=5)

    user_window.mainloop()

openLoginWindow()



