from random import *
from graphics import *

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
