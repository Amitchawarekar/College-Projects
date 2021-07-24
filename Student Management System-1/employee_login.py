from tkinter import *
import pymysql
from tkinter import messagebox as tsmg
from tkinter import ttk
import os
from PIL import Image, ImageTk


class emp_login_window:
    def __init__(self, root):
        self.root = root
        self.root.title('Login Window')
        self.root.geometry("1350x700+0+0")
        self.root.resizable(True, True)
        self.root.config(bg="white")

        self.bg1 = ImageTk.PhotoImage(file="image/bg-1.jpg")
        bg1 = Label(self.root, image=self.bg1).place(x=0, y=0, relwidth=1, relheight=1)

        login_frame = Frame(self.root, bg="white", bd=1, relief=RIDGE)
        login_frame.place(x=200, y=150, width=350, height=400)

        self.bg2 = ImageTk.PhotoImage(file="image/employee_bg_image.jpg")
        bg2 = Label(self.root, image=self.bg2).place(x=550, y=150, width=550, height=400)

        self.bg3 = ImageTk.PhotoImage(file="image/employee_login.jpg")
        bg3 = Label(login_frame, image=self.bg3).place(x=0, y=0, width=350, height=80)

        label = Label(login_frame, text="Welcome to Student Management System", font=('times new roman', 12, 'bold'),
                      justify=CENTER, bg="white", fg='blue')
        label.place(x=20, y=90)

        self.bg_uname = ImageTk.PhotoImage(file="image/username.png")
        bg_uname = Label(login_frame, image=self.bg_uname).place(x=20, y=130, width=30, height=30)
        username = Label(login_frame, text="Username", font=('Bell MT', 16, 'bold'), justify=CENTER, bg="white",
                         fg='black').place(x=50, y=130)
        self.txt_empid = Entry(login_frame, font=("times new roman", 15), bg="light grey")
        self.txt_empid.place(x=20, y=170, width=280)

        self.bg_pass = ImageTk.PhotoImage(file="image/download.png")
        bg_pass = Label(login_frame, image=self.bg_pass).place(x=20, y=205, width=30, height=30)
        password = Label(login_frame, text="Password", font=('Bell MT', 16, 'bold'), justify=CENTER, bg="white",
                         fg='black').place(x=50, y=205)
        self.txt_password = Entry(login_frame, font=("times new roman", 15), bg="light grey", show="*")
        self.txt_password.place(x=20, y=245, width=280)

        btn_reg = Button(login_frame, text="Register new Account?", command=self.Register_window,
                         font=("Times new roman", 13, 'bold'), bg="white", bd=0, fg="green", cursor="hand2")
        btn_reg.place(x=10, y=285)

        btn_forget = Button(login_frame, text="Forget Password?", command=self.forget_password,
                            font=("Times new roman", 13, 'bold'), bg="white", bd=0, fg="red", cursor="hand2")
        btn_forget.place(x=190, y=285)

        self.btn_image1 = ImageTk.PhotoImage(file="image/download1.jpg")
        btn_login = Button(login_frame, image=self.btn_image1, command=self.login_data, bd=0, bg="CRIMSON", fg="white",
                           cursor="hand2")
        btn_login.place(x=60, y=320, width=200, height=50)

        # ========footer ==============#
        footer = Label(self.root,
                       text="Developed By : Amit Anand Chawarekar           Email-ID : amit.chawarekar@gmail.com                           Contact no. :  9503016634,9921663430",
                       font=("goudy old style", 15), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)

    def login_data(self):
        if self.txt_empid.get() == "" or self.txt_password.get() == "":
            tsmg.showerror("Error", "All field are required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password="", database="srms1")
                cur = con.cursor()
                cur.execute("select * from registered_employee where empid=%s and password=%s",
                            (self.txt_empid.get(), self.txt_password.get()))
                row = cur.fetchone()

                if row == None:
                    tsmg.showerror('Error', "Invalid Username and password", parent=self.root)
                else:
                    tsmg.showinfo("Success", f"Welcome {self.txt_empid.get()}", parent=self.root)
                    self.root.destroy()
                    os.system("python employee_dashboard.py")
                con.close()

            except Exception as es:
                tsmg.showerror('Error', f" Error due to {str(es)}", parent=self.root)

    def reset_password(self):
        if self.combo_question.get() == "Select" or self.txt_answer.get() == "" or self.txt_new_paswword.get() == "":
            tsmg.showerror("Error", 'All Field are required', parent=self.root2)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password="", database="srms1")
                cur = con.cursor()
                cur.execute("select * from registered_employee where empid=%s and question=%s and answer=%s",
                            (self.txt_empid.get(), self.combo_question.get(), self.txt_answer.get()))
                row = cur.fetchone()

                if row == None:
                    tsmg.showerror('Error', "Please select the correct security Question/Enter Answer", parent=self.root2)
                else:
                    cur.execute("update registered_employee set password=%s where empid=%s",
                                (self.txt_new_paswword.get(), self.txt_empid.get()))
                    con.commit()
                    con.close()
                    tsmg.showinfo('Success', "Your Password has been reset,Please login with new password",
                                  parent=self.root2)
                    self.clear()
                    self.root2.destroy()

            except Exception as es:
                tsmg.showerror('Error', f" Error due to {str(es)}", parent=self.root)

    def forget_password(self):
        if self.txt_empid.get() == "":
            tsmg.showerror("Error", "Please Enter valid Employee ID to reset your password", parent=self.root)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password="", database="srms1")
                cur = con.cursor()
                cur.execute("select * from registered_employee where empid=%s",
                            (self.txt_empid.get()))
                row = cur.fetchone()

                if row == None:
                    tsmg.showerror('Error', "Please enter valid Employee ID to reset your password", parent=self.root)
                else:
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry('360x400+200+160')
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t = Label(self.root2, text='Forget Password', font=('Times new roman', 20, 'bold'), bg='yellow',
                              fg='blue')
                    t.pack(fill=X)

                    # ============================Forget Password================
                    question = Label(self.root2, text="Security Question", font=("times new roman", 17, "bold"),
                                     bg="white",
                                     fg="black").place(x=50, y=70)
                    self.combo_question = ttk.Combobox(self.root2, font=("times new roman", 15), state='readonly',
                                                       justify=CENTER)
                    self.combo_question['values'] = (
                        "Select", "your First Pet Name", "Your Birth Place", "Your Best Friend")
                    self.combo_question.place(x=50, y=110, width=260)
                    self.combo_question.current(0)

                    answer = Label(self.root2, text="Answer", font=("times new roman", 17, "bold"), bg="white",
                                   fg="black").place(x=50,
                                                     y=150)
                    self.txt_answer = Entry(self.root2, font=("times new roman", 15), bg="light yellow")
                    self.txt_answer.place(x=50, y=190, width=260)

                    new_password = Label(self.root2, text="New Password", font=("times new roman", 17, "bold"),
                                         bg="white", fg="black").place(x=75, y=230)
                    self.txt_new_paswword = Entry(self.root2, font=("times new roman", 15), bg="light yellow")
                    self.txt_new_paswword.place(x=50, y=270, width=260)

                    btn_reset_pass = Button(self.root2, text="ResetPassword?", command=self.reset_password,
                                            font=("Times new roman", 15, 'bold'), bg="green", fg="white",
                                            cursor="hand2")
                    btn_reset_pass.place(x=85, y=320)
            except Exception as es:
                tsmg.showerror('Error', f" Error due to {str(es)}", parent=self.root)

    def clear(self):
        self.combo_question.current(0)
        self.txt_empid.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_new_paswword.delete(0, END)
        self.txt_answer.delete(0, END)

    def Register_window(self):
        self.root.destroy()
        os.system("python employee_register.py")


root = Tk()
obj = emp_login_window(root)
root.mainloop()
