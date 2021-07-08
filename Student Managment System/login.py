from tkinter import *
import pymysql
from tkinter import messagebox as tsmg
from tkinter import ttk
import os
from PIL import Image,ImageTk
class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title('Login Window')
        self.root.geometry("1350x700+0+0")
        self.root.resizable(True,True)
        self.root.config(bg="white")

        self.bg1= ImageTk.PhotoImage(file="image/HKoPzd.jpg")
        bg1 = Label(self.root, image=self.bg1).place(x=0, y=0, relwidth=1, relheight=1)

        title=Label(self.root,text="Welcome to Manjiri Computers",font=("Lucida",40,"bold"),bg="brown",fg="yellow")
        title.pack(fill=X)

        login_frame = Frame(self.root, bg="orange",bd=5,relief=RIDGE)
        login_frame.place(x=440, y=150, width=410, height=400)

        self.bg2 = ImageTk.PhotoImage(file="image/images (3).jpg")
        bg2 = Label(login_frame, image=self.bg2).place(x=0, y=0, width=400, height=80)


        email=Label(login_frame,text="EMAIL ADDRESS",font=('times new roman',20,'bold'),justify=CENTER,bg="orange",fg='#581845').place(x=50,y=90)
        self.txt_email = Entry(login_frame, font=("times new roman", 15), bg="light grey")
        self.txt_email.place(x=50, y=130, width=300)

        password = Label(login_frame, text="PASSWORD", font=('times new roman', 20, 'bold'), justify=CENTER, bg="orange",fg='#581845').place(x=50, y=170)
        self.txt_password = Entry(login_frame, font=("times new roman", 15), bg="light grey",show="*")
        self.txt_password.place(x=50, y=210, width=300)

        btn_reg=Button(login_frame,text="Register new Account?",command=self.Register_window,font=("Times new roman",13,'bold'),bg="orange",bd=0,fg="blue",cursor="hand2")
        btn_reg.place(x=40,y=250)

        btn_forget=Button(login_frame,text="Forget Password?",command=self.forget_password,font=("Times new roman",13,'bold'),bg="orange",bd=0,fg="red",cursor="hand2")
        btn_forget.place(x=220,y=250)

        self.btn_image = Image.open("image/loginpng.png")
        resized = self.btn_image.resize((200,100), Image.ANTIALIAS)
        self.btn_image1 = ImageTk.PhotoImage(resized)

        btn_login = Button(login_frame,image=self.btn_image1,command=self.login_data,bd=1, bg="CRIMSON", fg="white",cursor="hand2")
        btn_login.place(x=90, y=300,width=200,height=50)

        # ========footer ==============#
        footer = Label(self.root, text="Developed By : Amit Anand Chawarekar           Email-ID : amit.chawarekar@gmail.com                           Contact no. :  9503016634,9921663430",
                       font=("goudy old style", 15), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)

    def login_data(self):
       if self.txt_email.get() == "" or self.txt_password.get() == "":
           tsmg.showerror("Error","All field are required",parent=self.root)
       else:
           try:
               con=pymysql.connect(host='localhost',user='root',password="",database="srms")
               cur=con.cursor()
               cur.execute("select * from employee where email=%s and password=%s",(self.txt_email.get(),self.txt_password.get()))
               row=cur.fetchone()

               if row == None:
                   tsmg.showerror('Error', "Invalid Username and password", parent=self.root)
               else:
                   tsmg.showinfo("Success",f"Welcome {self.txt_email.get()}",parent=self.root)
                   self.root.destroy()
                   os.system("python Dashboard.py")
               con.close()

           except Exception as es:
               tsmg.showerror('Error', f" Error due to {str(es)}", parent=self.root)

    def reset_password(self):
        if self.combo_question.get()=="Select" or self.txt_answer.get()== "" or self.txt_new_paswword.get()=="":
            tsmg.showerror("Error",'All Field are required',parent=self.root2)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password="", database="srms")
                cur = con.cursor()
                cur.execute("select * from employee where email=%s and question=%s and answer=%s",
                            (self.txt_email.get(),self.combo_question.get(),self.txt_answer.get()))
                row = cur.fetchone()

                if row == None:
                    tsmg.showerror('Error', "Please select the security Question/Enter Answer", parent=self.root2)
                else:
                    cur.execute("update employee set password=%s where email=%s",
                                (self.txt_new_paswword.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    tsmg.showinfo('Success',"Your Password has been reset,Please login with new password",parent=self.root2)
                    self.clear()
                    self.root2.destroy()

            except Exception as es:
                tsmg.showerror('Error', f" Error due to {str(es)}", parent=self.root)

    def forget_password(self):
        if self.txt_email.get() == "":
            tsmg.showerror("Error","Please Enter Email Address to reset your password",parent=self.root)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password="", database="srms")
                cur = con.cursor()
                cur.execute("select * from employee where email=%s",
                            (self.txt_email.get()))
                row = cur.fetchone()

                if row == None:
                    tsmg.showerror('Error', "Please enter valid Email Id to reset your password", parent=self.root)
                else:
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry('410x400+440+150')
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t = Label(self.root2, text='Forget Password', font=('Times new roman', 20, 'bold'), bg='yellow',
                              fg='blue')
                    t.pack(fill=X)

                    # ============================Forget Password================
                    question = Label(self.root2, text="Security Question", font=("times new roman", 17, "bold"),
                                     bg="white",
                                     fg="black").place(x=75, y=70)
                    self.combo_question = ttk.Combobox(self.root2, font=("times new roman", 15), state='readonly',
                                                       justify=CENTER)
                    self.combo_question['values'] = (
                    "Select", "your First Pet Name", "Your Birth Place", "Your Best Friend")
                    self.combo_question.place(x=75, y=110, width=260)
                    self.combo_question.current(0)

                    answer = Label(self.root2, text="Answer", font=("times new roman", 17, "bold"), bg="white",
                                   fg="black").place(x=75,
                                                    y=150)
                    self.txt_answer = Entry(self.root2, font=("times new roman", 15), bg="light yellow")
                    self.txt_answer.place(x=75, y=190, width=260)

                    new_password = Label(self.root2, text="New Password", font=("times new roman", 17, "bold"),
                                         bg="white", fg="black").place(x=75, y=230)
                    self.txt_new_paswword = Entry(self.root2, font=("times new roman", 15), bg="light yellow")
                    self.txt_new_paswword.place(x=75, y=270, width=260)

                    btn_reset_pass = Button(self.root2, text="ResetPassword?", command=self.reset_password,
                                            font=("Times new roman", 15, 'bold'), bg="green", fg="white",
                                            cursor="hand2")
                    btn_reset_pass.place(x=110, y=320)
            except Exception as es:
                tsmg.showerror('Error', f" Error due to {str(es)}", parent=self.root)

    def clear(self):
        self.combo_question.current(0)
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_new_paswword.delete(0,END)
        self.txt_answer.delete(0,END)


    def Register_window(self):
        self.root.destroy()
        os.system("python Register.py")




root = Tk()
obj = login_window(root)
root.mainloop()