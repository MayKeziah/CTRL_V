import graphics as g

#--------------------------------------------------------------------------
# Global Variables
#--------------------------------------------------------------------------
""" Size of Pop-Up Window (Square) """
dimension = 600

""" X and Y Coordinate upper limit (Square) """
limit = 100

""" Number of Gridlines on each side of X and Y Axis """
count = 4

""" The number of units on the x and y axis from gridline to gridline """
frequency = limit/count

""" index of command (mutated in getNextMove) """
i = 0
commands = ["up", "up", "left", "down", "right", "stop"]

""" The program will run until called with command = stop """
should_run = True

""" All Graphics Objects created, in case we need to undraw or mutate """
objects = []

""" Gui Color Scheme """
background = "black"

gridColor = "grey"

circleColor = "blue"

textColor = "grey"


#--------------------------------------------------------------------------
# MAIN displays a Graph and draws a circle
#   To use:
#   1) call main
#   2) click on a box to draw a circle
#   3) click to move the circle
#
#   Note:
#         1) current implementation makes the circle only move in accordance
#         with the commands listed in the 'commands' array. To change the
#         source of the commands, update the 'getNextCommand()' function.
#         2) current implementation uses a mouse-click in the window to
#         signal the next move. This will need to be updated to wait for
#         a signal to match our pasturized pickles
#--------------------------------------------------------------------------
def main():
    win = window("CTRL|V", background)
    grid(win)
    msg = prompt(win, limit - limit, limit - (frequency/2), "Click to Start")
    start = getCircle(win)
    newMsg(win, msg, "Say 'Stop' to Exit")
    global should_run
    while should_run:
        move(start, win, getNextMove())

    newMsg(win, msg, "Click to Close Window")
    signalMove(win)
    win.close()


#--------------------------------------------------------------------------
# NEWMSG changes the text of a message in a window
#   win: the window
#   msg: the message to change
#   text: the new text to display
#
#   Final State: The message displays the new text in the window
#--------------------------------------------------------------------------
def newMsg(win, msg, text):
    msg.undraw()
    msg.setText(text)
    msg.draw(win)


#--------------------------------------------------------------------------
# FREEGRAPHICS removes all drawn objects from the window
#
#   Note: not currently used, just here if we want it
#--------------------------------------------------------------------------
def freeGraphics():
    global objects
    for each in objects:
        each.undraw()


#--------------------------------------------------------------------------
# MOVE moves an object one box <command>
#   currentLocation: object to move
#   win: the window
#   command: the direction to move (up, down, left, right, stop, fire)
#
#   Final state: The object is moved <frequency> units <command>
#   EXCEPT: If <command> is stop, the program ends.
#           If <command> is fire, behavior undefined
#--------------------------------------------------------------------------
def move(currentLocation, win, command):
    global should_run
    signalMove(win)
    currentLocation.undraw()
    if command == "up":
        currentLocation._move(0, frequency)
    elif command == "down":
        currentLocation._move(0, -frequency)
    elif command == "left":
        currentLocation._move(-frequency, 0)
    elif command == "right":
        currentLocation._move(frequency, 0)
    elif command == "stop":
        should_run = False
##    elif command == "fire":
##        behavior undefined
    currentLocation.draw(win)



#--------------------------------------------------------------------------
# GETNEXTMOVE returns the next command
#   Note: Current implementation is a placeholder
#   iterates through global commands array.
#   returns the next element on call
#--------------------------------------------------------------------------
def getNextMove():
    global i
    global should_run
    global commands
    i = i + 1
    should_run = i < len(commands)
    if not(should_run):
        i = 0
        should_run = True
    return commands[i - 1]


#--------------------------------------------------------------------------
# WINDOW creates a new GUI-window
#   name: the title to display in the upper bar
#   color: the background color
#
#   returns the window
#--------------------------------------------------------------------------
def window(name, color):
    win = g.GraphWin(name, dimension, dimension)
    win.setCoords(-limit, -limit, limit, limit)
    win.setBackground(color)
    return win


#--------------------------------------------------------------------------
# GRID draws a grid in the window
#   lines are drawn every <frequency> units along both the x and y axis
#   creates an empty horizontal line along the top to see the message
#--------------------------------------------------------------------------
def grid(window):
    global objects
    start = -limit + frequency
    while(start < limit):
        gridlineH = g.Line(g.Point(limit, start), g.Point(-limit, start))
        gridlineH.setFill(gridColor)
        gridlineH.draw(window)
        objects.append(gridlineH)
        
        gridlineV = g.Line(g.Point(start, limit-frequency), g.Point(start, -limit))
        gridlineV.setFill(gridColor)
        gridlineV.draw(window)
        objects.append(gridlineV)
        start += frequency

        
#--------------------------------------------------------------------------
# PROMPT creates a new message at the top of the window prompting the user
#        in some way. To modify this message, call newMsg on it.
#
#   returns the message
#--------------------------------------------------------------------------
def prompt(window, x, y, message):
    global objects
    message = g.Text(g.Point(x, y), message)
    message.setFill(textColor)
    message.draw(window)
    objects.append(message)
    return message


#--------------------------------------------------------------------------
# GETCIRCLE creates a circle when a user clicks in the window
#   this is called only on the first mouse-click
#
#   returns the circle
#--------------------------------------------------------------------------
def getCircle(window):
    global objects
    pt = signalMove(window)
    x = toGrid(pt.getX())
    y = toGrid(pt.getY())
    circle = g.Circle(g.Point(x, y), frequency/2)
    circle.setFill(circleColor)
    circle.draw(window)
    objects.append(circle)
    return circle


#--------------------------------------------------------------------------
# TOGRID takes a random x or y unit and returns the nearest box location
#   Use when trying to draw an object in the middle of a box when the
#   user-given location is not in the middle of a box.
#       ___|___|___
#       ___|_O_|___
#          |   |
#--------------------------------------------------------------------------
def toGrid(num):
    floor = frequency*(num//frequency)
    ceil = floor + frequency
    return (floor + ceil)/2

def signalMove(win):
    return win.getMouse()

""" RUN PROGRAM """
main()
