from customtkinter import *
from CustomTkinterMessagebox import CTkMessagebox
dic={}
window = CTk()
window.geometry("400x300")
window.configure(fg_color="#de135c")
window.title("Вхід")
def showmessage(event):
    CTkMessagebox.messagebox(text="LogIn menu has not been implemented yet\n you can only register :)", title="error")
def writedown():
    if password.get() != passwordrepeat.get():
        CTkMessagebox.messagebox(text="Паролі не збігаються", title="error")
    elif len(login.get())<3:
        CTkMessagebox.messagebox(text="Логін повинен бути довжиною хочаб в 3 символи", title="error")
    else:
        file = open("users.txt", "r", encoding="UTF-8")
        reading = file.read().split()
        for i in reading:
            a=i.split(":")
            dic.update({a[0]:a[1]})
        if login.get() not in dic:
            file = open("users.txt", "a", encoding="UTF-8")
            file.write(f"{login.get()}:{password.get()}\n")
            title.destroy()
            login.destroy()
            password.destroy()
            passwordrepeat.destroy()
            enterbutton.destroy()
            loginlabel.destroy()
            CTkLabel(window, font=("", 42),text="Реєстрація успішна!",text_color="white").place(relx=0.5,rely=0.5, anchor="center")
        else:
            CTkMessagebox.messagebox(text="Це ім'я вже зайняте", title="error")
title = CTkLabel(window, font=("", 42), text="Вхід", text_color="white")
title.pack(pady=10)
login = CTkEntry(window, font=("", 20), width=300, placeholder_text="Ваше ім'я")
login.pack(pady=10)
password = CTkEntry(window, font=("", 20), width=300, placeholder_text="Ваш пароль")
password.pack(pady=10)
passwordrepeat = CTkEntry(window, font=("", 20), width=300, placeholder_text="Повторіть ваш пароль")
passwordrepeat.pack(pady=10)
enterbutton = CTkButton(window, text="Увійти", fg_color="white", hover_color="lightgray",text_color="black",command=writedown)
enterbutton.pack(pady=10)
loginlabel = CTkLabel(window, text="Логін", font=("",16,"underline"), text_color="white" )
loginlabel.place(x=5,y=1)
loginlabel.bind(sequence='<ButtonPress-1>',command=showmessage)
window.mainloop()