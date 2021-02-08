from tkinter import*
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import *
import fileinput
from tkinter.messagebox import*

root=Tk()
root.geometry("600x400")
root.title("Tähtkujud Tkinteris")

tabs=ttk.Notebook(root,width=300,height=300)


def open_(fail):
# file=askopenfilename()
 for text in fileinput.input(fail):
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

def funktion(a,fail):
    tabs.select(a)
    open_(fail)

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

#can=Canvas(tab2,width=300,height=200,bg="red")
#can.pack()

M=Menu(root)
root.config(menu=M)
m1=Menu(M,tearoff=1)
M.add_cascade(label="Tabs",menu=m1)
m1.add_command(label="kaljukits informatsioon",accelerator='Command+V',command=lambda:funktion(0,"tähtkujud.txt"))
m1.add_separator()
m1.add_command(label="veevalaja informatsioon",command=lambda:funktion(1,"TextFile2.txt"))
m1.add_separator()
m1.add_command(label="kalad informatsioon",command=lambda:funktion(2,"TextFile3.txt"))
m1.add_separator()
m1.add_command(label="jäär informatsioon",command=lambda:funktion(3,"TextFile4.txt"))
m1.add_separator()
m1.add_command(label="sõnn informatsioon",command=lambda:funktion(4,"TextFile5.txt"))
m1.add_separator()
m1.add_command(label="kaksikud informatsioon",command=lambda:funktion(5,"TextFile6.txt"))
m1.add_separator()
m1.add_command(label="vähk informatsioon",command=lambda:funktion(6,"TextFile7.txt"))
m1.add_separator()
m1.add_command(label="lõvi informatsioon",command=lambda:funktion(7,"TextFile8.txt"))
m1.add_separator()
m1.add_command(label="neitsi informatsioon",command=lambda:funktion(8,"TextFile9.txt"))
m1.add_separator()
m1.add_command(label="kaalud informatsioon",command=lambda:funktion(9,"TextFile10.txt"))
m1.add_separator()
m1.add_command(label="skorpion informatsioon",command=lambda:funktion(10,"TextFile11.txt"))
m1.add_separator()
m1.add_command(label="ambur informatsioon",command=lambda:funktion(11,"TextFile12.txt"))
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

can=Canvas(tab2,width=300,height=200)
can.pack()
can=Canvas(tab2,width=300,height=200)
can.pack()

can=Canvas(tab2,width=300,height=200)
can.pack()

can=Canvas(tab2,width=300,height=200)
can.pack()

can=Canvas(tab2,width=300,height=200)
can.pack()

can=Canvas(tab2,width=300,height=200)
can.pack()

can=Canvas(tab2,width=300,height=200)
can.pack()

can=Canvas(tab2,width=300,height=200)
can.pack()

can=Canvas(tab2,width=300,height=200)
can.pack()

can=Canvas(tab2,width=300,height=200)
can.pack()

can=Canvas(tab2,width=300,height=200)
can.pack()

can=Canvas(tab2,width=300,height=200)
can.pack()



m3=Menu(M,tearoff=0)
M.add_cascade(label="Zodiac signs image",menu=m3)
m3.add_command(label="Kaljukits",command=lambda:aries(0,"unnamed.png"))
m3.add_separator()
m3.add_command(label="Veevalaja",command=lambda:aquarius(1,"aquariuss.png"))
m3.add_separator()
m3.add_command(label="Kalad",command=lambda:pisces(2,"pisces.png"))
m3.add_separator()
m3.add_command(label="Jäär",command=lambda:aries(3,"aries.png"))
m3.add_separator()
m3.add_command(label="Sõnn",command=lambda:taurus(4,"taurus(1).png"))
m3.add_separator()
m3.add_command(label="Kaksikud",command=lambda:gemini(5,"gemini.png"))
m3.add_separator()
m3.add_command(label="Vähk",command=lambda:cancer(6,"cancer.png"))
m3.add_separator()
m3.add_command(label="Lõvi",command=lambda:leo(7,"leo.png"))
m3.add_separator()
m3.add_command(label="Neitsi",command=lambda:virgo(8,"kisspng-virgo.png"))
m3.add_separator()
m3.add_command(label="Kaalud",command=lambda:libra(9,"libraa.png"))
m3.add_separator()
m3.add_command(label="Skorpion",command=lambda:scorpion(10,"scorpion.png"))
m3.add_separator()
m3.add_command(label="Ambur",command=lambda:saggitarius(11,"saggitarius.png"))
m3.add_separator()

btn_open=Button(tab1,text="Open")
btn_save=Button(tab1,text="Save")
btn_exit=Button(tab1,text="Exit")
txt_box=scrolledtext.ScrolledText(tab1,width=40,height=5)
txt_kaljukits=scrolledtext.ScrolledText(tab1,width=50,height=15)
txt_veevalaja=scrolledtext.ScrolledText(tab2,width=50,height=15)
txt_kalad=scrolledtext.ScrolledText(tab3,width=50,height=15)
txt_jäär=scrolledtext.ScrolledText(tab4,width=500,height=15)
txt_sõnn=scrolledtext.ScrolledText(tab5,width=500,height=15)
txt_kaksikud=scrolledtext.ScrolledText(tab6,width=50,height=15)
txt_vähk=scrolledtext.ScrolledText(tab7,width=500,height=15)
txt_lõvi=scrolledtext.ScrolledText(tab8,width=500,height=15)
txt_neitsi=scrolledtext.ScrolledText(tab9,width=500,height=15)
txt_kaalud=scrolledtext.ScrolledText(tab10,width=50,height=15)
txt_skorpion=scrolledtext.ScrolledText(tab11,width=50,height=15)
txt_ambur=scrolledtext.ScrolledText(tab12,width=50,height=15)
#Text(tab1,width=40,heigh
txt_box.grid(row=0,column=0,columnspan=3)
btn_open.grid(row=1,column=0)
btn_save.grid(row=1,column=1)
btn_exit.grid(row=1,column=2)

#can1=Canvas(tab1,width=500,height=400,)
#img1=PhotoImage(file="tähtkujud.txt").subsample(3)
#can2.create_image(20,20,image=img2,anchor=NW)
#btn3=Button(tab1,text="tähtkujud",command=lambda:camry("tähtkujud.txt")

#vastus=Labe(aken,height=4,width=20,bg="yellow")
#vastus.pack(side=BOTTOM)

#btn3=Button(tab1,text="tähtkujud",command=lambda:camry("tähtkujud.txt")



def taurus():
 tabs.select(1)
 global img
 img=PhotoImage(file="taurus(1).png").subsample(sample)
 can.create_image(10.10,image=img,anchor=NW)

def scorpion():
 tabs.select(1)
 global img
 img=PhotoImage(file="scorpion.png").subsample(sample)
 can.create_image(10.10,image=img,anchor=NW)

def libra():
 tabs.select(1)
 global img
 img=PhotoImage(file="libraa.png").subsample(sample)
 can.create_image(10.10,image=img,anchor=NW)

def saggitarius():
 tabs.select(1)
 global img
 img=PhotoImage(file="saggitarius.png").subsample(sample)
 can.create_image(10.10,image=img,anchor=NW)

def leo():
 tabs.select(1)
 global img
 img=PhotoImage(file="leo.png").subsample(sample)
 can.create_image(10.10,image=img,anchor=NW)

def aries():
 tabs.select(1)
 global img
 img=PhotoImage(file="aries.png").subsample(sample)
 can.create_image(10.10,image=img,anchor=NW)

def pisces():
 tabs.select(1)
 global img
 img=PhotoImage(file="pisces.png").subsample(sample)
 can.create_image(10.10,image=img,anchor=NW)

def aquarius():
 tabs.select(1)
 global img
 img=PhotoImage(file="aquariuss.png").subsample(sample)
 can.create_image(10.10,image=img,anchor=NW)

def virgo():
 tabs.select(1)
 global img
 img=PhotoImage(file="pisces.png").subsample(sample)
 can.create_image(10.10,image=img,anchor=NW)

def capricorn():
 tabs.select(1)
 global img
 img=PhotoImage(file="aquariuss.png").subsample(sample)
 can.create_image(10.10,image=img,anchor=NW)

def gemini():
 tabs.select(1)
 global img
 img=PhotoImage(file="pisces.png").subsample(sample)
 can.create_image(10.10,image=img,anchor=NW)


#global img
#img=PhotoImage(file=name).subsample(sample)
#can.create_image()
#tabs.grid(row=1,column=0,columnspam=4)

tabs.pack(fill="both")
root.mainloop()
tabs.pack(fill="both")
root.mainloop()
tabs.pack(fill="both")
root.mainloop()
tabs.pack(fill="both")
root.mainloop()
tabs.pack(fill="both")
root.mainloop()
tabs.pack(fill="both")
root.mainloop()
tabs.pack(fill="both")
root.mainloop()
tabs.pack(fill="both")
root.mainloop()
tabs.pack(fill="both")
root.mainloop()
tabs.pack(fill="both")
root.mainloop()
tabs.pack(fill="both")
root.mainloop()
tabs.pack(fill="both")
root.mainloop()