
import board
import neopixel
import random
import touchio
from ncount import *
from prt import *
import time
REPL = True


# set up touch for input
touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

if REPL == False:
     Val = 0
     while Val == 0:
        compthink()
        if touch1.value:
            Val = Val +1
        if touch2.value:
            Val = Val +2

#from SWBrain import * #for Star Wars dataset
from STBrain import *  #for Star Trek dataset


oops = ["Well, dang!","Hmmm", "Maybe you should talk to my programmer!"]

while True:
    prt(Words[0],REPL)

    Done = False

    node = 1

    while not Done:
        prt(Words[node]+"?",REPL)



        answer = ""

        while answer == "":


            Val = 0
            if touch1.value:
                Val = Val +1
                touched = time.monotonic()
            if touch2.value:
                Val = Val +2
                touched = time.monotonic()

            if Val == 1:
                answer = "y"
                node = Yes[node]
                prt("Yes",REPL)
                time.sleep(.5)
                if node == 0:
                    prt("I was right!",REPL)
            if Val == 2:
                answer = "n"
                prt("No",REPL)
                time.sleep(.5)
                node = No[node]
                if node == 0:
                    prt(random.choice(oops),REPL)

        compthink()

        if node == 0:
            time.sleep(1)
            prt("let's try again",REPL)
            time.sleep(1)
            Done = True

