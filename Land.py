import random
import noise
import BackGround
from cmu_112_graphics import *

# https://github.com/RedHenDev/ursina_tutorials/tree/main/python_minecraft_tut_2021/perlin%20noise
class Landlayer():
    def __init__(self, height, width, landDensity, maxheight, bgcolor, co):
        self.height = height
        self.width = width
        self.landDensity = landDensity
        # self.landData = [0] * int(self.width/self.landDensity)
        self.landData=[]
        for row in range(int(self.width/self.landDensity)):
            self.landData += [[0] * 2]

        self.maxheight = maxheight
        self.bgcolor = bgcolor
        self.co = co
        self.makeLandData()

    def makeLandData(self):
        landnum = int(self.width / self.landDensity)
        for i in range(landnum):
            seed = random.random()
            self.landData[i][0] = i * self.landDensity
            self.landData[i][1]=self.makeLand(i, 0, 70 + seed * self.co)

    def makeLand(self, n, m=0, maxheight= 320):
        return max(noise.noise(n * 0.1, m * 0.5) * maxheight, 2) - 2

    def drawLandfromData(self,offset,img):
        landsum = len(self.landData)
        draw = ImageDraw.Draw(img)
        poly = []
        poly.append((0, self.height))
        x = 0
        for i in range(len(self.landData)):
            poly.append((self.landData[i][0]-offset, self.height - self.landData[i][1]))

        poly.append((self.width, self.height))
        draw.polygon(poly, fill=self.bgcolor)
        return img

    def updateLandData(self, offset):
        # int(self.width/self.landDensity)
        # print("before",self.landData)
        landsum = len(self.landData)
        index = 0
        while (index < len(self.landData)):
            # calculate x
            # x = index * self.landDensity
            if self.landData[index][0] - offset < 0:
                self.landData.pop(index)
            # else:
            #     self.landData[index][0] -= offset
            index += 1


        self.landData.sort(key=lambda x:x[0], reverse=False)


        index=len(self.landData)
        while index<landsum:
            seed = random.random()
            self.landData.append([offset+index*self.landDensity
                                     ,self.makeLand(len(self.landData), 0, 20 + seed * self.co)])
            index+=1

        # print("last data:",self.landData)


    def generateLandLayer(self):

        poly = []
        poly.append((0, self.height))
        x = 0
        for i in range(len(self.landData)):
            poly.append((i * self.landDensity,
                         self.height - self.landData[i]))
        poly.append((self.width, self.height))
        bgColor = (255, 255, 255) 
        draw = ImageDraw.Draw(self.img)
        draw.polygon(poly, fill=self.bgcolor)
        return self.img