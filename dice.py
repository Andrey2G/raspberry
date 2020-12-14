import RPi.GPIO as IO            # calling for header file which helps us use GPIO’s of PI
import time                              # calling for time to provide delays in program
from random import seed
from random import randint


seed(1)

DISPLAY = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67]            # string of characters storing PORT values for each digit.

#SNAKE = [0x1,0x2,0x3,0x4,0x5,0x6,]
IO.setwarnings(False)            # do not show any warnings
IO.setmode (IO.BCM)           # programming the GPIO by BCM pin numbers. (like PIN29 as‘GPIO5’)

IO.setup(15,IO.IN, pull_up_down=IO.PUD_DOWN)
IO.setup(13,IO.OUT)             # initialize GPIO Pins as outputs
IO.setup(6,IO.OUT)
IO.setup(16,IO.OUT)
IO.setup(20,IO.OUT)
IO.setup(21,IO.OUT)
IO.setup(19,IO.OUT)
IO.setup(26,IO.OUT)
IO.setup(12,IO.OUT)


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





def DICE():
    value=randint(1,6)
    return value

def PORT(pin):                    # assigning GPIO logic by taking 'pin' value
    if(pin&0x01 == 0x01):
        IO.output(13,1)            # if  bit0 of 8bit 'pin' is true, pull PIN13 high
    else:
        IO.output(13,0)            # if  bit0 of 8bit 'pin' is false, pull PIN13 low
    if(pin&0x02 == 0x02):
        IO.output(6,1)             # if  bit1 of 8bit 'pin' is true, pull PIN6 high
    else:
        IO.output(6,0)            #if  bit1 of 8bit 'pin' is false, pull PIN6 low
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
        IO.output(12,1)            # if  bit7 of 8bit 'pin' is true, pull PIN12 high
    else:
        IO.output(12,0)            # if  bit7 of 8bit 'pin' is false, pull PIN12 low


def START():
    if IO.input(15) == IO.HIGH: 
        return True
    else:
        return False


#while 1:
#    if IO.input(10) == IO.HIGH :
#        break

SNAKE(0)

while True:
    if START():
        break

qty=1
while 1:
     SNAKE(qty)
     qty=qty+1
     time.sleep(0.1)
     if qty == 7: qty = 1
     

#    for x in range(10):
#        pin=DISPLAY[x]
#        PORT(pin);
        #time.sleep(0.3)

