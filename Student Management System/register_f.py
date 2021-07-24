import pymysql
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image, ImageTk
import os
import tempfile
import smtplib
import credentials as cr
from tkcalendar import DateEntry

class RegisterClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1240x480+0+150")
        self.root.config(bg="white")
        self.root.focus_force()
        self.chk_print = 0
        # ========Title ==============#
        title = Label(self.root, text="Student Registration Form", font=("goudy old style", 20, "bold"), bg="#033054",
                      fg="white").place(x=10, y=15, width=1220, height=35)

        # ==========varaibles=================
        self.var_regid = StringVar()
        self.var_date = StringVar()
        self.var_batch = StringVar()
        self.var_rname = StringVar()
        self.var_gender = StringVar()
        self.var_contact1 = StringVar()
        self.var_contact2 = StringVar()
        self.var_course = StringVar()
        self.var_coursefees = StringVar()
        self.var_amountpaid = StringVar()
        self.var_date_ap = StringVar()
        self.var_balance_amount = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()

        # =========Widgets ===========
        lbl_Regid = Label(self.root, text="Reg_ID", font=("goudy old style", 17, "bold"), bg="white").place(x=10, y=60)
        lbl_Date = Label(self.root, text="Date", font=("goudy old style", 17, "bold"), bg="white").place(x=10, y=100)
        lbl_batch = Label(self.root, text="Batch", font=("goudy old style", 17, "bold"), bg="white").place(x=370, y=100)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 17, "bold"), bg="white").place(x=10, y=140)
        lbl_gender = Label(self.root, text="Gender", font=("goudy old style", 17, "bold"), bg="white").place(x=370,
                                                                                                             y=140)
        lbl_contact1 = Label(self.root, text="Contact 1", font=("goudy old style", 17, "bold"), bg="white").place(x=10,
                                                                                                                  y=180)
        lbl_contact2 = Label(self.root, text="Contact 2", font=("goudy old style", 17, "bold"), bg="white").place(x=370,
                                                                                                                  y=180)
        lbl_email = Label(self.root, text="Email-ID", font=("goudy old style", 17, "bold"), bg="white").place(x=10, y=220)
        lbl_dob = Label(self.root, text="D.O.B", font=("goudy old style", 17, "bold"), bg="white").place(x=370, y=220)

        lbl_course = Label(self.root, text="Course", font=("goudy old style", 17, "bold"), bg="white").place(x=10,
                                                                                                             y=260)
        lbl_coursefees = Label(self.root, text="Course Fee", font=("goudy old style", 17, "bold"), bg="white").place(
            x=370, y=260)
        lbl_amount_paid = Label(self.root, text="Amount Paid", font=("goudy old style", 17, "bold"), bg="white").place(
            x=10, y=300)
        lbl_date_ap = Label(self.root, text="Date(AP)", font=("goudy old style", 17, "bold"), bg="white").place(x=370,
                                                                                                                y=300)
        lbl_balance = Label(self.root, text="Balance", font=("goudy old style", 17, "bold"), bg="white").place(x=10,
                                                                                                               y=340)

        lbl_address = Label(self.root, text="Address", font=("goudy old style", 16, "bold"), bg="white").place(x=370,
                                                                                                               y=340)
        lbl_note = Label(self.root, text="#NOTE--Please Preview before saving form",
                         font=("goudy old style", 15, 'bold'), bg="white", fg='red').place(x=10,
                                                                                           y=440)

        # =========Entry Fields ===========
        self.course_list = ["Select "]

        # Function call to update course list
        self.fetch_course()
        self.txt_regid = Entry(self.root, textvariable=self.var_regid, font=("goudy old style", 15, "bold"),
                               bg="light yellow")
        self.txt_regid.place(x=150, y=60, width=200)
        txt_date = DateEntry(self.root, textvariable=self.var_date, font=("goudy old style", 15, "bold"),
                         bg="light yellow").place(x=150, y=100, width=200)
        self.txt_batch = ttk.Combobox(self.root, textvariable=self.var_batch,
                                      values=("Select", "January", "February", "March", "April", "May", "June", "July",
                                              "August", "September", "October", 'November', "December"),
                                      font=("goudy old style", 15, "bold"), state='readonly', justify=CENTER)
        self.txt_batch.place(x=482, y=100, width=200)
        self.txt_batch.current(0)

        self.txt_name = Entry(self.root, textvariable=self.var_rname, font=("goudy old style", 15, "bold"),
                              bg="light yellow")
        self.txt_name.place(x=150, y=140, width=200)

        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender,
                                       values=("Select", "Male", "Female", "Other"),
                                       font=("goudy old style", 15, "bold"), state='readonly', justify=CENTER)
        self.txt_gender.place(x=482, y=140, width=200)
        self.txt_gender.current(0)

        txt_contact1 = Entry(self.root, textvariable=self.var_contact1, font=("goudy old style", 15, "bold"),
                             bg="light yellow").place(x=150, y=180, width=200)
        txt_contact2 = Entry(self.root, textvariable=self.var_contact2, font=("goudy old style", 15, "bold"),
                             bg="light yellow").place(x=482, y=180, width=200)
        txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15, "bold"),
                         bg="light yellow").place(x=150, y=220, width=200)
        txt_dob = DateEntry(self.root, textvariable=self.var_dob, font=("goudy old style", 15, "bold"),
                        bg="light yellow").place(x=482, y=220, width=200)

        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course, values=self.course_list,
                                       font=("goudy old style", 15, "bold"), state='readonly', justify=CENTER)
        self.txt_course.place(x=150, y=260, width=200)
        self.txt_course.current(0)

        txt_coursefees = Entry(self.root, textvariable=self.var_coursefees, font=("goudy old style", 15, "bold"),
                               bg="light yellow").place(x=482, y=260, width=200)
        txt_amount_paid = Entry(self.root, textvariable=self.var_amountpaid, font=("goudy old style", 15, "bold"),
                                bg="light yellow").place(x=150, y=300, width=200)
        txt_date_ap = DateEntry(self.root, textvariable=self.var_date_ap, font=("goudy old style", 15, "bold"),
                            bg="light yellow").place(x=482, y=300, width=200)
        txt_balance = Entry(self.root, textvariable=self.var_balance_amount, font=("goudy old style", 15, "bold"),
                            bg="light yellow").place(x=150, y=340, width=200)

        self.txt_Address = Text(self.root, width=28, height=2, font=("", 10), bg="light yellow")
        self.txt_Address.place(x=482, y=340)

        # ===========Buttons =============
        self.btn_save = Button(self.root, text="Save", font=("goudy old style", 15, "bold"),
                               bg="brown", fg="white", cursor="hand2", command=self.save)
        self.btn_save.place(x=1100, y=19, width=110, height=30)
        self.btn_add = Button(self.root, text="Register", font=("goudy old style", 15, "bold"), command=self.add,
                              bg="#2196f3", fg="white", cursor="hand2")
        self.btn_add.place(x=10, y=400, width=110, height=40)
        self.btn_update = Button(self.root, text="Update", font=("goudy old style", 15, "bold"), command=self.update,
                                 bg="#4caf50", fg="white", cursor="hand2")
        self.btn_update.place(x=130, y=400, width=110, height=40)
        self.btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), command=self.delete,
                                 bg="#f44336", fg="white", cursor="hand2")
        self.btn_delete.place(x=250, y=400, width=110, height=40)
        self.btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), command=self.clear,
                                bg="#6078db", fg="white", cursor="hand2")
        self.btn_clear.place(x=370, y=400, width=110, height=40)
        self.btn_print = Button(self.root, text="Print", font=("goudy old style", 15, "bold"),
                                bg="orange", fg="white", cursor="hand2", command=self.print)
        self.btn_print.place(x=490, y=400, width=110, height=40)
        self.btn_preview = Button(self.root, text="Preview", font=("goudy old style", 15, "bold"), command=self.Prewiew,
                                  bg="purple", fg="white", cursor="hand2")
        self.btn_preview.place(x=610, y=400, width=110, height=40)
        self.btn_check = Button(self.root, text="C", font=("goudy old style", 15, "bold"), command=self.check,
                                bg="#6078db", fg="white", cursor="hand2")
        self.btn_check.place(x=100, y=340, width=20, height=28)

        self.btn_E_table = Button(self.root, text="Enquiry Table", font=("goudy old style", 12, "bold"),
                                  command=self.enquiry_table,
                                  bg="#6078db", fg="white", cursor="hand2")
        self.btn_E_table.place(x=850, y=50, width=130, height=25)

        self.btn_R_table = Button(self.root, text="Registration Table", font=("goudy old style", 12, "bold"),
                                  command=self.Register_table,
                                  bg="#6078db", fg="white", cursor="hand2")
        self.btn_R_table.place(x=1000, y=50, width=130, height=25)
        btn_X = Button(self.root, text="X", font=("goudy old style", 18, "bold"), bg="white", bd=1, fg="red",
                       cursor="hand2", command=self.blank_frame).place(x=1150, y=50, width=30, height=25)
        #self.btn_print.config(state=DISABLED)
        self.btn_save.config(state=DISABLED)
        # ========Apllication Form Frame==================================================

        A_frame = LabelFrame(self.root, text='Application Form', font=("times new roman", 15), bg="white")
        A_frame.place(x=730, y=80, width=470, height=389)
        self.sample = f'''\t              Manjiri Computers,
              Indar Complex,Bhadgaon 9421513829
---------------------------------------------------------------
                              Application Form
---------------------------------------------------------------
             Registration ID       :- ______
             Date                        :- DD-MM-YYYY
             Batch                       :- ____________
             Name of Student      :- 
             Gender                    :- ___________
             Contact 1                 :- ___________
             Contact 2                 :- ___________
             EmailID                   :- ___________
             D.O.B                      :- DD-MM-YYYY
             Course                     :- ___________
             Course Fee              :- Rs.___________
             Amount Paid            :- Rs.___________
             Date of Payment       :- DD-MM-YYYY
             Balance Amount       :- Rs.___________
             Address                    :- ___________
         _________________              _______________
          Administrative Sign                   Student Sign
        '''
        scroll_y = Scrollbar(A_frame, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)

        self.txt_Application_form = Text(A_frame, font=('times new roman', 15), bg='light yellow',
                                         yscrollcommand=scroll_y.set)
        self.txt_Application_form.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.txt_Application_form.yview)
        self.txt_Application_form.insert(END, self.sample)

    # ==============Registration  table ==============================================
    def Register_table(self):

        self.C_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.C_frame.place(x=730, y=80, width=470, height=389)

        # =============Search Panel==================
        self.var_Search = StringVar()

        lbl_search_regid = Label(self.C_frame, text="Search by|Name ", font=("goudy old style", 15, "bold"),
                                        bg="white").place(x=10, y=10)
        self.txt_search_CourseName = Entry(self.C_frame, textvariable=self.var_Search,
                                           font=("goudy old style", 15, "bold"), bg="light yellow")
        self.txt_search_CourseName.place(x=160, y=10, width=180)

        btn_Search = Button(self.C_frame, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white",
                            cursor="hand2", command=self.search).place(x=350, y=10, width=110, height=28)

        # ==========Content ============

        lbl_registration_table = Label(self.C_frame, text="Registration table", font=("goudy old style", 15, "bold"),
                                       bg="white").place(x=170, y=40)

        self.D_frame = Frame(self.C_frame, bg="white")
        self.D_frame.place(x=0, y=70, width=470, height=319)

        scroll_x = Scrollbar(self.D_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.D_frame, orient=VERTICAL)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', background='white', font=('Arial', 12), foreground='black', rowheight=28,
                        fieldbackground='white')
        style.map('Treeview', background=[('selected', 'green')])
        self.RegisterTable = ttk.Treeview(self.D_frame, columns=(
            'regid', 'date', 'batch', 'name', 'gender', 'contact1', 'contact2', 'email', 'course', 'dob', 'coursefees',
            'amountpaid', 'date_ap',
            'balance', 'address', 'applicationform'),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.RegisterTable.xview)
        scroll_y.config(command=self.RegisterTable.yview)

        self.RegisterTable.heading("regid", text="REG ID")
        self.RegisterTable.heading("date", text="Date")
        self.RegisterTable.heading("batch", text="Batch")
        self.RegisterTable.heading("name", text="Name")
        self.RegisterTable.heading("gender", text="Gender")
        self.RegisterTable.heading("contact1", text="Contact1")
        self.RegisterTable.heading("contact2", text="Contact2")
        self.RegisterTable.heading("email", text="Email-ID")
        self.RegisterTable.heading("dob", text="D.O.B")
        self.RegisterTable.heading("course", text="Course")
        self.RegisterTable.heading("coursefees", text="Course fee")
        self.RegisterTable.heading("amountpaid", text="Amounnt Paid")
        self.RegisterTable.heading("date_ap", text="Date(Ap)")
        self.RegisterTable.heading("balance", text="Balance")
        self.RegisterTable.heading("address", text="Address")
        self.RegisterTable.heading("applicationform", text="Applicaion form")

        self.RegisterTable['show'] = "headings"
        self.RegisterTable.column("regid", width=150)
        self.RegisterTable.column("date", width=150)
        self.RegisterTable.column("batch", width=150)
        self.RegisterTable.column("name", width=150)
        self.RegisterTable.column("gender", width=150)
        self.RegisterTable.column("contact1", width=150)
        self.RegisterTable.column("contact2", width=150)
        self.RegisterTable.column("email", width=150)
        self.RegisterTable.column("dob", width=150)
        self.RegisterTable.column("course", width=150)
        self.RegisterTable.column("coursefees", width=150)
        self.RegisterTable.column("amountpaid", width=150)
        self.RegisterTable.column("date_ap", width=150)
        self.RegisterTable.column("balance", width=150)
        self.RegisterTable.column("address", width=150)
        self.RegisterTable.column("applicationform", width=150)
        self.RegisterTable.pack(fill=BOTH, expand=1)
        self.RegisterTable.bind('<ButtonRelease-1>', self.get_data)
        self.show()

    # =============Enquiry Table============================================================
    def enquiry_table(self):
        self.E_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.E_frame.place(x=730, y=80, width=470, height=389)
        # ======Search panel ===========
        self.var_Search = StringVar()
        lbl_search = Label(self.E_frame, text="Search by|Name ", font=("goudy old style", 15, "bold"),
                           bg="white").place(x=10, y=10)
        self.txt_search = Entry(self.E_frame, textvariable=self.var_Search,
                                font=("goudy old style", 15, "bold"), bg="light yellow")
        self.txt_search.place(x=160, y=10, width=180)

        btn_Search = Button(self.E_frame, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white",
                            cursor="hand2", command=self.e_search).place(x=350, y=10, width=120, height=28)

        # ==========Content ============
        lbl_enquiry_table = Label(self.E_frame, text="Enquiry table", font=("goudy old style", 15, "bold"),
                                  bg="white").place(x=170, y=40, width=147)
        self.F_frame = Frame(self.E_frame)
        self.F_frame.place(x=0, y=70, width=470, height=319)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', background='white', font=('Arial', 12), foreground='black', rowheight=28,
                        fieldbackground='white')
        style.map('Treeview', background=[('selected', 'green')])

        scroll_x = Scrollbar(self.F_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.F_frame, orient=VERTICAL)
        self.EnquiryTable = ttk.Treeview(self.F_frame, columns=(
            'date', 'name', 'course', 'coursefees', 'contact1', 'contact2', 'followup', 'email', 'address'),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.EnquiryTable.xview)
        scroll_y.config(command=self.EnquiryTable.yview)

        self.EnquiryTable.heading("date", text="Date")
        self.EnquiryTable.heading("name", text="Name")
        self.EnquiryTable.heading("course", text="Course")
        self.EnquiryTable.heading("coursefees", text="Course Fees")
        self.EnquiryTable.heading("contact1", text="Contact1")
        self.EnquiryTable.heading("contact2", text="Contact2")
        self.EnquiryTable.heading("contact2", text="Contact2")
        self.EnquiryTable.heading("followup", text="Followup")
        self.EnquiryTable.heading("email", text="Email")
        self.EnquiryTable.heading("address", text="Address")
        self.EnquiryTable['show'] = "headings"
        self.EnquiryTable.column("date", width=150)
        self.EnquiryTable.column("name", width=150)
        self.EnquiryTable.column("course", width=150)
        self.EnquiryTable.column("coursefees", width=150)
        self.EnquiryTable.column("contact1", width=150)
        self.EnquiryTable.column("contact2", width=150)
        self.EnquiryTable.column("followup", width=150)
        self.EnquiryTable.column("email", width=150)
        self.EnquiryTable.column("address", width=150)
        self.EnquiryTable.pack(fill=BOTH, expand=1)
        self.EnquiryTable.bind('<ButtonRelease-1>', self.get_e_data)
        self.e_show()

    # ==================================================================
    def Prewiew(self):
        self.btn_print.config(state=NORMAL)
        self.btn_save.config(state=NORMAL)

        A_frame = LabelFrame(self.root, text='Application Form', font=("times new roman", 15), bg="white")
        A_frame.place(x=730, y=80, width=470, height=389)
        new_sample = f'''\t           Manjiri Computers,
                Indar Complex,Bhadgaon 9421513829
---------------------------------------------------------------
                          Application Form
---------------------------------------------------------------
               Registration ID        :- {self.var_regid.get()}
               Date                        :- {self.var_date.get()}
               Batch                       :- {self.var_batch.get()}
               Name of Student      :- {self.var_rname.get()}
               Gender                    :- {self.var_gender.get()}
               Contact 1                 :- {self.var_contact1.get()}
               Contact 2                 :- {self.var_contact2.get()}
               EmailID                   :- {self.var_email.get()}
               D.O.B                      :- {self.var_dob.get()}
               Course                     :- {self.var_course.get()}
               Course Fee              :- Rs.{self.var_coursefees.get()}
               Amount Paid            :- Rs.{self.var_amountpaid.get()}
               Date of Payment       :- {self.var_date_ap.get()}
               Balance Amount       :- Rs.{self.var_balance_amount.get()}
               Address                    :- {self.txt_Address.get("1.0", END)}

    _____________                 _____________
    Administrative Sign            Student Sign
    '''
        scroll_y = Scrollbar(A_frame, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)

        self.txt_Application_form = Text(A_frame, font=('times new roman', 15), bg='light yellow',
                                         yscrollcommand=scroll_y.set)
        self.txt_Application_form.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.txt_Application_form.yview)
        self.txt_Application_form.delete('1.0', END)
        self.txt_Application_form.insert(END, new_sample)
        self.chk_print = 1

    def blank_frame(self):
        self.btn_save.config(state=DISABLED)
        self.btn_print.config(state=DISABLED)
        A_frame = LabelFrame(self.root, text='Application Form', font=("times new roman", 15), bg="white")
        A_frame.place(x=730, y=80, width=470, height=389)
        self.sample = f'''\t           Manjiri Computers,
                Indar Complex,Bhadgaon 9421513829
---------------------------------------------------------------
                          Application Form
---------------------------------------------------------------
               Registration ID        :- ____________
               Date                        :- DD-MM-YYYY
               Batch                       :- ____________
               Name of Student      :- ____________
               Gender                    :- ____________
               Contact 1                 :- ____________
               Contact 2                 :-____________
               EmailID                   :- ___________
               D.O.B                      :- DD-MM-YYYY
               Course                     :- ____________
               Course Fee              :- Rs.____________
               Amount Paid            :- Rs.____________
               Date of Payment       :- DD-MM-YYYY
               Balance Amount       :- Rs.____________
               Address                    :- ____________


    _____________                 _____________
    Administrative Sign            Student Sign
                '''
        scroll_y = Scrollbar(A_frame, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)

        self.txt_Application_form = Text(A_frame, font=('times new roman', 15), bg='light yellow',
                                         yscrollcommand=scroll_y.set)
        self.txt_Application_form.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.txt_Application_form.yview)
        self.txt_Application_form.insert(END, self.sample)
        # self.f = Frame(self.root,bg='white')
        # self.f.place(x=720, y=80, width=470, height=500)

    def get_data(self, event):
        self.txt_name.config(state="readonly")
        self.txt_regid.config(state="readonly")
        self.btn_add.config(state=DISABLED)
        self.btn_update.config(state=NORMAL)
        self.btn_delete.config(state=NORMAL)
        r = self.RegisterTable.focus()
        content = self.RegisterTable.item(r)
        row = content["values"]
        self.var_regid.set(row[0]),
        self.var_date.set(row[1]),
        self.var_batch.set(row[2]),
        self.var_rname.set(row[3]),
        self.var_gender.set(row[4]),
        self.var_contact1.set(row[5]),
        self.var_contact2.set(row[6]),
        self.var_email.set(row[7]),
        self.var_dob.set(row[8]),
        self.var_course.set(row[9]),
        self.var_coursefees.set(row[10]),
        self.var_amountpaid.set(row[11]),
        self.var_date_ap.set(row[12]),
        self.var_balance_amount.set(row[13]),
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert(END, row[14])

    def get_e_data(self, event):
        # self.txt_regid.config(state="readonly")
        r = self.EnquiryTable.focus()
        content = self.EnquiryTable.item(r)
        row = content["values"]
        self.var_date.set(row[0]),
        self.var_rname.set(row[1]),
        self.var_course.set(row[2]),
        self.var_coursefees.set(row[3]),
        self.var_contact1.set(row[4]),
        self.var_contact2.set(row[5]),
        self.var_email.set(row[7]),
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert(END, row[8])

    def add(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srms1")
        cur = con.cursor()
        try:
            if self.var_rname.get() == "" or self.var_date.get() == "" or self.var_batch.get() == "" or self.var_gender.get() == "" or self.var_contact1.get() == "" or self.var_contact2.get() == ""  or self.var_dob.get() == "":
                messagebox.showerror("Error", "All Fields are Required", parent=self.root)
            elif self.var_coursefees.get() == "" or self.var_amountpaid.get() == "" or self.var_date_ap.get() == "" or self.var_balance_amount.get() == "" or self.txt_Address.get(
                    '1.0', END) == "":
                messagebox.showerror("Error", "All Fields are Required", parent=self.root)
            elif len(self.var_contact1.get()) > 10 or len(self.var_contact2.get()) > 10:
                messagebox.showerror("Error", "Mobile no. is not valid")
            elif len(self.var_contact1.get()) < 10 or len(self.var_contact2.get()) < 10:
                messagebox.showerror("Error", "Mobile no. is not valid")
            else:
                cur.execute('select * from register_student where name =%s', (self.var_rname.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Name is already present", parent=self.root)
                else:

                    cur.execute(
                        "insert into register_student(date,batch,name,gender,contact1,contact2,email,dob,course,coursefees,amountpaid,date_ap,balance,address,applicationform) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.var_date.get(),
                            self.var_batch.get(),
                            self.var_rname.get(),
                            self.var_gender.get(),
                            self.var_contact1.get(),
                            self.var_contact2.get(),
                            self.var_email.get(),
                            self.var_dob.get(),
                            self.var_course.get(),
                            self.var_coursefees.get(),
                            self.var_amountpaid.get(),
                            self.var_date_ap.get(),
                            self.var_balance_amount.get(),
                            self.txt_Address.get("1.0", END),
                            self.var_rname.get() + '.txt'

                        ))
                    con.commit()
                    cur.execute("delete from enquiry_student where name=%s", (self.var_rname.get(),))
                    con.commit()

                    messagebox.showinfo("Success", "Student Registered successfully", parent=self.root)
                    self.send_mail()
                    self.show()


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def send_mail(self):


        rx = {self.var_email.get()}
        sub = 'Registration Confirmation'
        msg = f'''
        Hello {self.var_rname.get()},you have been Successfully Registered to our institute for {self.var_course.get()} course.
        Thank you for joining with us.
        With Regards.'''

        mailer = smtplib.SMTP('smtp.gmail.com', 587)
        mailer.ehlo()
        mailer.starttls()
        mailer.login(cr.auth['user_name'], cr.auth['password'])

        email_body = '\r\n'.join(['To:%s' % rx, 'From:%s' % (cr.auth['user_name']),
                                  'Subject:%s' % sub, '', msg])

        mailer.sendmail(cr.auth['user_name'], rx, email_body)
        # print('Email sent')

    def update(self):

        con = pymysql.connect(host="localhost", user="root", password="", database="srms1")
        cur = con.cursor()
        try:
            if self.var_regid.get() == "":
                messagebox.showerror("Error", "Reg id  should be required", parent=self.root)
            else:
                cur.execute('select * from register_student where name=%s', (self.var_rname.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Select Student from list", parent=self.root)
                else:

                    cur.execute(
                        "update register_student set date=%s,batch=%s,name=%s,gender=%s,contact1=%s,contact2=%s,email=%s,dob=%s,course=%s,coursefees=%s,amountpaid=%s,date_ap=%s,balance=%s,address=%s where regid=%s",
                        (
                            self.var_date.get(),
                            self.var_batch.get(),
                            self.var_rname.get(),
                            self.var_gender.get(),
                            self.var_contact1.get(),
                            self.var_contact2.get(),
                            self.var_email.get(),
                            self.var_dob.get(),
                            self.var_course.get(),
                            self.var_coursefees.get(),
                            self.var_amountpaid.get(),
                            self.var_date_ap.get(),
                            self.var_balance_amount.get(),
                            self.txt_Address.get("1.0", END),
                            self.var_regid.get()))

                    con.commit()
                    con.close()
                    file = open('Application forms/' + (self.var_rname.get()) + ".txt", 'w')
                    file.write(self.txt_Application_form.get('1.0', END))
                    file.close()
                    messagebox.showinfo("Success", "Student Updated successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def delete(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srms1")
        cur = con.cursor()
        try:
            if self.var_regid.get() == "":
                messagebox.showerror("Error", "Reg ID should be required", parent=self.root)
            else:
                cur.execute('select * from register_student where name=%s', (self.var_rname.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please select student from list", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from register_student where name=%s", (self.var_rname.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Student Deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def clear(self):
        self.txt_name.config(state=NORMAL)
        self.btn_add.config(state=NORMAL)
        self.btn_update.config(state=DISABLED)
        self.btn_delete.config(state=DISABLED)
        self.btn_print.config(state=DISABLED)
        self.var_regid.set("")
        self.var_date.set("")
        self.var_batch.set("Select")
        self.var_rname.set("")
        self.var_gender.set("Select")
        self.var_contact1.set("")
        self.var_contact2.set("")
        self.var_email.set("")
        self.var_dob.set("")
        self.var_course.set("Select")
        self.var_coursefees.set("")
        self.var_amountpaid.set("")
        self.var_date_ap.set("")
        self.var_balance_amount.set("")
        self.txt_Address.delete("1.0", END)
        self.txt_regid.config(state=NORMAL)
        self.txt_Application_form.delete('1.0', END)
        self.txt_Application_form.insert(END, self.sample)
        
    def show(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srms1")
        cur = con.cursor()
        try:
            cur.execute("select * from register_student")
            rows = cur.fetchall()
            self.RegisterTable.delete(*self.RegisterTable.get_children())
            for row in rows:
                self.RegisterTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def e_show(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srms1")
        cur = con.cursor()
        try:
            cur.execute("select * from enquiry_student")
            rows = cur.fetchall()
            self.EnquiryTable.delete(*self.EnquiryTable.get_children())
            for row in rows:
                self.EnquiryTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def fetch_course(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srms1")
        cur = con.cursor()
        try:
            cur.execute("select name from course")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.course_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def search(self):
        if self.txt_search_CourseName.get() == "":
            messagebox.showerror("Error", "Please enter Student  name", parent=self.root)
        con = pymysql.connect(host="localhost", user="root", password="", database="srms1")
        cur = con.cursor()
        try:
            cur.execute("select * from register_student where name LIKE '%" + str(self.var_Search.get()) + "%'")
            row = cur.fetchone()
            if row != None:
                self.RegisterTable.delete(*self.RegisterTable.get_children())
                self.RegisterTable.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        self.var_Search.set('')


    def e_search(self):
        if self.txt_search.get() == "":
            messagebox.showerror("Error", "Please enter Student  name", parent=self.root)
        con = pymysql.connect(host="localhost", user="root", password="", database="srms1")
        cur = con.cursor()
        try:
            cur.execute("select * from enquiry_student where name=%s", (self.var_Search.get(),))
            row = cur.fetchone()
            if row != None:
                self.EnquiryTable.delete(*self.EnquiryTable.get_children())
                self.EnquiryTable.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        self.var_Search.set('')


    def save(self):
        self.btn_print.config(state=DISABLED)
        self.file = open('Application forms/' + (self.var_rname.get()) + ".txt", 'w')
        self.file.write(self.txt_Application_form.get('1.0', END))
        self.file.close()
        messagebox.showinfo('Saved', 'Application Form Saved')
        self.clear()

    def print(self):
        if self.chk_print ==1:
            messagebox.showinfo('Print','Please wait while printing',parent=self.root)
            file_ = tempfile.mktemp('.txt')
            open(file_, 'w').write(self.txt_Application_form.get("1.0", END))
            os.startfile(file_, 'print')
        else:
            messagebox.showerror('Print','Please preview application form,to print Application Form',parent=self.root)


    def check(self):
        fees = float(self.var_coursefees.get())
        paid = float(self.var_amountpaid.get())
        result = fees - paid
        self.var_balance_amount.set(result)


if __name__ == "__main__":
    root = Tk()
    obj1 = RegisterClass(root)
    root.mainloop()
