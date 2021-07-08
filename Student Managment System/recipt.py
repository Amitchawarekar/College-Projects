import pymysql
from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import os
import tempfile


class Recipt:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1240x480+0+130")
        self.root.config(bg="white")
        self.root.focus_force()

        title = Label(self.root, text="Print Recipt", font=("goudy old style", 20, "bold"), bg="#033054",
                      fg="white").place(x=10,y=15,width=1180,height=35)

        # ===============Variables===============================
        self.var_date = StringVar()
        self.var_i_no = StringVar()
        self.var_i_recipt_no = StringVar()
        self.var_name = StringVar()
        self.var_sum_or_rs = StringVar()
        self.var_course = StringVar()
        self.var_course_fees = StringVar()
        self.var_fees_paid = StringVar()
        self.var_paid_by = StringVar()
        self.var_balance = StringVar()
        self.var_recipt = StringVar()

        # ====Labels=============================================
        lbl_date = Label(self.root, text="Date", font=("goudy old style", 16, "bold"), bg="white").place(x=20, y=60)
        lbl_inst_no = Label(self.root, text="Inst.No", font=("goudy old style", 16, "bold"), bg="white").place(x=20,y=100)
        lbl_inst_recipt_no = Label(self.root, text="Inst. Recipt No.", font=("goudy old style", 16, "bold"),bg="white").place(x=20, y=140)
        lbl_Name = Label(self.root, text="Name", font=("goudy old style", 16, "bold"), bg="white").place(x=20, y=180)
        lbl_sum_of_Rs = Label(self.root, text="Sum of Rupees", font=("goudy old style", 16, "bold"), bg="white").place(x=20, y=220)
        lbl_Course = Label(self.root, text="Course", font=("goudy old style", 16, "bold"), bg="white").place(x=20,y=260)
        lbl_course_fee = Label(self.root, text="Course Fee(Rs.)", font=("goudy old style", 16, "bold"),bg="white").place(x=20, y=300)
        lbl_fees_paid = Label(self.root, text="Fees paid(Rs.)", font=("goudy old style", 16, "bold"), bg="white").place(x=20, y=340)
        lbl_paid_by = Label(self.root, text="Paid By", font=("goudy old style", 16, "bold"), bg="white").place(x=20,y=380)
        lbl_Balance = Label(self.root, text="Balance", font=("goudy old style", 16, "bold"), bg="white").place(x=20,y=420)


        # ==============Entry Fields================================

        self.course_list = ["Select "]

        # Function call to update course list
        self.fetch_course()

        txt_date = DateEntry(self.root, textvariable=self.var_date, font=("goudy old style", 13, "bold"), width=18,
                             bg="light yellow").place(x=210, y=60)
        txt_inst_no = Entry(self.root, textvariable=self.var_i_no, font=("goudy old style", 13, "bold"),
                            bg="light yellow").place(x=210, y=100)
        txt_inst_recipt_no = Entry(self.root, textvariable=self.var_i_recipt_no, font=("goudy old style", 13, "bold"),
                                   bg="light yellow").place(x=210, y=140)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 13, "bold"),
                         bg="light yellow").place(x=210, y=180)
        txt_sum_of_rs = Entry(self.root, textvariable=self.var_sum_or_rs, font=("goudy old style", 13, "bold"),
                              bg="light yellow").place(x=210, y=220)

        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course, values=self.course_list,
                                       font=("goudy old style", 13, "bold"), state='readonly', justify=CENTER)
        self.txt_course.place(x=210, y=260, width=185)
        self.txt_course.current(0)
        txt_course_fee = Entry(self.root, textvariable=self.var_course_fees, font=("goudy old style", 13, "bold"),
                               bg="light yellow").place(x=210, y=300)
        txt_fees_paid = Entry(self.root, textvariable=self.var_fees_paid, font=("goudy old style", 13, "bold"),
                              bg="light yellow").place(x=210, y=340)
        self.txt_paid_by = ttk.Combobox(self.root, textvariable=self.var_paid_by,
                                        values=("Select", "Cash", "PhonePe", "GooglePay", "Paytm"),
                                        font=("goudy old style", 13, "bold"), state='readonly', justify=CENTER)
        self.txt_paid_by.place(x=210, y=380, width=185)
        self.txt_paid_by.current(0)
        txt_Balance = Entry(self.root, textvariable=self.var_balance, font=("goudy old style", 13, "bold"),
                            bg="light yellow").place(x=210, y=420)

        # ===============Button==========================================
        self.btn_preview = Button(self.root, text="Preview", font=("goudy old style", 15, "bold"), bg="purple",
                                  fg="white",
                                  cursor="hand2", command=self.preview)
        self.btn_preview.place(x=10, y=450, width=90, height=30)
        self.btn_Print = Button(self.root, text="Print", font=("goudy old style", 15, "bold"), bg="orange",
                                fg="white", cursor="hand2", command=self.print)
        self.btn_Print.place(x=110, y=450, width=90, height=30)
        self.btn_Print.config(state=DISABLED)
        self.btn_save = Button(self.root, text="Save", font=("goudy old style", 15, "bold"), bg="#6078db", fg="white",
                               cursor="hand2", command=self.save)
        self.btn_save.place(x=210, y=450, width=90, height=30)
        self.btn_save.config(state=DISABLED)
        self.btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="green", fg="white",
                                cursor="hand2", command=self.clear)
        self.btn_clear.place(x=310, y=450, width=90, height=30)
        self.btn_check = Button(self.root, text="C", font=("goudy old style", 15, "bold"), command=self.check,
                                bg="#6078db", fg="white", cursor="hand2")
        self.btn_check.place(x=130, y=420, width=20, height=28)

        self.btn_R_table = Button(self.root, text="Registration Table", font=("goudy old style", 12, "bold"),
                                  command=self.register_table,
                                  bg="#6078db", fg="white", cursor="hand2")
        self.btn_R_table.place(x=700, y=50, width=130, height=28)

        self.btn_recipt_table = Button(self.root, text="Recipt Table", font=("goudy old style", 12, "bold"),
                                       bg="#6078db", fg="white", cursor="hand2", command=self.recipt_table)
        self.btn_recipt_table.place(x=880, y=50, width=130, height=28)

        btn_X = Button(self.root, text="X", font=("goudy old style", 18, "bold"), bg="white", bd=1, fg="red",
                       cursor="hand2", command=self.blank_frame).place(x=1050, y=50, width=30, height=25)

        # ========Apllication Form Frame==================================================

        A_frame = LabelFrame(self.root, text='Recipt Frame', font=("times new roman", 15), bg="white")
        A_frame.place(x=620, y=80, width=450, height=389)
        self.sample = f'''\t                     Manjiri Computers,
                        Indar Complex,Bhadgaon 9421513829
----------------------------------------------------------------------
                                             Recipt
----------------------------------------------------------------------
Inst No.            :- ______                Date :- mm-dd-yyyy

Inst Recipt No.:- ______

Name                :- ______

Sum of Rupees:- ______

Course              :- ______

Course Fee(RS):- ______               BY:- ______

Fees Paid(Rs)   :- ______                Balance Fee(Rs):- ______


                                                                 Manjiri Computers 

                                                               Authorised Signatory


                '''
        scroll_y = Scrollbar(A_frame, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)

        self.txt_Application_form = Text(A_frame, font=('times new roman', 13), bg='light yellow',
                                         yscrollcommand=scroll_y.set)
        self.txt_Application_form.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.txt_Application_form.yview)
        self.txt_Application_form.insert(END, self.sample)

    # ========================Registeration Table=========================================
    def register_table(self):

        self.C_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.C_frame.place(x=620, y=80, width=450, height=389)

        # =============Search Panel==================
        self.var_Search = StringVar()

        lbl_search_search_regid = Label(self.C_frame, text="Search by|Name ", font=("goudy old style", 15, "bold"),
                                        bg="white").place(x=10, y=10)
        self.txt_search_student = Entry(self.C_frame, textvariable=self.var_Search,
                                        font=("goudy old style", 15, "bold"), bg="light yellow")
        self.txt_search_student.place(x=160, y=10, width=180)

        btn_Search = Button(self.C_frame, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white",
                            cursor="hand2", command=self.r_search).place(x=350, y=10, width=110, height=28)

        # ==========Content ============

        lbl_registration_table = Label(self.C_frame, text="Registration table", font=("goudy old style", 15, "bold"),
                                       bg="white").place(x=170, y=40)

        self.D_frame = Frame(self.C_frame, bg="white")
        self.D_frame.place(x=0, y=70, width=450, height=319)

        scroll_x = Scrollbar(self.D_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.D_frame, orient=VERTICAL)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', background='white', font=('Arial', 12), foreground='black', rowheight=28,
                        fieldbackground='white')
        style.map('Treeview', background=[('selected', 'green')])
        self.RegisterTable = ttk.Treeview(self.D_frame, columns=(
            'regid', 'name', 'course', 'coursefees',
            'amountpaid',
            'balance'),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.RegisterTable.xview)
        scroll_y.config(command=self.RegisterTable.yview)

        self.RegisterTable.heading("regid", text="REG ID")
        self.RegisterTable.heading("name", text="Name")
        self.RegisterTable.heading("course", text="Course")
        self.RegisterTable.heading("coursefees", text="Course fee")
        self.RegisterTable.heading("amountpaid", text="Amount Paid")
        self.RegisterTable.heading("balance", text="Balance")

        self.RegisterTable['show'] = "headings"
        self.RegisterTable.column("regid", width=50)
        self.RegisterTable.column("name", width=150)
        self.RegisterTable.column("course", width=150)
        self.RegisterTable.column("coursefees", width=150)
        self.RegisterTable.column("amountpaid", width=150)
        self.RegisterTable.column("balance", width=150)
        self.RegisterTable.pack(fill=BOTH, expand=1)
        self.RegisterTable.bind('<ButtonRelease-1>', self.get_data)
        self.show()

    def recipt_table(self):
        self.T_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.T_frame.place(x=620, y=80, width=450, height=389)

        # =============Search Panel==================
        self.var_Search = StringVar()

        lbl_search_name = Label(self.T_frame, text="Search by|Name ", font=("goudy old style", 15, "bold"),
                                bg="white").place(x=10, y=10)
        self.txt_search_student_recipt = Entry(self.T_frame, textvariable=self.var_Search,
                                               font=("goudy old style", 15, "bold"), bg="light yellow")
        self.txt_search_student_recipt.place(x=160, y=10, width=180)

        btn_Search = Button(self.T_frame, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white",
                            cursor="hand2", command=self.recipt_search).place(x=350, y=10, width=110, height=28)

        # ==========Content ============

        lbl_Recipt_Table = Label(self.T_frame, text="Recipt table", font=("goudy old style", 15, "bold"),
                                 bg="white").place(x=170, y=40)

        self.D_frame = Frame(self.T_frame, bg="white")
        self.D_frame.place(x=0, y=70, width=450, height=319)

        scroll_x = Scrollbar(self.D_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.D_frame, orient=VERTICAL)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', background='white', font=('Arial', 12), foreground='black', rowheight=28,
                        fieldbackground='white')
        style.map('Treeview', background=[('selected', 'green')])
        self.ReciptTable = ttk.Treeview(self.D_frame, columns=(
        'date', 'instno', 'instreciptno', 'name', 'sofruppes', 'course', 'coursefees', 'amountpaid', 'paidby',
        'balance', 'recipt'),
                                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.ReciptTable.xview)
        scroll_y.config(command=self.ReciptTable.yview)

        self.ReciptTable.heading("date", text="Date")
        self.ReciptTable.heading("instno", text="Inst No.")
        self.ReciptTable.heading("instreciptno", text="Inst Recipt No.")
        self.ReciptTable.heading("name", text="Name")
        self.ReciptTable.heading("sofruppes", text="Sum of Rupees")
        self.ReciptTable.heading("course", text="Course")
        self.ReciptTable.heading("coursefees", text="Course Fees")
        self.ReciptTable.heading("amountpaid", text="Amount Paid")
        self.ReciptTable.heading("paidby", text="Paid By")
        self.ReciptTable.heading("balance", text="Balance")
        self.ReciptTable.heading("recipt", text="Recipt")

        self.ReciptTable['show'] = "headings"
        self.ReciptTable.column("date", width=100)
        self.ReciptTable.column("instno", width=50)
        self.ReciptTable.column("instreciptno", width=150)
        self.ReciptTable.column("name", width=150)
        self.ReciptTable.column("sofruppes", width=150)
        self.ReciptTable.column("course", width=150)
        self.ReciptTable.column("coursefees", width=150)
        self.ReciptTable.column("amountpaid", width=150)
        self.ReciptTable.column("paidby", width=150)
        self.ReciptTable.column("balance", width=150)
        self.ReciptTable.column("recipt", width=150)
        self.ReciptTable.pack(fill=BOTH, expand=1)
        self.ReciptTable.bind('<ButtonRelease-1>', self.recipt_get_data)
        self.recipt_show()

    # ===============Functions==============================
    def preview(self):
        self.btn_save.config(state=NORMAL)
        self.btn_Print.config(state=NORMAL)
        A_frame = LabelFrame(self.root, text='Recipt Frame', font=("times new roman", 15), bg="white")
        A_frame.place(x=620, y=80, width=450, height=389)
        new_sample = f'''\t                     Manjiri Computers,
                        Indar Complex,Bhadgaon 9421513829
----------------------------------------------------------------------
                                             Office Copy
----------------------------------------------------------------------
Inst No.            :- {self.var_i_no.get()}                       \t\t \tDate :-{self.var_date.get()}

Inst Recipt No.:- {self.var_i_recipt_no.get()}

Name                :- {self.var_name.get()}

Sum of Rupees:- {self.var_sum_or_rs.get()}

Course              :- {self.var_course.get()}

Course Fee(RS):- {self.var_course_fees.get()}                      \t \t\tBY:-{self.var_paid_by.get()}

Fees Paid(Rs)   :- {self.var_fees_paid.get()}                 \t\t\tBalance Fee(Rs):-{self.var_balance.get()}


                                                                 Manjiri Computers 

                                                               Authorised Signatory



                                        Manjiri Computers,
                        Indar Complex,Bhadgaon 9421513829
----------------------------------------------------------------------
                                             Student Copy
----------------------------------------------------------------------
Inst No.            :- {self.var_i_no.get()}                       \t\t \tDate :-{self.var_date.get()}

Inst Recipt No.:- {self.var_i_recipt_no.get()}

Name                :- {self.var_name.get()}

Sum of Rupees:- {self.var_sum_or_rs.get()}

Course              :- {self.var_course.get()}

Course Fee(RS):- {self.var_course_fees.get()}                      \t \t\tBY:-{self.var_paid_by.get()}

Fees Paid(Rs)   :- {self.var_fees_paid.get()}                \t\t\tBalance Fee(Rs):-{self.var_balance.get()}


                                                                 Manjiri Computers 

                                                               Authorised Signatory

                '''
        scroll_y = Scrollbar(A_frame, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)

        self.txt_Application_form = Text(A_frame, font=('times new roman', 13), bg='light yellow',
                                         yscrollcommand=scroll_y.set)
        self.txt_Application_form.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.txt_Application_form.yview)
        self.txt_Application_form.delete('1.0', END)
        self.txt_Application_form.insert(END, new_sample)

    def blank_frame(self):
        A_frame = LabelFrame(self.root, text='Recipt Frame', font=("times new roman", 15), bg="white")
        A_frame.place(x=620, y=80, width=450, height=389)
        self.sample = f'''\t                     Manjiri Computers,
                        Indar Complex,Bhadgaon 9421513829
----------------------------------------------------------------------
                                             Recipt
----------------------------------------------------------------------
Inst No.            :- ______                Date :- mm-dd-yyyy

Inst Recipt No.:- ______

Name                :- ______

Sum of Rupees:- ______

Course              :- ______

Course Fee(RS):- ______               BY:- ______

Fees Paid(Rs)   :- ______                Balance Fee(Rs):- ______


                                                                 Manjiri Computers 

                                                               Authorised Signatory


                '''
        scroll_y = Scrollbar(A_frame, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)

        self.txt_Application_form = Text(A_frame, font=('times new roman', 13), bg='light yellow',
                                         yscrollcommand=scroll_y.set)
        self.txt_Application_form.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.txt_Application_form.yview)
        self.txt_Application_form.insert(END, self.sample)
        # self.f = Frame(self.root,bg='white')
        # self.f.place(x=720, y=80, width=470, height=500)

    def fetch_course(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srms")
        cur = con.cursor()
        try:
            cur.execute("select name from course")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.course_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def get_data(self, event):
        # self.txt_regid.config(state="readonly")
        r = self.RegisterTable.focus()
        content = self.RegisterTable.item(r)
        row = content["values"]
        self.var_name.set(row[1]),
        self.var_course.set(row[2])
        self.var_course_fees.set(row[3])
        self.var_fees_paid.set(row[4])
        self.var_balance.set(row[5])

    def recipt_get_data(self, event):
        # self.txt_regid.config(state="readonly")
        r = self.ReciptTable.focus()
        content = self.ReciptTable.item(r)
        row = content["values"]
        self.var_date.set(row[0]),
        self.var_i_no.set(row[1])
        self.var_i_recipt_no.set(row[2])
        self.var_name.set(row[3])
        self.var_sum_or_rs.set(row[4])
        self.var_course.set(row[5])
        self.var_course_fees.set(row[6])
        self.var_fees_paid.set(row[7])
        self.var_paid_by.set(row[8])
        self.var_balance.set(row[9])

    def show(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srms")
        cur = con.cursor()
        try:
            cur.execute("select regid,name,course,coursefees,amountpaid,balance from register_student")
            rows = cur.fetchall()
            self.RegisterTable.delete(*self.RegisterTable.get_children())
            for row in rows:
                self.RegisterTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def recipt_show(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srms")
        cur = con.cursor()
        try:
            cur.execute("select * from recipt_table")
            rows = cur.fetchall()
            self.ReciptTable.delete(*self.ReciptTable.get_children())
            for row in rows:
                self.ReciptTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def r_search(self):
        if self.txt_search_student.get() == "":
            messagebox.showerror("Error", "Please enter Student  name", parent=self.root)
        con = pymysql.connect(host="localhost", user="root", password="", database="srms")
        cur = con.cursor()
        try:
            cur.execute(
                f"select regid,name,course,coursefees,amountpaid,balance from register_student where name LIKE '%{self.var_Search.get()}%'")
            row = cur.fetchone()
            if row != None:
                self.RegisterTable.delete(*self.RegisterTable.get_children())
                self.RegisterTable.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def recipt_search(self):
        if self.txt_search_student_recipt.get() == "":
            messagebox.showerror("Error", "Please enter Student  name", parent=self.root)
        con = pymysql.connect(host="localhost", user="root", password="", database="srms")
        cur = con.cursor()
        try:
            cur.execute(
                f"select date,instno,instreciptno,name,sofruppes,course,coursefees,amountpaid,paidby,balance,recipt from recipt_table where name LIKE '%{self.var_Search.get()}%'")
            row = cur.fetchone()
            if row != None:
                self.ReciptTable.delete(*self.ReciptTable.get_children())
                self.ReciptTable.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def clear(self):
        self.var_date.set("MM-DD-YYYY")
        self.var_i_no.set("")
        self.var_i_recipt_no.set("")
        self.var_name.set("")
        self.var_sum_or_rs.set("")
        self.var_course.set("Select")
        self.var_course_fees.set("")
        self.var_fees_paid.set("")
        self.var_paid_by.set("Select")
        self.var_balance.set("")
        self.var_Search.set('')

    def print(self):
        file_ = tempfile.mktemp('.txt')
        open(file_, 'w').write(self.txt_Application_form.get("1.0", END))
        os.startfile(file_, 'print')

    def save(self):
        self.btn_Print.config(state=DISABLED)
        self.file = open('Recipt/' + (self.var_name.get()) + ".txt", 'w+')
        self.file.write(self.txt_Application_form.get('1.0', END))
        self.file.close()
        messagebox.showinfo('Saved', 'Recipt Saved')
        con = pymysql.connect(host="localhost", user="root", password="", database="srms")
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Student Name should be required", parent=self.root)
            else:
                cur.execute('select * from recipt_table where name =%s', (self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Name is already present", parent=self.root)
                else:
                    cur.execute(
                        "insert into recipt_table(date,instno,instreciptno,name,sofruppes,course,coursefees,amountpaid,paidby,balance,recipt) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.var_date.get(),
                            self.var_i_no.get(),
                            self.var_i_recipt_no.get(),
                            self.var_name.get(),
                            self.var_sum_or_rs.get(),
                            self.var_course.get(),
                            self.var_course_fees.get(),
                            self.var_fees_paid.get(),
                            self.var_paid_by.get(),
                            self.var_balance.get(),
                            self.var_name.get() + '.txt',
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Recipt added successfully", parent=self.root)
                    self.show()
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

        self.clear()

    def check(self):
        fees = float(self.var_course_fees.get())
        paid = float(self.var_fees_paid.get())
        result = fees - paid
        self.var_balance.set(result)


if __name__ == "__main__":
    root = Tk()
    obj = Recipt(root)
    root.mainloop()