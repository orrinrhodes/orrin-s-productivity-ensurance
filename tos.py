import os.path
from tkinter import *
from pynput.mouse import Button as Key, Controller #tkinter button
mouse = Controller()

#get Isaac -- absolutely essential for QoL tings
cd = os.getcwd();
icon = cd+'\\tos\isaacicon.ico'

widget = Tk()
widget.iconbitmap(icon)

ws = widget.winfo_screenwidth()
hs = widget.winfo_screenheight()
#print(ws,'x', hs)

#get Isaac
cd = os.getcwd()
icon = cd+'\\tos\images\isaacicon.ico'

#pretty colors
widget.title('Productivity')
bg = 'green'
fg = 'yellow'
box = Label(
    widget,
    text='BE PRODUCTIVE',
    font=('digital numbers',20),
    background = bg, foreground=fg
    )
box.pack(anchor='center')
box.master.wm_attributes('-alpha',0.9)
#borderlesss
box.master.overrideredirect(True)

#function
def exit():
    widget.destroy()

def msg():
    print('hey lol')

exit1 = Button(widget, text='Click to exit', command=exit)
exit1.pack(pady=2)

#above all
box.master.wm_attributes('-topmost',True)
box.master.lift()

#position
x = 200; y = 200
def pos():
    mpos = mouse.position
    new = '{0}x{1}+{2}+{3}'.format(x,y,round(mpos[0]-x/2),round(mpos[1]-y/2))
    widget.geometry(new)
    widget.after(1,pos)
pos()
#GO
widget.mainloop()


if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
if str(type(True))=="<class 'bool'>" and True!=False:
    print(True,'is True!')
