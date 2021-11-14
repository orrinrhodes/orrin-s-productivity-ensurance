print('hey lol');

import os.path
from tkinter import *

#get Isaac
cd = os.getcwd();
icon = cd+'\\tos\images\isaacicon.ico'

#tos app
tos = Tk();
#QoL tings
tos.title('ToS Simulator');
tos.iconbitmap(icon);

tos.geometry('500x500+500+1000')

#GO!
tos.mainloop();