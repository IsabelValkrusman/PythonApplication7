from tkinter import*
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import *
import fileinput
from tkinter.messagebox import*

#fail=open("tähtkujud.txt","r")
#sisu=fail.read()
#täht=[]
#b=täht[s]

#for line in sisu.splitlines():
# if line:  täht=map(str.strip,line.split(':'))
#  täht.append(key)
#  kys_vas[key]=value

#for i in range(12):

root=Tk()
root.geometry("300x400")
root.title("Tähtkujud Tkinteris")

tabs=ttk.Notebook(root,width=300,height=300)
#texts=["Kaljukits","Veevalaja","Kalad","Jäär","Sõnn","Kaksikud","Vähk","Lõvi","Neitsi","Kaalud","Skorpion","Ambur"]
#for i in range(12):
# tab=Frame(tabs)
# tabs.add(tab,text=texts[i])
# fail=open("tähtkujud.txt*","r")
# sisu=fail.read()

tab1=Frame(tabs)
tab2=Frame(tabs)
tab3=Frame(tabs)
tab4=Frame(tabs)
tab5=Frame(tabs)
tab6=Frame(tabs)
tab7=Frame(tabs)
tab8=Frame(tabs)
tab9=Frame(tabs)
tab10=Frame(tabs)
tab11=Frame(tabs)
tab12=Frame(tabs)
tabs.add(tab1,text="Kaljukits")
tabs.add(tab2,text="Veevalaja")
tabs.add(tab3,text="Kalad")
tabs.add(tab4,text="Jäär")
tabs.add(tab5,text="Sõnn")
tabs.add(tab6,text="Kaksikud")
tabs.add(tab7,text="Vähk")
tabs.add(tab8,text="Lõvi")
tabs.add(tab9,text="Neitsi")
tabs.add(tab10,text="Kaalud")
tabs.add(tab11,text="Skorpion")
tabs.add(tab12,text="Ambur")

M=Menu(root)
root.config(menu=M)
m1=Menu(M,tearoff=1)
M.add_cascade(label="Tabs",menu=m1)
m1.add_command(label="Tab1",accelerator='Command+V',command=lambda:funktioń(0))
m1.add_separator()
m1.add_command(label="Tab2",command=lambda:funktion(1))
m1.add_separator()
m1.add_command(label="Tab3",command=lambda:funktion(2))
m1.add_separator()
m1.add_command(label="Tab4",command=lambda:funktion(3))
m1.add_separator()
m1.add_command(label="Tab5",command=lambda:funktion(4))
m1.add_separator()
m1.add_command(label="Tab6",command=lambda:funktion(5))
m1.add_separator()
m1.add_command(label="Tab7",command=lambda:funktion(6))
m1.add_separator()
m1.add_command(label="Tab8",command=lambda:funktion(7))
m1.add_separator()
m1.add_command(label="Tab9",command=lambda:funktion(8))
m1.add_separator()
m1.add_command(label="Tab10",command=lambda:funktion(9))
m1.add_separator()
m1.add_command(label="Tab11",command=lambda:funktion(10))
m1.add_separator()
m1.add_command(label="Tab12",command=lambda:funktion(11))
m1.add_separator()

m2=Menu(M,tearoff=0)
M.add_cascade(label="BG Colors",menu=m2)
m2.add_command(label="Salmon",command=lambda:root.config(bg="salmon"))
m2.add_separator()
m2.add_command(label="MediumSpringGreen",command=lambda:root.config(bg="MediumSpringGreen"))
m2.add_separator()
m2.add_command(label="PowderBlue",command=lambda:root.config(bg="powderblue"))
m2.add_separator()
m2.add_command(label="MediumPurple",command=lambda:root.config(bg="mediumpurple"))
m2.add_separator()
m2.add_command(label="OliveDrab",command=lambda:root.config(bg="olivedrab"))
m2.add_separator()
m2.add_command(label="DarkRed",command=lambda:root.config(bg="darkred"))
m2.add_separator()
m2.add_command(label="Tomato",command=lambda:root.config(bg="tomato"))
m2.add_separator()
m2.add_command(label="MediumPurple",command=lambda:root.config(bg="mediumpurple"))
m2.add_separator()
m2.add_command(label="Teal",command=lambda:root.config(bg="teal"))
m2.add_separator()
m2.add_command(label="Aquamarine",command=lambda:root.config(bg="aquamarine"))
m2.add_separator()
m2.add_command(label="PaleGreen",command=lambda:root.config(bg="palegreen"))
m2.add_separator()
m2.add_command(label="DarkBlue",command=lambda:root.config(bg="darkblue"))
m2.add_separator()
m2.add_command(label="Khaki",command=lambda:root.config(bg="khaki"))
m2.add_separator()
m2.add_command(label="Thistle",command=lambda:root.config(bg="thistle"))
m2.add_separator()

m3=Menu(M,tearoff=0)
M.add_cascade(label="Zodiac signs image",menu=m3)
m3.add_command(label="Kaljukits",command=lambda:image_("unnamed.png"))
m3.add_separator()
m3.add_command(label="Veevalaja",command=lambda:image_("aquariuss.png"))
m3.add_separator()
m3.add_command(label="Kalad",command=lambda:image_("pisces.png"))
m3.add_separator()
m3.add_command(label="Jäär",command=lambda:image_("aries.png"))
m3.add_separator()
m3.add_command(label="Sõnn",command=lambda:image_("taurus(1).png"))
m3.add_separator()
m3.add_command(label="Kaksikud",command=lambda:image_("gemini.png"))
m3.add_separator()
m3.add_command(label="Vähk",command=lambda:image_("cancer.png"))
m3.add_separator()
m3.add_command(label="Lõvi",command=lambda:image_("leo.png"))
m3.add_separator()
m3.add_command(label="Neitsi",command=lambda:image_("kisspng-virgo.png"))
m3.add_separator()
m3.add_command(label="Kaalud",command=lambda:image_("libraa.png"))
m3.add_separator()
m3.add_command(label="Skorpion",command=lambda:image_("scorpion.png"))
m3.add_separator()
m3.add_command(label="Ambur",command=lambda:image_("saggitarius.png"))
m3.add_separator()

btn_open=Button(tab1,text="Open")
btn_save=Button(tab1,text="Save")
btn_exit=Button(tab1,text="Exit")
txt_box=scrolledtext.ScrolledText(tab1,width=50,height=15)
#Text(tab1,width=40,heigh
txt_box.grid(row=0,column=0,columnspan=3)
btn_open.grid(row=1,column=0)
btn_save.grid(row=1,column=1)
btn_exit.grid(row=1,column=2)


def lahenda():
 if (day.get()!="" and month.get()!=""):
  d_=int(d.get())
  m_=int(m.get())
  d.configure(bg="lightblue")
  m.configure(bg="lightblue")
  if (d_>23 and m_==12) or (d_<20 and m_==1):
   print(Kaljukits)
  elif (d_>21 and m_==1) or (d_<19 and m_==2):
   print(Veevalaja)
  elif (d_>20 and m_==2) or (d_<20 and m_==3):
   print(Kala)
  elif (d_>21 and m_==3) or (d_<20 and m_==4):
   print(Jäär)
  elif (d_>21 and m_==4) or (d_<21 and m_==5):
   print(Sõnn)
  elif (d_>22 and m_==5) or (d_<21 and m_==6):
   print(Kaksikud)
  elif (d_>22 and m_==6) or (d_<22 and m_==7):
   print(Vähk)
  elif (d_>23 and m_==7) or (d_<21 and m_==8):
   print(Lõvi)
  elif (d_>22 and m_==8) or (d_<23 and m_==9):
   print(Neitsi)
  elif (d_>24 and m_==9) or (d_<23 and m_==10):
   print(Kaalud)
  elif (d_>24 and m_==10) or (d_<22 and m_==11):
   print(Skorpion)
  elif (d_>24 and m_==11) or (d_<22 and m_==12):
   print(Ambur)

month=Entry(root,font="Calibri 26",fg="green",bg="lightblue",width=3)
month.grid(row=0,column=0)
x=Label(root,text="Kuu",font="Calibri 26",fg="green")
x.grid(row=0,column=1)

day=Entry(root,font="Calibri 26",fg="green",bg="lightblue",width=3)
day.grid(row=0,column=0)
y=Label(root,text="Päev",font="Calibri 26",fg="green")
y.grid(row=0,column=1)
can=Canvas(tab2,width=300,height=200)
can.grid
name=Entry(root,font="Calibri 26",fg="green",bg="lightblue",width=3)
name.grid(row=0,column=0)
image_=Canvas(width=3)
image_.grid(row=0,column=0)

#vastus=Labe(aken,height=4,width=20,bg="yellow")
#vastus.pack(side=BOTTOM)

def open_():
 file=askopenfilename()
 for text in fileinput.input(file):
  txt_box.insert(0.0,text)

def save_():
 file=asksaveasfile(mode='w',defaultextension=((".txt"),(".docx")),filetypes=(("Notepad",".txt"),("Word",".docx")))
 t=txt_box.get(0.0,END)
 file.write(t)
 file.close()

def exit_():
 if askyesno("Exit","Yes/No"):
  showinfo("Exit","Message: Yes")
  root.destroy()
 else:
  showinfo("No")

def taurus():
 global img
 img=PhotoImage(file="taurus(1).png").subsample(sample)
 can.create_image(10.10,image=img,anchor=NW)

def scorpion():
 global img
 img=PhotoImage(file="scorpion.png").subsample(sample)
 can.create_image(10.10,image=img,anchor=NW)

def libra():
 global img
 img=PhotoImage(file="libraa.png").subsample(sample)
 can.create_image(10.10,image=img,anchor=NW)

def saggitarius():
 global img
 img=PhotoImage(file="saggitarius.png").subsample(sample)
 can.create_image(10.10,image=img,anchor=NW)

def leo():
 global img
 img=PhotoImage(file="leo.png").subsample(sample)
 can.create_image(10.10,image=img,anchor=NW)

def aries():
 global img
 img=PhotoImage(file="aries.png").subsample(sample)
 can.create_image(10.10,image=img,anchor=NW)

def aquariuss():
 global img
 img=PhotoImage(file="aquariuss.png").subsample(sample)
 can.create_image(10.10,image=img,anchor=NW)

def pisces():
 global img
 img=PhotoImage(file="pisces.png").subsample(sample)
 can.create_image(10.10,image=img,anchor=NW)

def funktion(a):
 tabs.select(a)

#global img
#img=PhotoImage(file=name).subsample(sample)
#can.create_image()
#tabs.grid(row=1,column=0,columnspam=4)
root.mainloop()