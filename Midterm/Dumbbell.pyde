def setup():
    size(500, 500) 
    noStroke() 
    
def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(0.25)
    fill(0) 
    rect(32, 55,  45, 10) 
    rect(47, 25,  10, 30)
    rect(28, 20,  45, 10)
    ellipse(18, 60, 30, 30) 
    ellipse(88, 60, 30, 30)
    pop()

def draw():
    for i in range(500):
        for k in range(500):
            drawObject(k*25, i*20, 40)

    #save("Phase 4.png")
