from tkinter import *
from PIL import Image,ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from completeproduct import productClass
from sales import salesClass
import sqlite3
from tkinter import messagebox
import os
import time

class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Minder |  Developed by Kshitij & Utkarsh")
        self.root.config(bg="white")
        #=====Title=======
        self.icon_title = PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Inventory Minder",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #======btn_logout========
        btn_logout = Button(self.root,text="Logout",command=self.logout,font=("times new roman",15,"bold"),bg = "yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)

        #======clock=====
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Minder\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #=====Left Menu=====
        self.MenuLogo=Image.open("images/IM.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.LANCZOS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        self.employeeLogo=Image.open("images/11.png")
        self.employeeLogo=self.employeeLogo.resize((40,40),Image.LANCZOS)
        self.employeeLogo=ImageTk.PhotoImage(self.employeeLogo)

        self.supplierLogo=Image.open("images/12.png")
        self.supplierLogo=self.supplierLogo.resize((40,40),Image.LANCZOS)
        self.supplierLogo=ImageTk.PhotoImage(self.supplierLogo)

        self.categoryLogo=Image.open("images/13.png")
        self.categoryLogo=self.categoryLogo.resize((40,40),Image.LANCZOS)
        self.categoryLogo=ImageTk.PhotoImage(self.categoryLogo)

        self.productLogo=Image.open("images/14.png")
        self.productLogo=self.productLogo.resize((40,40),Image.LANCZOS)
        self.productLogo=ImageTk.PhotoImage(self.productLogo)

        self.salesLogo=Image.open("images/15.png")
        self.salesLogo=self.salesLogo.resize((40,40),Image.LANCZOS)
        self.salesLogo=ImageTk.PhotoImage(self.salesLogo)

        self.exitLogo=Image.open("images/16.png")
        self.exitLogo=self.exitLogo.resize((40,40),Image.LANCZOS)
        self.exitLogo=ImageTk.PhotoImage(self.exitLogo)

        lbl_menu = Label(LeftMenu,text="Menu",font=("times new roman",20),bg ="pink",bd=4,relief=RIDGE,).pack(side=TOP,fill=X)

        btn_employee = Button(LeftMenu,text="Employee",command=self.employee,image=self.employeeLogo,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg ="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier = Button(LeftMenu,text="Supplier",command=self.supplier,image=self.supplierLogo,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg ="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category = Button(LeftMenu,text="Category",command=self.category,image=self.categoryLogo,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg ="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product = Button(LeftMenu,text="Product",command=self.product,image=self.productLogo,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg ="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales = Button(LeftMenu,text="Sales",command=self.sales,image=self.salesLogo,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg ="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit = Button(LeftMenu,text="Exit",command=self.exit,image=self.exitLogo,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg ="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #======content=====
        self.lbl_employee = Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="purple",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier = Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_category = Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="slateblue",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)

        self.lbl_product = Label(self.root,text="Total Product\n[ 0 ]",bd=5,relief=RIDGE,bg="olivedrab",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        self.lbl_sales = Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)


        #======footer======
        lbl_footer=Label(self.root,text="INVENTORY MINDER | Developed by PYTHON PIRATES\nFor any Technical Issue Contact: 950xxxx987",font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        self.update_content()
#=============================================================================================================================
    
    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)
    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supplierClass(self.new_win)
    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)
    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)
    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)



    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from product")
            product = cur.fetchall()
            self.lbl_product.config(text=f"Total Product\n[ {str(len(product))} ]") #making a list that has multiple data
            
            cur.execute("Select * from supplier")
            supplier = cur.fetchall()
            self.lbl_supplier.config(text=f"Total Suppliers\n[ {str(len(supplier))} ]") #making a list that has multiple data
            
            cur.execute("Select * from category")
            category = cur.fetchall()
            self.lbl_category.config(text=f"Total Category\n[ {str(len(category))} ]") #making a list that has multiple data
        
            cur.execute("Select * from employee")
            employee = cur.fetchall()
            self.lbl_employee.config(text=f"Total Employees\n[ {str(len(employee))} ]") #making a list that has multiple data
            bill = len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales\n[{str(bill)}]')

            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Inventory Minder\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
            self.lbl_clock.after(200,self.update_content)

        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")

    def exit(self):
        self.root.destroy()



if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()