import pymysql
from tkinter import *
from tkinter import ttk, messagebox

from register_f import RegisterClass



class Viewresult:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1240x480+0+130")
        self.root.config(bg="white")
        self.root.focus_force()

        #=====================title====================
        title = Label(self.root, text="VIEW STUDENT RESULTS", font=("goudy old style", 20, "bold"), bg="#033054",
                      fg="white").place(x=10, y=15, width=1220, height=35)
        #==============variables=============
        self.var_search=StringVar()

        #============search==========
        lbl_select = Label(self.root, text="Search By Name", font=("goudy old style", 20, "bold"), bg="white").place(
            x=180, y=100)
        txt_select = Entry(self.root,textvariable=self.var_search,font=("goudy old style", 20), bg="light yellow").place(
            x=400, y=100,width=300)

        btn_Search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white",
                            cursor="hand2",command=self.search).place(x=740, y=100, width=100, height=35)
        btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="grey", fg="white",
                            cursor="hand2",command=self.clear).place(x=870, y=100, width=100, height=35)


        lbl_name = Label(self.root, text="Name", font=("goudy old style", 20, "bold"), bg="white",bd=2,relief=GROOVE).place(x=80, y=230,width=200,height=50)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 20, "bold"), bg="white",bd=2,relief=GROOVE).place(x=280,y=230,width=200,height=50)
        lbl_obj_m = Label(self.root, text="Objective Marks", font=("goudy old style", 20, "bold"),bd=2,relief=GROOVE , bg="white").place(x=480, y=230,width=200,height=50)
        lbl_pract_m = Label(self.root, text="Practical Marks", font=("goudy old style", 20, "bold"), bg="white",bd=2,relief=GROOVE).place(x=680, y=230,width=200,height=50)
        lbl_total_m = Label(self.root, text="Total Marks", font=("goudy old style", 20, "bold"), bg="white",bd=2,relief=GROOVE).place(x=880, y=230,width=200,height=50)

        self.lbl_name = Label(self.root, font=("goudy old style", 17, "bold"), bg="white", bd=2,relief=GROOVE)
        self.lbl_name.place(x=80, y=280, width=200, height=50)
        self.lbl_course = Label(self.root,font=("goudy old style", 17, "bold"), bg="white", bd=2,relief=GROOVE)
        self.lbl_course.place(x=280, y=280, width=200, height=50)
        self.lbl_obj_m = Label(self.root,  font=("goudy old style", 17, "bold"), bd=2, relief=GROOVE, bg="white")
        self.lbl_obj_m.place(x=480, y=280, width=200, height=50)
        self.lbl_pract_m= Label(self.root, font=("goudy old style", 17, "bold"), bg="white", bd=2,relief=GROOVE)
        self.lbl_pract_m.place(x=680, y=280, width=200, height=50)
        self.lbl_total_m = Label(self.root,font=("goudy old style", 17, "bold"), bg="white", bd=2,relief=GROOVE)
        self.lbl_total_m.place(x=880, y=280, width=200, height=50)

#===================================================================================================================
    def search(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srms")
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Erroe"," Student Name should be required",parent=self.root)
            else:
                cur.execute("select * from result where name=%s", (self.var_search.get(),))
                row = cur.fetchone()
                if row != None:
                    self.lbl_name.config(text=row[1])
                    self.lbl_course.config(text=row[2])
                    self.lbl_obj_m.config(text=row[3])
                    self.lbl_pract_m.config(text=row[4])
                    self.lbl_total_m.config(text=row[5])
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)

        except EXCEPTION as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    def clear(self):
        self.lbl_name.config(text="")
        self.lbl_course.config(text="")
        self.lbl_obj_m.config(text="")
        self.lbl_pract_m.config(text="")
        self.lbl_total_m.config(text="")
        self.var_search.set("")



if __name__ == "__main__":
    root = Tk()
    obj = Viewresult(root)
    root.mainloop()