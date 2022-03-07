import turtle

class Enemy(object):
    element=turtle.Turtle()
    position=[]
    def __init__(self,element,position):
        self.element=element
        self.position=position
    def begin(self):
        self.element.penup()
        self.element.shape('square')
        self.element.color('red')
        self.element.goto(self.position[0],self.position[1])

