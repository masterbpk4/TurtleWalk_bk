# Brenden Kelley
# Last Update 11/8/2020

import turtle

gerald = turtle.Turtle()
gerald.penup()
gerald.speed(10)

distance = []
disttraveled = 0
f = open("linedrawing.txt", 'r')

for line in f:
    linesplit = line.split()
    if len(linesplit) == 1 & len(linesplit) < 2:
        gerald.penup()
    if len(linesplit) > 1:
        color = linesplit[0]
        x = int(linesplit[1])
        y = int(linesplit[2])
        gerald.pencolor(color)
        gerald.goto(x, y)
        if gerald.isdown():
            dist = int(turtle.distance(x,y))
            distance.append(dist)
        else:
            gerald.pendown()



for i in range(len(distance)):
    disttraveled = disttraveled + distance[i]

gerald.penup()
gerald.goto(150,-200)
gerald.write('Total distance marked = ' + str(disttraveled))

turtle.done()








