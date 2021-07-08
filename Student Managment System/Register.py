from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox as tsmg
import pymysql
import os

class Register:
    def __init__(self, root1):
        self.root1 = root1
        self.root1.title('Registration Window')
        self.root1.geometry("1350x700+0+0")
        self.root1.config(bg="white")

        # ==========Bg image====================
        self.bg = ImageTk.PhotoImage(file="image/city3.png")
        bg = Label(self.root1, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #============Registration frame=================
        frame1=Frame(self.root1,bg="white")
        frame1.place(x=290,y=100, width=700, height=500)

        title= Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

        #===========================Row1
        f_name= Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="grey").place(x=50,y=100)
        self.txt_fname= Entry(frame1,font=("times new roman",15),bg="light grey")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="grey").place(x=370, y=100)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="light grey")
        self.txt_lname.place(x=370, y=130, width=250)
        #=============================Row2
        contact = Label(frame1, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="grey").place(x=50,y=170)
        self.txt_contact = Entry(frame1, font=("times new roman", 15), bg="light grey")
        self.txt_contact.place(x=50, y=200, width=250)

        email= Label(frame1, text=" Email", font=("times new roman", 15, "bold"), bg="white", fg="grey").place(x=370, y=170)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="light grey")
        self.txt_email.place(x=370, y=200, width=250)

        #============================Row3
        question = Label(frame1, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="grey").place( x=50, y=240)
        self.combo_question= ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.combo_question['values']=("Select","your First Pet Name","Your Birth Place","Your Best Friend")
        self.combo_question.place(x=50,y=270,width=250)
        self.combo_question.current(0)

        answer = Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="grey").place(x=370, y=240)
        self.txt_answer = Entry(frame1, font=("times new roman", 15), bg="light grey")
        self.txt_answer.place(x=370, y=270, width=250)


        #=============================Row4
        password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="grey").place(x=50, y=310)
        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="light grey")
        self.txt_password.place(x=50, y=340, width=250)

        c_password = Label(frame1, text=" Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="grey").place(x=370,y=310)
        self.txt_cpassword = Entry(frame1, font=("times new roman", 15), bg="light grey")
        self.txt_cpassword.place(x=370, y=340, width=250)

        #----------------------Terms
        self.var_chk= IntVar()
        check= Checkbutton(frame1,text="I Agree with terms and conditions",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",12),bg="white").place(x=50,y=380)

        self.btn_image=ImageTk.PhotoImage(file="image/register.png")
        btn_register=Button(frame1,image=self.btn_image,height=30,width=160,bd=0,cursor="hand2",command=self.Register_data).place(x=50,y=420)
        btn_login = Button(frame1, text="Sign In",font=("times new roman",20),command=self.login_window,bd=0,cursor="hand2",bg="green",fg="white").place(x=280, y=420,height=35)

    def login_window(self):
        self.root1.destroy()
        os.system("python login.py")

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.combo_question.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)

    def Register_data(self):
        if self.txt_fname.get() == "" or self.txt_lname.get() == "" or self.txt_contact.get()=="" or self.txt_email.get() =="" or self.combo_question.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            tsmg.showerror('Error',"All Field are Required",parent=self.root1)
        elif self.txt_password.get() != self.txt_cpassword.get():
            tsmg.showerror("Error","Password and confirm password should be same",parent=self.root1)
        elif self.var_chk.get() == 0:
            tsmg.showerror('Error',"Please agree our terms and conditions",parent=self.root1)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="srms")
                cur = con.cursor()
                cur.execute("select * from employee where email=%s",self.txt_email.get())
                row=cur.fetchone()
                # print(row)
                if row!=None:
                    tsmg.showerror('Error', "User already exists,Please try with another email", parent=self.root1)
                else:
                    cur.execute("insert into employee (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                            (self.txt_fname.get(),
                             self.txt_lname.get(),
                             self.txt_contact.get(),
                             self.txt_email.get(),
                             self.combo_question.get(),
                             self.txt_answer.get(),
                             self.txt_password.get()
                            ))
                    con.commit()
                    con.close()
                    self.clear()
                    tsmg.showinfo("Success","Registration Successful",parent=self.root1)
            except Exception as es:
                tsmg.showerror('Error', f" Error due to {str(es)}", parent=self.root1)








root = Tk()
obj = Register(root)
root.mainloop()
