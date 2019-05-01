from random import *
from graphics import *

def draw_circle(X, Y, rad, col, window):
    circle = Circle(Point(X,Y), rad)
    circle.setFill(col)
    circle.setOutline(col)
    circle.draw(window)

def draw_sunflowers(X, Y, rad, col1, col2, window):
    flower1Core = draw_circle(X, Y, rad, col1, window)
    for i in range(7):
        flower1Pedal = draw_circle(X - rad / 1.5, Y - rad, rad / 2.3, col2, window) #bottom left
        flower2Pedal = draw_circle(X + rad, Y + rad, rad / 2.3, col2, window) #upper right
        flower3Pedal = draw_circle(X + rad / 1.5, Y - rad, rad / 2.3, col2, window) # bottom right
        flower4Pedal = draw_circle(X - rad, Y + rad, rad / 2.3, col2, window) #upper left
        flower5Pedal = draw_circle(X + rad / 15, Y + rad, rad/ 2.3, col2, window) #top
        flower6Pedal = draw_circle(X + rad, Y + rad / 15, rad / 2.3, col2, window) #left
        flower7Pedal = draw_circle(X - rad, Y + rad / 15, rad / 2.3, col2, window) #right

window = GraphWin("Partly Cloudy", 1000, 800)
window.setCoords(0, 0, 1000, 800)
window.setBackground(color_rgb(134, 206, 250))

#grass
grass = Rectangle(Point(0, 0), Point(1000, 200))
grass.setFill(color_rgb(0, 55, 0))
grass.setOutline(color_rgb(0, 55, 0))
grass.draw(window)

#hill
hill = Oval(Point(100, 330), Point(900,-600))
hill.setFill(color_rgb(0,55,0))
hill.setOutline(color_rgb(0, 55, 0))
hill.draw(window)

sunflowerX = 50
sunflowerY = 200
sunflowerRadius = 10
sunflowerColor1 = (color_rgb(43, 29, 14))
sunflowerColor2 = "aquamarine"
draw_sunflowers(sunflowerX, sunflowerY, sunflowerRadius, sunflowerColor1,
                sunflowerColor2, window)

