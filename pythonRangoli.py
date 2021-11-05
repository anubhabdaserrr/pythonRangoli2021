import turtle as tt

#Set properties
tt.bgcolor('black')
tt.pensize(2)
tt.speed(100)

#Draw two innermost circles (each with multiple circles inside it) one on top of other
def centralCircles():
    
    #Upper circle
    tt.begin_fill()
    tt.color('white','light steel blue')
    tt.circle(50)
    tt.circle(40)
    tt.circle(30)
    tt.circle(20)
    tt.circle(10)
    tt.end_fill()

    #Lower circle
    tt.left(180)
    tt.begin_fill()
    tt.color('white','light green')
    tt.circle(50)
    tt.circle(40)
    tt.circle(30)
    tt.circle(20)
    tt.circle(10)
    tt.end_fill()

centralCircles()

#Draw petal of inner flowers
def petal1(petalAngle,radius,color):

    tt.begin_fill()
    tt.color('white',color)

    tt.seth(petalAngle)
    tt.circle(radius,90)
    tt.left(90)
    tt.circle(radius,90)

    tt.end_fill()

#Draw 8 inner flowers of different colors
def insideFlowers():

    colors = ['purple','gold','orange','light sky blue','brown','medium sea green','blue','pale violet red']
    angles = [-135,-90,-45,0,45,90, 135,180]
    for startAngle, color in zip(angles,colors):
        tt.seth(startAngle)

        tt.penup()
        tt.goto(0,0)
        tt.forward(180)
        tt.pendown()
        for petalAngle in range(0,360,30): 
            petal1(petalAngle,50,color)

insideFlowers()

#draw 2 concentric circles between inner and outer flowers
tt.color('white','medium slate blue')
tt.penup()
tt.seth(90)
tt.goto(290,0)
tt.pendown()

tt.begin_fill()
tt.circle(290)
tt.penup()
tt.seth(0)
tt.forward(20)

tt.seth(90)

tt.pendown()
tt.circle(310)
tt.end_fill()

#Petal of outer flowers
def petal2(x,y,petalAngle,radius):

    tt.seth(petalAngle)
    tt.circle(radius,90)
    tt.left(90)
    tt.circle(radius,90)

#Draw 16 outer flowers
def outsideFlowers():

    angles = [-157.5,-135,-112.5,-90,-67.5,-45,-22.5,0,22.5,45,67.5,90, 112.5,135,157.5,180]
    for startAngle in angles:
        tt.seth(startAngle)

        tt.penup()
        tt.goto(0,0)
        tt.forward(450)
        tt.pendown()

        for petalAngle in range(0,360,30): 
            petal2(0,0,petalAngle,50)

        for petalAngle in range(0,360,30): 
            petal2(0,0,petalAngle,60)

outsideFlowers()

ts = tt.getscreen()
#ts.getcanvas().postscript(file="pythonRangoli.eps")
tt.hideturtle()

tt.exitonclick()