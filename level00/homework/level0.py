from turtle import*


#we want to paint a house

#step 1:  draw a square
speed(2)
width(10)
color("gray")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#end of square
 
forward(70)
color("black")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("green")
right(150)
forward(200)

left(120)
forward(200)

exitonclick()
