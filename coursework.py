from tkinter import * 
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk, Image
from tkinter import messagebox as mb
import random
"""
настройки главного окна
"""
root = Tk()
root['bg'] = 'black'
root.title('курсовая емае')
root.iconbitmap('icon.ico')
root.wm_attributes( '-alpha', 0.9 )
root.geometry('480x380')
root.resizable( width = False, height = False )
nb = ttk.Notebook(root)
nb.pack(fill='both', expand='yes')
"""
страницы
"""
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
page3 = ttk.Frame(nb)
page4 = ttk.Frame(nb)
page5 = ttk.Frame(nb)
"""
функции
"""
def show():
    print("Количество подгрупп нового курса - ", variable10.get() + variable11.get() + variable12.get() + variable13.get())

def check_page_3():
    s = message_entry.get()
    def showerror():
        mb.showerror(
                "Ошибка", "Введите корректные данные в поле \"Дата\"")
    if len(s) == 10 and s[2] == "." and s[5] == ".":
        day = s[0:2]
        month = s[3:5]
        year = s[6:10]
        if day.isalpha() or month.isalpha() or year.isalpha():
            showerror()
        day = int(day)
        month = int(month)
        year = int(year)
        if day > 31 or day < 1 or month > 12 or month < 1 or year < 1000:
            showerror()
        message_entry.delete(0, END)
        print("Вы ввели дату "+s)
    else:
        showerror()

def check_page_4():
    def showerror():
        mb.showerror("Ошибка", "Введите корректные данные в поле \"Оценка\"")
    if variable10.get() == 0:
        s_4 = message_entry4.get()
        if not s_4.isdigit():
            showerror()
        else:
            s_4 = int(s_4)
            if s_4 < 0 or s_4 > 5:
                showerror()
            else:
                message_entry4.delete(0, END)
                print("Вы ввели "+str(s_4))        
    elif variable10.get() == 1:
        s_4 = message_entry4.get()
        if not s_4.isdigit():
            showerror()
        else:
            s_4 = int(s_4)
            if s_4 < 0 or s_4 > 10:
                showerror()
            else:
                message_entry4.delete(0, END)
                print("Вы ввели "+str(s_4))
    elif variable10.get() == 2:
        s_4 = message_entry4.get()
        if not s_4.isdigit():
            showerror()
        else:
            s_4 = int(s_4)
            if s_4 < 0 or s_4 > 100:
                showerror()
            else:
                message_entry4.delete(0, END)
                print("Вы ввели "+str(s_4)) 

def change_grading_system_label():
    if variable10.get() == 0:
        label17['text'] = '(0-5)'
    elif variable10.get() == 1:
        label17['text'] = '(0-10)'
    elif variable10.get() == 2:
        label17['text'] = '(0-100)'            

def check_page_2():            
    s_6 = message_entry6.get()
    if s_6.isdigit():
        mb.showerror(
            "Ошибка", "Введите корректные данные в поле \"ФИО студента\"")
    else:
        message_entry6.delete(0, END)
        print("Вы ввели " + s_6)
        
def check_page_1():            
    s_3 = message_entry3.get()
    if s_3.isdigit() or len(s_3) < 1:
        mb.showerror(
            "Ошибка", "Введите корректные данные в поле \"Название курса\"")
    else:
        message_entry3.delete(0, END)
        print("Вы создали курс " + s_3)
        if variable14.get() == 0:
            print("без подгрупп")
        elif variable14.get() == 1:
            print("есть подгруппы а и б")
        elif variable14.get() == 2:
            print("есть подгруппы а, б и в")
        elif variable14.get() == 3:
            print("есть подгруппы а, б, в и г")
        variable14.set(0)

    
def select():
    print ("Результаты успеваемости по " + variable4.get() + ":")

def select_item(event):
    value = (listbox.get(listbox.curselection()))
    random_values = random.random()*100
    print(value + ": " + str(random_values))
    label = Label(page5, text=random_values, font="Arial 12", bg = 'white')
    label.pack()
    label.place(x=65, y=220)
    
"""
маленькие списки
"""
Subgroups = ["", "а", "б", "в"]
TypeofTask = ["", "Домашнее", "Лаб.работа"]
Students = ['','Тришин Владислав', 'Осмонкулов Жылдызбек', 'кот Тимофей', 'Какой-то левый чел']
Courses = ["", "ЯПВУ", "Информатика"]
TypeofLesson = ['', 'Лекция', 'Практика', 'Лабораторное']

message1 = StringVar(root)
message2 = StringVar(root)
message3 = StringVar(root)
#page4
message4 = StringVar(root)
message5 = StringVar(root)
message6 = StringVar(root)

variable1 = StringVar(root)
variable1.set(Courses[0]) # default value
variable2 = StringVar(root)
variable2.set(Courses[0]) # default value
variable3 = StringVar(root)
variable3.set(Courses[0]) # default value
variable4 = StringVar(root)
variable4.set(Courses[0]) # default value
variable5 = StringVar(root)
variable5.set(Students[0]) # default value
variable6 = StringVar(root)
variable6.set(TypeofLesson[0]) # default value
variable7 = StringVar(root)
variable7.set(Students[0]) # default value
variable8 = StringVar(root)
variable8.set(TypeofLesson[0]) # default value
variable9 = StringVar(root)
variable9.set(Subgroups[0]) # default value
#page4
variable10 = IntVar()
variable10.set(0)
#page1
variable14 = IntVar()
variable14.set(0)

menu1 = OptionMenu(page2, variable1, *Courses)
menu1.pack()
menu1.place(x=240, y=37)
menu2 = OptionMenu(page3, variable2, *Courses)
menu2.pack()
menu2.place(x=240, y=37)
menu3 = OptionMenu(page4, variable3, *Courses)
menu3.pack()
menu3.place(x=240, y=37)
menu4 = OptionMenu(page5, variable4, *Courses)
menu4.pack()
menu4.place(x=240, y=37)
menu5 = OptionMenu(page3, variable5, *Students)
menu5.pack()
menu5.place(x=240, y=117)
menu6 = OptionMenu(page3, variable6, *TypeofLesson)
menu6.pack()
menu6.place(x=240, y=77)
menu7 = OptionMenu(page4, variable7, *Students)
menu7.pack()
menu7.place(x=240, y=117)
menu8 = OptionMenu(page4, variable8, *TypeofTask)
menu8.pack()
menu8.place(x=240, y=77)
menu9 = OptionMenu(page2, variable9, *Subgroups)
menu9.pack()
menu9.place(x=240, y=117)

message_entry = Entry(page3, textvariable=message1)
message_entry.place(x=302, y=175, anchor="c")
message_entry2 = Entry(page3, textvariable=message2)
message_entry2.place(x=302, y=215, anchor="c")
message_entry3 = Entry(page1, textvariable=message3)
message_entry3.place(x=302, y=55, anchor="c")
#page4
message_entry4 = Entry(page4, textvariable=message4)
message_entry4.place(x=302, y=210, anchor="c")
message_entry5 = Entry(page4, textvariable=message5)
message_entry5.place(x=302, y=250, anchor="c")
#page2
message_entry6 = Entry(page2, textvariable=message6)
message_entry6.place(x=302, y=92, anchor="c")
#page1
subgroups_none = Radiobutton(page1, text="<нет>",
                  variable=variable14, value=0)
subgroups_ab = Radiobutton(page1, text="2",
                    variable=variable14, value=1)
subgroups_abc = Radiobutton(page1, text="3",
                   variable=variable14, value=2)
subgroups_abcd = Radiobutton(page1, text="4",
                   variable=variable14, value=3)
subgroups_none.place(x=240, y=80)
subgroups_ab.place(x=240, y=100)
subgroups_abc.place(x=240, y=120)
subgroups_abcd.place(x=240, y=140)
#page4
grading_to_5 = Radiobutton(page4, command=change_grading_system_label, text="(0-5)", variable=variable10, value=0)
grading_to_10 = Radiobutton(page4, command=change_grading_system_label, text="(0-10)", variable=variable10, value=1)
grading_to_100 = Radiobutton(page4, command=change_grading_system_label, text="(0-100)", variable=variable10, value=2)

grading_to_5.place(x=240, y=160)
grading_to_10.place(x=300, y=160)
grading_to_100.place(x=360, y=160)

"""
метки с текстом и не только
"""
label1 = Label(page1, text="ДОБАВИТЬ НОВЫЙ КУРС", justify=CENTER, font="Consolas 14")
label1.pack()

label2 = Label(page2, text="ДОБАВИТЬ СТУДЕНТА В КУРС", justify=CENTER, font="Consolas 14")
label2.pack()

label3 = Label(page3, text="ОТМЕТИТЬ ПОСЕЩАЕМОСТЬ", justify=CENTER, font="Consolas 14")
label3.pack()

label4 = Label(page4, text="ОТМЕТИТЬ УСПЕВАЕМОСТЬ", justify=CENTER, font="Consolas 14")
label4.pack()

label5 = Label(page5, text="РЕЗУЛЬТАТЫ СТУДЕНТОВ", justify=CENTER, font="Consolas 14")
label5.pack()

label6 = Label(page2, text="Выберите курс", font="Arial 12")
label6.pack()
label6.place(x=60, y=40)

label6 = Label(page3, text="Выберите курс", font="Arial 12")
label6.pack()
label6.place(x=60, y=40)

label6 = Label(page4, text="Выберите курс", font="Arial 12")
label6.pack()
label6.place(x=60, y=40)

label6 = Label(page5, text="Выберите курс", font="Arial 12")
label6.pack()
label6.place(x=60, y=40)

label7 = Label(page5, text="Информация:", font="Arial 12")
label7.pack()
label7.place(x=60, y=185)

label8 = Label(page1, text="Введите название", font="Arial 12")
label8.pack()
label8.place(x=60, y=40)

label9 = Label(page3, text="Тип занятия", font="Arial 12")
label9.pack()
label9.place(x=60, y=80)

label10 = Label(page3, text="Выберите студента", font="Arial 12")
label10.pack()
label10.place(x=60, y=120)

label11 = Label(page3, text="Дата", font="Arial 12")
label11.pack()
label11.place(x=60, y=160)

label12 = Label(page3, text="Комментарий", font="Arial 12")
label12.pack()
label12.place(x=60, y=200)

label13 = Label(page4, text="Тип задания", font="Arial 12")
label13.pack()
label13.place(x=60, y=80)

label14 = Label(page4, text="Выберите студента", font="Arial 12")
label14.pack()
label14.place(x=60, y=120)

label15 = Label(page4, text="Оценка", font="Arial 12")
label15.pack()
label15.place(x=60, y=200)

label16 = Label(page4, text="Комментарий", font="Arial 12")
label16.pack()
label16.place(x=60, y=240)

label17 = Label(page4, text="(0-5)", font="Arial 12", fg = '#32CD32')
label17.pack()
label17.place(x=120, y=200)

label18 = Label(page3, text="(дд.мм.гггг)", font="Arial 12", fg = '#4B0082')
label18.pack()
label18.place(x=112, y=162)

label19 = Label(page2, text="ФИО студента", font="Arial 12")
label19.pack()
label19.place(x=60, y=80)

label20 = Label(page2, text="Подгруппа", font="Arial 12")
label20.pack()
label20.place(x=60, y=120)

label21 = Label(page1, text="Количество подгрупп:", font="Arial 12")
label21.pack()
label21.place(x=60, y=80)

label22 = Label(page4, text="Система оценивания", font="Arial 12")
label22.pack()
label22.place(x=60, y=160)

canvas1 = Canvas(page5, width=350, height=50, bg='white')
canvas1.pack()
canvas1.place(x=60, y=215)
"""
названия страниц
"""
nb.add(page1, text='Добавить курс')
nb.add(page2, text='Доб.студента')
nb.add(page3, text='Посещаемость')
nb.add(page4, text='Успеваемость')
nb.add(page5, text='Результаты  ')
"""
кнопки
"""
button1 = Button(page1, text="Создать", command=check_page_1)
button1.pack()
button1.place(x=400, y=320)
button2 = Button(page2, text="Сохранить", command=check_page_2)
button2.pack()
button2.place(x=400, y=320)
button3 = Button(page3, text="Сохранить", command=check_page_3)
button3.pack()
button3.place(x=400, y=320)
button4 = Button(page4, text="Сохранить", command=check_page_4)
button4.pack()
button4.place(x=400, y=320)
button5 = Button(page5, text="Выбрать", command=select)
button5.pack()
button5.place(x=360, y=40)
"""
списки listbox
"""
listbox = Listbox(page5, width=39, height=5, font=('arial', 13))
listbox.bind('<<ListboxSelect>>', select_item)
listbox.place(x=60, y=75)

for item in Students:
    listbox.insert(END, item)

"""
цикл главного окна
"""    
root.mainloop()

