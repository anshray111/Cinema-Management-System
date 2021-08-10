import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import sys
import cx_Oracle
con = cx_Oracle.connect('system/rutu2633432@localhost')

def Admin_Table():
    Admin_Table_Window=tk.Tk()
    
    Admin_Table_Window.geometry("600x450+332+109")
    Admin_Table_Window.minsize(120, 1)
    Admin_Table_Window.maxsize(1284, 701)
    Admin_Table_Window.resizable(0,0)
    Admin_Table_Window.title("Admin Table")
    
    treev = ttk.Treeview(Admin_Table_Window, selectmode ='browse')
    treev.place(relx=0.3,rely=0.3)
    treev["columns"] = ("1", "2", "3")
    
    # Defining heading
    treev['show'] = 'headings'
    treev.column("1", width = 50, anchor ='c')
    treev.column("2", width = 100, anchor ='c')
    treev.column("3", width = 100, anchor ='c')
    treev.heading("1", text ="Sr No.")
    treev.heading("2", text ="Admin ID")
    treev.heading("3", text ="Password")
    
    Cursor = con.cursor()
    Cursor.execute("select * from Admin_Table")
    tempCount=0
    for i in Cursor:
        tempCount+=1
        var0=tempCount
        var1=i[0]
        var2=i[1]
        treev.insert("", 'end', values =(tempCount,var1,var2))
    def Add():
        Add_Window=tk.Tk()
        Add_Window.geometry("293x195+481+237")
        Add_Window.minsize(120, 1)
        Add_Window.maxsize(1284, 701)
        Add_Window.resizable(0,0)
        Add_Window.title("Insertion")
        Add_Window.configure(background="#d9d9d9")

        Admin_ID_Label = tk.Label(Add_Window)
        Admin_ID_Label.place(relx=0.137, rely=0.154, height=41, width=94)
        Admin_ID_Label.configure(background="#d9d9d9")
        Admin_ID_Label.configure(font="-family {Segoe UI} -size 11")
        Admin_ID_Label.configure(foreground="#000000")
        Admin_ID_Label.configure(text='Admin ID')

        Password_Label = tk.Label(Add_Window)
        Password_Label.place(relx=0.137, rely=0.462, height=41, width=94)
        Password_Label.configure(background="#d9d9d9")
        Password_Label.configure(font="-family {Segoe UI} -size 11")
        Password_Label.configure(foreground="#000000")
        Password_Label.configure(text='Password')

        Admin_ID_Entry = tk.Entry(Add_Window)
        Admin_ID_Entry.place(relx=0.546, rely=0.154, height=40, relwidth=0.389)

        Password_Entry = tk.Entry(Add_Window)
        Password_Entry.place(relx=0.546, rely=0.462, height=40, relwidth=0.389)
        
        def Submit():
            try :
                tempCursor=con.cursor()
                tempCursor.execute(f"Insert into Admin_Table Values({int(Admin_ID_Entry.get())},'{Password_Entry.get()}')")
            except Exception as e:
                tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
                print(f"Insert into Admin_Table Values(int({Admin_ID_Entry.get()},'{Password_Entry.get()}')")
                Add_Window.destroy()
                Admin_Table_Window.destroy()
                Admin_Table()
            else:
                tk.messagebox.showinfo('RESULT','YOUR DATA IS SUCCESSFULLY ADDED')
                con.commit()
                Add_Window.destroy()
                Admin_Table_Window.destroy()
                Admin_Table()
                
        Submit_Button = tk.Button(Add_Window,command=Submit)
        Submit_Button.place(relx=0.375, rely=0.77, height=34, width=87)
        Submit_Button.configure(activebackground="#ececec")
        Submit_Button.configure(activeforeground="#000000")
        Submit_Button.configure(background="#d9d9d9")
        Submit_Button.configure(font="-family {Segoe UI} -size 11")
        Submit_Button.configure(foreground="#000000")
        Submit_Button.configure(cursor="hand2")
        Submit_Button.configure(text='Submit')
        
    
    Add_Button = tk.Button(Admin_Table_Window,command=Add)
    Add_Button.place(relx=0.417, rely=0.844, height=44, width=87)
    Add_Button.configure(activebackground="#ececec")
    Add_Button.configure(activeforeground="#000000")
    Add_Button.configure(background="#ffc13b")
    Add_Button.configure(font="-family {Segoe UI} -size 11 -weight bold")
    Add_Button.configure(foreground="#1e3d59")
    Add_Button.configure(text='ADD')
    Add_Button.configure(cursor="hand2")
    
    def Modify():
        
        try:
            selected_item = treev.selection()[0] ## get selected item
            values = tuple(treev.item(selected_item)['values'])
            
        except Exception as e:
            tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
            Admin_Table_Window.destroy()
            Admin_Table()
            
        else:
            Add_Window=tk.Tk()
            Add_Window.geometry("293x174+470+251")
            Add_Window.minsize(120, 1)
            Add_Window.maxsize(1284, 701)
            Add_Window.resizable(0,0)
            Add_Window.title("Modification")
            Add_Window.configure(background="#d9d9d9")

            Password_Label = tk.Label(Add_Window)
            Password_Label.place(relx=0.102, rely=0.287, height=37, width=94)
            Password_Label.configure(background="#d9d9d9")
            Password_Label.configure(font="-family {Segoe UI} -size 11")
            Password_Label.configure(foreground="#000000")
            Password_Label.configure(text='Password')

            Password_Entry = tk.Entry(Add_Window)
            Password_Entry.place(relx=0.546, rely=0.23, height=50, relwidth=0.389)
            Password_Entry.insert(0,values[2])
            
            def Submit():
                try :
                    tempCursor=con.cursor()
                    tempCursor.execute(f"UPDATE Admin_Table SET Password='{Password_Entry.get()}' where Admin_ID={values[1]}")
                except Exception as e:
                    tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
                    Add_Window.destroy()
                    Admin_Table_Window.destroy()
                    Admin_Table()
                else:
                    tk.messagebox.showinfo('RESULT','YOUR DATA IS SUCCESSFULLY MODIFIED')
                    Add_Window.destroy()
                    Admin_Table_Window.destroy()
                    con.commit()
                    Admin_Table()
                
            Submit_Button = tk.Button(Add_Window,command=Submit)
            Submit_Button.place(relx=0.375, rely=0.77, height=34, width=87)
            Submit_Button.configure(activebackground="#ececec")
            Submit_Button.configure(activeforeground="#000000")
            Submit_Button.configure(background="#d9d9d9")
            Submit_Button.configure(font="-family {Segoe UI} -size 11")
            Submit_Button.configure(foreground="#000000")
            Submit_Button.configure(cursor="hand2")
            Submit_Button.configure(text='Submit')


    Modify_Button = tk.Button(Admin_Table_Window,command=Modify)
    Modify_Button.place(relx=0.617, rely=0.844, height=44, width=87)
    Modify_Button.configure(activebackground="#ececec")
    Modify_Button.configure(activeforeground="#000000")
    Modify_Button.configure(background="#ffc13b")
    Modify_Button.configure(font="-family {Segoe UI} -size 11 -weight bold")
    Modify_Button.configure(foreground="#1e3d59")
    Modify_Button.configure(text='MODIFY')
    Modify_Button.configure(cursor="hand2")
    
    def Delete():
        try:
            selected_item = treev.selection()[0] ## get selected item
            values = tuple(treev.item(selected_item)['values'])
            tempCursor=con.cursor()
            tempCursor.execute(f"Delete from Admin_Table where Admin_ID={values[1]}")
            treev.delete(selected_item)
            con.commit()
            
        except Exception as e:
            tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
            Admin_Table_Window.destroy()
            Admin_Table()

    Delete_Button = tk.Button(Admin_Table_Window,command=Delete)
    Delete_Button.place(relx=0.817, rely=0.844, height=44, width=87)
    Delete_Button.configure(activebackground="#ececec")
    Delete_Button.configure(activeforeground="#000000")
    Delete_Button.configure(background="#ffc13b")
    Delete_Button.configure(font="-family {Segoe UI} -size 11 -weight bold")
    Delete_Button.configure(foreground="#1e3d59")
    Delete_Button.configure(text='DELETE')
    Delete_Button.configure(cursor="hand2")

    con.commit()
    
def Theatre():
    Theatre_Window=tk.Tk()
    
    Theatre_Window.geometry("600x450+332+109")
    Theatre_Window.minsize(120, 1)
    Theatre_Window.maxsize(1284, 701)
    Theatre_Window.resizable(0,0)
    Theatre_Window.title("Theatre Table")
    
    treev = ttk.Treeview(Theatre_Window, selectmode ='browse')
    treev.place(relx=0.125,rely=0.254)
    treev["columns"] = ("1", "2", "3", "4", "5")
    
    # Defining heading
    treev['show'] = 'headings'
    treev.column("1", width = 50, anchor ='c')
    treev.column("2", width = 100, anchor ='c')
    treev.column("3", width = 100, anchor ='c')
    treev.column("4", width = 100, anchor ='c')
    treev.column("5", width = 100, anchor ='c')
    treev.heading("1", text ="Sr No.")
    treev.heading("2", text ="Theatre ID")
    treev.heading("3", text ="Theatre Name")
    treev.heading("4", text ="Location")
    treev.heading("5", text ="No of Seats")
    
    Cursor = con.cursor()
    Cursor.execute("select * from Theatre")
    tempCount=0
    for i in Cursor:
        tempCount+=1
        var0=tempCount
        var1=i[0]
        var2=i[1]
        var3=i[2]
        var4=i[3]
        treev.insert("", 'end', values =(var0,var1,var2,var3,var4))
        
    def Add():
        Add_Window=tk.Tk()
        Add_Window.geometry("293x363+481+156")
        Add_Window.minsize(120, 1)
        Add_Window.maxsize(1284, 701)
        Add_Window.resizable(0,0)
        Add_Window.title("Insertion")
        Add_Window.configure(background="#d9d9d9")

        Theatre_ID_Entry = tk.Entry(Add_Window)
        Theatre_ID_Entry.place(relx=0.478, rely=0.091, height=40, relwidth=0.423)
        
        Theatre_Name_Label = tk.Label(Add_Window)
        Theatre_Name_Label.place(relx=0.102, rely=0.303, height=45, width=94)
        Theatre_Name_Label.configure(activebackground="#f9f9f9")
        Theatre_Name_Label.configure(activeforeground="black")
        Theatre_Name_Label.configure(font="-family {Segoe UI} -size 11")
        Theatre_Name_Label.configure(background="#d9d9d9")
        Theatre_Name_Label.configure(foreground="#000000")
        Theatre_Name_Label.configure(text='Theatre Name')

        Location_Label = tk.Label(Add_Window)
        Location_Label.place(relx=0.102, rely=0.515, height=45, width=94)
        Location_Label.configure(activebackground="#f9f9f9")
        Location_Label.configure(activeforeground="black")
        Location_Label.configure(font="-family {Segoe UI} -size 11")
        Location_Label.configure(background="#d9d9d9")
        Location_Label.configure(foreground="#000000")
        Location_Label.configure(text='Location')

        No_Of_Seats_Label = tk.Label(Add_Window)
        No_Of_Seats_Label.place(relx=0.102, rely=0.727, height=45, width=94)
        No_Of_Seats_Label.configure(activebackground="#f9f9f9")
        No_Of_Seats_Label.configure(activeforeground="black")
        No_Of_Seats_Label.configure(font="-family {Segoe UI} -size 11")
        No_Of_Seats_Label.configure(background="#d9d9d9")
        No_Of_Seats_Label.configure(foreground="#000000")
        No_Of_Seats_Label.configure(text='No Of Seats')

        Theatre_Name_Entry = tk.Entry(Add_Window)
        Theatre_Name_Entry.place(relx=0.478, rely=0.303, height=40 , relwidth=0.423)
        
        Location_Entry = tk.Entry(Add_Window)
        Location_Entry.place(relx=0.478, rely=0.515, height=40, relwidth=0.423)
        
        No_Of_Seats_Entry = tk.Entry(Add_Window)
        No_Of_Seats_Entry.place(relx=0.478, rely=0.727, height=40, relwidth=0.423)

        Theatre_ID_Label = tk.Label(Add_Window)
        Theatre_ID_Label.place(relx=0.102, rely=0.091, height=45, width=94)
        Theatre_ID_Label.configure(activebackground="#f9f9f9")
        Theatre_ID_Label.configure(activeforeground="black")
        Theatre_ID_Label.configure(font="-family {Segoe UI} -size 11")
        Theatre_ID_Label.configure(background="#d9d9d9")
        Theatre_ID_Label.configure(foreground="#000000")
        Theatre_ID_Label.configure(text='Theatre ID')
        
        def Submit():
            try :
                tempCursor=con.cursor()
                tempCursor.execute(f"INSERT INTO Theatre Values({int(Theatre_ID_Entry.get())},'{Theatre_Name_Entry.get()}','{Location_Entry.get()}',{int(No_Of_Seats_Entry.get())})")
            except Exception as e:
                tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
                Add_Window.destroy()
                Theatre_Window.destroy()
                Theatre()
            else:
                tk.messagebox.showinfo('RESULT','YOUR DATA IS SUCCESSFULLY ADDED')
                Add_Window.destroy()
                Theatre_Window.destroy()
                con.commit()
                Theatre()

        Submit_Button = tk.Button(Add_Window,command=Submit)
        Submit_Button.place(relx=0.307, rely=0.882, height=34, width=117)
        Submit_Button.configure(activebackground="#ececec")
        Submit_Button.configure(activeforeground="#000000")
        Submit_Button.configure(background="#d9d9d9")
        Submit_Button.configure(cursor="hand2")
        Submit_Button.configure(font="-family {Segoe UI} -size 11")
        Submit_Button.configure(foreground="#000000")
        Submit_Button.configure(text='Submit')

        
    Add_Button = tk.Button(Theatre_Window,command=Add)
    Add_Button.place(relx=0.417, rely=0.844, height=44, width=87)
    Add_Button.configure(activebackground="#ececec")
    Add_Button.configure(activeforeground="#000000")
    Add_Button.configure(background="#ffc13b")
    Add_Button.configure(font="-family {Segoe UI} -size 11 -weight bold")
    Add_Button.configure(foreground="#1e3d59")
    Add_Button.configure(text='ADD')
    Add_Button.configure(cursor="hand2")
    
    def Modify():
        try:
            selected_item = treev.selection()[0]
            values = tuple(treev.item(selected_item)['values'])
            
        except Exception as e:
            tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
            Theatre_Window.destroy()
            Theatre()
            
        else:
            Add_Window=tk.Tk()
            Add_Window.geometry("293x274+481+185")
            Add_Window.minsize(120, 1)
            Add_Window.maxsize(1284, 701)
            Add_Window.resizable(0, 0)
            Add_Window.title("Modification")
            Add_Window.configure(background="#d9d9d9")

            Theatre_Name_Label = tk.Label(Add_Window)
            Theatre_Name_Label.place(relx=0.102, rely=0.182, height=34, width=84)
            Theatre_Name_Label.configure(activebackground="#f9f9f9")
            Theatre_Name_Label.configure(activeforeground="black")
            Theatre_Name_Label.configure(background="#d9d9d9")
            Theatre_Name_Label.configure(foreground="#000000")
            Theatre_Name_Label.configure(text='Theatre Name')

            Location_Label = tk.Label(Add_Window)
            Location_Label.place(relx=0.102, rely=0.401, height=34, width=84)
            Location_Label.configure(activebackground="#f9f9f9")
            Location_Label.configure(activeforeground="black")
            Location_Label.configure(background="#d9d9d9")
            Location_Label.configure(foreground="#000000")
            Location_Label.configure(text='Location')

            No_Of_Seats_Label = tk.Label(Add_Window)
            No_Of_Seats_Label.place(relx=0.102, rely=0.62, height=34, width=84)
            No_Of_Seats_Label.configure(activebackground="#f9f9f9")
            No_Of_Seats_Label.configure(activeforeground="black")
            No_Of_Seats_Label.configure(background="#d9d9d9")
            No_Of_Seats_Label.configure(foreground="#000000")
            No_Of_Seats_Label.configure(text='No Of Seats')

            Theatre_Name_Entry = tk.Entry(Add_Window)
            Theatre_Name_Entry.place(relx=0.478, rely=0.175, height=30, relwidth=0.423)
            Theatre_Name_Entry.insert(0,values[2])

            Location_Entry = tk.Entry(Add_Window)
            Location_Entry.place(relx=0.478, rely=0.401, height=30, relwidth=0.423)
            Location_Entry.insert(0,values[3])
    
            No_Of_Seats_Entry = tk.Entry(Add_Window)
            No_Of_Seats_Entry.place(relx=0.478, rely=0.62, height=30, relwidth=0.423)
            No_Of_Seats_Entry.insert(0,values[4])
            
            def Submit():
                try :
                    tempCursor=con.cursor()
                    tempCursor.execute(f"UPDATE Theatre SET Theatre_Name='{Theatre_Name_Entry.get()}',Location='{Location_Entry.get()}',No_Of_Seats={int(No_Of_Seats_Entry.get())} where Theatre_ID={values[1]}")
                except Exception as e:
                    tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
                    Add_Window.destroy()
                    Theatre_Window.destroy()
                    Theatre()
                else:
                    tk.messagebox.showinfo('RESULT','YOUR DATA IS SUCCESSFULLY MODIFIED')
                    Add_Window.destroy()
                    Theatre_Window.destroy()
                    con.commit()
                    Theatre()
            
            Submit_Button = tk.Button(Add_Window,command=Submit)
            Submit_Button.place(relx=0.307, rely=0.839, height=34, width=117)
            Submit_Button.configure(activebackground="#ececec")
            Submit_Button.configure(activeforeground="#000000")
            Submit_Button.configure(background="#d9d9d9")
            Submit_Button.configure(cursor="hand2")
            Submit_Button.configure(foreground="#000000")
            Submit_Button.configure(text='Submit')

    
    Modify_Button = tk.Button(Theatre_Window,command=Modify)
    Modify_Button.place(relx=0.617, rely=0.844, height=44, width=87)
    Modify_Button.configure(activebackground="#ececec")
    Modify_Button.configure(activeforeground="#000000")
    Modify_Button.configure(background="#ffc13b")
    Modify_Button.configure(font="-family {Segoe UI} -size 11 -weight bold")
    Modify_Button.configure(foreground="#1e3d59")
    Modify_Button.configure(text='MODIFY')
    Modify_Button.configure(cursor="hand2")
    
    def Delete():
        try:
            selected_item = treev.selection()[0] ## get selected item
            values = tuple(treev.item(selected_item)['values'])
            tempCursor=con.cursor()
            tempCursor.execute(f"Delete from Theatre where Theatre_ID={values[1]}")
            treev.delete(selected_item)
            con.commit()
            
        except Exception as e:
            tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
            Theatre_Window.destroy()
            Theatre()
    
    Delete_Button = tk.Button(Theatre_Window,command=Delete)
    Delete_Button.place(relx=0.817, rely=0.844, height=44, width=87)
    Delete_Button.configure(activebackground="#ececec")
    Delete_Button.configure(activeforeground="#000000")
    Delete_Button.configure(background="#ffc13b")
    Delete_Button.configure(font="-family {Segoe UI} -size 11 -weight bold")
    Delete_Button.configure(foreground="#1e3d59")
    Delete_Button.configure(text='DELETE')
    Delete_Button.configure(cursor="hand2")

    con.commit()
    
    
def Customer():
    Customer_Window=tk.Tk()
    
    Customer_Window.geometry("600x450+332+109")
    Customer_Window.minsize(120, 1)
    Customer_Window.maxsize(1284, 701)
    Customer_Window.resizable(0,0)
    Customer_Window.title("Customer Table")
    
    treev = ttk.Treeview(Customer_Window, selectmode ='browse')
    treev.place(relx=0.155,rely=0.254)
    treev["columns"] = ("1", "2", "3", "4")
    
    # Defining heading
    treev['show'] = 'headings'
    treev.column("1", width = 50, anchor ='c')
    treev.column("2", width = 100, anchor ='c')
    treev.column("3", width = 100, anchor ='c')
    treev.column("4", width = 150, anchor ='c')
    treev.heading("1", text ="Sr No.")
    treev.heading("2", text ="Customer ID")
    treev.heading("3", text ="Customer Name")
    treev.heading("4", text ="Customer Password")
    
    Cursor = con.cursor()
    Cursor.execute("select * from Customer")
    tempCount=0
    for i in Cursor:
        tempCount+=1
        var0=tempCount
        var1=i[0]
        var2=i[1]
        var3=i[2]
        treev.insert("", 'end', values =(var0,var1,var2,var3))

    def Add():
        Add_Window=tk.Tk()
        Add_Window.geometry("293x274+481+185")
        Add_Window.minsize(120, 1)
        Add_Window.maxsize(1284, 701)
        Add_Window.resizable(0, 0)
        Add_Window.title("Insertion")
        Add_Window.configure(background="#d9d9d9")

        Customer_ID_Label = tk.Label(Add_Window)
        Customer_ID_Label.place(relx=0.034, rely=0.182, height=34, width=114)
        Customer_ID_Label.configure(activebackground="#f9f9f9")
        Customer_ID_Label.configure(activeforeground="black")
        Customer_ID_Label.configure(background="#d9d9d9")
        Customer_ID_Label.configure(foreground="#000000")
        Customer_ID_Label.configure(text='ID')

        Customer_Name_Label = tk.Label(Add_Window)
        Customer_Name_Label.place(relx=0.034, rely=0.401, height=34, width=114)
        Customer_Name_Label.configure(activebackground="#f9f9f9")
        Customer_Name_Label.configure(activeforeground="black")
        Customer_Name_Label.configure(background="#d9d9d9")
        Customer_Name_Label.configure(foreground="#000000")
        Customer_Name_Label.configure(text='Name')

        Customer_Password_Label = tk.Label(Add_Window)
        Customer_Password_Label.place(relx=0.034, rely=0.62, height=34, width=114)
        Customer_Password_Label.configure(activebackground="#f9f9f9")
        Customer_Password_Label.configure(activeforeground="black")
        Customer_Password_Label.configure(background="#d9d9d9")
        Customer_Password_Label.configure(foreground="#000000")
        Customer_Password_Label.configure(text='Password')

        Customer_ID_Entry = tk.Entry(Add_Window)
        Customer_ID_Entry.place(relx=0.478, rely=0.175, height=30, relwidth=0.423)
        
        Customer_Name_Entry = tk.Entry(Add_Window)
        Customer_Name_Entry.place(relx=0.478, rely=0.401, height=30, relwidth=0.423)

        Customer_Password_Entry = tk.Entry(Add_Window)
        Customer_Password_Entry.place(relx=0.478, rely=0.62, height=30, relwidth=0.423)
        
        def Submit():
            try :
                tempCursor=con.cursor()
                tempCursor.execute(f"INSERT INTO Customer Values({int(Customer_ID_Entry.get())},'{Customer_Name_Entry.get()}','{Customer_Password_Entry.get()}')")
            except Exception as e:
                tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
                Add_Window.destroy()
                Customer_Window.destroy()
                Customer()
            else:
                tk.messagebox.showinfo('RESULT','YOUR DATA IS SUCCESSFULLY ADDED')
                Add_Window.destroy()
                Customer_Window.destroy()
                con.commit()
                Customer()
        
        Submit_Button = tk.Button(Add_Window,command=Submit)
        Submit_Button.place(relx=0.307, rely=0.839, height=34, width=117)
        Submit_Button.configure(activebackground="#ececec")
        Submit_Button.configure(activeforeground="#000000")
        Submit_Button.configure(background="#d9d9d9")
        Submit_Button.configure(cursor="hand2")
        Submit_Button.configure(foreground="#000000")
        Submit_Button.configure(text='Submit')

        
    Add_Button = tk.Button(Customer_Window,command=Add)
    Add_Button.place(relx=0.417, rely=0.844, height=44, width=87)
    Add_Button.configure(activebackground="#ececec")
    Add_Button.configure(activeforeground="#000000")
    Add_Button.configure(background="#ffc13b")
    Add_Button.configure(font="-family {Segoe UI} -size 11 -weight bold")
    Add_Button.configure(foreground="#1e3d59")
    Add_Button.configure(text='ADD')
    Add_Button.configure(cursor="hand2")
    
    def Modify():
        try:
            selected_item = treev.selection()[0]
            values = tuple(treev.item(selected_item)['values'])
            
        except Exception as e:
            tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
            Theatre_Window.destroy()
            Theatre()
            
        else:
            Add_Window=tk.Tk()
            Add_Window.geometry("293x195+481+237")
            Add_Window.minsize(120, 1)
            Add_Window.maxsize(1284, 701)
            Add_Window.resizable(0,0)
            Add_Window.title("Modification")
            Add_Window.configure(background="#d9d9d9")

            Customer_Name_Label = tk.Label(Add_Window)
            Customer_Name_Label.place(relx=0.137, rely=0.154, height=41, width=94)
            Customer_Name_Label.configure(background="#d9d9d9")
            Customer_Name_Label.configure(font="-family {Segoe UI} -size 11")
            Customer_Name_Label.configure(foreground="#000000")
            Customer_Name_Label.configure(text='Name')

            Customer_Password_Label = tk.Label(Add_Window)
            Customer_Password_Label.place(relx=0.137, rely=0.462, height=41, width=94)
            Customer_Password_Label.configure(background="#d9d9d9")
            Customer_Password_Label.configure(font="-family {Segoe UI} -size 11")
            Customer_Password_Label.configure(foreground="#000000")
            Customer_Password_Label.configure(text='Password')

            Customer_Name_Entry = tk.Entry(Add_Window)
            Customer_Name_Entry.place(relx=0.546, rely=0.154, height=40, relwidth=0.389)
            Customer_Name_Entry.insert(0,values[2])

            Customer_Password_Entry = tk.Entry(Add_Window)
            Customer_Password_Entry.place(relx=0.546, rely=0.462, height=40, relwidth=0.389)
            Customer_Password_Entry.insert(0,values[3])
            
            def Submit():
                try :
                    tempCursor=con.cursor()
                    tempCursor.execute(f"UPDATE Customer SET C_Name='{Customer_Name_Entry.get()}',C_Password='{Customer_Password_Entry.get()}' where C_ID={values[1]}")
                except Exception as e:
                    tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
                    Add_Window.destroy()
                    Customer_Window.destroy()
                    Customer()
                else:
                    tk.messagebox.showinfo('RESULT','YOUR DATA IS SUCCESSFULLY MODIFIED')
                    Add_Window.destroy()
                    Customer_Window.destroy()
                    con.commit()
                    Customer()
                
            Submit_Button = tk.Button(Add_Window,command=Submit)
            Submit_Button.place(relx=0.375, rely=0.77, height=34, width=87)
            Submit_Button.configure(activebackground="#ececec")
            Submit_Button.configure(activeforeground="#000000")
            Submit_Button.configure(background="#d9d9d9")
            Submit_Button.configure(font="-family {Segoe UI} -size 11")
            Submit_Button.configure(foreground="#000000")
            Submit_Button.configure(cursor="hand2")
            Submit_Button.configure(text='Submit')

    Modify_Button = tk.Button(Customer_Window,command=Modify)
    Modify_Button.place(relx=0.617, rely=0.844, height=44, width=87)
    Modify_Button.configure(activebackground="#ececec")
    Modify_Button.configure(activeforeground="#000000")
    Modify_Button.configure(background="#ffc13b")
    Modify_Button.configure(font="-family {Segoe UI} -size 11 -weight bold")
    Modify_Button.configure(foreground="#1e3d59")
    Modify_Button.configure(text='MODIFY')
    Modify_Button.configure(cursor="hand2")
    
    def Delete():
        try:
            selected_item = treev.selection()[0] ## get selected item
            values = tuple(treev.item(selected_item)['values'])
            tempCursor=con.cursor()
            tempCursor.execute(f"Delete from Customer where C_ID={values[1]}")
            treev.delete(selected_item)
            con.commit()
            
        except Exception as e:
            tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
            Customer_Window.destroy()
            Customer()
    
    Delete_Button = tk.Button(Customer_Window,command=Delete)
    Delete_Button.place(relx=0.817, rely=0.844, height=44, width=87)
    Delete_Button.configure(activebackground="#ececec")
    Delete_Button.configure(activeforeground="#000000")
    Delete_Button.configure(background="#ffc13b")
    Delete_Button.configure(font="-family {Segoe UI} -size 11 -weight bold")
    Delete_Button.configure(foreground="#1e3d59")
    Delete_Button.configure(text='DELETE')
    Delete_Button.configure(cursor="hand2")

    con.commit()
    
def Customer_Phone():
    Customer_Phone_Window=tk.Tk()
    Customer_Phone_Window.geometry("600x450+332+109")
    Customer_Phone_Window.minsize(120, 1)
    Customer_Phone_Window.maxsize(1284, 701)
    Customer_Phone_Window.resizable(0,0)
    Customer_Phone_Window.title("Customer Phone Table")
    
    treev = ttk.Treeview(Customer_Phone_Window, selectmode ='browse')
    treev.place(relx=0.3,rely=0.3)
    treev["columns"] = ("1", "2", "3")
    
    # Defining heading
    treev['show'] = 'headings'
    treev.column("1", width = 50, anchor ='c')
    treev.column("2", width = 100, anchor ='c')
    treev.column("3", width = 100, anchor ='c')
    treev.heading("1", text ="Sr No.")
    treev.heading("2", text ="Customer ID")
    treev.heading("3", text ="Phone Number")
    
    Cursor = con.cursor()
    Cursor.execute("select * from Customer_Phone")
    tempCount=0
    for i in Cursor:
        tempCount+=1
        var0=tempCount
        var1=i[0]
        var2=i[1]
        treev.insert("", 'end', values =(tempCount,var1,var2))
    
    def Add():
        Add_Window=tk.Tk()
        Add_Window.geometry("293x195+481+237")
        Add_Window.minsize(120, 1)
        Add_Window.maxsize(1284, 701)
        Add_Window.resizable(0,0)
        Add_Window.title("Insertion")
        Add_Window.configure(background="#d9d9d9")

        Customer_ID_Label = tk.Label(Add_Window)
        Customer_ID_Label.place(relx=0.107, rely=0.154, height=41, width=114)
        Customer_ID_Label.configure(background="#d9d9d9")
        Customer_ID_Label.configure(font="-family {Segoe UI} -size 11")
        Customer_ID_Label.configure(foreground="#000000")
        Customer_ID_Label.configure(text='Customer ID')

        Phone_No_Label = tk.Label(Add_Window)
        Phone_No_Label.place(relx=0.107, rely=0.462, height=41, width=114)
        Phone_No_Label.configure(background="#d9d9d9")
        Phone_No_Label.configure(font="-family {Segoe UI} -size 11")
        Phone_No_Label.configure(foreground="#000000")
        Phone_No_Label.configure(text='Phone Number')

        Customer_ID_Entry = tk.Entry(Add_Window)
        Customer_ID_Entry.place(relx=0.546, rely=0.154, height=40, relwidth=0.389)

        Phone_No_Entry = tk.Entry(Add_Window)
        Phone_No_Entry.place(relx=0.546, rely=0.462, height=40, relwidth=0.389)
        
        def Submit():
            try :
                tempCursor=con.cursor()
                tempCursor.execute(f"INSERT INTO Customer_Phone Values({int(Customer_ID_Entry.get())},'{Phone_No_Entry.get()}')")
            except Exception as e:
                tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
                Add_Window.destroy()
                Customer_Phone_Window.destroy()
                Customer_Phone()
            else:
                tk.messagebox.showinfo('RESULT','YOUR DATA IS SUCCESSFULLY ADDED')
                Add_Window.destroy()
                Customer_Phone_Window.destroy()
                con.commit()
                Customer_Phone()
                
        
        Submit_Button = tk.Button(Add_Window,command=Submit)
        Submit_Button.place(relx=0.375, rely=0.769, height=34, width=87)
        Submit_Button.configure(activebackground="#ececec")
        Submit_Button.configure(activeforeground="#000000")
        Submit_Button.configure(background="#d9d9d9")
        Submit_Button.configure(font="-family {Segoe UI} -size 11")
        Submit_Button.configure(foreground="#000000")
        Submit_Button.configure(cursor="hand2")
        Submit_Button.configure(text='Submit')
    
    Add_Button = tk.Button(Customer_Phone_Window,command=Add)
    Add_Button.place(relx=0.617, rely=0.844, height=44, width=87)
    Add_Button.configure(activebackground="#ececec")
    Add_Button.configure(activeforeground="#000000")
    Add_Button.configure(background="#ffc13b")
    Add_Button.configure(font="-family {Segoe UI} -size 11 -weight bold")
    Add_Button.configure(foreground="#1e3d59")
    Add_Button.configure(text='ADD')
    Add_Button.configure(cursor="hand2")
    
    def Delete():
        try:
            selected_item = treev.selection()[0] ## get selected item
            values = tuple(treev.item(selected_item)['values'])
            tempCursor=con.cursor()
            tempCursor.execute(f"Delete from Customer_Phone where C_ID={values[1]} and Phone_No={values[2]}")
            treev.delete(selected_item)
            con.commit()
            
        except Exception as e:
            tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
            Customer_Window.destroy()
            Customer()
    
    Delete_Button = tk.Button(Customer_Phone_Window,command=Delete)
    Delete_Button.place(relx=0.817, rely=0.844, height=44, width=87)
    Delete_Button.configure(activebackground="#ececec")
    Delete_Button.configure(activeforeground="#000000")
    Delete_Button.configure(background="#ffc13b")
    Delete_Button.configure(font="-family {Segoe UI} -size 11 -weight bold")
    Delete_Button.configure(foreground="#1e3d59")
    Delete_Button.configure(text='DELETE')
    Delete_Button.configure(cursor="hand2")

    con.commit()
    
def MovieActors():
    MovieActorsWindow=tk.Tk()
    
    MovieActorsWindow.geometry("600x450+332+109")
    MovieActorsWindow.minsize(120, 1)
    MovieActorsWindow.maxsize(1284, 701)
    MovieActorsWindow.resizable(0,0)
    MovieActorsWindow.title("Movie Actors Table")
    
    treev = ttk.Treeview(MovieActorsWindow, selectmode ='browse')
    treev.place(relx=0.2,rely=0.2)
    treev["columns"] = ("0","1","2")
    
    # Defining heading
    treev['show'] = 'headings'
    treev.column("0", width = 50, anchor ='c')
    treev.column("1", width = 150, anchor ='c')
    treev.column("2", width = 150, anchor ='c')
    treev.heading("0", text ="Sr. No.")
    treev.heading("1", text ="Movie ID")
    treev.heading("2", text ="Actors")


    Cursor = con.cursor()
    Cursor.execute("select * from Movie_Actors")
    tempCount=0
    for i in Cursor:
        tempCount+=1
        var0=tempCount
        var1=i[0]
        var2=i[1]
        treev.insert("", 'end', values =(tempCount,var1,var2))
    def Add():
        Add_Window=tk.Tk()
        Add_Window.geometry("293x195+481+237")
        Add_Window.minsize(120, 1)
        Add_Window.maxsize(1284, 701)
        Add_Window.resizable(0,0)
        Add_Window.title("New Add_Windowlevel")
        Add_Window.configure(background="#d9d9d9")

        Movie_ID_Label = tk.Label(Add_Window)
        Movie_ID_Label.place(relx=0.137, rely=0.154, height=41, width=94)
        Movie_ID_Label.configure(background="#d9d9d9")
        Movie_ID_Label.configure(font="-family {Segoe UI} -size 11")
        Movie_ID_Label.configure(foreground="#000000")
        Movie_ID_Label.configure(text='Movie ID')

        Actor_Label = tk.Label(Add_Window)
        Actor_Label.place(relx=0.137, rely=0.462, height=41, width=94)
        Actor_Label.configure(background="#d9d9d9")
        Actor_Label.configure(font="-family {Segoe UI} -size 11")
        Actor_Label.configure(foreground="#000000")
        Actor_Label.configure(text="Actor's Name")

        Movie_ID_Entry = tk.Entry(Add_Window)
        Movie_ID_Entry.place(relx=0.546, rely=0.154, height=40, relwidth=0.389)

        Actor_Entry = tk.Entry(Add_Window)
        Actor_Entry.place(relx=0.546, rely=0.462, height=40, relwidth=0.389)
        
        def Submit():
            try :
                tempCursor=con.cursor()
                tempCursor.execute(f"INSERT INTO Movie_Actors Values({int(Movie_ID_Entry.get())},'{Actor_Entry.get()}')")
            except Exception as e:
                tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
                Add_Window.destroy()
                MovieActorsWindow.destroy()
                MovieActors()
            else:
                tk.messagebox.showinfo('RESULT','YOUR DATA IS SUCCESSFULLY ADDED')
                Add_Window.destroy()
                MovieActorsWindow.destroy()
                con.commit()
                MovieActors()
        
        Submit_Button = tk.Button(Add_Window,command=Submit)
        Submit_Button.place(relx=0.375, rely=0.769, height=34, width=87)
        Submit_Button.configure(activebackground="#ececec")
        Submit_Button.configure(activeforeground="#000000")
        Submit_Button.configure(background="#d9d9d9")
        Submit_Button.configure(font="-family {Segoe UI} -size 11")
        Submit_Button.configure(foreground="#000000")
        Submit_Button.configure(text='Submit')
        
    
    Add_Button = tk.Button(MovieActorsWindow,command=Add)
    Add_Button.place(relx=0.617, rely=0.844, height=44, width=87)
    Add_Button.configure(activebackground="#ececec")
    Add_Button.configure(activeforeground="#000000")
    Add_Button.configure(background="#ffc13b")
    Add_Button.configure(font="-family {Segoe UI} -size 11 -weight bold")
    Add_Button.configure(foreground="#1e3d59")
    Add_Button.configure(text='ADD')
    Add_Button.configure(cursor="hand2")
    

    def Delete():
        try:
            selected_item = treev.selection()[0] ## get selected item
            values = tuple(treev.item(selected_item)['values'])
            tempCursor=con.cursor()
            tempCursor.execute(f"Delete from Movie_Actors where Movie_ID={values[1]} and Actors='{values[2]}'")
            treev.delete(selected_item)
            con.commit()
            
        except Exception as e:
            tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
            MovieActorsWindow.destroy()
            MovieActors()

    Delete_Button = tk.Button(MovieActorsWindow,command=Delete)
    Delete_Button.place(relx=0.817, rely=0.844, height=44, width=87)
    Delete_Button.configure(activebackground="#ececec")
    Delete_Button.configure(activeforeground="#000000")
    Delete_Button.configure(background="#ffc13b")
    Delete_Button.configure(font="-family {Segoe UI} -size 11 -weight bold")
    Delete_Button.configure(foreground="#1e3d59")
    Delete_Button.configure(text='DELETE')
    Delete_Button.configure(cursor="hand2")
        
    con.commit()
    
def MovieDirectors():
    MovieDirectorsWindow=tk.Tk()
    
    MovieDirectorsWindow.geometry("600x450+332+109")
    MovieDirectorsWindow.minsize(120, 1)
    MovieDirectorsWindow.maxsize(1284, 701)
    MovieDirectorsWindow.resizable(0,0)
    MovieDirectorsWindow.title("Movie Directors")
    
    treev = ttk.Treeview(MovieDirectorsWindow, selectmode ='browse')
    treev.place(relx=0.2,rely=0.25)
    treev["columns"] = ("0","1","2")
    
    # Defining heading
    treev['show'] = 'headings'
    treev.column("0", width = 50, anchor ='c')
    treev.column("1", width = 150, anchor ='c')
    treev.column("2", width = 150, anchor ='c')
    treev.heading("0", text ="Sr No")
    treev.heading("1", text ="Movie ID")
    treev.heading("2", text ="Actors")


    Cursor = con.cursor()
    Cursor.execute("select * from Movie_Directors")
    tempCount=0
    for i in Cursor:
        tempCount+=1
        var0=tempCount
        var1=i[0]
        var2=i[1]
        treev.insert("", 'end', values =(tempCount,var1,var2))
    def Add():
        Add_Window=tk.Tk()
        Add_Window.geometry("293x195+481+237")
        Add_Window.minsize(120, 1)
        Add_Window.maxsize(1284, 701)
        Add_Window.resizable(0,0)
        Add_Window.title("New Add_Windowlevel")
        Add_Window.configure(background="#d9d9d9")

        Movie_ID_Label = tk.Label(Add_Window)
        Movie_ID_Label.place(relx=0.127, rely=0.154, height=41, width=104)
        Movie_ID_Label.configure(background="#d9d9d9")
        Movie_ID_Label.configure(font="-family {Segoe UI} -size 11")
        Movie_ID_Label.configure(foreground="#000000")
        Movie_ID_Label.configure(text='Movie ID')

        Password_Label = tk.Label(Add_Window)
        Password_Label.place(relx=0.127, rely=0.462, height=41, width=104)
        Password_Label.configure(background="#d9d9d9")
        Password_Label.configure(font="-family {Segoe UI} -size 11")
        Password_Label.configure(foreground="#000000")
        Password_Label.configure(text="Director's Name")

        Movie_ID_Entry = tk.Entry(Add_Window)
        Movie_ID_Entry.place(relx=0.546, rely=0.154, height=40, relwidth=0.389)

        Password_Entry = tk.Entry(Add_Window)
        Password_Entry.place(relx=0.546, rely=0.462, height=40, relwidth=0.389)
        
        def Submit():
            try :
                tempCursor=con.cursor()
                tempCursor.execute(f"INSERT INTO Movie_Directors Values({int(Movie_ID_Entry.get())},'{Password_Entry.get()}')")
            except Exception as e:
                tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
                Add_Window.destroy()
                MovieDirectorsWindow.destroy()
                MovieDirectors()
            else:
                tk.messagebox.showinfo('RESULT','YOUR DATA IS SUCCESSFULLY ADDED')
                Add_Window.destroy()
                MovieDirectorsWindow.destroy()
                con.commit()
                MovieDirectors()
        
        Submit_Button = tk.Button(Add_Window,command=Submit)
        Submit_Button.place(relx=0.375, rely=0.769, height=34, width=87)
        Submit_Button.configure(activebackground="#ececec")
        Submit_Button.configure(activeforeground="#000000")
        Submit_Button.configure(background="#d9d9d9")
        Submit_Button.configure(font="-family {Segoe UI} -size 11")
        Submit_Button.configure(foreground="#000000")
        Submit_Button.configure(text='Submit')
        
    
    Add_Button = tk.Button(MovieDirectorsWindow,command=Add)
    Add_Button.place(relx=0.617, rely=0.844, height=44, width=87)
    Add_Button.configure(activebackground="#ececec")
    Add_Button.configure(activeforeground="#000000")
    Add_Button.configure(background="#ffc13b")
    Add_Button.configure(font="-family {Segoe UI} -size 11 -weight bold")
    Add_Button.configure(foreground="#1e3d59")
    Add_Button.configure(text='ADD')
    Add_Button.configure(cursor="hand2")
   
    
    def Delete():
        try:
            selected_item = treev.selection()[0] ## get selected item
            values = tuple(treev.item(selected_item)['values'])
            tempCursor=con.cursor()
            tempCursor.execute(f"Delete from Movie_Directors where Movie_ID={values[1]} and Directors='{values[2]}'")
            treev.delete(selected_item)
            con.commit()
            
        except Exception as e:
            tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
            MovieDirectorsWindow.destroy()
            MovieDirectors()

    Delete_Button = tk.Button(MovieDirectorsWindow,command=Delete)
    Delete_Button.place(relx=0.817, rely=0.844, height=44, width=87)
    Delete_Button.configure(activebackground="#ececec")
    Delete_Button.configure(activeforeground="#000000")
    Delete_Button.configure(background="#ffc13b")
    Delete_Button.configure(font="-family {Segoe UI} -size 11 -weight bold")
    Delete_Button.configure(foreground="#1e3d59")
    Delete_Button.configure(text='DELETE')
    Delete_Button.configure(cursor="hand2")
    
    
def WorksFor():
    worksforWindow=tk.Tk()
    
    worksforWindow.geometry("600x450+332+109")
    worksforWindow.minsize(120, 1)
    worksforWindow.maxsize(1284, 701)
    worksforWindow.resizable(0,0)
    worksforWindow.title("WorksFor")
    
    treev = ttk.Treeview(worksforWindow, selectmode ='browse')
    treev.place(relx=0.2,rely=0.2)
    treev["columns"] = ("0","1","2")
    
    # Defining heading
    treev['show'] = 'headings'
    treev.column("0", width = 50, anchor ='c')
    treev.column("1", width = 150, anchor ='c')
    treev.column("2", width = 150, anchor ='c')
    treev.heading("0", text ="Sr No")
    treev.heading("1", text ="Admin ID")
    treev.heading("2", text ="Theatre ID")
    
    Cursor = con.cursor()
    Cursor.execute("select * from WorkFor")
    tempCount=0
    for i in Cursor:
        tempCount+=1
        var0=tempCount
        var1=i[0]
        var2=i[1]
        treev.insert("", 'end', values =(tempCount,var1,var2))
    def Add():
        Add_Window=tk.Tk()
        Add_Window.geometry("293x195+481+237")
        Add_Window.minsize(120, 1)
        Add_Window.maxsize(1284, 701)
        Add_Window.resizable(0,0)
        Add_Window.title("New Add_Windowlevel")
        Add_Window.configure(background="#d9d9d9")

        Admin_ID_Label = tk.Label(Add_Window)
        Admin_ID_Label.place(relx=0.137, rely=0.154, height=41, width=94)
        Admin_ID_Label.configure(background="#d9d9d9")
        Admin_ID_Label.configure(font="-family {Segoe UI} -size 11")
        Admin_ID_Label.configure(foreground="#000000")
        Admin_ID_Label.configure(text='Admin ID')

        Theatre_ID_Label = tk.Label(Add_Window)
        Theatre_ID_Label.place(relx=0.137, rely=0.462, height=41, width=94)
        Theatre_ID_Label.configure(background="#d9d9d9")
        Theatre_ID_Label.configure(font="-family {Segoe UI} -size 11")
        Theatre_ID_Label.configure(foreground="#000000")
        Theatre_ID_Label.configure(text='Theatre ID')

        Admin_ID_Entry=tk.Entry(Add_Window)
        Admin_ID_Entry.place(relx=0.546, rely=0.154, height=40, relwidth=0.389)

        Theatre_ID_Entry= tk.Entry(Add_Window)
        Theatre_ID_Entry.place(relx=0.546, rely=0.462, height=40, relwidth=0.389)
        
        def Submit():
            try :
                tempCursor=con.cursor()
                tempCursor.execute(f"INSERT INTO WorkFor Values({int(Admin_ID_Entry.get())},{int(Theatre_ID_Entry.get())})")
            except Exception as e:
                tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
                Add_Window.destroy()
                worksforWindow.destroy()
                WorksFor()
            else:
                tk.messagebox.showinfo('RESULT','YOUR DATA IS SUCCESSFULLY ADDED')
                Add_Window.destroy()
                worksforWindow.destroy()
                con.commit()
                worksfor()
        
        Submit_Button = tk.Button(Add_Window,command=Submit)
        Submit_Button.place(relx=0.375, rely=0.769, height=34, width=87)
        Submit_Button.configure(activebackground="#ececec")
        Submit_Button.configure(activeforeground="#000000")
        Submit_Button.configure(background="#d9d9d9")
        Submit_Button.configure(font="-family {Segoe UI} -size 11")
        Submit_Button.configure(foreground="#000000")
        Submit_Button.configure(text='Submit')
        
    
    Add_Button = tk.Button(worksforWindow,command=Add)
    Add_Button.place(relx=0.617, rely=0.844, height=44, width=87)
    Add_Button.configure(activebackground="#ececec")
    Add_Button.configure(activeforeground="#000000")
    Add_Button.configure(background="#ffc13b")
    Add_Button.configure(font="-family {Segoe UI} -size 11 -weight bold")
    Add_Button.configure(foreground="#1e3d59")
    Add_Button.configure(text='ADD')
    Add_Button.configure(cursor="hand2")
   
    
    
    def Delete():
        try:
            selected_item = treev.selection()[0] ## get selected item
            values = tuple(treev.item(selected_item)['values'])
            tempCursor=con.cursor()
            tempCursor.execute(f"Delete from WorkFor where Admin_ID={values[1]} and Theatre_ID={values[2]}")
            treev.delete(selected_item)
            con.commit()
            
        except Exception as e:
            tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
            worksforWindow.destroy()
            worksfor()

    Delete_Button = tk.Button(worksforWindow,command=Delete)
    Delete_Button.place(relx=0.817, rely=0.844, height=44, width=87)
    Delete_Button.configure(activebackground="#ececec")
    Delete_Button.configure(activeforeground="#000000")
    Delete_Button.configure(background="#ffc13b")
    Delete_Button.configure(font="-family {Segoe UI} -size 11 -weight bold")
    Delete_Button.configure(foreground="#1e3d59")
    Delete_Button.configure(text='DELETE')
    Delete_Button.configure(cursor="hand2")
    
def Show():
    ShowWindow=tk.Tk()
    
    ShowWindow.geometry("600x450+332+109")
    ShowWindow.minsize(120, 1)
    ShowWindow.maxsize(1284, 701)
    ShowWindow.resizable(0,0)
    ShowWindow.title("Show")
    
    treev = ttk.Treeview(ShowWindow, selectmode ='browse')
    treev.place(relx=0.04,rely=0.3)
    treev["columns"] = ("0","1","2","3","4","5")
    
    # Defining heading
    treev['show'] = 'headings'
    treev.column("0", width = 50, anchor ='c')
    treev.column("1", width = 65, anchor ='c')
    treev.column("2", width = 150, anchor ='c')
    treev.column("3", width = 150, anchor ='c')
    treev.column("4", width = 100, anchor ='c')
    treev.column("5", width = 65, anchor ='c')
    treev.heading("0", text ="Sr No")
    treev.heading("1", text ="Show ID")
    treev.heading("2", text ="Stating Time")
    treev.heading("3", text ="Ending Time")
    treev.heading("4", text ="Language")
    treev.heading("5", text ="Movie ID")
    
    Cursor = con.cursor()
    Cursor.execute("select * from Show_Movie")
    tempCount=0
    for i in Cursor:
        tempCount+=1
        var0=tempCount
        var1=i[0]
        var2=i[1]
        var3=i[2]
        var4=i[3]
        var5=i[4]
        treev.insert("", 'end', values =(tempCount,var1,var2,var3,var4,var5))
    def Add():
        
        Show_Add_Window=tk.Tk()
        Show_Add_Window.geometry("621x427+335+109")
        Show_Add_Window.minsize(120, 1)
        Show_Add_Window.maxsize(1284, 701)
        Show_Add_Window.resizable(1,  1)
        Show_Add_Window.title("New Show_Add_Windowlevel")
        Show_Add_Window.configure(background="#f3f8e4")
        
        HeadingLabel = tk.Label(Show_Add_Window)
        HeadingLabel.place(relx=0.209, rely=0.07, height=67, width=356)
        HeadingLabel.configure(background="#d9d9d9")
        HeadingLabel.configure(disabledforeground="#a3a3a3")
        HeadingLabel.configure(foreground="#000000")
        HeadingLabel.configure(text='''Add New Movie Show''')
        
        Show_Add_Window.geometry("621x427+335+109")
        Show_Add_Window.minsize(120, 1)
        Show_Add_Window.maxsize(1284, 701)
        Show_Add_Window.resizable(1,  1)
        Show_Add_Window.title("New Show_Add_Windowlevel")
        Show_Add_Window.configure(background="#f3f8e4")

        ShowIDLabel = tk.Label(Show_Add_Window)
        ShowIDLabel.place(relx=0.209, rely=0.281, height=30, width=95)
        ShowIDLabel.configure(background="#d9d9d9")
        ShowIDLabel.configure(disabledforeground="#a3a3a3")
        ShowIDLabel.configure(foreground="#000000")
        ShowIDLabel.configure(text='''Show ID''')

        ShowIDEntry = tk.Entry(Show_Add_Window)
        ShowIDEntry.place(relx=0.37, rely=0.281, height=30, relwidth=0.409)
        ShowIDEntry.configure(background="white")
        ShowIDEntry.configure(disabledforeground="#a3a3a3")
        ShowIDEntry.configure(font="TkFixedFont")
        ShowIDEntry.configure(foreground="#000000")
        ShowIDEntry.configure(insertbackground="black")

        StTimeLabel = tk.Label(Show_Add_Window)
        StTimeLabel.place(relx=0.209, rely=0.375, height=30, width=96)
        StTimeLabel.configure(background="#d9d9d9")
        StTimeLabel.configure(disabledforeground="#a3a3a3")
        StTimeLabel.configure(foreground="#000000")
        StTimeLabel.configure(text='''Stating Time''')

        StTimeEntry = tk.Entry(Show_Add_Window)
        StTimeEntry.place(relx=0.37, rely=0.375, height=30, relwidth=0.409)
        StTimeEntry.configure(background="white")
        StTimeEntry.configure(disabledforeground="#a3a3a3")
        StTimeEntry.configure(font="TkFixedFont")
        StTimeEntry.configure(foreground="#000000")
        StTimeEntry.configure(insertbackground="black")

        EnTimeLabel = tk.Label(Show_Add_Window)
        EnTimeLabel.place(relx=0.209, rely=0.468, height=29, width=95)
        EnTimeLabel.configure(background="#d9d9d9")
        EnTimeLabel.configure(disabledforeground="#a3a3a3")
        EnTimeLabel.configure(foreground="#000000")
        EnTimeLabel.configure(text='''Ending Time''')

        EndTimeEntry = tk.Entry(Show_Add_Window)
        EndTimeEntry.place(relx=0.37, rely=0.468, height=30, relwidth=0.409)

        EndTimeEntry.configure(background="white")
        EndTimeEntry.configure(disabledforeground="#a3a3a3")
        EndTimeEntry.configure(font="TkFixedFont")
        EndTimeEntry.configure(foreground="#000000")
        EndTimeEntry.configure(insertbackground="black")

        LanLabel = tk.Label(Show_Add_Window)
        LanLabel.place(relx=0.209, rely=0.562, height=30, width=95)
        LanLabel.configure(background="#d9d9d9")
        LanLabel.configure(disabledforeground="#a3a3a3")
        LanLabel.configure(foreground="#000000")
        LanLabel.configure(text='''Language''')

        LanEntry = tk.Entry(Show_Add_Window)
        LanEntry.place(relx=0.37, rely=0.562, height=30, relwidth=0.409)
        LanEntry.configure(background="white")
        LanEntry.configure(disabledforeground="#a3a3a3")
        LanEntry.configure(font="TkFixedFont")
        LanEntry.configure(foreground="#000000")
        LanEntry.configure(insertbackground="black")

        MovIDLabel = tk.Label(Show_Add_Window)
        MovIDLabel.place(relx=0.209, rely=0.656, height=29, width=95)
        MovIDLabel.configure(background="#d9d9d9")
        MovIDLabel.configure(cursor="fleur")
        MovIDLabel.configure(disabledforeground="#a3a3a3")
        MovIDLabel.configure(foreground="#000000")
        MovIDLabel.configure(text='''Movie ID''')

        MovieIDEntry = tk.Entry(Show_Add_Window)
        MovieIDEntry.place(relx=0.37, rely=0.656, height=30, relwidth=0.409)

        MovieIDEntry.configure(background="white")
        MovieIDEntry.configure(disabledforeground="#a3a3a3")
        MovieIDEntry.configure(font="TkFixedFont")
        MovieIDEntry.configure(foreground="#000000")
        MovieIDEntry.configure(insertbackground="black")
       
        def Submit():
            try :
                tempCursor=con.cursor()
                tempCursor.execute(f"INSERT INTO Show_movie Values({int(ShowIDEntry.get())},{'StTimeEntry.get()'},{'EndTimeEntry.get()'},{'LanEntry.get()'},{int(MovieIDEntry.get())})")
            except Exception as e:
                tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
                Show_Add_Window.destroy()
                ShowWindow.destroy()
                Show()
            else:
                tk.messagebox.showinfo('RESULT','YOUR DATA IS SUCCESSFULLY ADDED')
                Add_Window.destroy()
                Show_Add_Window.destroy()
                con.commit()
                Show()
        
        Submit_Button = tk.Button(Show_Add_Window,command=Submit)
        Submit_Button.place(relx=0.375, rely=0.769, height=34, width=87)
        Submit_Button.configure(activebackground="#ececec")
        Submit_Button.configure(activeforeground="#000000")
        Submit_Button.configure(background="#d9d9d9")
        Submit_Button.configure(font="-family {Segoe UI} -size 11")
        Submit_Button.configure(foreground="#000000")
        Submit_Button.configure(text='Submit')
        
    
    Add_Button = tk.Button(ShowWindow,command=Add)
    Add_Button.place(relx=0.417, rely=0.844, height=44, width=87)
    Add_Button.configure(activebackground="#ececec")
    Add_Button.configure(activeforeground="#000000")
    Add_Button.configure(background="#ffc13b")
    Add_Button.configure(font="-family {Segoe UI} -size 11 -weight bold")
    Add_Button.configure(foreground="#1e3d59")
    Add_Button.configure(text='ADD')
    Add_Button.configure(cursor="hand2")
   
           
    def Modify():
        Show_Add_Window=tk.Tk()
        Show_Add_Window.geometry("621x427+335+109")
        Show_Add_Window.minsize(120, 1)
        Show_Add_Window.maxsize(1284, 701)
        Show_Add_Window.resizable(1,  1)
        Show_Add_Window.title("New Show_Add_Windowlevel")
        Show_Add_Window.configure(background="#f3f8e4")
        
        HeadingLabel = tk.Label(Show_Add_Window)
        HeadingLabel.place(relx=0.209, rely=0.07, height=67, width=356)
        HeadingLabel.configure(background="#d9d9d9")
        HeadingLabel.configure(disabledforeground="#a3a3a3")
        HeadingLabel.configure(foreground="#000000")
        HeadingLabel.configure(text='''Modify existing Movie Show''')
        
        Show_Add_Window.geometry("621x427+335+109")
        Show_Add_Window.minsize(120, 1)
        Show_Add_Window.maxsize(1284, 701)
        Show_Add_Window.resizable(1,  1)
        Show_Add_Window.title("New Show_Add_Windowlevel")
        Show_Add_Window.configure(background="#f3f8e4")

        ShowIDLabel = tk.Label(Show_Add_Window)
        ShowIDLabel.place(relx=0.209, rely=0.281, height=30, width=95)
        ShowIDLabel.configure(background="#d9d9d9")
        ShowIDLabel.configure(disabledforeground="#a3a3a3")
        ShowIDLabel.configure(foreground="#000000")
        ShowIDLabel.configure(text='''Show ID''')

        ShowIDEntry = tk.Entry(Show_Add_Window)
        ShowIDEntry.place(relx=0.37, rely=0.281, height=30, relwidth=0.409)
        ShowIDEntry.configure(background="white")
        ShowIDEntry.configure(disabledforeground="#a3a3a3")
        ShowIDEntry.configure(font="TkFixedFont")
        ShowIDEntry.configure(foreground="#000000")
        ShowIDEntry.configure(insertbackground="black")

        StTimeLabel = tk.Label(Show_Add_Window)
        StTimeLabel.place(relx=0.209, rely=0.375, height=30, width=96)
        StTimeLabel.configure(background="#d9d9d9")
        StTimeLabel.configure(disabledforeground="#a3a3a3")
        StTimeLabel.configure(foreground="#000000")
        StTimeLabel.configure(text='''Stating Time''')

        StTimeEntry = tk.Entry(Show_Add_Window)
        StTimeEntry.place(relx=0.37, rely=0.375, height=30, relwidth=0.409)
        StTimeEntry.configure(background="white")
        StTimeEntry.configure(disabledforeground="#a3a3a3")
        StTimeEntry.configure(font="TkFixedFont")
        StTimeEntry.configure(foreground="#000000")
        StTimeEntry.configure(insertbackground="black")

        EnTimeLabel = tk.Label(Show_Add_Window)
        EnTimeLabel.place(relx=0.209, rely=0.468, height=29, width=95)
        EnTimeLabel.configure(background="#d9d9d9")
        EnTimeLabel.configure(disabledforeground="#a3a3a3")
        EnTimeLabel.configure(foreground="#000000")
        EnTimeLabel.configure(text='''Ending Time''')

        EndTimeEntry = tk.Entry(Show_Add_Window)
        EndTimeEntry.place(relx=0.37, rely=0.468, height=30, relwidth=0.409)

        EndTimeEntry.configure(background="white")
        EndTimeEntry.configure(disabledforeground="#a3a3a3")
        EndTimeEntry.configure(font="TkFixedFont")
        EndTimeEntry.configure(foreground="#000000")
        EndTimeEntry.configure(insertbackground="black")

        LanLabel = tk.Label(Show_Add_Window)
        LanLabel.place(relx=0.209, rely=0.562, height=30, width=95)
        LanLabel.configure(background="#d9d9d9")
        LanLabel.configure(disabledforeground="#a3a3a3")
        LanLabel.configure(foreground="#000000")
        LanLabel.configure(text='''Language''')

        LanEntry = tk.Entry(Show_Add_Window)
        LanEntry.place(relx=0.37, rely=0.562, height=30, relwidth=0.409)
        LanEntry.configure(background="white")
        LanEntry.configure(disabledforeground="#a3a3a3")
        LanEntry.configure(font="TkFixedFont")
        LanEntry.configure(foreground="#000000")
        LanEntry.configure(insertbackground="black")

        MovIDLabel = tk.Label(Show_Add_Window)
        MovIDLabel.place(relx=0.209, rely=0.656, height=29, width=95)
        MovIDLabel.configure(background="#d9d9d9")
        MovIDLabel.configure(cursor="fleur")
        MovIDLabel.configure(disabledforeground="#a3a3a3")
        MovIDLabel.configure(foreground="#000000")
        MovIDLabel.configure(text='''Movie ID''')

        MovieIDEntry = tk.Entry(Show_Add_Window)
        MovieIDEntry.place(relx=0.37, rely=0.656, height=30, relwidth=0.409)

        MovieIDEntry.configure(background="white")
        MovieIDEntry.configure(disabledforeground="#a3a3a3")
        MovieIDEntry.configure(font="TkFixedFont")
        MovieIDEntry.configure(foreground="#000000")
        MovieIDEntry.configure(insertbackground="black")
       
        def Submit():
            try :
                tempCursor=con.cursor()
                tempCursor.execute(f"UPDATE Show_movie SET Show_ID={int(ShowIDEntry.get())},St_Time='{ StTimeEntry.get()}',End_Time='{EndTimeEntry.get()}',Language='{LanEntry.get()}',Movie_ID={int(MovieIDEntry.get())} where Show_ID={values[1]}")
            except Exception as e:
                tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
                Show_Add_Window.destroy()
                ShowWindow.destroy()
                Show()
            else:
                tk.messagebox.showinfo('RESULT','YOUR DATA IS SUCCESSFULLY ADDED')
                Show_Add_Window.destroy()
                ShowWindow.destroy()
                con.commit()
                Show()
        
        Submit_Button = tk.Button(Show_Add_Window,command=Submit)
        Submit_Button.place(relx=0.375, rely=0.769, height=34, width=87)
        Submit_Button.configure(activebackground="#ececec")
        Submit_Button.configure(activeforeground="#000000")
        Submit_Button.configure(background="#d9d9d9")
        Submit_Button.configure(font="-family {Segoe UI} -size 11")
        Submit_Button.configure(foreground="#000000")
        Submit_Button.configure(text='Submit')
    
    Modify_Button = tk.Button(ShowWindow,command=Modify)
    Modify_Button.place(relx=0.617, rely=0.844, height=44, width=87)
    Modify_Button.configure(activebackground="#ececec")
    Modify_Button.configure(activeforeground="#000000")
    Modify_Button.configure(background="#ffc13b")
    Modify_Button.configure(font="-family {Segoe UI} -size 11 -weight bold")
    Modify_Button.configure(foreground="#1e3d59")
    Modify_Button.configure(text='MODIFY')
    Modify_Button.configure(cursor="hand2")
    
    def Delete():
        try:
            selected_item = treev.selection()[0] ## get selected item
            values = tuple(treev.item(selected_item)['values'])
            tempCursor=con.cursor()
            tempCursor.execute(f"Delete from Show_movie where Show_ID={values[1]}")
            treev.delete(selected_item)
            con.commit()
            
        except Exception as e:
            tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
            ShowWindow.destroy()
            worksfor()

    Delete_Button = tk.Button(ShowWindow,command=Delete)
    Delete_Button.place(relx=0.817, rely=0.844, height=44, width=87)
    Delete_Button.configure(activebackground="#ececec")
    Delete_Button.configure(activeforeground="#000000")
    Delete_Button.configure(background="#ffc13b")
    Delete_Button.configure(font="-family {Segoe UI} -size 11 -weight bold")
    Delete_Button.configure(foreground="#1e3d59")
    Delete_Button.configure(text='DELETE')
    Delete_Button.configure(cursor="hand2")
    
def Movie():
    MovieWindow=tk.Tk()
    
    MovieWindow.geometry("600x450+332+109")
    MovieWindow.minsize(120, 1)
    MovieWindow.maxsize(1284, 701)
    MovieWindow.resizable(0,0)
    MovieWindow.title("Movie")
    
    treev = ttk.Treeview(MovieWindow, selectmode ='browse')
    treev.place(relx=0.08,rely=0.2)
    treev["columns"] = ("0","1","2","3")
    
    # Defining heading
    treev['show'] = 'headings'
    treev.column("0", width = 50, anchor ='c')
    treev.column("1", width = 150, anchor ='c')
    treev.column("2", width = 150, anchor ='c')
    treev.column("3", width = 150, anchor ='c')
    treev.heading("0", text ="Sr No")
    treev.heading("1", text ="Movie ID")
    treev.heading("2", text ="Movie Name")
    treev.heading("3", text ="Release Date")
    Cursor = con.cursor()
    Cursor.execute("select * from Movie")
    tempCount=0
    for i in Cursor:
        tempCount+=1
        var0=tempCount
        var1=i[0]
        var2=i[1]
        var3=str(i[2])[0:10]
        treev.insert("", 'end', values =(tempCount,var1,var2,var3))
    def Add():
        
        Movie_ADD_Window=tk.Tk()
        Movie_ADD_Window.geometry("293x268+481+175")
        Movie_ADD_Window.minsize(120, 1)
        Movie_ADD_Window.maxsize(1284, 701)
        Movie_ADD_Window.resizable(1,  1)
        Movie_ADD_Window.title("Insertion")
        Movie_ADD_Window.configure(background="#d9d9d9")

        Movie_ID_Entry = tk.Entry(Movie_ADD_Window)
        Movie_ID_Entry.place(relx=0.512, rely=0.093, height=40, relwidth=0.389)
        
        Movie_Name_Entry = tk.Entry(Movie_ADD_Window)
        Movie_Name_Entry.place(relx=0.512, rely=0.373, height=40, relwidth=0.389)
       
        RD_Entry = tk.Entry(Movie_ADD_Window)
        RD_Entry.place(relx=0.512, rely=0.634, height=40, relwidth=0.389)

        Movie_ID_Label = tk.Label(Movie_ADD_Window)
        Movie_ID_Label.place(relx=0.068, rely=0.112, height=41, width=114)
        Movie_ID_Label.configure(background="#d9d9d9")
        Movie_ID_Label.configure(disabledforeground="#a3a3a3")
        Movie_ID_Label.configure(font="-family {Segoe UI} -size 11")
        Movie_ID_Label.configure(foreground="#000000")
        Movie_ID_Label.configure(text='Movie ID')

        Movie_Name_Label = tk.Label(Movie_ADD_Window)
        Movie_Name_Label.place(relx=0.068, rely=0.373, height=41, width=114)

        Movie_Name_Label.configure(activebackground="#f9f9f9")
        Movie_Name_Label.configure(activeforeground="black")
        Movie_Name_Label.configure(background="#d9d9d9")
        Movie_Name_Label.configure(font="-family {Segoe UI} -size 11")
        Movie_Name_Label.configure(foreground="#000000")
        Movie_Name_Label.configure(text='Movie Name')

        RD_Label = tk.Label(Movie_ADD_Window)
        RD_Label.place(relx=0.068, rely=0.634, height=41, width=114)
        RD_Label.configure(activebackground="#f9f9f9")
        RD_Label.configure(activeforeground="black")
        RD_Label.configure(background="#d9d9d9")
        RD_Label.configure(font="-family {Segoe UI} -size 11")
        RD_Label.configure(foreground="#000000")
        RD_Label.configure(text='Release Date')

        def Submit():
            try :
                tempCursor=con.cursor()
                tempCursor.execute(f"INSERT INTO Movie Values({int(Movie_ID_Entry.get())},'{Movie_Name_Entry.get()}',TO_DATE('{RD_Entry.get()}','DD.MM.YYYY'))")
            except Exception as e:
                tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
                print(f"INSERT INTO Movie Values({int(Movie_ID_Entry.get())},'{Movie_Name_Entry.get()}',TO_DATE('{RD_Entry.get()}'),'DD.MM.YYYY'))")
                Movie_ADD_Window.destroy()
                MovieWindow.destroy()
                Movie()
            else:
                tk.messagebox.showinfo('RESULT','YOUR DATA IS SUCCESSFULLY ADDED')
                Movie_ADD_Window.destroy()
                MovieWindow.destroy()
                con.commit()
                Movie()
        
        Submit_Button = tk.Button(Movie_ADD_Window,command=Submit)
        Submit_Button.place(relx=0.341, rely=0.821, height=34, width=87)
        Submit_Button.configure(activebackground="#ececec")
        Submit_Button.configure(activeforeground="#000000")
        Submit_Button.configure(background="#d9d9d9")
        Submit_Button.configure(font="-family {Segoe UI} -size 11")
        Submit_Button.configure(foreground="#000000")
        Submit_Button.configure(cursor="hand2")
        Submit_Button.configure(text='Submit')
    
    Add_Button = tk.Button(MovieWindow,command=Add)
    Add_Button.place(relx=0.417, rely=0.844, height=44, width=87)
    Add_Button.configure(activebackground="#ececec")
    Add_Button.configure(activeforeground="#000000")
    Add_Button.configure(background="#ffc13b")
    Add_Button.configure(font="-family {Segoe UI} -size 11 -weight bold")
    Add_Button.configure(foreground="#1e3d59")
    Add_Button.configure(text='ADD')
    Add_Button.configure(cursor="hand2")
   
    def Modify():
        
        try:
            selected_item = treev.selection()[0] ## get selected item
            values = tuple(treev.item(selected_item)['values'])
            
        except Exception as e:
            tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
            MovieWindow.destroy()
            Movie()
            
        else:
            Add_Window=tk.Tk()
            Add_Window.geometry("293x195+481+237")
            Add_Window.minsize(120, 1)
            Add_Window.maxsize(1284, 701)
            Add_Window.resizable(0,0)
            Add_Window.title("Insertion")
            Add_Window.configure(background="#d9d9d9")

            Movie_Name_Label = tk.Label(Add_Window)
            Movie_Name_Label.place(relx=0.107, rely=0.154, height=41, width=114)
            Movie_Name_Label.configure(background="#d9d9d9")
            Movie_Name_Label.configure(font="-family {Segoe UI} -size 11")
            Movie_Name_Label.configure(foreground="#000000")
            Movie_Name_Label.configure(text='Movie Name')

            Release_Date_Label = tk.Label(Add_Window)
            Release_Date_Label.place(relx=0.107, rely=0.462, height=41, width=114)
            Release_Date_Label.configure(background="#d9d9d9")
            Release_Date_Label.configure(font="-family {Segoe UI} -size 11")
            Release_Date_Label.configure(foreground="#000000")
            Release_Date_Label.configure(text='Release Date')

            Movie_Name_Entry = tk.Entry(Add_Window)
            Movie_Name_Entry.place(relx=0.546, rely=0.154, height=40, relwidth=0.389)
            Movie_Name_Entry.insert(0,values[2])

            RD_Entry = tk.Entry(Add_Window)
            RD_Entry.place(relx=0.546, rely=0.462, height=40, relwidth=0.389)
            RD_Entry.insert(0,values[3])

            def Submit():
                try :
                    tempCursor=con.cursor()
                    tempCursor.execute(f"UPDATE Movie SET Movie_Name='{Movie_Name_Entry.get()}', Release_Date=TO_DATE('{RD_Entry.get()} 00:00:00','YYYY.MM.DD HH24:MI:SS') where Movie_ID={values[1]}")
                except Exception as e:
                    tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
                    print(f"UPDATE Movie SET Movie_Name='{Movie_Name_Entry.get()}', Release_Date=TO_DATE('{RD_Entry.get()} 00:00:00','YYYY.MM.DD HH24:MI:SS') where Movie_ID={values[1]}")
                    Movie_ADD_Window.destroy()
                    MovieWindow.destroy()
                    Movie()
                else:
                    tk.messagebox.showinfo('RESULT','YOUR DATA IS SUCCESSFULLY ADDED')
                    Movie_ADD_Window.destroy()
                    MovieWindow.destroy()
                    con.commit()
                    Movie()

            Submit_Button = tk.Button(Add_Window,command=Submit)
            Submit_Button.place(relx=0.375, rely=0.769, height=34, width=87)
            Submit_Button.configure(activebackground="#ececec")
            Submit_Button.configure(activeforeground="#000000")
            Submit_Button.configure(background="#d9d9d9")
            Submit_Button.configure(font="-family {Segoe UI} -size 11")
            Submit_Button.configure(foreground="#000000")
            Submit_Button.configure(cursor="hand2")
            Submit_Button.configure(text='Submit')

    Modify_Button = tk.Button(MovieWindow,command=Modify)
    Modify_Button.place(relx=0.617, rely=0.844, height=44, width=87)
    Modify_Button.configure(activebackground="#ececec")
    Modify_Button.configure(activeforeground="#000000")
    Modify_Button.configure(background="#ffc13b")
    Modify_Button.configure(font="-family {Segoe UI} -size 11 -weight bold")
    Modify_Button.configure(foreground="#1e3d59")
    Modify_Button.configure(text='MODIFY')
    Modify_Button.configure(cursor="hand2")
    
    def Delete():
        try:
            selected_item = treev.selection()[0] ## get selected item
            values = tuple(treev.item(selected_item)['values'])
            tempCursor=con.cursor()
            tempCursor.execute(f"Delete from Movie where Movie_ID={values[1]}")
            treev.delete(selected_item)
            con.commit()
            
        except Exception as e:
            tk.messagebox.showinfo('ERROR','ERROR !! \n'+str(e))
            MovieWindow.destroy()
            Movie()

    Delete_Button = tk.Button(MovieWindow,command=Delete)
    Delete_Button.place(relx=0.817, rely=0.844, height=44, width=87)
    Delete_Button.configure(activebackground="#ececec")
    Delete_Button.configure(activeforeground="#000000")
    Delete_Button.configure(background="#ffc13b")
    Delete_Button.configure(font="-family {Segoe UI} -size 11 -weight bold")
    Delete_Button.configure(foreground="#1e3d59")
    Delete_Button.configure(text='DELETE')
    Delete_Button.configure(cursor="hand2")
    
    
top=tk.Tk()

top.geometry("600x450+332+109")
top.minsize(120, 1)
top.maxsize(1284, 701)
top.resizable(0,0)
top.title("New Toplevel")
top.configure(background="#1e3d59")

Admin_Table_Button = tk.Button(top,command=Admin_Table)
Admin_Table_Button.place(relx=0.15, rely=0.244, height=44, width=177)
Admin_Table_Button.configure(activebackground="#ececec")
Admin_Table_Button.configure(activeforeground="#000000")
Admin_Table_Button.configure(background="#ffc13b")
Admin_Table_Button.configure(cursor="hand2")
Admin_Table_Button.configure(disabledforeground="#a3a3a3")
Admin_Table_Button.configure(font="-family {Segoe UI} -size 14 -weight bold")
Admin_Table_Button.configure(foreground="#1e3d59")
Admin_Table_Button.configure(highlightbackground="#d9d9d9")
Admin_Table_Button.configure(highlightcolor="black")
Admin_Table_Button.configure(pady="0")
Admin_Table_Button.configure(text='''Admin''')


Movie_Actors_Button = tk.Button(top,command=MovieActors)
Movie_Actors_Button.place(relx=0.567, rely=0.244, height=44, width=177)
Movie_Actors_Button.configure(activebackground="#ececec")
Movie_Actors_Button.configure(activeforeground="#000000")
Movie_Actors_Button.configure(background="#ffc13b")
Movie_Actors_Button.configure(cursor="hand2")
Movie_Actors_Button.configure(disabledforeground="#a3a3a3")
Movie_Actors_Button.configure(font="-family {Segoe UI} -size 14 -weight bold")
Movie_Actors_Button.configure(foreground="#1e3d59")
Movie_Actors_Button.configure(highlightbackground="#d9d9d9")
Movie_Actors_Button.configure(highlightcolor="black")
Movie_Actors_Button.configure(pady="0")
Movie_Actors_Button.configure(text='''Movie Actors''')

Theatre_Button = tk.Button(top,command=Theatre)
Theatre_Button.place(relx=0.15, rely=0.4, height=44, width=177)
Theatre_Button.configure(activebackground="#ececec")
Theatre_Button.configure(activeforeground="#000000")
Theatre_Button.configure(background="#ffc13b")
Theatre_Button.configure(cursor="hand2")
Theatre_Button.configure(disabledforeground="#a3a3a3")
Theatre_Button.configure(font="-family {Segoe UI} -size 14 -weight bold")
Theatre_Button.configure(foreground="#1e3d59")
Theatre_Button.configure(highlightbackground="#d9d9d9")
Theatre_Button.configure(highlightcolor="black")
Theatre_Button.configure(pady="0")
Theatre_Button.configure(text='''Theatre''')

Movie_Directors_Button = tk.Button(top,command=MovieDirectors)
Movie_Directors_Button.place(relx=0.567, rely=0.4, height=44, width=177)
Movie_Directors_Button.configure(activebackground="#ececec")
Movie_Directors_Button.configure(activeforeground="#000000")
Movie_Directors_Button.configure(background="#ffc13b")
Movie_Directors_Button.configure(cursor="hand2")
Movie_Directors_Button.configure(disabledforeground="#a3a3a3")
Movie_Directors_Button.configure(font="-family {Segoe UI} -size 14 -weight bold")
Movie_Directors_Button.configure(foreground="#1e3d59")
Movie_Directors_Button.configure(highlightbackground="#d9d9d9")
Movie_Directors_Button.configure(highlightcolor="black")
Movie_Directors_Button.configure(pady="0")
Movie_Directors_Button.configure(text='''Movie Directors''')

Work_For_Button = tk.Button(top,command=WorksFor)
Work_For_Button.place(relx=0.567, rely=0.556, height=44, width=177)
Work_For_Button.configure(activebackground="#ececec")
Work_For_Button.configure(activeforeground="#000000")
Work_For_Button.configure(background="#ffc13b")
Work_For_Button.configure(cursor="hand2")
Work_For_Button.configure(disabledforeground="#a3a3a3")
Work_For_Button.configure(font="-family {Segoe UI} -size 14 -weight bold")
Work_For_Button.configure(foreground="#1e3d59")
Work_For_Button.configure(highlightbackground="#d9d9d9")
Work_For_Button.configure(highlightcolor="black")
Work_For_Button.configure(pady="0")
Work_For_Button.configure(text='Work For')

Show_Movie_Button = tk.Button(top,command=Show)
Show_Movie_Button.place(relx=0.567, rely=0.711, height=44, width=177)
Show_Movie_Button.configure(activebackground="#ececec")
Show_Movie_Button.configure(activeforeground="#000000")
Show_Movie_Button.configure(background="#ffc13b")
Show_Movie_Button.configure(cursor="hand2")
Show_Movie_Button.configure(disabledforeground="#a3a3a3")
Show_Movie_Button.configure(font="-family {Segoe UI} -size 14 -weight bold")
Show_Movie_Button.configure(foreground="#1e3d59")
Show_Movie_Button.configure(highlightbackground="#d9d9d9")
Show_Movie_Button.configure(highlightcolor="black")
Show_Movie_Button.configure(pady="0")
Show_Movie_Button.configure(text='''Show Movie''')

Customer_Button = tk.Button(top,command=Customer)
Customer_Button.place(relx=0.15, rely=0.556, height=44, width=177)
Customer_Button.configure(activebackground="#ececec")
Customer_Button.configure(activeforeground="#000000")
Customer_Button.configure(background="#ffc13b")
Customer_Button.configure(cursor="hand2")
Customer_Button.configure(disabledforeground="#a3a3a3")
Customer_Button.configure(font="-family {Segoe UI} -size 14 -weight bold")
Customer_Button.configure(foreground="#1e3d59")
Customer_Button.configure(highlightbackground="#d9d9d9")
Customer_Button.configure(highlightcolor="black")
Customer_Button.configure(pady="0")
Customer_Button.configure(text='''Customer''')

Customer_Phone_Button = tk.Button(top,command=Customer_Phone)
Customer_Phone_Button.place(relx=0.15, rely=0.711, height=44, width=177)
Customer_Phone_Button.configure(activebackground="#ececec")
Customer_Phone_Button.configure(activeforeground="#000000")
Customer_Phone_Button.configure(background="#ffc13b")
Customer_Phone_Button.configure(cursor="hand2")
Customer_Phone_Button.configure(disabledforeground="#a3a3a3")
Customer_Phone_Button.configure(font="-family {Segoe UI} -size 14 -weight bold")
Customer_Phone_Button.configure(foreground="#1e3d59")
Customer_Phone_Button.configure(highlightbackground="#d9d9d9")
Customer_Phone_Button.configure(highlightcolor="black")
Customer_Phone_Button.configure(pady="0")
Customer_Phone_Button.configure(text='''Customer_Phone''')

Tickets_Button = tk.Button(top)
Tickets_Button.place(relx=0.567, rely=0.867, height=44, width=177)
Tickets_Button.configure(activebackground="#ececec")
Tickets_Button.configure(activeforeground="#000000")
Tickets_Button.configure(background="#ffc13b")
Tickets_Button.configure(cursor="hand2")
Tickets_Button.configure(disabledforeground="#1e3d59")
Tickets_Button.configure(font="-family {Segoe UI} -size 14 -weight bold")
Tickets_Button.configure(foreground="#1e3d59")
Tickets_Button.configure(highlightbackground="#d9d9d9")
Tickets_Button.configure(highlightcolor="black")
Tickets_Button.configure(pady="0")
Tickets_Button.configure(text='''Tickets''')

Movie_Button = tk.Button(top,command=Movie)
Movie_Button.place(relx=0.15, rely=0.867, height=44, width=177)
Movie_Button.configure(activebackground="#ececec")
Movie_Button.configure(activeforeground="#000000")
Movie_Button.configure(background="#ffc13b")
Movie_Button.configure(cursor="hand2")
Movie_Button.configure(disabledforeground="#a3a3a3")
Movie_Button.configure(font="-family {Segoe UI} -size 14 -weight bold")
Movie_Button.configure(foreground="#1e3d59")
Movie_Button.configure(highlightbackground="#d9d9d9")
Movie_Button.configure(highlightcolor="black")
Movie_Button.configure(pady="0")
Movie_Button.configure(text='''Movie''')

Heading = tk.Label(top)
Heading.place(relx=0.15, rely=0.044, height=61, width=424)
Heading.configure(background="#1e3d59")
Heading.configure(disabledforeground="#a3a3a3")
Heading.configure(font="-family {Segoe UI} -size 24 -weight bold")
Heading.configure(foreground="#ffc13b")
Heading.configure(text='''Cinema Booking System''')

top.mainloop()


