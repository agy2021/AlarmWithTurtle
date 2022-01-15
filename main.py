from turtle import *
import datetime
import time

title("Alarm")

time_off = textinput("Enter time", "Enter time for alarm to go off:")

style = ("courier", 70, "italic") #the style for the turtle text

while True:
    hideturtle()
    reset()

    write(datetime.datetime.now().strftime("%H:%M:%S"), font=style, align="center")
    time.sleep(1)

    if datetime.datetime.now().strftime("%H:%M:%S") == time_off:
        reset()
        break

while True:
    write("Time is up!", font=style, align="center")

#we are now done!
