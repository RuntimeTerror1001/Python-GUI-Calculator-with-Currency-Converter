# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:52:16 2020

@author: Parth
"""

#importing modules to be used
import tkinter
import math
from tkinter import StringVar
from tkinter import Entry
from tkinter import Button

expression = "" 
rte=etr=rtp=ptr=rtu=utr=rtc=ctr=rty=ytr=rtye=yetr=calc=''
plus=minus=mult=div=facto=sqr=exp=msine=mcos=mtan=msinh=mcosh=mtanh=vpi=ve=brack1=brack2=currcon=''
  
#defining functions to enter,evaluate,clear screen;calculator functions  
def enter(num): 
    global expression
    expression = expression + str(num) 

    equation.set(expression) 
    
def equalto(): 
    try: 
  
        global expression 
  
        total = str(eval(expression))   
        equation.set(total)   
        expression = "" 
   
    except: 
  
        equation.set("Error") 
        expression = "" 
    
def clrscr(): 
    global expression 

    expression = "" 
    equation.set("")

def fact():
    try:
        global expression

        exp=float(expression)
        pro=str(math.factorial(exp))
        equation.set(pro)
        expression=""
    
    except:
        
        equation.set("Error")
        expression=""

def root():
    global expression
    
    x=float(expression)
    sqroot=str(math.sqrt(x))
    equation.set(sqroot)
    expression=""
    
def sine():
    global expression
    
    x=float(expression)
    si=str(math.sin(x))
    equation.set(si)
    expression=""
    
def cosine():
    global expression
    
    x=float(expression)
    co=str(math.cos(x))
    equation.set(co)
    expression=""

def tangent():
    global expression
    
    x=float(expression)
    ta=str(math.tan(x))
    equation.set(ta)
    expression=""
    
def sineh():
    global expression
    
    x=float(expression)
    sih=str(math.sinh(x))
    equation.set(sih)
    expression=""
    
def cosineh():
    global expression
    
    x=float(expression)
    coh=str(math.cosh(x))
    equation.set(coh)
    expression=""

def tangenth():
    global expression
    
    x=float(expression)
    tah=str(math.tanh(x))
    equation.set(tah)
    expression=""    
    
def currency():
    global expression
    global rte
    global etr
    global rtp
    global ptr
    global rtu
    global utr
    global rtc
    global ctr
    global rty
    global ytr
    global rtye
    global yetr
    global plus
    global minus
    global mult
    global div
    global facto
    global sqr
    global exp
    global msine
    global mcos
    global mtan
    global msinh
    global mcosh
    global mtanh
    global vpi
    global ve
    global brack1
    global brack2
    global calc
    global currcon
    
    def rte():
        global expression
    
        exp=float(expression)
        euro=0.012*exp
        equation.set(euro)
    
    def etr():
        global expression
    
        exp=float(expression)
        rupee=85.54*exp
        equation.set(rupee)

    def rtp():
        global expression
    
        exp=float(expression)
        pound=0.010*exp
        equation.set(pound)

    def ptr():
        global expression
    
        exp=float(expression)
        rupee=95.40*exp
        equation.set(rupee)
        
    def rtu():
        global expression
    
        exp=float(expression)
        usd=0.013*exp
        equation.set(usd)

    def utr():
        global expression
    
        exp=float(expression)
        rupee=76.01*exp
        equation.set(rupee)
    
    def rtc():
        global expression
    
        exp=float(expression)
        cd=0.018*exp
        equation.set(cd)

    def ctr():
        global expression
    
        exp=float(expression)
        rupee=55.73*exp
        equation.set(rupee)
        
    def rty():
        global expression
        
        exp=float(expression)
        rupee=0.093*exp
        equation.set(rupee)

    def ytr():
        global expression
        
        exp=float(expression)
        yuan=10.76*exp
        equation.set(yuan)
    
    def rtye():
        global expression
        
        exp=float(expression)
        rupee=1.41*exp
        equation.set(rupee)

    def yetr():
        global expression
    
        exp=float(expression)
        yen=0.71*exp
        equation.set(yen)
        
    plus.destroy()
    minus.destroy()
    mult.destroy()
    div.destroy()
    facto.destroy()
    sqr.destroy()
    exp.destroy()
    msine.destroy()
    mcos.destroy()
    mtan.destroy()
    msinh.destroy()
    mcosh.destroy()
    mtanh.destroy()
    vpi.destroy()
    ve.destroy()
    brack1.destroy()
    brack2.destroy()
    currcon.destroy()
        
    rte= Button(gui,text='Rs. to eur',fg='white',bg='black',
                command=rte,height=1,width=7,
                activebackground='dim gray')
    rte.grid(row=6,column=0)
    
    etr= Button(gui,text='eur to Rs',fg='white',bg='black',
                command=etr,height=1,width=7,
                activebackground='dim gray')
    etr.grid(row=6,column=1)

    rtp= Button(gui,text='Rs to Pds',fg='white',bg='black',
                command=rtp,height=1,width=7,
                activebackground='dim gray')
    rtp.grid(row=6,column=3)
    
    ptr= Button(gui,text='Pds to Rs',fg='white',bg='black',
                command=ptr,height=1,width=7,
                activebackground='dim gray')
    ptr.grid(row=6,column=4)
    
    rtu= Button(gui,text='Rs to $',fg='white',bg='black',
                command=rtu,height=1,width=7,
                activebackground='dim gray')
    rtu.grid(row=8,column=0)
    
    utr= Button(gui,text='$ to Rs',fg='white',bg='black',
                command=utr,height=1,width=7,
                activebackground='dim gray')
    utr.grid(row=8,column=1)
    
    rtc= Button(gui,text='Rs to can',fg='white',bg='black',
                command=rtc,height=1,width=7,
                activebackground='dim gray')
    rtc.grid(row=8,column=3)

    ctr= Button(gui,text='can to Rs',fg='white',bg='black',
                command=ctr,height=1,width=7,
                activebackground='dim gray')
    ctr.grid(row=8,column=4)
    
    rty= Button(gui,text='Rs to Yuan',fg='white',bg='black',
                command=rty,height=1,width=7,
                activebackground='dim gray')
    rty.grid(row=9,column=0)
    
    ytr= Button(gui,text='Yuan to Rs',fg='white',bg='black',
                command=ytr,height=1,width=7,
                activebackground='dim gray')
    ytr.grid(row=9,column=1)
    
    rtye= Button(gui,text='Rs to Yen',fg='white',bg='black',
                 command=rtye,height=1,width=7,
                 activebackground='dim gray')
    rtye.grid(row=9,column=3)
    
    yetr= Button(gui,text='Yen to Rs',fg='white',bg='black',
                 command=yetr,height=1,width=7,
                 activebackground='dim gray')
    yetr.grid(row=9,column=4)
        
    calc= Button(gui,text='Calc',fg='black',bg='dark goldenrod',
                 comman=main,height=1,width=7,
                 activebackground='goldenrod')
    calc.grid(row=3,column=5)

def main():
    global rte
    global etr
    global rtp
    global ptr
    global rtu
    global utr
    global rtc
    global ctr
    global rty
    global ytr
    global rtye
    global yetr
    global plus
    global minus
    global mult
    global div
    global facto
    global sqr
    global exp
    global msine
    global mcos
    global mtan
    global msinh
    global mcosh
    global mtanh
    global vpi
    global ve
    global brack1
    global brack2
    global calc
    global currcon
    
    rte.destroy()
    etr.destroy()
    rtp.destroy()
    ptr.destroy()
    rtu.destroy()
    utr.destroy()
    rtc.destroy()
    ctr.destroy()
    rty.destroy()
    ytr.destroy()
    rtye.destroy()
    yetr.destroy()
    calc.destroy()
        
    button1= Button(gui,text='1',fg='white',bg='blue',
                    command=lambda: enter(1),height=1,width=7,
                    activebackground='powder blue')
    button1.grid(row=2,column=0)
    
    button2= Button(gui,text='2',fg='white',bg='blue',
                    command=lambda: enter(2),height=1,width=7,
                    activebackground='powder blue')
    button2.grid(row=2,column=1)
    
    button3= Button(gui,text='3',fg='white',bg='blue',
                    command=lambda: enter(3),height=1,width=7,
                    activebackground='powder blue')
    button3.grid(row=2,column=2)
    
    button4= Button(gui,text='4',fg='white',bg='blue',
                    command=lambda: enter(4),height=1,width=7,
                    activebackground='powder blue')
    button4.grid(row=3,column=0)
    
    button5= Button(gui,text='5',fg='white',bg='blue',
                    command=lambda: enter(5),height=1,width=7,
                    activebackground='powder blue')
    button5.grid(row=3,column=1)
    
    button6= Button(gui,text='6',fg='white',bg='blue',
                    command=lambda: enter(6),height=1,width=7,
                    activebackground='powder blue')
    button6.grid(row=3,column=2)
    
    button7= Button(gui,text='7',fg='white',bg='blue',
                    command=lambda: enter(7),height=1,width=7,
                    activebackground='powder blue')
    button7.grid(row=4,column=0)
    
    button8= Button(gui,text='8',fg='white',bg='blue',
                    command=lambda: enter(8),height=1,width=7,
                    activebackground='powder blue')
    button8.grid(row=4,column=1)
    
    button9= Button(gui,text='9',fg='white',bg='blue',
                    command=lambda: enter(9),height=1,width=7,
                    activebackground='powder blue')
    button9.grid(row=4,column=2)
    
    button0= Button(gui,text='0',fg='white',bg='blue',
                    command=lambda: enter(0),height=1,width=7,
                    activebackground='powder blue')
    button0.grid(row=5,column=0)
    
    dot= Button(gui,text='.',fg='white',bg='blue',
                command=lambda: enter("."),height=1,width=7,
                activebackground='powder blue')
    dot.grid(row=5,column=1)
    
    equal= Button(gui,text='=',fg='white',bg='blue',
                  command=equalto,height=1,width=7,
                  activebackground='powder blue')
    equal.grid(row=5,column=2)
    
    plus= Button(gui,text='+',fg='white',bg='blue',
                 command=lambda: enter("+"),height=1,width=7,
                 activebackground='powder blue')
    plus.grid(row=2,column=3)
    
    minus= Button(gui,text='-',fg='white',bg='blue',
                  command=lambda: enter("-"),height=1,width=7,
                  activebackground='powder blue')
    minus.grid(row=3,column=3)
    
    mult= Button(gui,text='*',fg='white',bg='blue',
                 command=lambda: enter("*"),height=1,width=7,
                 activebackground='powder blue')
    mult.grid(row=4,column=3)
    
    div= Button(gui,text='/',fg='white',bg='blue',
                command=lambda: enter("/"),height=1,width=7,
                activebackground='powder blue')
    div.grid(row=5,column=3)
    
    clear= Button(gui,text='AC',fg='black',bg='dark orange',
                  command=clrscr,height=1,width=7,
                  activebackground='powder blue')
    clear.grid(row=2,column=5)
    
    facto= Button(gui,text='Factorial',fg='black',bg='white',
                  command=fact,height=1,width=7,
                  activebackground='powder blue')
    facto.grid(row=3,column=4)
    
    sqr= Button(gui,text='Root',fg='black',bg='white',
                command=root,height=1,width=7,
                activebackground='powder blue')
    sqr.grid(row=4,column=4)
    
    exp= Button(gui,text='**',fg='black',bg='white',
                command=lambda: enter("**"),height=1,width=7,
                activebackground='powder blue')
    exp.grid(row=5,column=4)
    
    msine= Button(gui,text='sine()',fg='white',bg='black',
                  command=sine,height=1,width=7
                  ,activebackground='powder blue')
    msine.grid(row=6,column=0)
    
    mcos= Button(gui,text='cos()',fg='white',bg='black',
                  command=cosine,height=1,width=7,
                  activebackground='powder blue')
    mcos.grid(row=6,column=1)
    
    mtan= Button(gui,text='tan()',fg='white',bg='black',
                  command=tangent,height=1,width=7
                  ,activebackground='powder blue')
    mtan.grid(row=6,column=2)  
    
    msinh= Button(gui,text='sinh()',fg='white',bg='black',
                  command=sineh,height=1,width=7,
                  activebackground='powder blue')
    msinh.grid(row=7,column=0)
    
    mcosh= Button(gui,text='cosh()',fg='white',bg='black',
                  command=cosineh,height=1,width=7,
                  activebackground='powder blue')
    mcosh.grid(row=7,column=1)
    
    mtanh= Button(gui,text='tanh()',fg='white',bg='black',
                  command=tangenth,height=1,width=7,
                  activebackground='powder blue')
    mtanh.grid(row=7,column=2)
    
    vpi= Button(gui,text='π',fg='white',bg='red',
                command=lambda: enter(3.14159),height=1,width=4,
                activebackground='powder blue')
    vpi.grid(row=3,column=5)
    
    ve= Button(gui,text='e',fg='white',bg='red',
               command=lambda: enter(2.71828),height=1,width=4,
               activebackground='powder blue')
    ve.grid(row=4,column=5)
    
    brack1= Button(gui,text='(',fg='black',bg='yellow',
                   command=lambda: enter("("),height=1,width=2,
                   activebackground='powder blue')
    brack1.grid(row=5,column=5)
    brack2= Button(gui,text=')',fg='black',bg='yellow',
                   command=lambda: enter(")"),height=1,width=2,
                   activebackground='powder blue')
    brack2.grid(row=5,column=6)
    
    currcon= Button(gui,text='Currency',fg='black',bg='dark goldenrod',
                    command=currency,height=1,width=7,
                    activebackground='goldenrod')
    currcon.grid(row=6,column=5)
  
if __name__=="__main__":

#making basic window using tkinter
    gui=tkinter.Tk()
    equation=StringVar()

#defining basic window's dimensions,etc. 
    gui.configure(background="grey")
    gui.title('Simple Calculator')
    gui.geometry('375x200')
        
#setting the entry box for user input
    text_ip=Entry(gui,justify='left'
                  ,textvariable=equation)
    text_ip.grid(columnspan=5, ipadx=75)
    
    equation.set('')
    
    button1= Button(gui,text='1',fg='white',bg='blue',
                    command=lambda: enter(1),height=1,width=7,
                    activebackground='powder blue')
    button1.grid(row=2,column=0)
    
    button2= Button(gui,text='2',fg='white',bg='blue',
                    command=lambda: enter(2),height=1,width=7,
                    activebackground='powder blue')
    button2.grid(row=2,column=1)
    
    button3= Button(gui,text='3',fg='white',bg='blue',
                    command=lambda: enter(3),height=1,width=7,
                    activebackground='powder blue')
    button3.grid(row=2,column=2)
    
    button4= Button(gui,text='4',fg='white',bg='blue',
                    command=lambda: enter(4),height=1,width=7,
                    activebackground='powder blue')
    button4.grid(row=3,column=0)
    
    button5= Button(gui,text='5',fg='white',bg='blue',
                    command=lambda: enter(5),height=1,width=7,
                    activebackground='powder blue')
    button5.grid(row=3,column=1)
    
    button6= Button(gui,text='6',fg='white',bg='blue',
                    command=lambda: enter(6),height=1,width=7,
                    activebackground='powder blue')
    button6.grid(row=3,column=2)
    
    button7= Button(gui,text='7',fg='white',bg='blue',
                    command=lambda: enter(7),height=1,width=7,
                    activebackground='powder blue')
    button7.grid(row=4,column=0)
    
    button8= Button(gui,text='8',fg='white',bg='blue',
                    command=lambda: enter(8),height=1,width=7,
                    activebackground='powder blue')
    button8.grid(row=4,column=1)
    
    button9= Button(gui,text='9',fg='white',bg='blue',
                    command=lambda: enter(9),height=1,width=7,
                    activebackground='powder blue')
    button9.grid(row=4,column=2)
    
    button0= Button(gui,text='0',fg='white',bg='blue',
                    command=lambda: enter(0),height=1,width=7,
                    activebackground='powder blue')
    button0.grid(row=5,column=0)
    
    dot= Button(gui,text='.',fg='white',bg='blue',
                command=lambda: enter("."),height=1,width=7,
                activebackground='powder blue')
    dot.grid(row=5,column=1)
    
    equal= Button(gui,text='=',fg='white',bg='blue',
                  command=equalto,height=1,width=7,
                  activebackground='powder blue')
    equal.grid(row=5,column=2)
    
    plus= Button(gui,text='+',fg='white',bg='blue',
                 command=lambda: enter("+"),height=1,width=7,
                 activebackground='powder blue')
    plus.grid(row=2,column=3)
    
    minus= Button(gui,text='-',fg='white',bg='blue',
                  command=lambda: enter("-"),height=1,width=7,
                  activebackground='powder blue')
    minus.grid(row=3,column=3)
    
    mult= Button(gui,text='*',fg='white',bg='blue',
                 command=lambda: enter("*"),height=1,width=7,
                 activebackground='powder blue')
    mult.grid(row=4,column=3)
    
    div= Button(gui,text='/',fg='white',bg='blue',
                command=lambda: enter("/"),height=1,width=7,
                activebackground='powder blue')
    div.grid(row=5,column=3)
    
    clear= Button(gui,text='AC',fg='black',bg='dark orange',
                  command=clrscr,height=1,width=7,
                  activebackground='powder blue')
    clear.grid(row=2,column=5)
    
    facto= Button(gui,text='Factorial',fg='black',bg='white',
                  command=fact,height=1,width=7,
                  activebackground='powder blue')
    facto.grid(row=3,column=4)
    
    sqr= Button(gui,text='Root',fg='black',bg='white',
                command=root,height=1,width=7,
                activebackground='powder blue')
    sqr.grid(row=4,column=4)
    
    exp= Button(gui,text='**',fg='black',bg='white',
                command=lambda: enter("**"),height=1,width=7,
                activebackground='powder blue')
    exp.grid(row=5,column=4)
    
    msine= Button(gui,text='sine()',fg='white',bg='black',
                  command=sine,height=1,width=7
                  ,activebackground='powder blue')
    msine.grid(row=6,column=0)
    
    mcos= Button(gui,text='cos()',fg='white',bg='black',
                  command=cosine,height=1,width=7,
                  activebackground='powder blue')
    mcos.grid(row=6,column=1)
    
    mtan= Button(gui,text='tan()',fg='white',bg='black',
                  command=tangent,height=1,width=7
                  ,activebackground='powder blue')
    mtan.grid(row=6,column=2)  
    
    msinh= Button(gui,text='sinh()',fg='white',bg='black',
                  command=sineh,height=1,width=7,
                  activebackground='powder blue')
    msinh.grid(row=7,column=0)
    
    mcosh= Button(gui,text='cosh()',fg='white',bg='black',
                  command=cosineh,height=1,width=7,
                  activebackground='powder blue')
    mcosh.grid(row=7,column=1)
    
    mtanh= Button(gui,text='tanh()',fg='white',bg='black',
                  command=tangenth,height=1,width=7,
                  activebackground='powder blue')
    mtanh.grid(row=7,column=2)
    
    vpi= Button(gui,text='π',fg='white',bg='red',
                command=lambda: enter(3.14159),height=1,width=4,
                activebackground='powder blue')
    vpi.grid(row=3,column=5)
    
    ve= Button(gui,text='e',fg='white',bg='red',
               command=lambda: enter(2.71828),height=1,width=4,
               activebackground='powder blue')
    ve.grid(row=4,column=5)
    
    brack1= Button(gui,text='(',fg='black',bg='yellow',
                   command=lambda: enter("("),height=1,width=2,
                   activebackground='powder blue')
    brack1.grid(row=5,column=5)
    brack2= Button(gui,text=')',fg='black',bg='yellow',
                   command=lambda: enter(")"),height=1,width=2,
                   activebackground='powder blue')
    brack2.grid(row=5,column=6)
    
    currcon= Button(gui,text='Currency',fg='black',bg='dark goldenrod',
                    command=currency,height=1,width=7,
                    activebackground='goldenrod')
    currcon.grid(row=6,column=5)


 
 #calling main loop    
    gui.mainloop()    
