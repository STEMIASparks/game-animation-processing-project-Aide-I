x = 0
y = 0
d = 55



def setup():
    size(560,560)

def draw():
    background(0)
    global x,y,d

        square(x,y,d)
    
    y = y+1
    if y >= 500:
        y = 50
    if y <= 0 and x <=600:
        x = x+10
    elif y < 600 and x >= 600:
        y += 10
    elif y >= 600 and x >= 0:
        x = x-10
    elif y >=0 and x < 0:
       y = y-10
    
    
def keyPressed():
    if keyCode == DOWN:
        y = y+15
    if keyCode == DOWN:
        rect(30, 20, 55, 55)
