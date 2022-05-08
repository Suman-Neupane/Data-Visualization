from tkinter import*
from turtle import color, width
from tkinter import filedialog, messagebox, ttk
import matplotlib.pyplot as plt
from PIL import ImageTk,Image
import pandas as pd
def openFile(event):
    filename=filedialog.askopenfilename()
    label_file["text"]= filename
    return None

def loadFile(event):
    file_path= label_file["text"]
    try:
        excel_filename=r"{}".format(file_path)
        if excel_filename[-4:] ==".csv":
            df= pd.read_csv(excel_filename)
        else:
            df= pd.read_excel(excel_filename)
    except ValueError:
        root.messagebox.showerror("Information","The file you have choosen is invalid")
        return None
    except FileNotFoundError:
        root.messagebox.showerror("Information", f"No such file as{file_path}")
        return None
    clear_data()
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column) # let the column heading = column name

    df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
    for row in df_rows:
        tv1.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
    return None


def clear_data():
    tv1.delete(*tv1.get_children())
    return None


def dataview(event):
    file_path= label_file["text"]
    try:
        excel_filename=r"{}".format(file_path)
        if excel_filename[-4:] ==".csv":
            df= pd.read_csv(excel_filename)
            plt.bar(df['Country'],df['Deaths'])
            plt.xlabel('Country')
            plt.ylabel('Deaths')
            plt.show()
        else:
            df= pd.read_excel(excel_filename)
    except ValueError:
        root.messagebox.showerror("Information","The file you have choosen is invalid")
        return None
    except FileNotFoundError:
        root.messagebox.showerror("Information", f"No such file as{file_path}")
        return None


def piechart(event):
    
    file_path= label_file["text"]
    
    excel_filename=r"{}".format(file_path)
    if excel_filename[-4:] ==".csv":

        df= pd.read_csv(excel_filename)
        x=df['Country']
        y=df['Deaths']
        plt.pie(y,labels=x,startangle=90)
        plt.legend(title="five country")
        plt.show()
        
    else:
        df= pd.read_excel(excel_filename)
def scatter(event):
    file_path= label_file["text"]
    
    
    excel_filename=r"{}".format(file_path)
    if excel_filename[-4:] ==".csv":

        df= pd.read_csv(excel_filename)
        x=df['Country']
        y=df['Deaths']
        plt.scatter(x,y,color='yellow')

        x=df['Country']
        y=df['Recovered']
        plt.scatter(x,y,color="green")
        plt.show()
        
    else:
        df= pd.read_excel(excel_filename)
    

root=Tk()
root.title("Data Analysis Tools")
root.geometry("1350x700+0+0")

title=Label(root,text="Data Analysis", bd=10,font=("times new roman",40,"bold"),bg="black",fg="green")
title.pack(side=TOP,fill=X)


#=============import frame======================#
Manage_Frame=Frame(root,bd=4,relief=RIDGE, bg="yellow")
Manage_Frame.place(x=20,y=100,width=450,height=560)

m_title=Label(Manage_Frame,text="import file",font=("times new roman",30,"bold"),bg="Red",fg="black")
m_title.grid(row=0,columnspan=2,pady=20)

#--------upload button----------------------------
b=Button(Manage_Frame,text="upload",padx=5,pady=5,font="lucida 14 bold")
b.grid(row=1,column=1)
b.bind("<Button-1>",openFile)

#-----browse button-------------------------------
b=Button(Manage_Frame,text="load",padx=5,pady=5,font="lucida 14 bold")
b.grid(row=1,column=3)
b.bind("<Button-1>",loadFile)

# The file/file path text
label_file= ttk.Label(Manage_Frame,text="No File Selected")
label_file.place(rely=0,relx=0)

 
#-----bargraph button-------------------------------
c=Button(Manage_Frame,text="Bargraph",padx=5,pady=5,font="lucida 14 bold")
c.grid(row=24,column=1)
c.bind("<Button-1>",dataview)

#------------piechart-------
d=Button(Manage_Frame,text="piechart",padx=5,pady=5,font="lucida 14 bold")
d.grid(row=27,column=1)
d.bind("<Button-1>",piechart)


#------------Scatter-----------
e=Button(Manage_Frame,text="Scatter",padx=5,pady=5,font="lucida 14 bold")
e.grid(row=29,column=1)
e.bind("<Button-1>",scatter)






# label for datavisulaiztion
m_title2=Label(Manage_Frame,text="Data Visulatzation",font=("times new roman",20,"bold"),bg="white",fg="black")
m_title2.grid(row=20,column=0)

m_title2=Label(Manage_Frame,text="                       ",font=("times new roman",15,"bold"),bg="white",fg="black")
m_title2.grid(row=21,column=0)

m_title2=Label(Manage_Frame,text="Choose Type Of Graph:",font=("times new roman",15,"bold"),bg="white",fg="black")
m_title2.grid(row=21,column=0)






 #------detailframe-------------
Detail_frame=Frame(root,bd=4,relief=RIDGE,bg='blue')
Detail_frame.place(x=500,y=100,width=800,height=300)


#--------graphframe-------------------
# scvalue=StringVar()
# scvalue.set("")
# screen=Entry(root,textvar=scvalue,font="lucida 40 bold")
# # screen.pack(fill=X,ipadx=8,pady=10,padx=10)
# screen.place(x=500,y=400,width=800,height=280)


# ------TREEVIEW Widget----------
tv1= ttk.Treeview(Detail_frame)
tv1.place(relheight=1,relwidth=1)
treescrolly = Scrollbar(Detail_frame, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
treescrollx = Scrollbar(Detail_frame, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget



root.mainloop()