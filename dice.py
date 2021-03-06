import RPi.GPIO as IO        
import time       
from random import seed
from random import randint

DISPLAY = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67]
global inLoop
inLoop = True

def SETUP():
    print("setup")
    seed(1)
    IO.setwarnings(False)           
    IO.setmode (IO.BCM)           
    IO.setup(15,IO.IN, pull_up_down=IO.PUD_DOWN)
    IO.setup(13,IO.OUT)           
    IO.setup(6,IO.OUT)
    IO.setup(16,IO.OUT)
    IO.setup(20,IO.OUT)
    IO.setup(21,IO.OUT)
    IO.setup(19,IO.OUT)
    IO.setup(26,IO.OUT)
    IO.setup(12,IO.OUT)
    IO.add_event_detect(15, IO.RISING,callback=result_ready)
    SNAKE(0)

def result_ready(self):
    print("ready result")
    print(self)
    if self !=15:
        print("try o stop the loop")
        global inLoop
        inLoop=False
    

def SNAKE(qty):   
    if qty == 0:
        IO.output(13,0); IO.output(6,0); IO.output(16,0); IO.output(20,0); IO.output(21,0); IO.output(19,0); IO.output(26,0)
    elif qty == 1:
        IO.output(13,1); IO.output(6,0); IO.output(16,0); IO.output(20,0); IO.output(21,0); IO.output(19,0); IO.output(26,0)
    elif qty == 2:
        IO.output(13,0); IO.output(6,1); IO.output(16,0); IO.output(20,0); IO.output(21,0); IO.output(19,0); IO.output(26,0)
    elif qty == 3:
        IO.output(13,0); IO.output(6,0); IO.output(16,1); IO.output(20,0); IO.output(21,0); IO.output(19,0); IO.output(26,0)
    elif qty == 4:
        IO.output(13,0); IO.output(6,0); IO.output(16,0); IO.output(20,1); IO.output(21,0); IO.output(19,0); IO.output(26,0)
    elif qty == 5:
        IO.output(13,0); IO.output(6,0); IO.output(16,0); IO.output(20,0); IO.output(21,1); IO.output(19,0); IO.output(26,0)
    elif qty == 6:
        IO.output(13,0); IO.output(6,0); IO.output(16,0); IO.output(20,0); IO.output(21,0); IO.output(19,1); IO.output(26,0)

def randomDICE():
    value=randint(1,6)
    return value

def PORT(pin):                   
    if(pin&0x01 == 0x01):
        IO.output(13,1)          
    else:
        IO.output(13,0)          
    if(pin&0x02 == 0x02):
        IO.output(6,1)           
    else:
        IO.output(6,0)           
    if(pin&0x04 == 0x04):
        IO.output(16,1)
    else:
        IO.output(16,0)
    if(pin&0x08 == 0x08):
        IO.output(20,1)
    else:
        IO.output(20,0)   
    if(pin&0x10 == 0x10):
        IO.output(21,1)
    else:
        IO.output(21,0)
    if(pin&0x20 == 0x20):
        IO.output(19,1)
    else:
        IO.output(19,0)
    if(pin&0x40 == 0x40):
        IO.output(26,1)
    else:
        IO.output(26,0)
    if(pin&0x80 == 0x80):
        IO.output(12,1)          
    else:
        IO.output(12,0)          

def display_result(value):
    inLoop = False
    print("display result")
    print(value)    
    pin=DISPLAY[int(value)]
    PORT(pin)



def START():
    if IO.input(15) == IO.HIGH: 
        return True
    else:
        return False
