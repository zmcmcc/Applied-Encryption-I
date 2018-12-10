#This script draws a ugly bird face,
#which is a simplified imitation from
#http://goinkscape.com/how-to-draw-a-cartoon-turkey/
import turtle

turtle.screensize(200, 150, "white")
turtle.speed(0)
turtle.hideturtle()

turtle.home()
turtle.pensize(2)# pen size

#face outline
turtle.fillcolor('brown')
turtle.begin_fill()
turtle.circle(100,360)
turtle.end_fill()
turtle.penup()


#two eyes' outline
turtle.goto(-35,90)
turtle.pendown()
turtle.fillcolor('white')
turtle.begin_fill()
turtle.circle(25,360)
turtle.end_fill()
turtle.penup()

turtle.goto(35,90)
turtle.pendown()
turtle.fillcolor('white')
turtle.begin_fill()
turtle.circle(25,360)
turtle.end_fill()
turtle.penup()

#two eyeballs 
turtle.goto(-30,105)
turtle.pendown()
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(8,360)
turtle.end_fill()
turtle.penup()

turtle.goto(30,105)
turtle.pendown()
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(8,360)
turtle.end_fill()
turtle.penup()

#The beak
turtle.goto(0,20)
turtle.left(70)
turtle.pendown()
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.forward(60)
turtle.goto(0,20)
turtle.right(320)
turtle.forward(60)

turtle.right(90)
for i in range(40):
    turtle.forward(1)
    turtle.right(1)

turtle.end_fill()


