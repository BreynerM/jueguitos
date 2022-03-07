import turtle
from me import Me
from enemy import Enemy

import time

window=turtle.Screen()
window.bgcolor('black')
me=Me(turtle.Turtle(),[0,0])
me.begin()
enemy=[]
for i in range(5):
    newEnemy=Enemy(turtle.Turtle(),[50*(i+1),50*(i+1)])
    newEnemy.begin()
    enemy.append(newEnemy)


window.mainloop()

