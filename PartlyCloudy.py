from random import *
from graphics import *

def draw_circle(X, Y, rad, col, window):
    circle = Circle(Point(X,Y), rad)
    circle.setFill(col)
    circle.setOutline(col)
    circle.draw(window)
    
def draw_clouds(X, Y, rad, col, window):
    cloud = Circle(Point(X, Y), rad)
    cloud.setFill(col)
    cloud.setOutline(col)
    cloud.draw(window)

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

for i in range(100):
    cloudX = randint(0, 1000)
    cloudY = randint(600, 800)
    cloudRadius = randint(1, 7)
    cloudColor = "White"
    draw_clouds(cloudX, cloudY, cloudRadius, cloudColor, window)
