# import turtle
# import time
# turtle.pensize(2)
# turtle.circle(10)
# turtle.circle(20)
# turtle.circle(40)
# turtle.circle(80)
# turtle.circle(100)
# time.sleep(20)

import turtle
import time
import os

for i in range(100):
    turtle.circle(10 + 1 + i)
    turtle.right(90)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    # turtle.left(90)
# time.sleep(i)
