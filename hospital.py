import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

class hsptl():
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management")

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")

        title = tk.Label(self.root, text="Hospital Management System", bd=4, relief="raised", bg="gray", fg="white", font=("Elephant",45,"italic"))
        title.pack(side="top", fill="x")

        # admit frame

        admitFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(150,150,230))
        admitFrame.place(width=self.width/3, height=self.height-180, x=20, y=100)

        idLbl = tk.Label(admitFrame, text="Enter_ID:", bg=self.clr(150,150,230), font=("Arial",15,"bold"))
        idLbl.grid(row=0, column=0, padx=20, pady=15)
        self.id = tk.Entry(admitFrame, width=18, bd=3, font=("arial",15,"bold"))
        self.id.grid(row=0, column=1, padx=10, pady=15)

        nameLbl = tk.Label(admitFrame, text="Enter_Name:", bg=self.clr(150,150,230), font=("Arial",15,"bold"))
        nameLbl.grid(row=1, column=0, padx=20, pady=15)
        self.name = tk.Entry(admitFrame, width=18, bd=3, font=("arial",15,"bold"))
        self.name.grid(row=1, column=1, padx=10, pady=15)

        groupLbl = tk.Label(admitFrame, text="B_Group:", bg=self.clr(150,150,230), font=("Arial",15,"bold"))
        groupLbl.grid(row=2, column=0, padx=20, pady=15)
        self.group = tk.Entry(admitFrame, width=18, bd=3, font=("arial",15,"bold"))
        self.group.grid(row=2, column=1, padx=10, pady=15)

        deseaseLbl = tk.Label(admitFrame, text="Desease:", bg=self.clr(150,150,230), font=("Arial",15,"bold"))
        deseaseLbl.grid(row=3, column=0, padx=20, pady=15)
        self.desease = tk.Entry(admitFrame, width=18, bd=3, font=("arial",15,"bold"))
        self.desease.grid(row=3, column=1, padx=10, pady=15)

        medLbl = tk.Label(admitFrame, text="Medication:", bg=self.clr(150,150,230), font=("Arial",15,"bold"))
        medLbl.grid(row=4, column=0, padx=20, pady=15)
        self.medicine = tk.Entry(admitFrame, width=18, bd=3, font=("arial",15,"bold"))
        self.medicine.grid(row=4, column=1, padx=10, pady=15)

        pointLbl = tk.Label(admitFrame, text="H_Points:", bg=self.clr(150,150,230), font=("Arial",15,"bold"))
        pointLbl.grid(row=5, column=0, padx=20, pady=15)
        self.point = tk.Entry(admitFrame, width=18, bd=3, font=("arial",15,"bold"))
        self.point.grid(row=5, column=1, padx=10, pady=15)

        addrLbl = tk.Label(admitFrame, text="Address:", bg=self.clr(150,150,230), font=("Arial",15,"bold"))
        addrLbl.grid(row=6, column=0, padx=20, pady=15)
        self.addr = tk.Entry(admitFrame, width=18, bd=3, font=("arial",15,"bold"))
        self.addr.grid(row=6, column=1, padx=10, pady=15)

        okBtn = tk.Button(admitFrame,command=self.admitFun, text="Admit", width=20, bd=3, relief="raised", bg="light gray", font=("Arial",20,"bold"))
        okBtn.grid(row=7, column=0, padx=30, pady=20, columnspan=2)



        # detail Frame 

        self.detFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(150,230,120))
        self.detFrame.place(width=self.width/2+140, height= self.height-180, x=self.width/3+40, y=100)

        pidLbl = tk.Label(self.detFrame, text="Enter_ID:", bg=self.clr(150,230,120), font=("arial",15,"bold"))
        pidLbl.grid(row=0, column=0, padx=20, pady=20)
        self.pid = tk.Entry(self.detFrame, bd=3, width=16, font=("airal",15))
        self.pid.grid(row=0, column=1, padx=10, pady=20)

        srchBtn = tk.Button(self.detFrame,command=self.srchFun, text="Search",width=8,font=("arial",12,"bold"),bd=3,relief="raised")
        srchBtn.grid(row=0, column=2)

        medBtn = tk.Button(self.detFrame,command=self.medFun, text="Medication",width=8,font=("arial",12,"bold"),bd=3,relief="raised")
        medBtn.grid(row=0, column=3, padx=10, pady=20)

        pointBtn = tk.Button(self.detFrame,command=self.pointFrame, text="H_Update",width=7,font=("arial",12,"bold"),bd=3,relief="raised")
        pointBtn.grid(row=0, column=4, padx=10, pady=20)

        disBtn = tk.Button(self.detFrame,command=self.desFun, text="Discharge",width=7,font=("arial",12,"bold"),bd=3,relief="raised")
        disBtn.grid(row=0, column=5, padx=10, pady=20)

        self.tabFun()

    def tabFun(self):
        tabFrame = tk.Frame(self.detFrame, bd=4, relief="sunken", bg="cyan")
        tabFrame.place(width=self.width/2+80, height=self.height-300, x=27, y=80)

        x_scrol = tk.Scrollbar(tabFrame, orient="horizontal")
        x_scrol.pack(side="bottom", fill="x")

        y_scrol = tk.Scrollbar(tabFrame, orient="vertical")
        y_scrol.pack(side="right", fill="y")

        self.table = ttk.Treeview(tabFrame,xscrollcommand=x_scrol.set, yscrollcommand=y_scrol.set,
                                  columns=("pid","name","bg","desease","points","med","addr"))

        x_scrol.config(command=self.table.xview)
        y_scrol.config(command=self.table.yview)
        
        self.table.heading("pid", text="Patient_ID")
        self.table.heading("name", text="Patient_Name")
        self.table.heading("bg", text="B_Group")
        self.table.heading("desease", text="Desease")
        self.table.heading("points", text="H_Points")
        self.table.heading("med", text="Medication")
        self.table.heading("addr", text="Patient_Address")
        self.table["show"]= "headings"

        self.table.pack(fill="both", expand=1)

    def admitFun(self):
        id = self.id.get()
        name = self.name.get()
        bg = self.group.get()
        des = self.desease.get()
        p = self.point.get()
        med = self.medicine.get()
        addr = self.addr.get()

        if id and name and bg and des and p and med and addr:
            point = int(p)
            try:
                self.dbFun()
                self.cur.execute("insert into hospital(id,name,b_group,desease,points,medics,addr) values(%s,%s,%s,%s,%s,%s,%s)",(id,name,bg,des,point,med,addr))
                self.con.commit()
                tk.messagebox.showinfo("Success",f"Patient {name} with ID:{id} is admitted!")
                self.clearFun()
                self.cur.execute("select * from hospital where id=%s",id)
                row = self.cur.fetchone()

                self.table.delete(*self.table.get_children())
                self.table.insert('',tk.END,  values=row)
                self.con.close()
            
            except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {e}")
        else:
            tk.messagebox.showerror("Error", "Please Fill All Input Fields!")

    def srchFun(self):
        id = self.pid.get()
        try:
            self.dbFun()
            self.cur.execute("select * from hospital where id=%s",id)
            row = self.cur.fetchone()
            if row:
                self.table.delete(*self.table.get_children())
                self.table.insert('',tk.END,  values=row)
                self.con.close()
            else:
                tk.messagebox.showerror("Error",f"Invalid Patient ID:{id}")
        except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {e}")  

    def medFun(self):
        id = self.pid.get()
        try:
            self.dbFun()
            self.cur.execute("select medics from hospital where id=%s",id)
            row = self.cur.fetchone()
            if row:
                tk.messagebox.showinfo("Medicine", f"Recommonded Medicine for Patient is/are:{row[0]}")
                self.con.close()
            else:
                tk.messagebox.showerror("Error",f"Invalid Patient ID:{id}")
        except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {e}") 

    def pointFrame(self):
        id = self.pid.get()
        if id:
            self.pFrame = tk.Frame(self.root, bd=4, relief="ridge", bg=self.clr(250,100,80))
            self.pFrame.place(width=self.width/3,height=200, x=self.width/3+40, y=180)

            pointLbl = tk.Label(self.pFrame, text="Add Point:", bg=self.clr(250,100,80), font=("Arial",15,"bold"))
            pointLbl.grid(row=0, column=0, padx=20, pady=30)
            self.points = tk.Entry(self.pFrame, width=18, bd=3, font=("Arial",15,"bold"))
            self.points.grid(row=0, column=1, padx=10, pady=30)

            updBtn = tk.Button(self.pFrame,command=self.pointFun, text="Enter", width=20, bd=3, relief="raised", font=("Arial",20,"bold"))
            updBtn.grid(row=1,column=0, columnspan=2, padx=30, pady=40)

        else:
            tk.messagebox.showerror("Error","Please Insert Patient ID")

    def desFrame(self):
        self.pFrame.destroy()

    def pointFun(self):
        id = self.pid.get()
        newPoint = int(self.points.get())
        try:
            self.dbFun()
            self.cur.execute("select points from hospital where id=%s",id)
            row = self.cur.fetchone()
            if row:
                upd = row[0]+newPoint
                self.cur.execute("update hospital set points=%s where id=%s",(upd,id))
                self.con.commit()
                tk.messagebox.showinfo("Success","Healt Points Updated!")
                self.desFrame()
                self.cur.execute("select * from hospital where id=%s",id)
                data = self.cur.fetchone()

                self.table.delete(*self.table.get_children())
                self.table.insert('',tk.END,  values=data)
                self.con.close()

            else:
                tk.messagebox.showerror("Error","Please Insert Valid Patient ID")
                self.desFrame()
        except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {e}")

    def desFun(self):
        id = self.pid.get()
        try:
            self.dbFun()
            self.cur.execute("delete from hospital where id=%s",id)
            self.con.commit()
            tk.messagebox.showerror("Seccess", f"Patient with id:{id} discharged successfuly!")
            self.table.delete(*self.table.get_children())
            self.con.close()

        except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {e}")

    def dbFun(self):
        self.con = pymysql.connect(host="localhost", user="root", passwd="admin", database="rec")
        self.cur = self.con.cursor()

    def clr(self, r,g,b):
        return f"#{r:02x}{g:02x}{b:02x}"

    def clearFun(self):
        self.id.delete(0,tk.END)
        self.name.delete(0,tk.END)
        self.group.delete(0,tk.END)
        self.desease.delete(0,tk.END)
        self.point.delete(0,tk.END)
        self.medicine.delete(0,tk.END)
        self.addr.delete(0,tk.END)


root = tk.Tk()
obj = hsptl(root)
root.mainloop()