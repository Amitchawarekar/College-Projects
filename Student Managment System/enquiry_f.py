import pymysql
from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


from register_f import RegisterClass


class EnquiryClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1240x480+0+130")
        self.root.config(bg="white")
        self.root.focus_force()

        # ========Title ==============#
        self.course_list = ["Select Course"]
        # Function call to update course list
        self.fetch_course()
        title = Label(self.root, text="Enquiry Form", font=("goudy old style", 20, "bold"), bg="#033054",
                      fg="white").place(x=10, y=15, width=1220, height=35)

        #======variables =================
        self.var_date=StringVar()
        self.var_ename=StringVar()
        self.var_course =StringVar()
        self.var_coursefees =StringVar()
        self.var_contact1=StringVar()
        self.var_contact2=StringVar()
        self.var_followup=StringVar()
        self.var_city=StringVar()
        # =========Widgets ===========
        lbl_Date = Label(self.root, text="Date", font=("goudy old style", 18, "bold"), bg="white").place(x=10, y=60)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 18, "bold"), bg="white").place(x=10, y=100)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 18, "bold"), bg="white").place(x=10, y=140)
        lbl_coursefees = Label(self.root, text="Course fees", font=("goudy old style", 18, "bold"), bg="white").place(x=10, y=180)
        lbl_contact1 = Label(self.root, text="Contact 1", font=("goudy old style", 18, "bold"), bg="white").place(x=10,y=220)
        lbl_contact2 = Label(self.root, text="Contact 2", font=("goudy old style", 18, "bold"), bg="white").place(x=10,y=260)
        lbl_followup = Label(self.root, text="Followup", font=("goudy old style", 18, "bold"), bg="white").place(x=10,y=300)
        lbl_city = Label(self.root, text="City", font=("goudy old style", 18, "bold"), bg="white").place(x=10,y=340)
        lbl_address = Label(self.root, text="Address", font=("goudy old style", 18, "bold"), bg="white").place(x=10,y=380)


        #=======Entry Fields===============
        txt_date = DateEntry(self.root, textvariable=self.var_date,font=("goudy old style", 15, "bold"),bg="light yellow").place(x=140, y=60, width=200)
        txt_name = Entry(self.root, textvariable=self.var_ename,font=("goudy old style", 15, "bold"),bg="light yellow").place(x=140, y=100, width=200)

        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course, values=self.course_list,
                                       font=("goudy old style", 15, "bold"), state='readonly', justify=CENTER)
        self.txt_course.place(x=140, y=140, width=200)
        self.txt_course.current(0)

        txt_coursefees = Entry(self.root,textvariable=self.var_coursefees, font=("goudy old style", 15, "bold"),
                         bg="light yellow").place(x=140, y=180, width=200)

        txt_contact1 = Entry(self.root, textvariable=self.var_contact1, font=("goudy old style", 15, "bold"), bg="light yellow").place(x=140, y=220, width=200)
        txt_contact2 = Entry(self.root, textvariable=self.var_contact2, font=("goudy old style", 15, "bold"),
                             bg="light yellow").place(x=140, y=260, width=200)
        txt_followup =Entry(self.root, textvariable=self.var_followup, font=("goudy old style", 15, "bold"),
                             bg="light yellow").place(x=140, y=300, width=200)
        txt_city=Entry(self.root, textvariable=self.var_city, font=("goudy old style", 15, "bold"),
                             bg="light yellow").place(x=140, y=340, width=200)
        self.txt_Address = Text(self.root, width=28, height=2, font=("", 10), bg="light yellow")
        self.txt_Address.place(x=140, y=380)

        # ===========Buttons =============
        self.btn_add = Button(self.root, text="Save", font=("goudy old style", 15, "bold"),
                              bg="#2196f3", fg="white", cursor="hand2",command=self.add)
        self.btn_add.place(x=50, y=430, width=110, height=40)

        self.btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"),
                                 bg="#f44336", fg="white", cursor="hand2",command=self.delete)
        self.btn_delete.place(x=190, y=430, width=110, height=40)
        self.btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"),
                                bg="#6078db", fg="white", cursor="hand2",command=self.clear)
        self.btn_clear.place(x=330, y=430, width=110, height=40)

        # ======Search panel ===========
        self.var_Search = StringVar()
        lbl_search = Label(self.root, text="Search by|Name ", font=("goudy old style", 18, "bold"),
                                        bg="white").place(x=650, y=60)
        self.txt_search = Entry(self.root, textvariable=self.var_Search,
                                           font=("goudy old style", 15, "bold"), bg="light yellow")
        self.txt_search.place(x=830, y=60, width=180)

        btn_Search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white",
                            cursor="hand2",command=self.search).place(x=1030, y=60, width=120, height=28)

        # ==========Content ============
        self.E_frame = Frame(self.root, bd=2, relief=RIDGE)
        self.E_frame.place(x=650, y=100, width=530, height=340)

        scroll_x = Scrollbar(self.E_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.E_frame, orient=VERTICAL)

        style =ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview',background='white',font=('Arial',12),foreground = 'black',rowheight=28,fieldbackground='white' )
        style.map('Treeview',background=[('selected','green')])
        self.EnquiryTable = ttk.Treeview(self.E_frame, columns=('date','name','course','coursefees','contact1','contact2','followup','city','address'),
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
        self.EnquiryTable.heading("city", text="City")
        self.EnquiryTable.heading("address", text="Address")
        self.EnquiryTable['show'] = "headings"
        self.EnquiryTable.column("date", width=150)
        self.EnquiryTable.column("name", width=150)
        self.EnquiryTable.column("course", width=150)
        self.EnquiryTable.column("coursefees", width=150)
        self.EnquiryTable.column("contact1", width=150)
        self.EnquiryTable.column("contact2", width=150)
        self.EnquiryTable.column("followup", width=150)
        self.EnquiryTable.column("city", width=150)
        self.EnquiryTable.column("address", width=150)
        self.EnquiryTable.pack(fill=BOTH, expand=1)
        self.EnquiryTable.bind('<ButtonRelease-1>',self.get_data)
        self.show()


    #======================================================================


    def get_data(self, event):
        r = self.EnquiryTable.focus()
        content = self.EnquiryTable.item(r)
        row = content["values"]
        self.var_date.set(row[0]),
        self.var_ename.set(row[1]),
        self.var_course.set(row[2]),
        self.var_coursefees.set(row[3]),
        self.var_contact1.set(row[4]),
        self.var_contact2.set(row[5]),
        self.var_followup.set(row[6]),
        self.var_city.set(row[7]),
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert(END,row[8])

    def add(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srms")
        cur = con.cursor()
        try:
            if self.var_ename.get() == "":
                messagebox.showerror("Error", "Student Name should be required", parent=self.root)
            else:
                cur.execute('select * from enquiry_student where name =%s', (self.var_ename.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Name is already present", parent=self.root)
                else:
                    cur.execute(
                        "insert into enquiry_student(date,name,course,coursefees,contact1,contact2,followup,city,address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.var_date.get(),
                            self.var_ename.get(),
                            self.var_course.get(),
                            self.var_coursefees.get(),
                            self.var_contact1.get(),
                            self.var_contact2.get(),
                            self.var_followup.get(),
                            self.var_city.get(),
                            self.txt_Address.get("1.0", END)
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Student added successfully", parent=self.root)
                    self.show()
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)



    def delete(self):
        con =pymysql.connect(host="localhost", user="root", password="", database="srms")
        cur = con.cursor()
        try:
            if self.var_ename.get() == "":
                messagebox.showerror("Error", "Student name should be required", parent=self.root)
            else:
                cur.execute('select * from enquiry_student where name=%s', (self.var_ename.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please select student from list", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from enquiry_student where name=%s", (self.var_ename.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Student Deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)


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

    def clear(self):
        self.show()
        self.var_date.set("")
        self.var_ename.set("")
        self.var_course.set("Select")
        self.var_coursefees.set("")
        self.var_contact1.set("")
        self.var_contact2.set("")
        self.var_followup.set("")
        self.var_city.set("")
        self.txt_Address.delete("1.0", END)
        self.var_Search.set("")

    def show(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srms")
        cur = con.cursor()
        try:
            cur.execute("select * from enquiry_student")
            rows = cur.fetchall()
            self.EnquiryTable.delete(*self.EnquiryTable.get_children())
            for row in rows:
                self.EnquiryTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def search(self):
        if self.txt_search.get() == "":
            messagebox.showerror("Error", "Please enter Student  name", parent=self.root)
        con = pymysql.connect(host="localhost", user="root", password="", database="srms")
        cur = con.cursor()
        try:
            cur.execute("select * from enquiry_student where name=%s",(self.var_Search.get(),))
            row= cur.fetchone()
            if row != None:
                self.EnquiryTable.delete(*self.EnquiryTable.get_children())
                self.EnquiryTable.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = EnquiryClass(root)
    root.mainloop()
