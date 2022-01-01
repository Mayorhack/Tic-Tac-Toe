from tkinter import *
from tkinter import ttk,messagebox



cnt=0
button1,button2,button3,button4,button5,button6,button7,button8,button9=8,8,8,8,9,8,8,8,8

def mark(num):
    global cnt,button1,button2,button3,button4,button5,button6,button7,button8,button9 
    if num == 1 and cnt==0:
        b1.config(text="X")
        cnt=cnt+1
        button1=1
        
    elif num ==1 and cnt==1:
        b1.config(text="O")
        cnt=0
        button1=0
    elif num == 2 and cnt==0:
        b2.config(text="X")
        cnt=cnt+1
        button2=1
    elif num ==2 and cnt==1:
        b2.config(text="O")
        cnt=0
        button2=0
    elif num == 3 and cnt==0:
        b3.config(text="X")
        cnt=cnt+1
        button3=1
    elif num ==3 and cnt==1:
        b3.config(text="O")
        cnt=0
        button3=0
    elif num == 4 and cnt==0:
        b4.config(text="X")
        cnt=cnt+1
        button4=1
    elif num ==4 and cnt==1:
        b4.config(text="O")
        cnt=0
        button4=0
    elif num == 5 and cnt==0:
        b5.config(text="X")
        cnt=cnt+1
        button5=1
    elif num ==5 and cnt==1:
        b5.config(text="O")
        cnt=0
        button5=0
    elif num == 6 and cnt==0:
        b6.config(text="X")
        cnt=cnt+1
        button6=1
    elif num ==6 and cnt==1:
        b6.config(text="O")
        cnt=0
        button6=0
    elif num == 7 and cnt==0:
        b7.config(text="X")
        cnt=cnt+1
        button7=1
    elif num ==7 and cnt==1:
        b7.config(text="O")
        cnt=0
        button7=0
    elif num == 8 and cnt==0:
        b8.config(text="X")
        cnt=cnt+1
        button8=1
    elif num ==8 and cnt==1:
        b8.config(text="O")
        cnt=0
        button8=0
    elif num == 9 and cnt==0:
        b9.config(text="X")
        cnt=cnt+1
        button9=1
    elif num ==9 and cnt==1:
        b9.config(text="O")
        cnt=0
        button9=0
    if (button1+button2+button3==3 or button1+button5+button9==3 or button1+button4+button7==3 or button2+button5+button8==3
    or button3+button6+button9==3 or button4+button5+button6==3 or button3+button5+button7==3 or button7+button8+button9==3):
        messagebox.showinfo("Player 1 Wins", "Player 1 is the winner")
        window_g.destroy()
    elif (button1+button2+button3==0 or button1+button5+button9==0 or button1+button4+button7==0 or button2+button5+button8==0
    or button3+button6+button9==0 or button4+button5+button6==0 or button3+button5+button7==0 or button7+button8+button9==0):
        messagebox.showinfo("Player 2 Wins", "Player 2 is the winner")
        window_g.destroy()
    elif button1+button2+button3+button4+button5+button6+button7+button8+button9==5:
        messagebox.askokcancel("Draw","The match is a draw")
        window_g.destroy()

window=Tk()
def start():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,window_g
    window_g=Toplevel(window)
    b1=Button(window_g,height=10,width=10,command=lambda:mark(1) )
    b2=Button(window_g,height=10,width=10, command=lambda:mark(2))
    b3=Button(window_g,height=10,width=10, command=lambda:mark(3))
    b4=Button(window_g,height=10,width=10, command=lambda:mark(4))
    b5=Button(window_g,height=10,width=10, command=lambda:mark(5))
    b6=Button(window_g,height=10,width=10, command=lambda:mark(6))
    b7=Button(window_g,height=10,width=10, command=lambda:mark(7))
    b8=Button(window_g,height=10,width=10, command=lambda:mark(8))
    b9=Button(window_g,height=10,width=10, command=lambda:mark(9))
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)
    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)
    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)


but=Button(window,text="Start Game", command=start)
but2=Button(window, text="Close", command=window.destroy)
but.pack(pady=10, padx=10)
but2.pack(pady=10, padx=10)
window.mainloop()