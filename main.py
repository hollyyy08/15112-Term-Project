import Land
import Person
import BackGround
import imageEnhance as imgEnh
from cmu_112_graphics import *
import Plant

import random 
import pygame
from pygame.locals import *
from pygame import mixer
# from playsound import playsound

# https://www.pygame.org/docs/ref/music.html
# song credit:
# https://www.youtube.com/watch?v=k3YDs6Nq1H0
mixer.init()
#Load audio file
mixer.music.load('37 Bushi.ogg')
mixer.music.set_volume(0.3)
mixer.music.play(loops=-1)

# OOP reference:
# https://www.cs.cmu.edu/~112/notes/notes-oop-part1.html
# https://www.cnblogs.com/guan-zl/p/12956161.html

# Animations reference:
# https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html

# global variables
# https://stackoverflow.com/questions/423379/using-global-variables-in-a-function
def appinit(app,bgwidth,landheight,landdensity,treedensity,
            landmaxheight,landcoe,playerfiles,
            terrainnum,landcolor
            ):
    #player window size
    app.screenWidth=app.width
    app.screenHeight=app.height

    #background size
    app.BGwidth=bgwidth
    app.BGheight=app.height

    #beginnmode,infomode, gamemode,helpmode,filterinfomode,filtermode
    app.mode='beginningMode'
    app.gameOver=False
    app.motionOn = False

    #land lcation
    app.landloc=0

    app.msgtxt = 'None effects'

    #land,person,background
    app.scrollx=0

    app.player = Person.player(playerfiles,3)
    app.player.load()

    app.background=BackGround.BGlayer(terrainnum,bgwidth,app.height,treedensity)
    app.bglayer=app.background.makeallTreelayers(4)

    app.lander = Land.Landlayer(app.height, app.width+300, landdensity, landmaxheight, landcolor, landcoe)

    app.Titleimg= app.background.makeTitle(app.width,app.height)
	
	#flowers
    app.flowerctrl=Plant.flowerCtl(app.width, app.height)
    app.flowerctrl.makeflowers(int(random.random()*50))

#app start
def appStarted(app):
    playerfile=['person.png']
    appinit(app, 2000, 120, 32, 32,200, 30, playerfile,4,(133,187,101))
    #foot
    app.player.foo = app.height - onLandY(app,app.scrollx+app.width//3)

#control part
#begingmode
# https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#usingModes
# citations are the same for the rest of the modes used in this project.
def beginningMode_keyPressed(app, event):
    if event.key == 'e':
        app.mode = "infoMode"

def beginningMode_redrawAll(app, canvas):
    canvas.create_image(app.width/2, app.height/2, anchor='center',image=ImageTk.PhotoImage(app.Titleimg))
    canvas.create_text(app.width/2, 60, text = "Illusion", font ="Courier 24 bold")
    canvas.create_text(100, 100, anchor = NW,
                       text = "Press 'e' to begin your journey.", 
                       font = "Courier 16 italic")
    canvas.create_text(100, 130, anchor = NW,
                       text = "In this game, you will walk in a peach forest, when you wake up, \neverything is an illusion...", 
                       font = "Courier 16 italic")


def infoMode_keyPressed(app, event):
    if event.key == "e":
        app.mode = "gameMode"
    if event.key == "Left":
        app.mode = "beginningMode"


def infoMode_redrawAll(app, canvas):
    canvas.create_text(100, app.height/4,anchor = NW, 
                       text = "This game is inspired by a chinese legend called\
                                \n'The Peach Blossom Spring'.\
                                \n \
                                \nIn this game, you will only be able to move \
                                \nfoward with the right arrow key.You are free \
                                \nto stay as long as you want. But after you leave,\
                                \nyou cannot reenter this world anymore. You will be\
                                \nable to make a postcard before you leave, and it can\
                                \nbe saved in your computer. So at least there will be \
                                \nproof that this is not just an illusion...\
                                \n \
                                \nThe scenries will change randomly according to the mod \
                                \nof the gods living in this world. \
                                \n \
                                \nPress 'e' to continue.\
                                \nAt any time in the game, you can press the left arrow \
                                \nkey to return to the page before the current one.\
                                \n\nWhen you are ready to exit out of the game, you can press\
                                \n'e' to make a postcard.",
                              font = "Courier 16 italic")


#gamemode
def gameMode_timerFired(app):  #add to flower
    app.flowerctrl.updateFlowers()


def gameMode_keyPressed(app, event):
    if (event.key == 'e'):
        app.ogimg = app.getSnapshot()
        app.ogimg.convert("RGB")
        app.saveimg = app.ogimg
        app.mode = "filterInfoMode"

    # elif (event.key == 'n'):
    #     app.gameOver = True
    elif (event.key=='Right'):
        move(app, event)
    elif (event.key == "Left"):
        app.mode = "infoMode"


def gameMode_redrawAll(app,canvas):
    #draw background
   canvas.create_image(app.scrollx , app.height, anchor=SW,
                        image=ImageTk.PhotoImage(app.lander.drawLandfromData(app.landloc,app.bglayer)))

   #draw player
   canvas.create_image(app.width//3, app.player.foo, anchor = SW, image=
        ImageTk.PhotoImage(app.player.imgs[app.player.posi]))
		
   #draw flowers #add
   app.flowerctrl.drawflowers(canvas)

#    #draw others
#    canvas.create_text(100, 20, anchor = NW, 
#                       text="Would you like to make a postcard? This means ending the game.", 
#                       font = "Courier 16 italic")
#    canvas.create_text(100, 40, anchor = NW,
#                        text="Press 'y' to continue.",
#                        font = "Courier 16 italic")


# https://github.com/RedHenDev/ursina_tutorials/tree/main/python_minecraft_tut_2021/perlin%20noise    
def onLandY(app, instx):
    startx=app.lander.landData[0][0]
    if instx>app.lander.landData[len(app.lander.landData)-1][0]:
        lastindex=len(app.lander.landData)-1
    else:
        lastindex =min((instx-startx)//app.lander.landDensity,len(app.lander.landData))

    lastAlt = app.lander.landData[lastindex][1]
    ep = 0.01
    if lastindex == len(app.lander.landData) - 1:
       nextAlt=app.lander.height
    else:
        nextAlt=app.lander.landData[(lastindex+1)][1]

    return lastAlt + (nextAlt - lastAlt) * ((((ep) % app.lander.landDensity
                    +instx) % app.lander.landDensity) / app.lander.landDensity)

# https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#sidescrollerExamples
def move(app,event):
    if abs(app.scrollx) >= app.width/3:
        app.scrollx = 0
        randomlayers= random.randint(1,4)
        app.background.terrain[randomlayers-1]= random.randint(0,1)
        app.bglayer = app.background.makeallTreelayers(randomlayers)

        app.landlayer = app.lander.updateLandData(app.scrollx) #add
    else:
        if event.key == "Right":
            app.scrollx -= app.player.speed
        # elif event.key == "Left":
        #     app.scrollx += app.player.speed

    app.landloc+=app.player.speed   #add
    app.lander.updateLandData(app.landloc)
    app.player.foo = app.lander.height - onLandY(app, app.landloc + app.width // 2)+15


def filterInfoMode_keyPressed(app, event):
    if event.key == "e":
        app.mode = "filterMode"
    if event.key == "Left":
        app.mode = "gameMode"


def filterInfoMode_redrawAll(app, canvas):
    canvas.create_text(100, 170, anchor = NW,
                       text = 'Press mouse to change effects.', 
                       font = "Courier 16 italic")
    canvas.create_text(100, 200, anchor = NW,
                       text = "Press r when you've found the one you like, \
                           \nthe image will be stored in the same folder as the game, \
                            \nunder the name 'postcard'.\
                            \n \
                            \nYou can come back to this page if you press the left arrow,\
                            \njust in case you forget the instructions.", 
                       font = "Courier 16 italic")
    canvas.create_text(100, 310, anchor = NW,
                       text = "Press 'e' to continue.",
                       font = "Courier 16 italic")


#filtermodee
def filterMode_mousePressed(app, event):
    if event.x:
        img_en = imgEnh.img_Enhance(app.ogimg)
        app.saveimg, app.txt = img_en.select_effects()

def filterMode_keyPressed(app, event):
    if event.key == 'r':
        app.saveimg.save('postcard.jpg')
    if event.key == "Left":
        app.mode = "filterInfoMode"
        
        
def filterMode_redrawAll(app, canvas):
    # TODO image:
    canvas.create_image(app.width / 2, 300, image =ImageTk.PhotoImage(app.saveimg))
    # canvas.create_image(app.width / 2, 300, image =ImageTk.PhotoImage(app.getSnapShot()))


if __name__=='__main__':
    runApp(width=800, height=700)

mixer.music.stop()



