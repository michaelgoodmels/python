from gamegrid import *
from random import *

class Raumschiff(Actor):
    timer = 0

    def act(self):
        self.timer -= 1

class Geschoss(Actor):
    def act(self):
        ypos = self.getY()
        self.setY(ypos - 5)
        if ypos < 0:
            feld.removeActor(self)

    def collide(self, actor1, actor2):
        feld.removeActor(self)
        feld.removeActor(actor2)
        if feld.getNumberOfActors(Alien) == 0:
            gewonnen()
        return 0

class Alien(Actor):
    ypos = 0

    def act(self):
        self.ypos += 0.1
        self.setY(int(self.ypos))
        if randint(1, 1000) == 500:
            bombe = Bombe("sprites/creature_1.gif")
            bombe.addCollisionActor(raumschiff)
            feld.addActor(bombe, Location(self.getX(), self.getY() + 10))

class Bombe(Actor):
    def act(self):
        ypos = self.getY()
        self.setY(ypos + 5)
        if ypos > 600:
            feld.removeActor(self)

    def collide(self, actor1, actor2):
        gameover()
        return 0

def tasteGedrueckt(tastencode):
    xpos = raumschiff.getX()
    if tastencode == 37:
        if xpos > 20:
            raumschiff.setX(xpos - 5)
    elif tastencode == 39:
        if xpos < 580:
            raumschiff.setX(xpos + 5)
    elif tastencode == 32:
        schuss()

def schuss():
    if raumschiff.timer < 0:
        geschoss = Geschoss("sprites/bomb.gif")
        alien_liste = feld.getActors(Alien)
        for a in alien_liste:
            geschoss.addCollisionActor(a)
        feld.addActor(geschoss, Location(raumschiff.getX(), 590))
        raumschiff.timer = 10

def gameover():
    feld.doPause()
    msgDlg("GAME OVER")

def gewonnen():
    feld.refresh()
    feld.doPause()
    msgDlg("GEWONNEN!")

feld = GameGrid(600, 600, 1, None, "sprites/town.jpg", False)
feld.setTitle("Space Attack")
raumschiff = Raumschiff("sprites/spaceship.gif")
feld.addActor(raumschiff, Location(300, 586))

for reihe in range(50, 300, 50):
    for spalte in range(40, 570, 40):
        alien = Alien("sprites/alien.png")
        alien.ypos = reihe
        feld.addActor(alien, Location(spalte, reihe))

feld.setSimulationPeriod(20)
feld.addKeyRepeatListener(tasteGedrueckt)
feld.show()
feld.doRun()