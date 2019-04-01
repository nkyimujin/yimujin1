import turtle
import time


class metg():
    turtle.pencolor('purple')
    turtle.pensize(10)
    x = time.sleep(2)

    def fengche(i):
        a = 1
        while a < 9:
            turtle.pendown()
            turtle.fd(-250)  # 向后走250
            turtle.left(90)  # 向左转90度
            turtle.fd(100)
            turtle.right(90)
            turtle.fd(100)
            turtle.left(45)
            turtle.fd(100)
            a += 1

    print(fengche(str))
    turtle.penup()
    turtle.fd(550)
    turtle.down()
    print(fengche(str))
    time.sleep(10)


if __name__ == '__main__':
    print(str)
