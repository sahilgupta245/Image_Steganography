from tkinter import *
import sqlite3
import sys
import os
import cmd
import subprocess

root = Tk()
root.title("   Login Application")
width = 500
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

user = "Welcome"
USERNAME = StringVar()
PASSWORD = StringVar()
 
#FRAMES
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=50)
 
#LABELS
lbl_title = Label(Top, bg = "#9DC08B", text = "   Login Application", font=('times new roman', 22))
lbl_title.pack(fill=X)
lbl_username = Label(Form, text = "Username:", font=('times new roman', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(Form, text = "Password:", font=('times new roman', 14), bd=15)
lbl_password.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)
 

def Database():
    global conn, cursor
    conn = sqlite3.connect("ucw.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `ucw` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")       
    cursor.execute("SELECT * FROM `ucw` WHERE `username` = 'ucw123' AND `password` = 'ultimate'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `ucw` (username, password) VALUES('ucw123', 'ultimate')")
        conn.commit()

#Login part start
def loginn(event=None): 
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `ucw` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get())) 
        if cursor.fetchone() is not None:
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
            command="python main.py" #updated
            subprocess.Popen(command) #updated
            sys.exit() #updated
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")  
    
    cursor.close()
    conn.close()


#==============================ENTRY WIDGETS==================================
username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)
 
#==============================BUTTON WIDGETS=================================
btn_login = Button(Form, text="Login", width=10, command=loginn, bg="#F5FFC9",font=('times new roman', 15))
btn_login.grid(pady=25, row=3, columnspan=2)
btn_login.bind('<Return>', loginn)





if __name__ == '__main__':
    root.mainloop()