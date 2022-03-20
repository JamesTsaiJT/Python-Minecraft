# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 14:24:30 2021

@author: USER
"""

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

print(mc.player.getTilePos())

x = -10
y = 400
z = 180

mc.player.setTilePos(x,y,z)