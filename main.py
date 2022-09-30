import pyautogui
from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as tkFont
import time


root = Tk()
root.title('Sendmote v1.0')
x,y=450,550
root.geometry("%dx%d" %(x,y))
#root['bg'] = '#c7c7c7'

xx,yy=0,0

def key_pressed(event):
    if(event.char == "x"):
        global xx,yy
        w=Label(root,text="cursor coordinates: "+str(pyautogui.position()))
        w.place(x=130,y=10)
        xx,yy=pyautogui.position()

def move():
        pyautogui.moveTo(x=int(xx),y=int(yy))

def emote(n):
        pyautogui.click(int(xx),int(yy))
        if (n == 0):
                pyautogui.write("Cringe")
        if (n == 1):
                pyautogui.write("MmmHmm")
        if (n == 2):
                pyautogui.write("pepeJAM")
        if (n == 3):
                pyautogui.write("OkayChamp")
        if (n == 4):
                pyautogui.write("pepeFASTJAM ")
        if (n == 5):
                pyautogui.write("cmonBrug")
        if (n == 6):
                pyautogui.write("ANELEpls")
        if (n == 7):
                pyautogui.write("PogU")
        if (n == 8):
                pyautogui.write("PogO")
        if (n == 9):
                pyautogui.write("WeirdChamping")
        if (n == 10):
                pyautogui.write("Madge")
        if (n == 11):
                pyautogui.write("TROLL")
        if (n == 12):
                pyautogui.write("monkaW")
        if (n == 13):
                pyautogui.write("PepoG")
        if (n == 14):
                pyautogui.write("5Head")
        if (n == 15):
                pyautogui.write("PeepoGlad")
        if (n == 16):
                pyautogui.write("2Head")
        if (n == 17):
                pyautogui.write("PepeCringe")
        if (n == 18):
                pyautogui.write("Sadge")
        if (n == 19):
                pyautogui.write("Sadeg")
        if (n == 20):
                pyautogui.write("PauseChamp")
        if (n == 21):
                pyautogui.write("Clueless")
        if (n == 22):
                pyautogui.write("HarambeEZ")
        if (n == 23):
                pyautogui.write("HarambeLove")
        if (n == 24):
                pyautogui.write("MeArmy")
        if (n == 25):
                pyautogui.write("lebronJAM")

        pyautogui.typewrite(["Enter"])


def emote2(n):
        return lambda :emote(n)

l=0
for i in range(5):
        for j in range(5):
                image = Image.open("emotes\%s.png" % l)
                resize_image = image.resize((25, 25))
                globals()['key%s' % l] = ImageTk.PhotoImage(resize_image)
                globals()['button%s' % l] = Button(root, image=globals()['key%s' % l], command =emote2(l)).place(x=60*(i+1),y=60*(j+2))
                l+=1

t1 = Label(root, text = "Move the cursor over the field send a message,",font = tkFont.Font(family="Arial", size=8), fg="black").place(x=15,y=y-50)

t2 = Label(root, text = "then press the x key (without mouse clicking)",font = tkFont.Font(family="Arial", size=8), fg="black").place(x=15,y=y-30)

b1 = Button(root, text = "check",command=move).place(x=60,y=7)

root.bind("<Key>",key_pressed)

root.mainloop()

