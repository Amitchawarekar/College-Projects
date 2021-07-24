import pymysql
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image,ImageTk
from register_f import RegisterClass


class Resultclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1240x480+0+150")
        self.root.config(bg="white")
        self.root.focus_force()

        title = Label(self.root, text="ADD STUDENT RESULT", font=("goudy old style", 20, "bold"), bg="#033054",
                      fg="white").place(x=10, y=15, width=1220, height=35)

        # Image================================
        self.bg_img = Image.open("image/result.jpg")
        resized1 = self.bg_img.resize((540, 290), Image.ANTIALIAS)
        self.bg_img1 = ImageTk.PhotoImage(resized1)

        self.lbl_bg = Label(self.root, image=self.bg_img1).place(x=660, y=70, width=540, height=400)

        #========variables========================
        self.var_sname= StringVar()
        self.var_name= StringVar()
        self.var_course= StringVar()
        self.var_obj= StringVar()
        self.var_practical= StringVar()
        self.var_total= StringVar()

        # =====widgets============================
        self.student_list=[]
        #calling function for getting names in combobox
        self.fetch_name()
        lbl_select = Label(self.root, text="Select Student", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=52)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=110)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 20, "bold"), bg="white").place(x=50, y=170)
        lbl_obj = Label(self.root, text="Objective", font=("goudy old style", 20, "bold"), bg="white").place(x=50,y=230)
        lbl_pract = Label(self.root, text="Practical ", font=("goudy old style", 20, "bold"), bg="white").place(x=50,y=290)
        lbl_total= Label(self.root, text="Total out of 100", font=("goudy old style", 20, "bold"), bg="white").place(x=50,y=350)

        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_sname, values=self.student_list,
                                       font=("goudy old style", 15, "bold"), state='readonly', justify=CENTER)
        self.txt_student.place(x=290, y=52, width=180)
        self.txt_student.set('Select')

        btn_Search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white",
                            cursor="hand2",command=self.search).place(x=490, y=52, width=100, height=32)
        txt_name = Entry(self.root, textvariable=self.var_name,font=("goudy old style", 18, "bold"), bg="light yellow",state='readonly').place(x=290, y=110, width=300)
        txt_course= Entry(self.root, textvariable=self.var_course,font=("goudy old style", 18, "bold"), bg="light yellow",state='readonly').place(x=290, y=170, width=300)
        txt_obj= Entry(self.root, textvariable=self.var_obj,font=("goudy old style", 18, "bold"), bg="light yellow").place(x=290, y=230, width=300)
        txt_pract= Entry(self.root, textvariable=self.var_practical,font=("goudy old style", 18, "bold"), bg="light yellow").place(x=290, y=290, width=300)
        txt_total= Entry(self.root, textvariable=self.var_total,font=("goudy old style", 18, "bold"), bg="light yellow").place(x=290, y=350, width=300)

        #==========Buttons============================
        btn_total=Button(self.root,text='Total',font=('times new roman',15),bg='violet',activebackground='red',cursor='hand2',command=self.total).place(x=160,y=420,width=120,height=35)
        btn_add=Button(self.root,text='Submit',font=('times new roman',15),bg='lightgreen',activebackground='lightgreen',cursor='hand2',command=self.add).place(x=300,y=420,width=120,height=35)
        btn_clear=Button(self.root,text='Clear',font=('times new roman',15),bg='orange',activebackground='orange',cursor='hand2',command=self.clear).place(x=430,y=420,width=120,height=35)

        #=========Functions==========================
    def fetch_name(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srms1")
        cur = con.cursor()
        try:
            cur.execute("select name from register_student")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.student_list.append(row[0])

        except EXCEPTION as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def search(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srms1")
        cur = con.cursor()
        try:
            cur.execute("select name,course from register_student where name=%s", (self.var_sname.get(),))
            row = cur.fetchone()
            if row != None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)

        except EXCEPTION as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def add(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srms1")
        cur = con.cursor()
        try:
            if self.var_sname.get() == "":
                messagebox.showerror("Error", "First search student record", parent=self.root)
            else:
                cur.execute('select * from result where name=%s and course=%s', (self.var_name.get(),self.var_course.get()))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Result already present", parent=self.root)
                else:
                    cur.execute("insert into result(name,course,obj,practical,total) values(%s,%s,%s,%s,%s)", (
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_obj.get(),
                        self.var_practical.get(),
                        self.var_total.get(),

                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Result added successfully", parent=self.root)
                    self.clear()
        except EXCEPTION as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def clear(self):
        self.var_sname.set("Select"),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_obj.set(""),
        self.var_practical.set("")
        self.var_total.set("")

    def total(self):
        fees = float(self.var_obj.get())
        paid = float(self.var_practical.get())
        result = fees + paid
        self.var_total.set(result)


if __name__ == "__main__":
    root = Tk()
    obj = Resultclass(root)
    root.mainloop()