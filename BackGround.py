import random
import math
import tree as tree
import noise as noise

from cmu_112_graphics import *

# https://stackoverflow.com/questions/10225063/2d-terrain-generation-using-perlin-noise-tile-based
class BGlayer():
    def __init__(self,terrainnum,width,height,treeDensity):
        self.terrainnum=terrainnum
        self.terrain=[0]*terrainnum
        self.terrainImg=[None]*terrainnum
        self.width=width
        self.height=height
        self.buff=0
        self.treeDensity=treeDensity

#add perlin
# https://developer.nvidia.com/gpugems/gpugems2/part-iii-high-quality-rendering/chapter-26-implementing-improved-perlin-noise
# https://github.com/RedHenDev/ursina_tutorials/tree/main/python_minecraft_tut_2021/perlin%20noise
    def makeLand(self, n, m=0, maxheight= 320):
        return max(noise.noise(n * 0.1, m * 0.5) * maxheight, 2) - 2

    def makeTreelayer(self,n,draw):
        # add to draw mountain
        if n <2 and random.random() > 0.2:
            # and random.random() > 0.5
            poly = []
            poly.append([0, self.height])
            for i in range(self.buff, self.width + self.buff, 32): 
                poly.append([i, self.height - self.makeLand(i * 0.05, n * 0.5, 500 - n * 90)])
            poly[1][1] = (poly[1][1] - self.height) / 2.0 + self.height
            poly[-1][1] = (poly[-1][1] - self.height) / 2.0 + self.height
            poly.append([self.width + self.buff * 2, self.height])

            # change to tuple
            newpoly = []
            for j in range(len(poly)):
                newpoly.append(tuple(poly[j]))

            draw.polygon(newpoly, fill=(210 - n * 20, 210 - n * 20, 210 - n * 20))  #changge color
    #add end

        if self.terrain[n] == 0:
            treesum = self.width / (self.terrainnum * self.treeDensity)
            for i in range(0, int(treesum)):
                thetree = [random.choice([tree.tree1, tree.tree3, tree.tree3]),
                           random.choice([tree.tree2, tree.tree2, tree.tree3]),
                           random.choice([tree.tree0, tree.tree0, tree.tree3]),
                           random.choice([tree.tree0, tree.tree0, tree.tree4])][n]
                thetree(draw, random.random() *self.width + self.buff, self.height,
                        (120 - n * 80) + random.randrange(-10, 10))

        elif self.terrain[n] == 1:
            treesum = self.width / (self.terrainnum * self.treeDensity)
            for i in range(0, int(math.ceil(treesum / 2.0))):
                thetree = [random.choice([tree.tree1, tree.tree3, tree.tree3]),
                           random.choice([tree.tree1, tree.tree3, tree.tree1]),
                           random.choice([tree.tree2, tree.tree3, tree.tree2]),
                           random.choice([tree.tree1, tree.tree4, tree.tree4])][n]
                thetree(draw, random.random() * self.width + self.buff, self.height,
                        (120 - n * 80) + random.randrange(-10, 10))


    def makeallTreelayers(self, layernum):
        # draw canvas
        bgColor = (255, 255, 255) 
        img = Image.new('RGB', (self.width, self.height), bgColor)
        img = img.convert('RGB')
        draw = ImageDraw.Draw(img)
        # for i in range(self.terrainnum):
        for i in range(layernum):
            self.makeTreelayer(i,draw)
        # self.makeHouselayer(draw)
        return img


    def makeTitle(self,width,height):
        bgColor = (255, 255, 255) 
        img = Image.new('RGB', (width,height), bgColor)
        img = img.convert('RGB')
        draw = ImageDraw.Draw(img)
        [tree.tree0][0](draw, 400, 700, 30)
        return img


# def appStarted(app):
#     app.buff = 200
#     app.terrainnum=4
#     app.width=600
#     app.height, app.treeDensity=400,32
#     app.bg=BGlayer(app.terrainnum,app.width,app.height,app.treeDensity)
#     # title=BGlayer(1, app.width, app.height,1)
#     app.img=app.bg.makeallTreelayers(4)
#     print("size=",app.img.size)
#
# def redrawAll(app, canvas):
#     # canvas.create_image(100, 100, image=ImageTk.PhotoImage(app.bglayer))
#     # canvas.create_image(100,300,image=ImageTk.PhotoImage(app.person))
#
#     # canvas.create_image(100, 100, image=ImageTk.PhotoImage(sprite1))
#     canvas.create_image(400,300, image=ImageTk.PhotoImage(app.img))
#
# runApp(width=800, height=600)
#
#
#
#
#
#
# #
# #
# #
