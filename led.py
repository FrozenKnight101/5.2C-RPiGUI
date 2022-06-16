from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

red = LED(18)
blue = LED(23)
green = LED(24)

win = Tk()
win.title("Led GUI")
myFont = (tkinter.font.Font(family = 'Helvetica', size=20, weight="bold"))

def Red_LED():
    if red.is_lit:
        red.off()
        red_Button["text"] = "Red"
    else:
        red.on()
        blue.off()
        green.off()

def Blue_LED():
    if blue.is_lit:
        blue.off()
        blue_Button["text"] = "Blue"
    else:
        blue.on()
        red.off()
        green.off()

def Green_LED():
    if green.is_lit:
        green.off()
        green_Button["text"] = "Green"
    else:
        red.off()
        blue.off()
        green.on()
        
def complete():
    GPIO.cleanup()
    win.destroy()
    
red_Button= Button(win, text='Red', font= myFont, command= Red_LED, bg='red', height = 2, width= 25)
red_Button.grid(row=0, column=1)

blue_Button= Button(win, text='Blue', font= myFont, command= Blue_LED, bg='blue', height = 2, width= 25)
blue_Button.grid(row=1, column=1)

green_Button= Button(win, text='Green', font= myFont, command= Green_LED, bg='green', height = 2, width= 25)
green_Button.grid(row=2, column=1)

exit_Button= Button(win, text='Exit', font= myFont, command= complete, bg='white', height = 2, width= 25)
exit_Button.grid(row=3, column=1)

win.protocol("WM_DELETE_WINDOW", complete)
win.mainloop()