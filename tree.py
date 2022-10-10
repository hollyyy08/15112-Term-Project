import math
import random
from cmu_112_graphics import *

# https://www.educba.com/pointers-in-python/
def drawTree(**p):
    if p['depth'] < p['maxdepth'] and p['height'] >= 3:
        dep = p['depth']
        p['width'] *= p['dwidth'](dep)
        x0 = p['x'] + math.cos(p['angle']) * p['trunk']
        y0 = p['y'] - math.sin(p['angle']) * p['trunk']
        p['surf'].line((int(p['x']), int(p['y']),x0, y0),width=int(p['width']),fill=p['color'])


        p['width'] *= p['dwidth'](dep)
        a1 = p['angle'] - p['opening'] * p['dopening'](dep)
        a2 = p['angle'] + p['opening'] * p['dopening'](dep)

        h1 = p['height'] * p['dheight'](dep)
        x1 = x0 + math.cos(a1) * h1
        y1 = y0 - math.sin(a1) * h1

        h2 = p['height'] * p['dheight'](dep)
        x2 = x0 + math.cos(a2) * h2
        y2 = y0 - math.sin(a2) * h2

        p['surf'].line((x0, y0, x1, y1), width = int(p['width']), fill = p['color'])
        p['surf'].line((x0, y0, x2, y2), width = int(p['width']), fill = p['color'])

        p['trunk'] *= p['dtrunk'](dep)

        p['depth'] += .5
        p['x'], p['y'], p['height'], p['angle'] = x1, y1, h1, a1 - p['dangle'](dep)

        drawTree(**p)

        p['depth'] += .5
        p['x'], p['y'], p['height'], p['angle'] = x2, y2, h2, a2 + p['dangle'](dep)
        drawTree(**p)

    elif p['height'] < 5:
        dep = p['depth']
        p['width'] *= p['dwidth'](dep)

        radius = int(p['height']) + 2
        x0 = int(p['x']) - radius
        y0 = int(p['y']) - radius
        x1 = x0 + 2 * radius
        y1 = y0 + 2 * radius
        p['surf'].ellipse((x0,y0,x1,y1),fill = p['leaf'])


# https://www.cs.cmu.edu/~112/notes/notes-functions-redux.html#lambdaFns
# https://pythonhosted.org/SuRF/#:~:text=SuRF%20is%20an%20Object%20%2D%20RDF,as%20ActiveRDF%20does%20for%20ruby.
# https://pythonguides.com/python-turtle-random/
# https://pythonmana.com/2020/12/202012050606251283.html
def tree0(surf, x, y, shade = 0):
    drawTree(surf = surf,
               x = x,
               y = y,
               z = 0,
               angle = math.pi / 2,
               dangle = lambda dep: -(random.random() - 0.5) * math.pi / 3,
               theta = math.pi / 2,
            #    (235,180,190)
               leaf = (245, min(235, 130 + random.randrange(-5,30)), min(245, 170 + random.randrange(-17,10))),

               trunk = 180,
               dtrunk = lambda dep: 0.8 * random.random(),

               width = 15,
               dwidth = lambda dep: random.random() * 0.2 + 0.8,

               height = 70,
               dheight = lambda dep: random.random() * 0.6 + 0.4,

               opening = math.pi / 5,
               dopening = lambda dep: 0.8 + random.random() * 0.5,

               color = (100 + shade, 100 + shade, 100 + shade),
               depth = 0,
               maxdepth = 8
               )


def tree1(surf, x, y, shade = 200):
    drawTree(surf = surf,
               x = x,
               y = y,
               z = 0,
               angle = math.pi / 2,
               dangle = lambda dep: -(random.random() - 0.5) * math.pi / 3,
               theta = math.pi / 2,
               leaf = (min(225, 138 + shade), min(215, 161 + shade), min(245, 132 + shade)),

               trunk = 100,
               dtrunk = lambda dep: 0.8 * random.random(),

               width = 8,
               dwidth = lambda dep: random.random() * 0.2 + 0.8,

               height = 50,
               dheight = lambda dep: random.random() * 0.6 + 0.4,

               opening = math.pi / 6,
               dopening = lambda dep: 0.8 + random.random() * 0.5,

               color = (100 + shade, 100 + shade, 100 + shade),
               depth = 0,
               maxdepth = 8
               )


def tree2(surf, x, y, shade = 30):
    drawTree(surf = surf,
               x = x,
               y = y,
               z = 0,
               angle = math.pi / 2,
               dangle = lambda dep: 0,
               theta = math.pi / 2,
               leaf = (min(235, 160 + shade), min(225, 210 + shade), 210 + shade),

               trunk = 20,
               dtrunk = lambda dep: 0.9,

               width = 10,
               dwidth = lambda dep: random.random() * 0.3 + 0.7,

               height = 140,
               dheight = lambda dep: random.random() * 0.6 + 0.3,

               opening = math.pi / 4,
               dopening = lambda dep: ((dep * 2) % 2) * (0.8 + random.random() * 0.4),  # *(dep<2),

               color = (100 + shade, 100 + shade, 100 + shade),
               depth = 0,
               maxdepth = 6
               )


def tree3(surf, x, y, shade = 0):
    drawTree(surf = surf,
               x = x,
               y = y,
               z = 0,
               angle = math.pi / 2,
               dangle = lambda dep: -(random.random() - 0.5) * math.pi / 6,
               theta = math.pi / 2,
               leaf = (225, min(225, 90 + shade), min(225, 150 + shade)),

               trunk = 70,
               dtrunk = lambda dep: 0.8 * random.random(),

               width = 10,
               dwidth = lambda dep: random.random() * 0.2 + 0.6,

               height = 130,
               dheight = lambda dep: random.random() * 0.7 + 0.2,

               opening = math.pi / 5,
               dopening = lambda dep: random.random() * 2 - 1,

               color = (100 + shade, 100 + shade, 100 + shade),
               depth = 0,
               maxdepth = 8
               )


def tree4(surf, x, y, shade = 0):
    drawTree(surf = surf,
               x = x,
               y = y,
               z = 0,
               angle = math.pi / 2,
               dangle = lambda dep: (-math.pi / 6) + ((random.random() - 0.5) * (dep)) * 2,
               theta = math.pi / 2,
               leaf = (205, min(235, 0), min(235, 80 + random.randrange(-10, 20))),

               trunk = 90,
               dtrunk = lambda dep: 0.8 * random.random(),

               width = 8,
               dwidth = lambda dep: random.random() * 0.2 + 0.8,

               height = 50,
               dheight = lambda dep: random.random() * 0.5 + 0.5,

               opening = math.pi / 5,
               dopening = lambda dep: 0.8 + random.random() * 0.5 * dep * 2,

               color = (100 + shade, 100 + shade, 100 + shade),
               depth = 0,
               maxdepth = 5
               )



# def appStarted(app):
#     bgColor = (255, 255, 255)  # cyan
#     app.image1 = Image.new('RGB', (700, 600), bgColor)
#     # app.image2 = app.scaleImage(app.image1, 1/3)
#     app.draw = ImageDraw.Draw(app.image1)
#     for i in range(0, 5):
#         # app.image1 = Image.new('RGB', (700, 600), bgColor)
#         # app.draw = ImageDraw.Draw(app.image1)
#         [tree0, tree1, tree2, tree3, tree4][i](app.draw, 100 + i * 200, 500, 30)
#     # app.image2 = app.scaleImage(app.image1, 1.15)

# def redrawAll(app, canvas):
#     canvas.create_image(app.width/2, app.height/2, image = ImageTk.PhotoImage(app.image1))

# runApp(width=800, height=700)

