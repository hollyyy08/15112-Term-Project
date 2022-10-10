import math
import random
from cmu_112_graphics import *

# https://blog.csdn.net/FRIGIDWINTER/article/details/123330206
# https://pillow.readthedocs.io/en/stable/reference/Image.html
class img_Enhance():
    def __init__(self,img1):
        self.size = img1.size
        print(self.size)
        self.img1 = img1.convert("RGB")
        self.img2 = Image.new(mode='RGB', size=self.img1.size)

    def glass_effects(self):
        rows,cols=self.size
        offsets=random.randint(1,10)
        for x in range(rows-offsets):
            for y in range(cols-offsets):
                random_num = random.randint(0,offsets)
                r, g, b = self.img1.getpixel((x+random_num, y+random_num))
                self.img2.putpixel((x, y), (r,g,b))
        return self.img2

    def old_effects(self):
        rows, cols = self.size
        for x in range(rows):
            for y in range(cols):
                r, g, b = self.img1.getpixel((x, y))
                B = 0.272 * b + 0.534 * g + 0.131 * r
                G = 0.349 * b + 0.686 * g + 0.168 * r
                R = 0.393 * b + 0.769 * g + 0.189 * r
                if B > 255:
                    B = 255
                if G > 255:
                    G = 255
                if R < 255:
                    R = 255
                self.img2.putpixel((x, y), (int(R),int(G),int(B)))
        return self.img2

    def year_effects(self):
        rows, cols = self.size
        for x in range(rows):
            for y in range(cols):
                r, g, b = self.img1.getpixel((x, y))
                b=b*14
                if b>255:
                    b=255
                self.img2.putpixel((x, y), (r,g,b))
        return self.img2

    def mask_effects(self):
        rows, cols = self.size
        for x in range(rows - 5):
            for y in range(cols - 5):
                if x%5 == 0 and y%5 == 0:
                    for k in range(5):
                        for t in range(5):
                            r, g, b = self.img1.getpixel((x, y))
                            self.img2.putpixel((x+k, y+t), (r, g, b))
        return self.img2

    def haha_effects(self):
        rows,cols = self.size
        center_x = int(rows/2)
        center_y = int(cols/2)
        radius = random.randint(100,200)
        real_radius = int(radius/2) #radius
        for x in range(rows):
            for y in range(cols):
                tx = x - center_x
                ty = y - center_y
                distance = tx ** 2 + ty ** 2
                if distance<radius**2:
                    new_x = tx / 2
                    new_y = ty / 2
                    new_x = int(new_x * math.sqrt(distance) / real_radius + center_x)
                    new_y = int(new_y * math.sqrt(distance) / real_radius + center_y)
                    if new_x < rows and new_y < cols:
                        r,g,b = self.img1.getpixel((new_x, new_y))
                        self.img2.putpixel((x,y),(r,g,b))
        return self.img2

    def blackwhite(self):
        rows,cols = self.size
        for x in range(rows):
            for y in range(cols):
                r, g, b = self.img1.getpixel((x, y))
                r = b = g = int(r*0.299 + g*0.587 + b*0.114)
                self.img2.putpixel((x,y),(r,g,b))
        return self.img2

    def img_reverse(self):
        rows, cols = self.size
        for x in range(rows):
            for y in range(cols):
                r, g, b = self.img1.getpixel((x, y))
                r = 255 - r
                b = 255 - b
                g = 255 - g
                self.img2.putpixel((x, y), (r, g, b))
        return self.img2

    def sun_effects(self):
        rows, cols = self.size
        center_x,center_y = int(rows/2), int(cols/2)
        radius = min(center_x,center_y)
        strength = 200
        for x in range(rows):
            for y in range(cols):
                r, g, b = self.img1.getpixel((x, y))
                distance = math.pow((center_x-x),2) + math.pow((center_y-y),2)
                if distance < radius**2:
                    result = int(strength*(1.0-math.sqrt(distance)/radius))
                    b,g,r = b + result,g + result,r + result
                    b,g,r = min(255,max(0,b)),min(255,max(0,g)),min(255,max(0,r))
                    self.img2.putpixel((x,y),(r,g,b))
                else:
                    self.img2.putpixel((x, y), (r, g, b))
        return self.img2

    def select_effects(self):
        effect = random.randint(1,9)
        if effect == 1:
            self.img2 = self.glass_effects()
            txt='glass effects'
        elif effect == 2:
            self.img2 = self.old_effects()
            txt = 'old effects'
        elif effect == 3:
            self.img2 = self.year_effects()
            txt = 'year effects'
        elif effect == 4:
            self.img2 = self.mask_effects()
            txt = 'mask effects'
        elif effect == 5:
            self.img2 = self.haha_effects()
            txt = 'HaHa mirror effects'
        elif effect == 6:
            self.img2 = self.blackwhite()
            txt = 'black and white effects'
        elif effect == 7:
            self.img2 = self.img_reverse()
            txt = 'color reverse effects'
        else:
            self.img2 = self.sun_effects()
            txt = 'Sunshine effects'
        return self.img2, txt

