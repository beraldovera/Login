import tkinter
from tkinter import messagebox
import pandas as pd


# tela inicial
window = tkinter.Tk()
window.title("LOGIN PAGE")
window.geometry("840x520")
window.configure(bg="#fff")
frame = tkinter.Frame(bg="#fff")


# def login
def login():
    login = "userone"
    password = "1234"

    if login=='userone' and password=='1234':
        messagebox.showinfo("That's it!","You have entered successfully :)")
    else:
         messagebox.showinfo("OOps...", "Try again! ):")

# widgets

#labels
login_title = tkinter.Label(frame, text="LOGIN", bg="#fff", fg="#680D56", font=("Arial", 35, "bold")) 
user_lbl = tkinter.Label(frame, text="User", bg="#fff", fg="#680D56", font=("Arial", 12))
password_lbl = tkinter.Label(frame, text="Password", bg="#fff", fg="#680D56", font=("Arial", 12))
# entrys
user_entry = tkinter.Entry(frame, bg="#fff", borderwidth=4, fg="#333", font=("Arial", 14))
password_entry = tkinter.Entry(frame, bg="#fff", borderwidth=4, show="*", fg="#333", font=("Arial", 14))
# button
enter_button = tkinter.Button(frame, text="ENTER", bg="#680D56", fg="#fff", font=("Arial", 12), command=login)


# place widgets
login_title.grid(row=0, column=1, columnspan=1, pady=40)
user_lbl.grid(row=2, column=1)
user_entry.grid(row=3, column=1)
password_lbl.grid(row=4, column=1, pady=20)
password_entry.grid(row=5, column=1)
enter_button.grid(row=6, column=1, pady=20)


# mainloop
frame.pack()
window.mainloop()