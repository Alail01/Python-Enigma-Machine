from graphics import *
import time

def drawings():
  win = GraphWin("ENIGMA MACHINE",1000,800)
  win.setCoords(0,0,10,10)
  win.setBackground("white")
  z = Polygon(Point(1,1),Point(win.getWidth(),win.getHeight()),Point(1,20))
  z.setFill("Black")
  z.draw(win)

  return win

def main():
 win = GraphWin("",0,0)
 while (win.isOpen()):
     key = win.getKey()
     print(key)
     if (key == "Escape"):
         win.close()

main()
