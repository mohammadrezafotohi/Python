from tkinter import *

main=Tk()
main.title("Real Profit Calculator")
main.geometry("600x450")
nominal=StringVar()
inflation=StringVar()

nomilabel=Label(main,text="Nominal Profit Rate :")
nomilabel.grid(row=0,column=1)
inflabel=Label(main,text="Inflation Rate : ")
inflabel.grid(row=1,column=1)
rellabel=Label(main,text="Real Profit is : ")
rellabel.grid(row=2,column=1)

nomi_entry=Entry(main,textvariable=nominal)
inf_entry=Entry(main,textvariable=inflation)
rel_label=Label(main,text="0",height="10",width="10")
rel_label.grid(row=2,column=2)
nomi_entry.grid(row=0,column=2)
inf_entry.grid(row=1,column=2)

def cal():
    rpr=float(nomi_entry.get())-float(inf_entry.get())
    if rpr>=0:
        rel_label.config(text=rpr)
    else :
        rel_label.config(text=rpr,fg="red")

def cle():
    nominal.set("")
    inflation.set("")
    rel_label.config(text="0",fg="black")

exbtn=Button(main,text="Close",fg="red",command=main.destroy)
exbtn.grid(row=3,column=1)
calbtn=Button(main,text="Calculation", command=cal)
calbtn.grid(row=3,column=5)
clearbtn=Button(main,text="Clear",command=cle)
clearbtn.grid(row=3,column=2)

main.mainloop()

