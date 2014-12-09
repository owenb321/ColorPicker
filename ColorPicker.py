import math
import random
import lightpack
import ConfigParser
import os
import threading
import time

class ColorPicker:
    def __init__(self):        
        self.loadConfig()
        self.ConnectToLightpack()
        self.i = 0
        random.seed()
        
        print 'init'
        
    def loadConfig(self):
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.config = ConfigParser.ConfigParser()
        self.config.read(self.scriptDir + '/ColorPicker.ini')
        self.animType = self.config.getint('Animate', 'type')
        self.animInterval = self.config.getfloat('Animate', 'interval')
        
        colorConfigs = self.config.items('LEDColors')
        maxLed = int(max(colorConfigs, key=lambda x: int(x[0]))[0])
        self.ledColors=[ [0,0,0] for k in range(0, maxLed)]
        for colorConfig in colorConfigs:
            ledNum = int(colorConfig[0])
            rgbValues = [int(n) for n in colorConfig[1].split(',')]
            self.ledColors[ledNum-1] = rgbValues
        
    def ConnectToLightpack(self):
        try:
            self.host = self.config.get('Lightpack', 'host')
            self.port = self.config.getint('Lightpack', 'port')
            self.lpack = lightpack.lightpack(self.host, self.port)
            self.lpack.connect()
            return True
        except: return False

    def run(self):
        if self.lpack.lock() :
            self.lpack.turnOn()
            self.lpack.setFrame(self.ledColors)
            if self.animType == 1:
                self.lastFrame = list(self.ledColors)
                while True:
                    self.twinkle()
                    time.sleep(self.animInterval)
            else:
                input("Press ENTER to exit")
        
    def stop(self):
        self.timeranim.stop()
        self.lpack.unlock()

    def twinkle(self):
        try:
            self.i = self.i+1
            newFrame = self.lastFrame
            leds = len(self.lastFrame)
            att = 0.95
            for k  in range (0, leds):
                if random.randrange(100) < 10 :
                    r,g,b = self.ledColors[k]
                else :
                    r = int(newFrame[k][0] * att)
                    g = int(newFrame[k][1] * att)
                    b = int(newFrame[k][2] * att)

                newFrame[k] = [r,g,b]
            self.lpack.setFrame(newFrame)
            self.lastFrame = newFrame
            self.i += 1
        except Exception, e:
            print(str(e))

colors = ColorPicker()
colors.run()