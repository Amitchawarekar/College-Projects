from tkinter import *
from PIL import Image,ImageTk
from course import CourseClass
from register_f import RegisterClass
from enquiry_f import EnquiryClass
from result import Resultclass
from viewresult import Viewresult
from recipt import Recipt
from tkinter import messagebox
import pymysql
import pandas as pd
import os
class SMS:
    def __init__(self,root):
        self.root =root
        self.root.title("Student Management System")
        self.root.geometry("1320x690+0+0")
        self.root.overrideredirect(1)
        self.root.config(bg="white")


        #=====icons ===================
        self.logo_dash=Image.open("image/logo.png")
        resized= self.logo_dash.resize((70,50),Image.ANTIALIAS)
        self.logo_dash1=ImageTk.PhotoImage(resized)

        #========Title ==============#
        title= Label(self.root,text="Student Management System",padx=10,compound=LEFT,image=self.logo_dash1,font=("goudy old style",20,"bold"),bg="#722891",fg="white").place(x=0,y=0,relwidth=1,height=50)

        #==========Menu==============
        M_Frame= LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=60,width=1240,height=70)

        btn_course= Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),command=self.add_course,bg="#451F55",fg="white",cursor="hand2").place(x=10,y=5,width=160,height=30)

        btn_enquiry = Button(M_Frame, text="Enquiry Form", font=("goudy old style", 15, "bold"), bg="#451F55",fg="white", cursor="hand2", command=self.enquiry_student).place(x=180, y=5, width=160,height=30)
        btn_register = Button(M_Frame, text="Registration form", font=("goudy old style", 15, "bold"), bg="#451F55",fg="white", cursor="hand2", command=self.register_student).place(x=350, y=5, width=180,height=30)
        btn_result= Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#451F55",fg="white",cursor="hand2",command=self.frame).place(x=540,y=5,width=160,height=30)
        btn_view_result= Button(M_Frame,text="Recipt",font=("goudy old style",15,"bold"),bg="#451F55",fg="white",cursor="hand2",command=self.recipt).place(x=710,y=5,width=160,height=30)
        btn_logout= Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#451F55",fg="white",cursor="hand2",command=self.logout).place(x=880,y=5,width=160,height=30)
        btn_exit= Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#451F55",fg="white",cursor="hand2",command=self.exit).place(x=1050,y=5,width=160,height=30)
        btn_export= Button(self.root,text="Export",font=("goudy old style",15,"bold"),bg="green",fg="white",cursor="hand2",command=self.export).place(x=1100,y=10,width=130,height=32)

        #=====Content Window ================
        self.bg_img = Image.open("image/student-management-system.jpg")
        resized1 = self.bg_img.resize((1100,270), Image.ANTIALIAS)
        self.bg_img1 = ImageTk.PhotoImage(resized1)

        self.lbl_bg=Label(self.root,image= self.bg_img1).place(x=100,y=165,width=1100,height=270)

        #==== Update details ============
        lbl_course=Label(self.root,text="Courses",font=("goudy old style",20),bd=7,relief=RIDGE,bg="#34134C",fg="white").place(x=10,y=440,width=220,height=40)
        self.lbl_course=Label(self.root,text="Total Courses\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=10,y=480,width=220,height=140)

        lbl_student = Label(self.root, text="Students", font=("goudy old style", 20), bd=7, relief=RIDGE, bg="#34134C",fg="white").place(x=260, y=440,width=220,height=40)
        self.lbl_student = Label(self.root, text="Total Students\n[0]", font=("goudy old style", 20), bd=10, relief=RIDGE,bg="#038074", fg="white")
        self.lbl_student.place(x=260, y=480, width=220, height=140)

        lbl_result = Label(self.root, text="Result", font=("goudy old style", 20), bd=7, relief=RIDGE, bg="#34134C",fg="white").place(x=510, y=440,width=220,height=40)
        self.lbl_result = Label(self.root, text="Total Results\n[0]", font=("goudy old style", 20), bd=10, relief=RIDGE,bg="#0675ad", fg="white")
        self.lbl_result.place(x=510, y=480, width=220, height=140)

        lbl_recipt = Label(self.root, text="Recipt", font=("goudy old style", 20), bd=7, relief=RIDGE,bg="#34134C", fg="white").place(x=760, y=440, width=220, height=40)
        self.lbl_recipt = Label(self.root, text="Total Recipt\n[0]", font=("goudy old style", 20), bd=10, relief=RIDGE,
                                bg="green", fg="white")
        self.lbl_recipt.place(x=760, y=480, width=220, height=140)



        lbl_developed_by = Label(self.root, text="Developed By", font=("goudy old style", 20), bd=7, relief=RIDGE,bg="#34134C", fg="white").place(x=1010, y=440, width=220, height=40)
        self.lbl_developed_by = Label(self.root,text="Amit Anand Chawarekar \n Email-\namit.chawarekar@gmail.com \n 9503016634",
                                      font=("goudy old style", 13, "bold"), bd=5, relief=RIDGE, bg="crimson",
                                      fg="white")
        self.lbl_developed_by.place(x=1010, y=480, width=220, height=140)
        # ========footer ==============#
        footer = Label(self.root, text="SMS-Student Management System\nContact us for any Technical Issue:950xxxxx34",font=("goudy old style", 12), bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
        self.update_details()
        # ==========Form frame =======================

    def frame(self):
        f=Frame(self.root,bg="white")
        f.place(x=490, y=132, width=300, height=28)
        btn_result = Button(f, text="Add Result", font=("goudy old style", 15, "bold"), bg="#451F55", fg="white",
                            cursor="hand2", command=self.add_result).place(x=10, y=0, width=120, height=30)
        btn_view_result = Button(f, text="View Result", font=("goudy old style", 15, "bold"), bg="#451F55",
                                 fg="white", cursor="hand2", command=self.view_result).place(x=150, y=0, width=120,
                                                                                             height=30)

    def update_details(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srms")
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            cr = cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n [{str(len(cr))}]")

            cur.execute("select * from register_student")
            cr = cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n [{str(len(cr))}]")

            cur.execute("select * from result")
            cr = cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n [{str(len(cr))}]")

            cur.execute("select * from recipt_table")
            cr = cur.fetchall()
            self.lbl_recipt.config(text=f"Total Recipts\n [{str(len(cr))}]")

            self.lbl_course.after(200,self.update_details)


        except EXCEPTION as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def enquiry_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj = EnquiryClass(self.new_win)

    def register_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = RegisterClass(self.new_win)

    def add_result(self):
        frame = Frame(self.root, bg='white')
        frame.place(x=490, y=132, width=300, height=28)
        self.new_win = Toplevel(self.root)
        self.new_obj = Resultclass(self.new_win)

    def view_result(self):
        frame= Frame(self.root,bg='white')
        frame.place(x=490, y=132, width=300, height=28)

        self.new_win = Toplevel(self.root)
        self.new_obj = Viewresult(self.new_win)

    def recipt(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Recipt(self.new_win)

    def logout(self):
        op=messagebox.askyesno('Confirm','Do you really want to logout',parent=self.root)
        if op == True:
            self.root.destroy()
            os.system("python login.py")

    def exit(self):
        op=messagebox.askyesno('Confirm','Do you really want to Exit',parent=self.root)
        if op == True:
            self.root.destroy()

    def export(self):

        connection = pymysql.connect(host="localhost", user="root", password="", database="srms")
        enquiry = pd.read_sql(sql="Select * from enquiry_student", con=connection)
        enquiry.to_excel('Backup\ enquiry_student.xlsx')

        course = pd.read_sql(sql="Select * from course", con=connection)
        course.to_excel('Backup\ course.xlsx')

        register = pd.read_sql(sql="Select * from register_student", con=connection)
        enquiry.to_excel('Backup\ register_student.xlsx')

        cer_info = pd.read_sql(sql="Select * from result", con=connection)
        cer_info.to_excel('Backup\ result.xlsx')

        recipt = pd.read_sql(sql="Select * from recipt_table", con=connection)
        recipt.to_excel('Backup\ recipt_table.xlsx')

        messagebox.showinfo('backup', 'Backup is Successfully stored', parent=self.root)





if __name__ == "__main__":
    root=Tk()
    obj=SMS(root)
    root.mainloop()