from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

class form:
    def __init__(self, root):
        self.root = root
        self.root.title("Forms")
        self.root.geometry("1350x700+0+0")

    #============= Main Button Frame ==========================
        btn_frame= Frame(self.root,bd=7, relief=RIDGE, bg="crimson")
        btn_frame.place(x=0,y=0,width=100,height=680)
        btn=Button(btn_frame,text="Enquiry\nForm",command=self.Enquiry_form,font=("lucida",10,"bold"),bd=2).place(x=0,y=0,width=87,height=80)
        btn=Button(btn_frame,text="Registration\n Form",command=self.Registration_form,font=("lucida",10,"bold")).place(x=0,y=86,width=87,height=80)

    def Registration_form(self):

        R_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        R_Frame.place(x=105, y=0, width=1160, height=680)

        title = Label(R_Frame, text="  Registration form ", font=("times new roman", 20, "bold"), bd=5, relief=GROOVE,bg="yellow", fg="red")
        title.pack(side=TOP, fill=X)

        lbl_R_id = Label(R_Frame, text="Reg_ID", font=("lucida", 19, "bold"), bg="crimson", fg="white")
        lbl_R_id.place(x=10, y=50)

        txt_R_id = Entry(R_Frame, font=("times new roman", 18, "bold"), bd=5, relief=GROOVE)
        txt_R_id.place(x=10, y=90, width=220, height=35)


        r_date = Label(R_Frame, text="Date", font=("lucida", 19, "bold"), bg="crimson", fg="white")
        r_date.place(x=270, y=50)

        self.var_date=StringVar()
        r_txt_date = Entry(R_Frame,textvariable=self.var_date, font=("times new roman", 15, "bold"), bd=5,relief=GROOVE)
        r_txt_date.place(x=270, y=90, width=220, height=35)

        r_name = Label(R_Frame, text="Name of Student", font=("lucida", 19, "bold"), bg="crimson", fg="white")
        r_name.place(x=10, y=140)

        self.var_name = StringVar()
        r_txt_name = Entry(R_Frame,textvariable=self.var_name, font=("times new roman", 15, "bold"), bd=5,relief=GROOVE)
        r_txt_name.place(x=10, y=180, width=220, height=35)

        r_lbl_Gender = Label(R_Frame, text="Gender", font=("lucida", 19, "bold"), bg="crimson",fg="white")
        r_lbl_Gender.place(x=270,y=140)

        r_combo_gender = ttk.Combobox(R_Frame, font=("times new roman", 13, "bold"))
        r_combo_gender['values'] = ('male', 'female', 'other')
        r_combo_gender.place(x=270,y=180,width=220,height=35)

        r_lbl_DOB = Label(R_Frame, text="D.O.B", font=("lucida", 19, "bold"), bg="crimson",fg="white")
        r_lbl_DOB.place(x=530,y=140)

        r_txt_DOB = Entry(R_Frame, font=("lucida", 15, "bold"), bd=5,relief=GROOVE)
        r_txt_DOB.place(x=530,y=180,width=220,height=35)

        r_contact1 = Label(R_Frame, text="Contact  1", font=("lucida", 19, "bold"), bg="crimson",fg="white")
        r_contact1.place(x=10, y=230)

        r_txt_contact1 = Entry(R_Frame, font=("lucida", 15, "bold"),bd=5, relief=GROOVE)
        r_txt_contact1.place(x=10, y=270, width=220, height=35)

        r_contact2 = Label(R_Frame, text="Contact  2", font=("lucida", 19, "bold"), bg="crimson",fg="white")
        r_contact2.place(x=270, y=230)

        r_txt_contact2 = Entry(R_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        r_txt_contact2.place(x=270, y=270, width=220, height=35)

        r_course = Label(R_Frame, text="Course", font=("lucida", 19, "bold"), bg="crimson", fg="white")
        r_course.place(x=530, y=230)

        r_combo_course= ttk.Combobox(R_Frame, font=("lucida", 15, "bold"))
        r_combo_course['values'] = ('MS-CIT','C','MS Office','klick','tally')
        r_combo_course.place(x=530, y=270, width=220, height=35)

        r_course_fees = Label(R_Frame, text="Course Fees", font=("lucida", 19, "bold"), bg="crimson", fg="white")
        r_course_fees.place(x=10, y=320)

        r_txt_course_fees = Entry(R_Frame, font=("lucida", 15, "bold"), bd=5, relief=GROOVE)
        r_txt_course_fees.place(x=10, y=360, width=220, height=35)

        r_fees_paid = Label(R_Frame, text="Fees Paid", font=("lucida", 19, "bold"), bg="crimson", fg="white")
        r_fees_paid.place(x=270, y=320)

        r_txt_fees_paid = Entry(R_Frame, font=("lucida", 15, "bold"), bd=5, relief=GROOVE)
        r_txt_fees_paid.place(x=270, y=360, width=220, height=35)

        r_fees_remain= Label(R_Frame, text="Fees remaining", font=("lucida", 19, "bold"), bg="crimson", fg="white")
        r_fees_remain.place(x=530, y=320)

        r_txt_course_fees = Entry(R_Frame, font=("lucida", 15, "bold"), bd=5, relief=GROOVE)
        r_txt_course_fees.place(x=530, y=360, width=220, height=35)

        r_Address = Label(R_Frame, text="Address", font=("lucida", 19, "bold"), bg="crimson",fg="white")
        r_Address.place(x=10, y=410)

        r_txt_Address = Text(R_Frame, width=43, height=5, font=("", 15))
        r_txt_Address.place(x=10, y=450)

        # ==========Button frame ====================================================
        btn_Frame = Frame(R_Frame, bd=0, relief=RIDGE, bg="crimson")
        btn_Frame.place(x=10, y=590, width=720,)

        r_Addbtn = Button(btn_Frame, text="ADD", width=15, height=2, bd=2).grid(row=0, column=0,padx=10, pady=10)
        r_clearbtn = Button(btn_Frame, text="CLEAR", width=15, height=2, bd=2).grid(row=0, column=1,padx=10,pady=10)
        r_update = Button(btn_Frame, text="UPDATE", width=15, height=2, bd=2).grid(row=0, column=2, padx=10,pady=10)
        r_delete = Button(btn_Frame, text="DELETE", width=15, height=2, bd=2).grid(row=0, column=3,padx=10, pady=10)
        r_database_btn = Button(btn_Frame, text="DATABASE", width=15,height=2).grid(row=0, column=4,padx=10,pady=10)

    def get_data(self,event):
        r= self.Student_table.focus()
        content=self.Student_table.item(r)
        row= content["values"]
        print(row)

        self.var_date.set(row[0])
        self.var_name.set(row[1])






    def Enquiry_form(self):
        # ===================All variables ==========================
        self.e_txt_date = StringVar()
        self.e_txt_name = StringVar()
        self.e_txt_course = StringVar()
        self.e_txt_contact1 = StringVar()
        self.e_txt_contact2 = StringVar()
        self.e_txt_followup = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        # =========Enquiry form ==========================
        Enquiry_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Enquiry_Frame.place(x=105, y=0, width=1160, height=680)

        title = Label(Enquiry_Frame, text="  Enquiry Form", font=("times new roman", 20, "bold"), bd=5, relief=GROOVE,bg="yellow", fg="red")
        title.pack(side=TOP, fill=X)

        e_date = Label(Enquiry_Frame, text="Date:", font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        e_date.place(x=10, y=60)

        e_txt_date = Entry(Enquiry_Frame, textvariable=self.e_txt_date, font=("times new roman", 15, "bold"), bd=5,
                           relief=GROOVE)
        e_txt_date.place(x=130, y=60, width=300, height=35)

        e_name = Label(Enquiry_Frame, text="Name:", font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        e_name.place(x=10, y=100)

        e_txt_name = Entry(Enquiry_Frame, textvariable=self.e_txt_name, font=("times new roman", 15, "bold"), bd=5,
                           relief=GROOVE)
        e_txt_name.place(x=130, y=100, width=300, height=35)

        e_course = Label(Enquiry_Frame, text="Course:", font=("times new roman", 20, "bold"), bg="crimson", fg="white")
        e_course.place(x=450, y=100)

        e_txt_course = Entry(Enquiry_Frame, textvariable=self.e_txt_course, font=("times new roman", 15, "bold"), bd=5,
                             relief=GROOVE)
        e_txt_course.place(x=590, y=100, width=300, height=35)

        e_contact1 = Label(Enquiry_Frame, text="Contact1:", font=("times new roman", 20, "bold"), bg="crimson",
                           fg="white")
        e_contact1.place(x=10, y=150)

        e_txt_contact1 = Entry(Enquiry_Frame, textvariable=self.e_txt_contact1, font=("times new roman", 15, "bold"),
                               bd=5, relief=GROOVE)
        e_txt_contact1.place(x=130, y=150, width=300, height=35)

        e_contact2 = Label(Enquiry_Frame, text="Contact2:", font=("times new roman", 20, "bold"), bg="crimson",
                           fg="white")
        e_contact2.place(x=450, y=150)

        e_txt_contact2 = Entry(Enquiry_Frame, textvariable=self.e_txt_contact2, font=("times new roman", 15, "bold"),
                               bd=5, relief=GROOVE)
        e_txt_contact2.place(x=590, y=150, width=300, height=35)

        e_Address = Label(Enquiry_Frame, text="Address:", font=("times new roman", 20, "bold"), bg="crimson",
                          fg="white")
        e_Address.place(x=10, y=200)

        self.e_txt_Address = Text(Enquiry_Frame, width=42, height=4, font=("", 10))
        self.e_txt_Address.place(x=130, y=200)

        e_followup = Label(Enquiry_Frame, text="Follow Up:", font=("times new roman", 20, "bold"), bg="crimson",
                           fg="white")
        e_followup.place(x=450, y=200)

        e_txt_followup = Entry(Enquiry_Frame, textvariable=self.e_txt_followup, font=("times new roman", 15, "bold"),
                               bd=5, relief=GROOVE)
        e_txt_followup.place(x=590, y=200, width=300, height=35)

        # ==========Button frame =======================
        # ==========Button frame ====================================================
        btn_Frame = Frame(Enquiry_Frame, bd=0, relief=RIDGE, bg="crimson")
        btn_Frame.place(x=200, y=280, width=700)

        Addbtn = Button(btn_Frame, text="ADD", width=15, height=1, bd=2, command=self.add_data).grid(row=0, column=0,
                                                                                                     padx=10, pady=10)
        clearbtn = Button(btn_Frame, text="CLEAR", width=15, height=1, bd=2, command=self.e_clear).grid(row=0, column=1,
                                                                                                        padx=10,
                                                                                                        pady=10)
        AddtoRegbtn = Button(btn_Frame, text="Confirm", width=15, height=1, bd=2,command=self.confirm).grid(row=0, column=2, padx=10,
                                                                                       pady=10)
        delete = Button(btn_Frame, text="delete", width=15, height=1, bd=2, command=self.e_delete).grid(row=0, column=3,
                                                                                                        padx=10,
                                                                                                        pady=10)
        Updatebtn = Button(btn_Frame, text="UPDATE", width=15, command=self.e_update_data).grid(row=0, column=4,
                                                                                                padx=10,
                                                                                                pady=10)

        # =======================database Frame======================================
        f1 = Frame(Enquiry_Frame, bd=3, relief=RIDGE, bg="crimson")
        f1.place(x=0, y=330, width=1143, height=340)

        lbl_e_search = Label(f1, text="Search By", font=("times new roman", 15, "bold"), bg="crimson", fg="white")
        lbl_e_search.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.combo_e_search = ttk.Combobox(f1, font=("times new roman", 12, "bold"), width=15)
        self.combo_e_search['values'] = ('name')
        self.combo_e_search.grid(row=0, column=1, padx=10, pady=10)

        self.txt_e_search = Entry(f1, width=15, font=("times new roman", 12, "bold"), bd=2, relief=GROOVE)
        self.txt_e_search.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        searchbtn = Button(f1, text="Search", width=10, pady=5, command=self.e_search_data).grid(row=0, column=3,padx=10, pady=10)
        showallbtn = Button(f1, text="ShowAll", width=10, pady=5, command=self.e_fetchdata).grid(row=0, column=4,padx=10, pady=10)

        # ==============Table Frame ==================================

        Table_Frame = Frame(f1, bd=4, relief=RIDGE, bg="black")
        Table_Frame.place(x=0, y=50, width=1133, height=282)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame,columns=('date', 'name', 'course', 'contact1', 'contact2', 'address', 'followup'),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("date", text="Date")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("course", text="Course")
        self.Student_table.heading("contact1", text="Contact1")
        self.Student_table.heading("contact2", text="Contact2")
        self.Student_table.heading("address", text="Address")
        self.Student_table.heading("followup", text="followup")

        self.Student_table['show'] = "headings"
        self.Student_table.column("date", width=150)
        self.Student_table.column("name", width=150)
        self.Student_table.column("course", width=150)
        self.Student_table.column("contact1", width=150)
        self.Student_table.column("contact2", width=150)
        self.Student_table.column("address", width=150)
        self.Student_table.column("followup", width=150)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.e_get_cursor)

    def add_data(self):
        if self.e_txt_date.get() == "" or self.e_txt_name.get() == "" or self.e_txt_course.get() == "" or self.e_txt_contact1.get() == "" or self.e_txt_contact2.get() == "" or self.e_txt_contact2.get() == "" or self.e_txt_Address.get('1.0', END) == "":
            messagebox.showerror("Error", 'All fields are required!')
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="employee2")
            cur = con.cursor()
            cur.execute("insert into enquiry_form values(%s,%s,%s,%s,%s,%s,%s)", (self.e_txt_date.get(),
                                                                                  self.e_txt_name.get(),
                                                                                  self.e_txt_course.get(),
                                                                                  self.e_txt_contact1.get(),
                                                                                  self.e_txt_contact2.get(),
                                                                                  self.e_txt_Address.get('1.0', END),
                                                                                  self.e_txt_followup.get()
                                                                                  ))
            con.commit()
            self.e_fetchdata()
            self.e_clear()
            con.close()
            messagebox.showinfo("Success", "Record has been inserted")

    def confirm(self):
        self.Registration_form()
        self.get_data()


    def e_fetchdata(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="employee2")
        cur = con.cursor()
        cur.execute("select * from enquiry_form")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()

    def e_clear(self):
        self.e_txt_date.set("")
        self.e_txt_name.set("")
        self.e_txt_course.set("")
        self.e_txt_contact1.set("")
        self.e_txt_contact2.set("")
        self.e_txt_Address.delete("1.0", END)
        self.e_txt_followup.set("")

    def e_get_cursor(self, event):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        self.e_txt_date.set(row[0])
        self.e_txt_name.set(row[1])
        self.e_txt_course.set(row[2])
        self.e_txt_contact1.set(row[3])
        self.e_txt_contact2.set(row[4])
        self.e_txt_Address.delete("1.0", END)
        self.e_txt_Address.insert(END, row[5])
        self.e_txt_followup.set(row[6])

    def e_update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="employee2")
        cur = con.cursor()
        cur.execute("update  enquiry_form set date=%s,course=%s,contact1=%s,contact2=%s,address=%s,followup=%s where name=%s", (
                self.e_txt_date.get(),
                self.e_txt_course.get(),
                self.e_txt_contact1.get(),
                self.e_txt_contact2.get(),
                self.e_txt_Address.get('1.0', END),
                self.e_txt_followup.get(),
                self.e_txt_name.get()))
        con.commit()
        self.e_fetchdata()
        self.e_clear()
        con.close()

    def e_delete(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="employee2")
        cur = con.cursor()
        cur.execute("delete from enquiry_form where name=%s", self.e_txt_name.get())
        con.commit()
        con.close()
        self.e_fetchdata()
        self.e_clear()

    def e_search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="employee2")
        cur = con.cursor()
        cur.execute("select * from enquiry_form where " + str(self.combo_e_search.get()) + " LIKE '%" + str(
            self.txt_e_search.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()










root = Tk()
obj = form(root)
root.mainloop()
