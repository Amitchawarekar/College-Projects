import pymysql
from tkinter import *
from tkinter import ttk,messagebox
import sqlite3
from PIL import Image,ImageTk
class CourseClass:
    def __init__(self,root):
        self.root =root
        self.root.title("Student Management System")
        self.root.geometry("1240x480+0+130")
        self.root.config(bg="white")
        self.root.focus_force()

        # ========Title ==============#
        title= Label(self.root,text="Manage Course Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1220,height=35)

        #==========varaibles=================
        self.var_course=StringVar()
        self.var_duration= StringVar()

        # =========Widgets ===========
        lbl_CourseName= Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        lbl_Duration= Label(self.root,text="Duration",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=120)



        #=========Entry Fields ===========
        self.txt_CourseName= Entry(self.root,textvariable= self.var_course,font=("goudy old style",15,"bold"),bg="light yellow")
        self.txt_CourseName.place(x=150,y=60,width=200)
        txt_Duration=Entry(self.root,textvariable= self.var_duration,font=("goudy old style",15,"bold"),bg="light yellow").place(x=150,y=120,width=200)

        #===========Buttons =============
        self.btn_add =Button(self.root,text="Save",font=("goudy old style",15,"bold"),command=self.add,bg="#2196f3",fg="white",cursor="hand2")
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update= Button(self.root, text="Update", font=("goudy old style", 15, "bold"),command=self.update,bg="#4caf50", fg="white",cursor="hand2")
        self.btn_update.place(x=270, y=400, width=110, height=40)
        self.btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"),command=self.delete, bg="#f44336", fg="white",cursor="hand2")
        self.btn_delete.place(x=390, y=400, width=110, height=40)
        self.btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"),command=self.clear, bg="#6078db", fg="white",cursor="hand2")
        self.btn_clear.place(x=510, y=400, width=110, height=40)

        #======Search panel ===========
        self.var_Search=StringVar()
        lbl_search_CourseName = Label(self.root, text="Course Name", font=("goudy old style", 15, "bold"), bg="white").place(x=720,y=60)
        self.txt_search_CourseName = Entry(self.root, textvariable=self.var_Search, font=("goudy old style", 15, "bold"),bg="light yellow")
        self.txt_search_CourseName.place(x=870, y=60, width=180)

        btn_Search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white",cursor="hand2",command=self.search).place(x=1070, y=60, width=120, height=28)

        #==========Content ============
        self.C_frame= Frame(self.root,bd=2, relief=RIDGE)
        self.C_frame.place(x=720,y=100,width=470,height=340)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', background='white', font=('Arial', 12), foreground='black', rowheight=28,
                        fieldbackground='white')
        style.map('Treeview', background=[('selected', 'green')])

        scroll_x = Scrollbar(self.C_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.C_frame, orient=VERTICAL)
        self.CourseTable = ttk.Treeview(self.C_frame, columns=('cid','name','Duration'),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.CourseTable.xview)
        scroll_y.config(command=self.CourseTable.yview)

        self.CourseTable.heading("cid", text="Course ID")
        self.CourseTable.heading("name", text="Course name")
        self.CourseTable.heading("Duration", text="Duration")
        self.CourseTable['show'] = "headings"
        self.CourseTable.column("cid", width=150)
        self.CourseTable.column("name", width=150)
        self.CourseTable.column("Duration", width=150)
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind('<ButtonRelease-1>',self.get_data)
        self.show()

    #==================================================================
    def get_data(self,event):
        self.txt_CourseName.config(state="readonly")
        r= self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row= content["values"]
        print(row)

        self.var_course.set(row[1])
        self.var_duration.set(row[2])

    def add(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srms")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course name should be required", parent=self.root)
            else:
                cur.execute('select * from course where name=%s', (self.var_course.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Course Name already exists", parent=self.root)
                else:
                    cur.execute("insert into course(name,Duration) values(%s,%s)", (
                        self.var_course.get(),
                        self.var_duration.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Course added successfully", parent=self.root)
                    self.show()
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def update(self):
        con= pymysql.connect(host="localhost", user="root", password="", database="srms")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course name should be required", parent=self.root)
            else:
                cur.execute('select * from course where name=%s', (self.var_course.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Select Course from list", parent=self.root)
                else:
                    cur.execute("update course set duration=%s where name=%s", (
                        self.var_duration.get(),
                        self.var_course.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Course Update successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def delete(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srms")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course name should be required", parent=self.root)
            else:
                cur.execute('select * from course where name=%s', (self.var_course.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please select course from list", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Dp you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from course where name=%s", (self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Course Deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_Search.set("")
        self.txt_CourseName.config(state=NORMAL)




    def show(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srms")
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent=self.root)


    def search(self):
        if self.txt_search_CourseName.get() == "":
            messagebox.showerror("Error", "Please enter course name", parent=self.root)
        con = pymysql.connect(host="localhost", user="root", password="", database="srms")
        cur = con.cursor()
        try:

            cur.execute(f"select * from course where name LIKE '%{self.var_Search.get()}%'")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")



if __name__ == "__main__":
    root=Tk()
    obj=CourseClass(root)
    root.mainloop()