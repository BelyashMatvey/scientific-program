from PIL import Image
from PIL import ImageTk
import tkinter as tk
import math
import time
import random
import pyautogui as pya
def clicker():
    pya.click(x=500,y=500,clicks=5,interval=2.0)
deg=0
pilimage=Image.open('izo4.png')
newsize=(470,400)
pilimage=pilimage.resize(newsize)
pilimage.save('izo4.png')
def window1():
    poetry="Эта программа написана исключительно в научных целях.\nПоэтому копирование и использование \nэтой программы производится только с раз-\nрешения правообладателя.\n\n\t\tПравообладатель-Belyash."
    window=tk.Tk()
    window.title("Правила пользования")
    label2 = tk.Label(text=poetry, font="Courier 20")
    label2.place(relx=.2, rely=.3)
    btn=tk.Button(text="Я принимаю условия пользования", background="#555", foreground="#ccc",padx="20", pady="8", font="16", command=lambda:window.destroy())
    btn.pack()
    label2.pack()
    window.mainloop()
def window2():
    global root, line_2, canv, px, py, ox, oy,ox1,error
    root = tk.Tk()
    canv = tk.Canvas(root, width=600, height=400, bg="white")
    image=ImageTk.PhotoImage(pilimage)
    imagesprite=canv.create_image(300,250,image=image)
    px, py, ox, oy = 420,315,random.randint(310,400),264  #295
    line_2 = canv.create_line(px, py, ox, oy, width=4, fill="grey")
    root.title("Эксперимент")
    canv.focus_set()
    canv.pack()
    root.after(12000,lambda x=1:root.destroy())
    f.write(str(px)+" "+str(py)+"     "+str(ox)+" "+str(oy))
    root.bind("<space>", lambda event: quit(root))
    canv.bind("<Right>", lambda event: turner('right'))
    canv.bind("<Left>", lambda event: turner('left'))
    root.mainloop()
def turner(angle):
    deg = 0
    global px,py,ox,oy,ox1
    if angle=='right':
        deg=deg-0.25
        theta = math.radians(deg)
        cosang, sinang = math.cos(theta), math.sin(theta)
    elif angle=='left':
        deg=deg+0.25
        theta=math.radians(deg)
        cosang, sinang = math.cos(theta), math.sin(theta)
    tx, ty = ox - px, oy - py
    ox = (tx * cosang + ty * sinang) + px
    global error
    if 368>ox:
        error=str(int(368-ox))+"-"
    else:
        error=str(int(ox-368))+"+"
    #oy = (-tx * sinang + ty * cosang) + py
    global line_2
    canv.coords(line_2, px, py, ox, oy)
f=open("output.txt","w")
window1()
for i in range(2):
    window2()
    f.write("\n"+str(round(px))+" "+str(round(py))+"     "+str(round(ox))+" "+str(round(oy))+"      "+error+"\n"+"\n"+"\n"+"\n")


f.close()