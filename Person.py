#person
#定义人
from cmu_112_graphics import *
from PIL import Image

# https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#sidescrollerExamples
class player():
    def __init__(self,imgfiles,speed):
        self.x=0
        self.foo=0
        self.imgfiles=imgfiles
        self.posnum=0 
        self.posi=0  
        self.imgs=[]
        self.walknum=0  
        self.speed=speed
        self.movedir=1


    def getwalknum(self):
        return self.walknum

    #import person image
    def load(self):
        if len(self.imgfiles)==1:
            img = Image.open(self.imgfiles[0])
            # img = img.convert('RGB')
            self.imgs.append(img)
        elif len(self.imgfiles)>1:
            for imgitem in self.imgfiles:
                print(imgitem)
                img = Image.open(imgitem)
                # img = img.convert('RGB')
                self.imgs.append(img)
        #set posnum
        self.posnum=len(self.imgfiles)
        self.pwidth,self.pheight=img.size


    #change position
    def walk(self):
        self.walknum +=1
        self.posi = self.walknum%self.posnum

    def getSpeed(self):
        return self.speed

# def appStarted(app):
#     # app.buff = 200
#     # app.terrainnum = 4
#     # app.width = 600
#     # app.height, app.landDensity = 400, 32
#     # app.maxheight = 120
#     # app.bgcolor = (255, 0, 0)
#     # bg = Land(app.height, app.width, app.landDensity, app.maxheight, app.bgcolor, 50)
#     # app.img = bg.generateLandLayer()
#     app.person=Person([r"D:\jiajia\TP1\walking Medium.png"],5)
#     app.person.load()
#
#
# def redrawAll(app, canvas):
#     # canvas.create_image(100, 100, image=ImageTk.PhotoImage(app.bglayer))
#     # canvas.create_image(100,300,image=ImageTk.PhotoImage(app.person))
#
#     # canvas.create_image(100, 100, image=ImageTk.PhotoImage(sprite1))
#     canvas.create_image(400, 300, image=ImageTk.PhotoImage(app.person.imgs[0]))
#
# runApp(width=800, height=600)
#
