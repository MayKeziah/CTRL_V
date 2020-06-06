import graphics
def main():
    newwindow = graphics.GraphWin("Test", 500, 500)
    mypoint = graphics.Point(250, 250)
    mypoint.draw(newwindow)
    mycircle = graphics.Circle(mypoint, 100)
    mycircle.draw(newwindow)
    mypoint2 = graphics.Point(100, 100)
    mypoint2.draw(newwindow)
    myrectangle = graphics.Rectangle(mypoint, mypoint2)
    myrectangle.draw(newwindow)
    myline = graphics.Line(mypoint, mypoint2)
    myline.draw(newwindow)

def testText():
    testwin = graphics.GraphWin("Test Text", 200, 200)
    testwin.setCoords(0, 0, 2, 2)
    graphics.Circle(graphics.Point(1, 1), 0.5).draw(testwin)
    graphics.Text(graphics.Point(1, 1), "Circle!").draw(testwin)

def testMouse():
    win = graphics.GraphWin("Mouse Click")
    win.setCoords(-1, -1, 100, 100)
    p = win.getMouse()
    print("You clicked at", p.getX(), p.getY())

def clickHere():
    message = graphics.Text(graphics.Point(200, 100), "Click Here")
    rect = graphics.Rectangle(graphics.Point(160, 60), graphics.Point(240, 140))
    newwin = graphics.GraphWin("Clicky Window", 400, 400)
    rect.draw(newwin)
    rect.setFill("yellow")
    message.draw(newwin)
    pt = newwin.getMouse()
    while ((160 < pt.getX() < 240) and (60 < pt.getY() < 140)) == False:
        pt = newwin.getMouse()
    rect.undraw()
    message.setText("click to close")
    newwin.getMouse()

    newwin.close()

def ch4Ex8():
    import math
    #Make window
    lineWin = graphics.GraphWin("Draw a line!", 600, 600)
    lineWin.setCoords(0, 0, 600, 600)
    lineWin.setBackground("green")

    #Prompt clicks
    message = graphics.Text(graphics.Point(300, 550), "Click anywhere to start the line")
    message.draw(lineWin)
    pt1 = lineWin.getMouse()
    point1 = graphics.Point(pt1.getX(), pt1.getY())
    point1.draw(lineWin)
    message.setText("Click again to finish the line")
    pt2 = lineWin.getMouse()
    message.undraw()

    #Draw line
    newline = graphics.Line(pt1, pt2)
    newline.draw(lineWin)

    #Draw midpoint in cyan
    midpoint = graphics.Point((pt2.getX()+pt1.getX())/2, (pt2.getY()+pt1.getY())/2)
    midpoint.draw(lineWin)
    midpoint.setFill("cyan")
                              

    #find the length and slope of line(segment)
    dx = pt2.getX()-pt1.getX()
    dy = pt2.getY()-pt1.getY()
    slope = dy/dx
    length = math.sqrt(dx**2+dy**2)

    #Print line data
    message.setText("Length: "+str(round(length, 2))+"\nSlope: "+
                    str(round(slope, 2))+"\n\nClick anywhere to quit")
    message.draw(lineWin)
    lineWin.getMouse()
    
    lineWin.close()    

main()