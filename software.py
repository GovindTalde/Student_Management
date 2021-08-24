from tkinter import *
import time
from tkinter import Toplevel
from tkinter import messagebox
from tkinter.ttk import Treeview
import random
import sqlite3
import time
from tkinter import ttk, filedialog
import pandas

def addstudent():
    def submitadd():
        iD = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        ####DATABASE PROBLEM SOLVE@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2@@@@@@@@@2
        iD = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")

        conn = sqlite3.connect("open.db")
        c = conn.cursor()
        many_peoples = [
            (iD,name,mobile,email,address,gender,dob,addeddate,addedtime)
        ]
        c.executemany("INSERT INTO load VALUES(?,?,?,?,?,?,?,?,?)", many_peoples)
        c.execute("SELECT * FROM load")
        datas = c.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in  datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)
        conn.commit()
        conn.close()
        addroot.destroy()
        ####DATABASE PROBLEM SOLVE@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2@@@@@@@@@2

    addroot = Toplevel()
    addroot.grab_set()
    addroot.geometry('530x490+220+220')
    addroot.title('ADD student')
    addroot.config(bg='pale green')
    addroot.resizable(False, False)
    #--------------add student labels --------------------------
    idlabel = Label(addroot, text='Enter ID',bg='pale green',bd=0, font=('times', 20, 'bold'), relief=GROOVE,width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(addroot, text='Enter Name', bg='pale green',bd=0,font=('times', 20, 'bold'), relief=GROOVE,width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(addroot, text='Enter Mobile',bg='pale green',bd=0, font=('times', 20, 'bold'), relief=GROOVE,width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(addroot, text='Enter Email',bg='pale green',bd=0, font=('times', 20, 'bold'), relief=GROOVE,width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(addroot, text='Enter address',bg='pale green',bd=0, font=('times', 20, 'bold'), relief=GROOVE,width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(addroot, text='Enter Gender',bg='pale green',bd=0, font=('times', 20, 'bold'), relief=GROOVE,width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(addroot, text='Enter DOB',bg='pale green',bd=0, font=('times', 20, 'bold'), relief=GROOVE,width=12, anchor='w')
    doblabel.place(x=10, y=370)

    #---------------------------------------add student entry---------------------------------
    idval= StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    genderval = StringVar()
    addressval = StringVar()
    dobval = StringVar()


    identry = Entry(addroot, font=('roman',15, 'bold'), bd=3, textvariable=idval)
    identry.place(x=200, y=10)

    nameentry = Entry(addroot, font=('roman',15, 'bold'), bd=3, textvariable=nameval)
    nameentry.place(x=200, y=70)

    mobileentry = Entry(addroot, font=('roman',15, 'bold'), bd=3, textvariable=mobileval)
    mobileentry.place(x=200, y=130)

    emailentry = Entry(addroot, font=('roman',15, 'bold'), bd=3, textvariable=emailval)
    emailentry.place(x=200, y=190)

    addressentry = Entry(addroot, font=('roman',15, 'bold'), bd=3, textvariable=addressval)
    addressentry.place(x=200, y=250)

    genderentry = Entry(addroot, font=('roman',15, 'bold'), bd=3, textvariable=genderval)
    genderentry.place(x=200, y=310)

    dobentry = Entry(addroot, font=('roman',15, 'bold'), bd=3, textvariable=dobval)
    dobentry.place(x=200, y=370)

    #--------------add btn---------------------
    submitbtn = Button(addroot, text='ADD STUDENT', font=('roman',15,'bold'), width=14, bd=5,activebackground="green", activeforeground="white", command=submitadd)
    submitbtn.place(x=150, y=425)

    addroot.mainloop()

def searchstudent():
    def search():
        iD = idval.get()
        nam = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        if(nam != ''):
            conn = sqlite3.connect("open.db")
            c = conn.cursor()
            c.execute('SELECT * FROM load WHERE name=?',(nam,))
            datas = c.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)            
            conn.commit()
            conn.close()
        elif(iD != ''):
            conn = sqlite3.connect("open.db")
            c = conn.cursor()
            c.execute('SELECT * FROM load WHERE id=?',(iD,))
            datas = c.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)            
            conn.commit()
            conn.close()

        elif(mobile != ''):
            conn = sqlite3.connect("open.db")
            c = conn.cursor()
            c.execute('SELECT * FROM load WHERE mobile=?',(mobile,))
            datas = c.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)            
            conn.commit()
            conn.close()

        elif(email != ''):
            conn = sqlite3.connect("open.db")
            c = conn.cursor()
            c.execute('SELECT * FROM load WHERE email=?',(email,))
            datas = c.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)            
            conn.commit()
            conn.close()

        elif(address != ''):
            conn = sqlite3.connect("open.db")
            c = conn.cursor()
            c.execute('SELECT * FROM load WHERE address=?',(address,))
            datas = c.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)            
            conn.commit()
            conn.close()
    srearchroot = Toplevel()
    srearchroot.grab_set()
    srearchroot.geometry('530x550+220+220')
    srearchroot.title('SEARCH student')
    srearchroot.config(bg='pale green')
    srearchroot.resizable(False, False)
    #--------------add student labels --------------------------
    idlabel = Label(srearchroot, text='Enter ID',bg='pale green',bd=0, font=('times', 20, 'bold'), relief=GROOVE,width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(srearchroot, text='Enter Name', bg='pale green',bd=0,font=('times', 20, 'bold'), relief=GROOVE,width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(srearchroot, text='Enter Mobile',bg='pale green',bd=0, font=('times', 20, 'bold'), relief=GROOVE,width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(srearchroot, text='Enter Email',bg='pale green',bd=0, font=('times', 20, 'bold'), relief=GROOVE,width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(srearchroot, text='Enter address',bg='pale green',bd=0, font=('times', 20, 'bold'), relief=GROOVE,width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(srearchroot, text='Enter Gender',bg='pale green',bd=0, font=('times', 20, 'bold'), relief=GROOVE,width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(srearchroot, text='Enter DOB',bg='pale green',bd=0, font=('times', 20, 'bold'), relief=GROOVE,width=12, anchor='w')
    doblabel.place(x=10, y=370)

    datelabel = Label(srearchroot, text='Enter Date',bg='pale green',bd=0, font=('times', 20, 'bold'), relief=GROOVE,width=12, anchor='w')
    datelabel.place(x=10, y=430)

    #---------------------------------------add student entry---------------------------------
    idval= StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    genderval = StringVar()
    addressval = StringVar()
    dobval = StringVar()
    dateval = StringVar()


    identry = Entry(srearchroot, font=('roman',15, 'bold'), bd=3, textvariable=idval)
    identry.place(x=200, y=10)

    nameentry = Entry(srearchroot, font=('roman',15, 'bold'), bd=3, textvariable=nameval)
    nameentry.place(x=200, y=70)

    mobileentry = Entry(srearchroot, font=('roman',15, 'bold'), bd=3, textvariable=mobileval)
    mobileentry.place(x=200, y=130)

    emailentry = Entry(srearchroot, font=('roman',15, 'bold'), bd=3, textvariable=emailval)
    emailentry.place(x=200, y=190)

    addressentry = Entry(srearchroot, font=('roman',15, 'bold'), bd=3, textvariable=addressval)
    addressentry.place(x=200, y=250)

    genderentry = Entry(srearchroot, font=('roman',15, 'bold'), bd=3, textvariable=genderval)
    genderentry.place(x=200, y=310)

    dobentry = Entry(srearchroot, font=('roman',15, 'bold'), bd=3, textvariable=dobval)
    dobentry.place(x=200, y=370)

    dateentry = Entry(srearchroot, font=('roman',15, 'bold'), bd=3, textvariable=dateval)
    dateentry.place(x=200, y=430)

    #--------------add btn---------------------
    submitbtn = Button(srearchroot, text='SEARCH', font=('roman',15,'bold'), width=14, bd=5,activebackground="green", activeforeground="white", command=search)
    submitbtn.place(x=150, y=490)

    srearchroot.mainloop()

def deletestudent():
    def delete():
        dele = deleteval.get()
        conn = sqlite3.connect("open.db")
        c = conn.cursor()
        c.executemany("DELETE FROM load WHERE id = ?",(dele))
        conn.commit()
        conn.close()
        deleteroot.destroy()
        conn = sqlite3.connect("open.db")
        c = conn.cursor()
        c.execute("SELECT * FROM load")
        c.execute("SELECT * FROM load ORDER BY id")
        datas = c.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in  datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)
        conn.commit()
        conn.close()

    deleteroot = Toplevel()
    deleteroot.grab_set()
    deleteroot.geometry('530x230+220+160')
    deleteroot.title('DELETE student')
    deleteroot.config(bg='pale green')
    deleteroot.resizable(False, False)
    deleteval = StringVar()

    warn = Label(deleteroot, text='This will delete student with given ID permentely...',bg='pale green',bd=0,fg="red", font=('times', 14, 'bold'), relief=GROOVE, anchor='w')
    warn.place(x=10, y=10)

    idlabel = Label(deleteroot, text='Enter ID',bg='pale green',bd=0, font=('times', 20, 'bold'), relief=GROOVE,width=12, anchor='w')
    idlabel.place(x=10, y=60)

    deleteid = Entry(deleteroot, font=('roman',15, 'bold'), bd=3, textvariable=deleteval)
    deleteid.place(x=200, y=60)
    submitbtn = Button(deleteroot, text='DELETE', font=('roman',15,'bold'), width=14, bd=5,activebackground="green", activeforeground="white", command=delete)
    submitbtn.place(x=150, y=150)

def updatestudent():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()

        conn = sqlite3.connect("open.db")
        c = conn.cursor()
        strr = 'UPDATE load SET name=?,mobile=?,email=?,address=?,gender=?,dob=?,date=?,time=? where id=?'
        c.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        strr = 'SELECT * FROM load'
        c.execute(strr)
        datas = c.fetchall()
        conn.commit()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)

        updateroot.destroy()


    updateroot = Toplevel()
    updateroot.grab_set()
    updateroot.geometry('530x610+220+160')
    updateroot.title('UPDATE student')
    updateroot.config(bg='pale green')
    updateroot.resizable(False, False)
    #--------------add student labels --------------------------
    idlabel = Label(updateroot, text='Enter ID',bg='pale green',bd=0, font=('times', 20, 'bold'), relief=GROOVE,width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(updateroot, text='Enter Name', bg='pale green',bd=0,font=('times', 20, 'bold'), relief=GROOVE,width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(updateroot, text='Enter Mobile',bg='pale green',bd=0, font=('times', 20, 'bold'), relief=GROOVE,width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(updateroot, text='Enter Email',bg='pale green',bd=0, font=('times', 20, 'bold'), relief=GROOVE,width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(updateroot, text='Enter address',bg='pale green',bd=0, font=('times', 20, 'bold'), relief=GROOVE,width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(updateroot, text='Enter Gender',bg='pale green',bd=0, font=('times', 20, 'bold'), relief=GROOVE,width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(updateroot, text='Enter DOB',bg='pale green',bd=0, font=('times', 20, 'bold'), relief=GROOVE,width=12, anchor='w')
    doblabel.place(x=10, y=370)

    datelabel = Label(updateroot, text='Enter Date',bg='pale green',bd=0, font=('times', 20, 'bold'), relief=GROOVE,width=12, anchor='w')
    datelabel.place(x=10, y=430)

    timelabel = Label(updateroot, text='Enter time',bg='pale green',bd=0, font=('times', 20, 'bold'), relief=GROOVE,width=12, anchor='w')
    timelabel.place(x=10, y=490)

    #---------------------------------------add student entry---------------------------------
    idval= StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    genderval = StringVar()
    addressval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()


    identry = Entry(updateroot, font=('roman',15, 'bold'), bd=3, textvariable=idval)
    identry.place(x=200, y=10)

    nameentry = Entry(updateroot, font=('roman',15, 'bold'), bd=3, textvariable=nameval)
    nameentry.place(x=200, y=70)

    mobileentry = Entry(updateroot, font=('roman',15, 'bold'), bd=3, textvariable=mobileval)
    mobileentry.place(x=200, y=130)

    emailentry = Entry(updateroot, font=('roman',15, 'bold'), bd=3, textvariable=emailval)
    emailentry.place(x=200, y=190)

    addressentry = Entry(updateroot, font=('roman',15, 'bold'), bd=3, textvariable=addressval)
    addressentry.place(x=200, y=250)

    genderentry = Entry(updateroot, font=('roman',15, 'bold'), bd=3, textvariable=genderval)
    genderentry.place(x=200, y=310)

    dobentry = Entry(updateroot, font=('roman',15, 'bold'), bd=3, textvariable=dobval)
    dobentry.place(x=200, y=370)

    dateentry = Entry(updateroot, font=('roman',15, 'bold'), bd=3, textvariable=dateval)
    dateentry.place(x=200, y=430)

    timeentry = Entry(updateroot, font=('roman',15, 'bold'), bd=3, textvariable=timeval)
    timeentry.place(x=200, y=490)

    #--------------add btn---------------------
    submitbtn = Button(updateroot, text='UPDATE', font=('roman',15,'bold'), width=14, bd=5,activebackground="green", activeforeground="white", command=update)
    submitbtn.place(x=150, y=550)

    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])


    updateroot.mainloop()


def showstudent():
    pass

def exporttudent():
    ff = filedialog.asksaveasfilename()
    gg = studenttable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studenttable.item(i)
        pp = content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),
        dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd = ['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time']
    df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notifications', 'Student data is Saved {}'.format(paths))



ss = 'Black Pearl Softwares'


colors = ['red', 'green', 'blue']


def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text = 'Date :'+date_string+'\n'+'Time :'+time_string)
    clock.after(20,tick)

def login():
    def tick():
        time_string = time.strftime("%H:%M:%S")
        date_string = time.strftime("%d/%m/%Y")
        clock.config(text = 'Date :'+date_string+'\n'+'Time :'+time_string)
        clock.after(20,tick)

    u = userval.get()
    p = passval.get()
    loguserentry.delete(0, "end")
    logpassentry.delete(0, "end")

    if u == '1' and p == '2':
        root = Toplevel()
        root.configure(bg='coral')
        root.title("Black pearl softwares")
        root.geometry('1370x750+0+0')

        def exitstudent():
            res = messagebox.askyesnocancel("Notification", 'Do you want to exit')
            if (res == True):
                root.destroy()

        blackpearl = Label(root,text=ss,bg='coral', font=('Comic Sans MS',24,'bold')).place(x=400, y=5)
        clock = Label(root, font=('chiller',12 , 'italic bold'), bg='coral')
        clock.place(x=0, y=0, width=200)
        tick()        

        ShowDataFrame = Frame(root, bg='white')
        ShowDataFrame.place(x=5, y=40, width=1355, height=610)

        style = ttk.Style()
        style.configure('Treeview.Heading',background='pale green', font=('roman', 14, 'bold'), foreground='blue')
        style.configure('Treeview', font=('times', 14),rowheight=30)
        style.map("Treeview",background=[('selected','pale green')],foreground=[('selected','black')])


        scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)
        global studenttable
        studenttable = Treeview(ShowDataFrame, columns=('id', "name", 'mobile', 'email', 'address', 'gender', 'dob', 'date', 'time'),
        yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=studenttable.xview)
        scroll_y.config(command=studenttable.yview)
        studenttable.heading('id', text='ID',anchor=W)
        studenttable.heading('name', text='NAME',anchor=W)
        studenttable.heading('mobile', text='MOBILE NO.',anchor=W)
        studenttable.heading('email', text='EMAIL',anchor=W)
        studenttable.heading('address', text='ADDRESS',anchor=W)
        studenttable.heading('gender', text='GENDER',anchor=W)
        studenttable.heading('dob', text='DOB',anchor=W)
        studenttable.heading('date', text='DATE',anchor=W)
        studenttable.heading('time', text='TIME',anchor=W)
        studenttable.column('id', width=60)
        studenttable.column('name', width=300)
        studenttable.column('mobile', width=150)
        studenttable.column('email', width=250)
        studenttable.column('address', width=100)
        studenttable.column('gender', width=100)
        studenttable.column('dob', width=150)
        studenttable.column('date', width=110)
        studenttable.column('time', width=110)

        studenttable['show'] = 'headings'
        studenttable.pack(fill=BOTH, expand=1)

        ####DATABASE PROBLEM SOLVE@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2@@@@@@@@@2
        conn = sqlite3.connect("open.db")
        c = conn.cursor()
        strr = 'create table load(id int,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(50),dob varchar(50),date varchar(50),time varchar(50))'
        try:
            c.execute(strr)
        except:
            c.execute("SELECT * FROM load")
            datas = c.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in  datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                studenttable.insert('',END,values=vv)
            conn.commit()
            conn.close()
            ####DATABASE PROBLEM SOLVE@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2@@@@@@@@@2

        rootbuttonframe = Frame(root, bg='coral')
        rootbuttonframe.pack(side=BOTTOM)

        addbtn = Button(rootbuttonframe, width=12, text="1. ADD", font=('chiller', 14, 'bold'),bd=6, activebackground="green",
        activeforeground="white",command=addstudent)
        addbtn.pack(side=LEFT, expand=True)

        searchbtn = Button(rootbuttonframe, width=12,text="2. SEARCH",
        font=('chiller', 14, 'bold'),bd=6, activebackground="green", activeforeground="white",command=searchstudent)
        searchbtn.pack(side=LEFT, expand=True)

        deletebtn = Button(rootbuttonframe,width=12, text="3. DELETE", 
        font=('chiller', 14, 'bold'),bd=6, activebackground="green", activeforeground="white",command=deletestudent)
        deletebtn.pack(side=LEFT, expand=True)

        updatebtn = Button(rootbuttonframe,width=12, text="4. UPDATE",
        font=('chiller', 14, 'bold'),bd=6, activebackground="green", activeforeground="white",command=updatestudent)
        updatebtn.pack(side=LEFT, expand=True)

        showallbtn = Button(rootbuttonframe, width=12,text="5. SHOW ALL", 
        font=('chiller', 14, 'bold'),bd=6, activebackground="green", activeforeground="white",command=showstudent)
        showallbtn.pack(side=LEFT, expand=True)

        exportbtn = Button(rootbuttonframe,width=12, text="6. EXPORT", 
        font=('chiller', 14, 'bold'),bd=6, activebackground="green", activeforeground="white",command=exporttudent)
        exportbtn.pack(side=LEFT, expand=True)

        exitbtn = Button(rootbuttonframe,width=12, text="7. Exit", 
        font=('chiller', 14, 'bold'),bd=6, activebackground="green", activeforeground="white",command=exitstudent)
        exitbtn.pack(side=LEFT, expand=True)
        #======================================SORT BY========================================
        def sorting():
            sel = selected.get()
            if sel == "ID":
                conn = sqlite3.connect("open.db")
                c = conn.cursor()
                c.execute("SELECT * FROM load")
                c.execute("SELECT * FROM load ORDER BY id")
                datas = c.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in  datas:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                    studenttable.insert('',END,values=vv)
                conn.commit()
                conn.close()
            elif sel == "NAME":
                conn = sqlite3.connect("open.db")
                c = conn.cursor()
                c.execute("SELECT * FROM load")
                c.execute("SELECT * FROM load ORDER BY name")
                datas = c.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in  datas:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                    studenttable.insert('',END,values=vv)
                conn.commit()
                conn.close()
            elif sel == "DATE":
                conn = sqlite3.connect("open.db")
                c = conn.cursor()
                c.execute("SELECT * FROM load")
                c.execute("SELECT * FROM load ORDER BY date")
                datas = c.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in  datas:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                    studenttable.insert('',END,values=vv)
                conn.commit()
                conn.close()
            elif sel == "ADDRESS             ":
                conn = sqlite3.connect("open.db")
                c = conn.cursor()
                c.execute("SELECT * FROM load")
                c.execute("SELECT * FROM load ORDER BY address")
                datas = c.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in  datas:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                    studenttable.insert('',END,values=vv)
                conn.commit()
                conn.close()
            else:
                conn = sqlite3.connect("open.db")
                c = conn.cursor()
                c.execute("SELECT * FROM load")
                c.execute("SELECT * FROM load ORDER BY email")
                datas = c.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in  datas:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                    studenttable.insert('',END,values=vv)
                conn.commit()
                conn.close()
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@sorting@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2
        selected = StringVar()
        select = selected.set("Sort By")
        dropdown = OptionMenu(root,selected,"ID","NAME","ADDRESS             ","DATE","EMAIL")
        dropdown.place(x=1200, y=0, width=150,height=40)
        dropdown.config(font=('chiller', 14, 'italic bold'),fg="green")
        sortby = Button(root, text= "Get Sorted:",bd=5,relief=RIDGE, font=('chiller', 14, 'italic bold'),command=sorting)
        sortby.place(x=1050, y=0,width=150,height=40)
        sortby.config(font=('chiller', 14, 'italic bold'),fg="green")



        root.mainloop()
    else:
        messagebox.showinfo("Incorrect Values", "Enter correct Username and Password") 


loginwin = Tk()
loginwin.title('Black pearl softwares')
loginwin.config(bg='coral')
loginwin.title("Black pearl softwares")
loginwin.geometry('1370x750+0+0')
loginwin.resizable(False, False)
bgimg = PhotoImage(file = 'back.png')
labelbg = Label(loginwin, image = bgimg).place(relwidth=1, relheight=1)


logframe = Frame(loginwin, bg='gray25', width=600, height=400)
logframe.place(x=350, y=240)

userval = StringVar()
passval = StringVar()


def exitapp():
    res = messagebox.askyesnocancel("Notification", 'Do you want to exit')
    if (res == True):
        loginwin.destroy()

clock = Label(loginwin, font=('chiller',14 , 'italic bold'),fg='sky blue',bg="gray25")
clock.place(x=0, y=0, width=200)
tick()

blackpearl = Label(loginwin,text=ss,fg="DarkGoldenrod2",bg="gray87", font=('Comic Sans MS',36,'bold')).place(x=900, y=5)

logintitle = Label(logframe ,bg='gray24',fg='sky blue', text="-------Log In Hare------",font=('roman', 18, 'bold'))
logintitle.place(x=100, y=0)

loguserlabel = Label(logframe,text='Username',bg='gray24', fg='sky blue',font=('roman', 16, 'bold'))
loguserlabel.place(x=100, y=50)
loguserentry = Entry(logframe,font=('roman', 16, 'bold'),textvariable=userval)
loguserentry.place(x=120, y=100)

logpasslabel = Label(logframe,text='Password', bg='gray24',fg='sky blue',font=('roman', 16, 'bold'))
logpasslabel.place(x=100, y=170)

logpassentry = Entry(logframe,font=('roman', 16, 'bold'), textvariable=passval, show = '*')
logpassentry.place(x=120, y=220)

loginbutton = Button(loginwin, width=14,bg='goldenrod2',bd=5,
 text='Log In',font=('roman', 16, 'bold'),activebackground='green', activeforeground='white',command=login)
loginbutton.place(x=380, y=530)

exit_button = Button(loginwin, width=14, text="EXIT", bg="goldenrod2", bd=5, font=("roman", 16, "bold",),
    activebackground="green", activeforeground="white", command=exitapp)
exit_button.place(x=670, y=530)

loginwin.mainloop()