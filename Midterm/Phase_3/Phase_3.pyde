def setup():
    size(500, 500) 
    noStroke() 
    
def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(s)
    fill(0) 
    rect(32, 55,  45, 10) 
    rect(47, 25,  10, 30)
    rect(28, 20,  45, 10)
    ellipse(18, 60, 30, 30) 
    ellipse(88, 60, 30, 30)
    pop()

def draw():
    drawObject(0,0,0.25)
    drawObject(0,100,0.24)
