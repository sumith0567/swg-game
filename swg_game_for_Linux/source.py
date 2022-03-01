import tkinter as tk
import random

a=["GUN","WATER","SNAKE"]
s1=0
s2=0
def snake():
    global s1,s2
    b=random.choice(a)
    l4=tk.Label(sr,text=b,font=(None,14),bg='white',width=10).place(x=250,y=223)
    if b==a[0]:
        l6=tk.Label(sr,text="Computer won \nthe game..",font=(None,16),bg='#ff66bb',height=5,width=13).place(x=200,y=350)
        s2+=1
    elif b==a[1]:
        l6=tk.Label(sr,text="You won\nthe game!!",font=(None,16),bg='#ff66bb',height=5,width=13).place(x=200,y=350)
        s1+=1
    else:
        l6=tk.Label(sr,text="Its Draw!",font=(None,16),bg='#ff66bb',height=5,width=13).place(x=200,y=350)
    l7=tk.Label(sr,text=s1,font=(None,14),bg='orange',height=4,width=5).place(x=22,y=395)
    l8=tk.Label(sr,text=s2,font=(None,14),bg='#00ff22',height=4,width=5).place(x=87,y=395)
    return l4,l6,l7,l8
def water():
    global s1,s2
    b=random.choice(a)
    l4=tk.Label(sr,text=b,font=(None,14),bg='white',width=10).place(x=250,y=223)
    if b==a[2]:
        l6=tk.Label(sr,text="Computer won \nthe game..",font=(None,16),bg='#ff66bb',height=5,width=13).place(x=200,y=350)
        s2+=1
    elif b==a[0]:
        l6=tk.Label(sr,text="You won\nthe game!!",font=(None,16),bg='#ff66bb',height=5,width=13).place(x=200,y=350)
        s1+=1
    else:
        l6=tk.Label(sr,text="Its Draw!",font=(None,16),bg='#ff66bb',height=5,width=13).place(x=200,y=350)
    l7=tk.Label(sr,text=s1,font=(None,14),bg='orange',height=4,width=5).place(x=22,y=395)
    l8=tk.Label(sr,text=s2,font=(None,14),bg='#00ff22',height=4,width=5).place(x=87,y=395)
    return l4,l6,l7,l8

def gun():
    global s1,s2
    b=random.choice(a)
    l4=tk.Label(sr,text=b,font=(None,14),bg='white',width=10).place(x=250,y=223)
    if b==a[1]:
        l6=tk.Label(sr,text="Computer won \nthe game..",font=(None,16),bg='#ff66bb',height=5,width=13).place(x=200,y=350)
        s2+=1
    elif b==a[2]:
        l6=tk.Label(sr,text="You won\nthe game!!",font=(None,16),bg='#ff66bb',height=5,width=13).place(x=200,y=350)
        s1+=1
    else:
        l6=tk.Label(sr,text="Its Draw!",font=(None,16),bg='#ff66bb',height=5,width=13).place(x=200,y=350)
    l7=tk.Label(sr,text=s1,font=(None,14),bg='orange',height=4,width=5).place(x=22,y=395)
    l8=tk.Label(sr,text=s2,font=(None,14),bg='#00ff22',height=4,width=5).place(x=87,y=395)
    return l4,l6,l7,l8

sr=tk.Tk()
sr.title("Snake-Water-Gun")
sr.geometry('400x560')
sr.minsize(400,560)
sr.maxsize(400,560)
sr.configure(bg='#00aaff')

b1=tk.Button(sr,height=1,width=7,text="SNAKE",command=lambda:snake(),font=('italic',13),bg='green',fg='white').place(x=40,y=90)
b2=tk.Button(sr,height=1,width=7,text="WATER",command=lambda:water(),font=('italic',13),bg='green',fg='white').place(x=160,y=90)
b3=tk.Button(sr,height=1,width=7,text="GUN",command=lambda:gun(),font=('italic',13),bg='green',fg='white').place(x=280,y=90)


l1=tk.Label(sr,text="Select Your Choice:",font=('Oblique',17),bg='#00aaff').place(x=40,y=40)
l2=tk.Label(sr,text="VS",font=(None,30),bg='#00aaff').place(x=170,y=150)
l6=tk.Label(sr,text="Click a button\n to start",font=(None,16),bg='#ff66bb',height=5,width=13).place(x=200,y=350)
l7=tk.Label(sr,text=s1,font=(None,14),bg='orange',height=4,width=5).place(x=22,y=395)
l8=tk.Label(sr,text=s2,font=(None,14),bg='#00ff22',height=4,width=5).place(x=87,y=395)
l71=tk.Label(sr,text='Yours',font=(None,9),bg='#00ff22',height=2,width=8).place(x=20,y=360)
l81=tk.Label(sr,text='Computer',font=(None,9),bg='orange',height=2,width=8).place(x=85,y=360)
l9=tk.Label(sr,text="Score Board",font=(None,13),bg='yellow',height=1,width=12).place(x=18,y=333)
l3=tk.Label(sr,text="Computer Choice:",font=('Oblique',17),bg='#00aaff').place(x=20,y=220)
l4=tk.Label(sr,text="Lets Start",font=(None,14),bg='white',width=10).place(x=250,y=223)

l10=tk.Label(sr,text="Art By => Sumith D",font=('bold',16),bg='#2668af',fg='white',width=30,height=2).place(x=0,y=510)

sr.mainloop()