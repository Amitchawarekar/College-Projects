import pymysql
from tkinter import *
from tkinter import ttk, messagebox, StringVar
import sqlite3
from PIL import Image, ImageTk
import os
import tempfile
import smtplib
import credentials as cr
from tkcalendar import DateEntry


class ManageEmp:

    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management Page")
        self.root.geometry("1260x550+0+88")
        self.root.config(bg="white")
        self.root.focus_force()

        title = Label(self.root, text="Employee Management Form", font=("goudy old style", 20, "bold"), bg="brown",
                      fg="white").place(x=10, y=15, width=1260, height=35)

        # ======variables =================
        self.var_date = StringVar()
        self.var_empid = StringVar()
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_security_ques = StringVar()
        self.var_answer = StringVar()
        self.var_password = StringVar()
        self.var_cpassword = StringVar()
        # =========Row 1 ===========
        lbl_Date = Label(self.root, text="Date", font=("goudy old style", 18, "bold"), bg="white").place(x=10, y=60)
        txt_date = DateEntry(self.root, textvariable=self.var_date, font=("goudy old style", 15, "bold"),
                             bg="light yellow").place(x=10, y=100, width=200)
        lbl_empid = Label(self.root, text="Emp-ID", font=("goudy old style", 18, "bold"), bg="white").place(x=350, y=60)
        txt_empid = Entry(self.root, textvariable=self.var_empid, font=("goudy old style", 15, "bold"),
                          bg="light yellow").place(x=350, y=100, width=200)
        # =========Row 2===========
        lbl_fname = Label(self.root, text="First Name", font=("goudy old style", 18, "bold"), bg="white").place(x=10,
                                                                                                                y=140)
        txt_fname = Entry(self.root, textvariable=self.var_fname, font=("goudy old style", 15, "bold"),
                          bg="light yellow").place(x=10, y=180, width=200)
        lbl_lname = Label(self.root, text="Last Name", font=("goudy old style", 18, "bold"), bg="white").place(x=350,
                                                                                                               y=140)
        txt_lname = Entry(self.root, textvariable=self.var_lname, font=("goudy old style", 15, "bold"),
                          bg="light yellow").place(x=350, y=180, width=200)

        # =========Row 3 ===========
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 18, "bold"), bg="white").place(x=10,
                                                                                                               y=220)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15, "bold"),
                            bg="light yellow").place(x=10, y=260, width=200)

        lbl_email = Label(self.root, text="Email-ID", font=("goudy old style", 18, "bold"), bg="white").place(x=350,
                                                                                                              y=220)
        txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15, "bold"),
                          bg="light yellow").place(x=350, y=260, width=200)

        # =========Row 4 ===========
        lbl_security_ques = Label(self.root, text="Security Question", font=("goudy old style", 18, "bold"),
                                  bg="white").place(x=10, y=300)
        txt_security_ques = Entry(self.root, textvariable=self.var_security_ques, font=("goudy old style", 15, "bold"),
                                  bg="light yellow").place(x=10, y=340, width=200)

        lbl_answer = Label(self.root, text="Answer", font=("goudy old style", 18, "bold"), bg="white").place(x=350,
                                                                                                             y=300)
        txt_answer = Entry(self.root, textvariable=self.var_answer, font=("goudy old style", 15, "bold"),
                           bg="light yellow").place(x=350, y=340, width=200)

        # =========Row 5 ===========
        lbl_password = Label(self.root, text="Password", font=("goudy old style", 18, "bold"), bg="white").place(x=10,
                                                                                                                 y=380)
        txt_password = Entry(self.root, textvariable=self.var_password, font=("goudy old style", 15, "bold"),
                             bg="light yellow").place(x=10, y=420, width=200)
        lbl_cpassword = Label(self.root, text="Confirm Password", font=("goudy old style", 18, "bold"),
                              bg="white").place(x=350, y=380)
        txt_cpassword = Entry(self.root, textvariable=self.var_cpassword, font=("goudy old style", 15, "bold"),
                              bg="light yellow").place(x=350, y=420, width=200)

        # ===========Buttons =============
        self.btn_add = Button(self.root, text="Register", font=("goudy old style", 15, "bold"),
                              bg="#2196f3", fg="white", cursor="hand2", command=self.add)
        self.btn_add.place(x=20, y=460, width=110, height=40)

        self.btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"),
                                 bg="#f44336", fg="white", cursor="hand2", command=self.delete)
        self.btn_delete.place(x=160, y=460, width=110, height=40)
        self.btn_update = Button(self.root, text="Update", font=("goudy old style", 15, "bold"),
                                 bg="green", fg="white", cursor="hand2", command=self.update)
        self.btn_update.place(x=300, y=460, width=110, height=40)
        self.btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"),
                                bg="#6078db", fg="white", cursor="hand2", command=self.clear)
        self.btn_clear.place(x=440, y=460, width=110, height=40)
        self.btn_new_emp = Button(self.root, text="New Employees", font=("goudy old style", 12, "bold"),
                                  command=self.new_emp,
                                  bg="#6078db", fg="white", cursor="hand2")
        self.btn_new_emp.place(x=850, y=60, width=130, height=25)

        self.btn_registered_emp = Button(self.root, text="Registered Employees", font=("goudy old style", 12, "bold"),
                                         command=self.Registered_emp,
                                         bg="#6078db", fg="white", cursor="hand2")
        self.btn_registered_emp.place(x=1000, y=60, width=150, height=25)
        btn_X = Button(self.root, text="X", font=("goudy old style", 18, "bold"), bg="white", bd=1, fg="red",
                       cursor="hand2", command=self.blank_frame).place(x=1200, y=60, width=30, height=25)

    def new_emp(self):
        self.C_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.C_frame.place(x=730, y=110, width=490, height=400)

        # =============Search Panel==================
        self.var_Search = StringVar()

        lbl_search_empid = Label(self.C_frame, text="Search by|Emp-ID ", font=("goudy old style", 15, "bold"),
                                 bg="white").place(x=10, y=10)
        self.txt_search_empid = Entry(self.C_frame, textvariable=self.var_Search,
                                      font=("goudy old style", 15, "bold"), bg="light yellow")
        self.txt_search_empid.place(x=180, y=10, width=180)

        btn_Search = Button(self.C_frame, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4",
                            fg="white",
                            cursor="hand2", command=self.new_search).place(x=370, y=10, width=110, height=28)

        # ==========Content ============

        lbl_new_employee_table = Label(self.C_frame, text="New Employee table",
                                       font=("goudy old style", 15, "bold"),
                                       bg="white").place(x=170, y=40)

        self.D_frame = Frame(self.C_frame, bg="white")
        self.D_frame.place(x=0, y=70, width=490, height=330)

        scroll_x = Scrollbar(self.D_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.D_frame, orient=VERTICAL)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', background='white', font=('Arial', 12), foreground='black', rowheight=28,
                        fieldbackground='white')
        style.map('Treeview', background=[('selected', 'green')])
        self.new_employee_table = ttk.Treeview(self.D_frame,
                                               columns=('f_name', 'l_name', 'contact', 'email', 'question', 'answer'),
                                               xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.new_employee_table.xview)
        scroll_y.config(command=self.new_employee_table.yview)

        self.new_employee_table.heading("f_name", text="Frst Name")
        self.new_employee_table.heading("l_name", text="Last Name")
        self.new_employee_table.heading("contact", text="Contact")
        self.new_employee_table.heading("email", text="Email-ID")
        self.new_employee_table.heading("question", text="Question")
        self.new_employee_table.heading("answer", text="Answer")

        self.new_employee_table['show'] = "headings"
        self.new_employee_table.column("f_name", width=150)
        self.new_employee_table.column("l_name", width=150)
        self.new_employee_table.column("contact", width=150)
        self.new_employee_table.column("email", width=150)
        self.new_employee_table.column("question", width=150)
        self.new_employee_table.column("answer", width=150)
        self.new_employee_table.pack(fill=BOTH, expand=1)
        self.new_employee_table.bind('<ButtonRelease-1>', self.get_data_new)
        self.new_show()

    # =============Enquiry Table============================================================
    def Registered_emp(self):
        self.E_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.E_frame.place(x=730, y=110, width=490, height=400)
        # ======Search panel ===========
        self.var_Search = StringVar()
        lbl_search_empid = Label(self.E_frame, text="Search by|Emp-ID ", font=("goudy old style", 15, "bold"),
                                 bg="white").place(x=10, y=10)
        self.txt_search_empid = Entry(self.E_frame, textvariable=self.var_Search,
                                      font=("goudy old style", 15, "bold"), bg="light yellow")
        self.txt_search_empid.place(x=180, y=10, width=180)

        btn_Search = Button(self.E_frame, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4",
                            fg="white",
                            cursor="hand2", command=self.register_search).place(x=370, y=10, width=110, height=28)

        # ==========Content ============
        lbl_registered_emp_table = Label(self.E_frame, text="Registered Employee table",
                                         font=("goudy old style", 15, "bold"),
                                         bg="white").place(x=150, y=40, width=250)
        self.F_frame = Frame(self.E_frame)
        self.F_frame.place(x=0, y=70, width=490, height=330)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', background='white', font=('Arial', 12), foreground='black', rowheight=28,
                        fieldbackground='white')
        style.map('Treeview', background=[('selected', 'green')])

        scroll_x = Scrollbar(self.F_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.F_frame, orient=VERTICAL)
        self.Registered_employee_table = ttk.Treeview(self.F_frame, columns=(
            'date', 'empid', 'f_name', 'l_name', 'contact', 'email', 'question', 'answer', 'password', 'cpassword'),
                                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Registered_employee_table.xview)
        scroll_y.config(command=self.Registered_employee_table.yview)

        self.Registered_employee_table.heading("date", text="Date")
        self.Registered_employee_table.heading("empid", text="Emp-ID")
        self.Registered_employee_table.heading("f_name", text="First Name")
        self.Registered_employee_table.heading("l_name", text="Last Name")
        self.Registered_employee_table.heading("contact", text="Contact")
        self.Registered_employee_table.heading("email", text="Email-ID")
        self.Registered_employee_table.heading("question", text="Question")
        self.Registered_employee_table.heading("answer", text="Answer")
        self.Registered_employee_table.heading("password", text="Password")
        self.Registered_employee_table.heading("cpassword", text="Confirm Password")

        self.Registered_employee_table['show'] = "headings"
        self.Registered_employee_table.column("date", width=150)
        self.Registered_employee_table.column("empid", width=150)
        self.Registered_employee_table.column("f_name", width=150)
        self.Registered_employee_table.column("l_name", width=150)
        self.Registered_employee_table.column("contact", width=150)
        self.Registered_employee_table.column("email", width=150)
        self.Registered_employee_table.column("question", width=150)
        self.Registered_employee_table.column("answer", width=150)
        self.Registered_employee_table.column("password", width=150)
        self.Registered_employee_table.column("cpassword", width=150)
        self.Registered_employee_table.pack(fill=BOTH, expand=1)
        self.Registered_employee_table.bind('<ButtonRelease-1>', self.get_data_registered)
        self.r_show()

    def blank_frame(self):
        f = Frame(self.root, bg='white')
        f.place(x=730, y=110, width=490, height=400)

    # ----------------------------------------------------------------

    def get_data_new(self, event):
        r = self.new_employee_table.focus()
        content = self.new_employee_table.item(r)
        row = content["values"]
        self.var_fname.set(row[0]),
        self.var_lname.set(row[1]),
        self.var_contact.set(row[2]),
        self.var_email.set(row[3]),
        self.var_security_ques.set(row[4]),
        self.var_answer.set(row[5]),

    def get_data_registered(self, event):
        # self.txt_regid.config(state="readonly")
        r = self.Registered_employee_table.focus()
        content = self.Registered_employee_table.item(r)
        row = content["values"]
        self.var_date.set(row[0]),
        self.var_empid.set(row[1]),
        self.var_fname.set(row[2]),
        self.var_lname.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_email.set(row[5]),
        self.var_security_ques.set(row[6]),
        self.var_answer.set(row[7]),
        self.var_password.set(row[8]),
        self.var_cpassword.set(row[9]),

    def add(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srms1")
        cur = con.cursor()
        try:
            if self.var_date.get() == "" or self.var_empid.get() == "" or self.var_fname.get() == "" or self.var_lname.get() == "" or self.var_contact.get() == "" or self.var_email.get() == "" or self.var_security_ques.get() == "" or self.var_answer.get() == "" or self.var_password.get() == "" or self.var_cpassword.get() == "":
                messagebox.showerror("Error", "All Fields are Required", parent=self.root)
            elif len(self.var_contact.get()) > 10 or len(self.var_contact.get()) < 10:
                messagebox.showerror("Error", "Mobile no. is not valid")
            else:
                cur.execute('select * from registered_employee where empid =%s', (self.var_empid.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Employee ID is already present", parent=self.root)
                else:

                    cur.execute(
                        "insert into registered_employee(date,empid,f_name,l_name,contact,email,question,answer,password,cpassword) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.var_date.get(),
                            self.var_empid.get(),
                            self.var_fname.get(),
                            self.var_lname.get(),
                            self.var_contact.get(),
                            self.var_email.get(),
                            self.var_security_ques.get(),
                            self.var_answer.get(),
                            self.var_password.get(),
                            self.var_cpassword.get(),

                        ))
                    con.commit()
                    cur.execute("delete from emp_table where f_name=%s", (self.var_fname.get(),))
                    con.commit()

                    messagebox.showinfo("Success", "Employee Registered successfully", parent=self.root)
                    self.send_mail()
                    messagebox.showinfo("Email",f"Email Sent Successfully to {self.var_email.get()}",parent= self.root)
                    self.r_show()
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def update(self):

        con = pymysql.connect(host="localhost", user="root", password="", database="srms1")
        cur = con.cursor()
        try:
            if self.var_empid.get() == "":
                messagebox.showerror("Error", "Emp id  should be required", parent=self.root)
            else:
                cur.execute('select * from registered_employee where empid=%s', (self.var_empid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Select Employee from list", parent=self.root)
                else:

                    cur.execute(
                        "update registered_employee set date=%s,f_name=%s,l_name=%s,contact=%s,email=%s,question=%s,answer=%s,password=%s,cpassword=%s where empid=%s",
                        (
                            self.var_date.get(),
                            self.var_fname.get(),
                            self.var_lname.get(),
                            self.var_contact.get(),
                            self.var_email.get(),
                            self.var_security_ques.get(),
                            self.var_answer.get(),
                            self.var_password.get(),
                            self.var_cpassword.get(),
                            self.var_empid.get()))

                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Employee Updated successfully", parent=self.root)
                    self.r_show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def delete(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srms1")
        cur = con.cursor()
        try:
            if self.var_empid.get() == "":
                messagebox.showerror("Error", "Emp ID should be required", parent=self.root)
            else:
                cur.execute('select * from registered_employee where empid=%s', (self.var_empid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please select Employee from list", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from registered_employee where empid=%s", (self.var_empid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Employee Deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def clear(self):
        self.var_date.set("DD-MM-YYYY")
        self.var_empid.set(""),
        self.var_fname.set(""),
        self.var_lname.set(""),
        self.var_contact.set(""),
        self.var_email.set(""),
        self.var_security_ques.set(""),
        self.var_answer.set(""),
        self.var_password.set(""),
        self.var_cpassword.set("")

    def send_mail(self):

        rx = {self.var_email.get()}
        sub = 'Employee Registration Confirmation'
        msg = f'''
        Hello {self.var_fname.get()}{self.var_lname.get()},you have been Successfully Registered.
        Your Login Credientials :-
        Username :- {self.var_empid.get()}
        Password :- {self.var_password.get()}
        
        Thank you for joining with us.
        With Regards.'''

        mailer = smtplib.SMTP('smtp.gmail.com', 587)
        mailer.ehlo()
        mailer.starttls()
        mailer.login(cr.auth['user_name'], cr.auth['password'])

        email_body = '\r\n'.join(['To:%s' % rx, 'From:%s' % (cr.auth['user_name']),
                                  'Subject:%s' % sub, '', msg])

        mailer.sendmail(cr.auth['user_name'], rx, email_body)
        print('Email sent')

    def new_search(self):
        if self.txt_search_empid.get() == "":
            messagebox.showerror("Error", "Please enter Employee  name", parent=self.root)
        con = pymysql.connect(host="localhost", user="root", password="", database="srms1")
        cur = con.cursor()
        try:
            cur.execute("select * from emp_table where empid =%s", (self.var_Search.get()))
            row = cur.fetchone()
            if row != None:
                self.new_employee_table.delete(*self.new_employee_table.get_children())
                self.new_employee_table.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        self.var_Search.set('')

    def register_search(self):
        if self.txt_search_empid.get() == "":
            messagebox.showerror("Error", "Please enter Employee  name", parent=self.root)
        con = pymysql.connect(host="localhost", user="root", password="", database="srms1")
        cur = con.cursor()
        try:
            cur.execute("select * from registered_employee where empid=%s", (self.var_Search.get(),))
            row = cur.fetchone()
            if row != None:
                self.Registered_employee_table.delete(*self.Registered_employee_table.get_children())
                self.Registered_employee_table.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        self.var_Search.set('')

    def new_show(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srms1")
        cur = con.cursor()
        try:
            cur.execute("select * from emp_table")
            rows = cur.fetchall()
            self.new_employee_table.delete(*self.new_employee_table.get_children())
            for row in rows:
                self.new_employee_table.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def r_show(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srms1")
        cur = con.cursor()
        try:
            cur.execute("select * from registered_employee")
            rows = cur.fetchall()
            self.Registered_employee_table.delete(*self.Registered_employee_table.get_children())
            for row in rows:
                self.Registered_employee_table.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj1 = ManageEmp(root)
    root.mainloop()
