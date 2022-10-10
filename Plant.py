import random
import noise
from cmu_112_graphics import *

# https://www.cs.cmu.edu/~112/notes/notes-graphics.html#customColors
def rgbString(r, g, b):
    # Don't worry about the :02x part, but for the curious,
    # it says to use hex (base 16) with two digits.
    return f'#{r:02x}{g:02x}{b:02x}'

# https://pythonguides.com/python-turtle-random/
# https://pythonmana.com/2020/12/202012050606251283.html
class flower():
    def __init__(self, x, y, sp, asp, r, color):
        self.posx = x
        self.posy = y
        self.speed = sp
        self.aspeed = asp
        self.r = r  
        self.color = color

    def flow(self):
        if self.posy > 0:
            self.posx += self.speed+random.random() * self.speed * random.choice([1, -1]) 
            self.posy += self.speed + 0.5 * self.aspeed

    def getoval(self):
        return (self.posx - self.r,self.posy - self.r,
                self.posx + self.r,self.posy + self.r
                )


class flowerCtl():
    def __init__(self, width, height):
        self.flowers = []
        self.width = width
        self.height = height

    def makeflowers(self, n):
        for i in range(n):
            shade = random.randint(50, 150)
            c1 = 245, min(235, 120 + random.randrange(-5,50)), min(245, 170 + random.randrange(-57,10))
            c2 = 245, min(235, 130 + random.randrange(-7,24)), min(245, 170 + random.randrange(-17,20))
            c3 = 245, min(235, 120 + random.randrange(-5,10)), min(245, 170 + random.randrange(-21,16))
            c4 = 245, min(235, 130 + random.randrange(-2,43)), min(245, 170 + random.randrange(-27,10))
            c5 = 245, min(235, 130 + random.randrange(-5,30)), min(245, 170 + random.randrange(-12,17))
            # c3=(min(235, 232 + shade), min(225, 166 + shade), shade)
            # c4=(225, min(225, 76 + shade), min(225, 102 + shade))
            # c5=(235, min(235, 192 + shade), min(235, 203 + shade))
            # c1=(235, min(235, 180 + shade), min(245, 190 + shade))
            # c2=(min(225, 118 + shade), min(215, 161 + shade), min(245, 132 + shade))

            color = random.choice([c1,c2,c3,c4,c5])
            # print("color:",color)
            x = int(random.random() * 600)
            y = min(300,int(random.random() * 200))
            # y = random.randrange(130, 150)
            speed = int(random.random() * 5)+3
            aspeed = int(random.random() * 5)+2
            r =  random.random() + 4
            self.flowers.append(flower(x, y, speed, aspeed, r, color))

    def drawflowers(self, canvas):
        for i in range(len(self.flowers)):
            x0= self.flowers[i].posx
            y0=self.flowers[i].posy
            r=self.flowers[i].r
            color=self.flowers[i].color
            # print("type(color)",type(color))
            rgbString(color[0],color[1],color[2])

            # canvas.create_oval(x0-r, y0-3.0*r, x0+r, y0+3.0*r,
            #                    fill=rgbString(color[0],color[1],color[2]),
            #                    width = 0)
            canvas.create_oval(x0-r, y0-r, x0+r, y0+r,
                               fill=rgbString(color[0],color[1],color[2]),
                               width = 0)

    def updateFlowers(self):
        index = 0
        while index < len(self.flowers):
            self.flowers[index].flow()
            if (self.flowers[index].posx > self.width or self.flowers[index].posx < 0
                    or self.flowers[index].posy > self.height or self.flowers[index].posy < 0):

                self.flowers.pop(index)
            else:
                index += 1
        if len(self.flowers)<5:
            # self.makeflowers(80-len(self.flowers))
            self.makeflowers(60-len(self.flowers))
