from tkinter import * 
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk, Image
import random
"""
настройки главного окна
"""
root = Tk()
root['bg'] = 'black'
root.title('курсовая емае')
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
#def show_message():
    #print("Вы ввели: " + message1.get() + message2.get())

def save():
    print ("Вы выбрали:" + variable1.get() + variable2.get() + variable3.get())
    #def show_message()
    
def select():
    print ("Результаты успеваемости по " + variable4.get() + ":")

def select_item(event):
    value = (listbox.get(listbox.curselection()))
    random_values = random.random()*100
    print(value + ": " + str(random_values))
    label = Label(page5, text=random_values, font="Arial 12", bg = 'white')
    label.pack()
    label.place(x=65, y=220)

def new_course():
    print("Вы нажали создать курс")
"""
пока не работает, но обязательно заработает
"""
def show_message_delete():
    label_message = Label(root, text = "Вы ввели: " + message_entry.get(), justify=CENTER, font="Consolas 14")
    label_message.pack()
    label_message.place(x=60, y=40)
    root.after(2500, lambda: label_message.pack_forget())
"""
маленькие списки
"""
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

message_entry = Entry(page3, textvariable=message1)
message_entry.place(x=302, y=175, anchor="c")
message_entry2 = Entry(page3, textvariable=message2)
message_entry2.place(x=302, y=215, anchor="c")
message_entry3 = Entry(page1, textvariable=message3)
message_entry3.place(x=302, y=55, anchor="c")
#page4
message_entry4 = Entry(page4, textvariable=message2)
message_entry4.place(x=302, y=215, anchor="c")
message_entry5 = Entry(page4, textvariable=message3)
message_entry5.place(x=302, y=175, anchor="c")
"""
метки с текстом и не только
"""
#text = ScrolledText(page2)
#text.pack(expand=1, fill="both")
#page1.config(bg="black")

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
label15.place(x=60, y=160)

label16 = Label(page4, text="Комментарий", font="Arial 12")
label16.pack()
label16.place(x=60, y=200)

canvas1 = Canvas(page5, width=350, height=50, bg='white')
canvas1.pack()
canvas1.place(x=60, y=215)


#path = 'D:/gif.gif'
#img = ImageTk.PhotoImage(Image.open("D:\\gif.gif"))
#panel = Label(root, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")

#canvas = Canvas(root) 
#canvas.grid(row = 0, column = 0) 
#canvas.pack()
#photo = PhotoImage(file = 'D:/снюс.PNG') 
#canvas.create_image(0, 0, image=photo)

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
button1 = Button(page1, text="Создать", command=new_course)
button1.pack()
button1.place(x=400, y=320)
button2 = Button(page2, text="Сохранить", command=save and show_message_delete)
button2.pack()
button2.place(x=400, y=320)
button3 = Button(page3, text="Сохранить", command=save)
button3.pack()
button3.place(x=400, y=320)
button4 = Button(page4, text="Сохранить", command=save)
button4.pack()
button4.place(x=400, y=320)
button5 = Button(page5, text="Выбрать", command=select)
button5.pack()
button5.place(x=360, y=40)
"""
списки
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

