import turtle

turtle.speed(5)

# Corpo
turtle.color("gold")
turtle.begin_fill()
turtle.goto(1,1)
turtle.goto(150,1)
turtle.goto(75,150)
turtle.goto(1,1)
turtle.end_fill()

# Olho
turtle.penup()
turtle.color("black")
turtle.fillcolor("white")

turtle.begin_fill()
turtle.goto(75,50)
turtle.pendown()
turtle.pensize(2)
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(75,60)
turtle.pendown()
turtle.pensize(5)
turtle.goto(75,90)

# Cílios
turtle.penup()
turtle.goto(62,98)
turtle.pendown()
turtle.goto(57,103)

turtle.penup()
turtle.goto(75,100)
turtle.pendown()
turtle.goto(75,110)

turtle.penup()
turtle.goto(88,98)
turtle.pendown()
turtle.goto(93,103)

turtle.penup()
turtle.goto(75,50)
turtle.pendown()
turtle.goto(75,40)

turtle.penup()
turtle.goto(62,52)
turtle.pendown()
turtle.goto(57,47)

turtle.up()
turtle.goto(91,52)
turtle.down()
turtle.goto(95,46)

# Cartola
turtle.penup()
turtle.goto(65,150)
turtle.pendown()
turtle.pensize(3)
turtle.color("black")

turtle.begin_fill()
turtle.goto(85,150)
turtle.goto(85,160)
turtle.goto(80,160)
turtle.goto(80,210)
turtle.goto(70,210)
turtle.goto(70,160)
turtle.goto(65,160)
turtle.goto(65,150)
turtle.end_fill()

# Pernas
turtle.penup()
turtle.goto(60,0)
turtle.pensize(5)

turtle.pendown()
turtle.goto(60,-25)
turtle.goto(68,-20)
turtle.goto(68,-35)

turtle.penup()
turtle.goto(85,0)

turtle.pendown()
turtle.goto(85,-25)
turtle.goto(77,-20)
turtle.goto(77,-35)

# Braços
turtle.penup()
turtle.goto(50,0)
turtle.pendown()
turtle.goto(50,-45)

turtle.penup()
turtle.goto(95,0)
turtle.pendown()
turtle.goto(95,-45)

# Roupa

turtle.penup()
turtle.goto(15,30)
turtle.pensize(2)
turtle.color("brown")
turtle.pendown()
turtle.goto(135,30)

turtle.penup()
turtle.goto(30,30)
turtle.pendown()
turtle.goto(30,15)

turtle.penup()
turtle.goto(75,30)
turtle.pendown()
turtle.goto(75,15)

turtle.penup()
turtle.goto(115,30)
turtle.pendown()
turtle.goto(115,15)

turtle.penup()
turtle.goto(9,15)
turtle.pendown()
turtle.goto(141,15)

turtle.penup()
turtle.goto(15,15)
turtle.pendown()
turtle.goto(15,1)

turtle.penup()
turtle.goto(50,15)
turtle.pendown()
turtle.goto(50,1)

turtle.penup()
turtle.goto(85,15)
turtle.pendown()
turtle.goto(85,1)

turtle.penup()
turtle.goto(120,15)
turtle.pendown()
turtle.goto(120,1)


# Gravata
turtle.penup()
turtle.goto(65,20)
turtle.color("black")

turtle.pendown()
turtle.begin_fill()
turtle.goto(65,30)
turtle.goto(75,25)
turtle.goto(85,30)
turtle.goto(85,20)
turtle.goto(75,25)
turtle.goto(65,20)
turtle.end_fill()

turtle.done()