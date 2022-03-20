# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 20:34:02 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

time.sleep(3)

postion = mc.player.getTilePos()

while True:
    x, y, z = mc.player.getTilePos()
    mc.postToChat("你現在位於X:"+str(x)+
                  "Y:"+str(y)+
                  "Z:"+str(z))
    time.sleep(0.5)
