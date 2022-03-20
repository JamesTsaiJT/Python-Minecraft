# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 15:37:43 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

time.sleep(1)

x, y, z = mc.player.getTilePos()
mc.setBlock(x, y, z, 46)
"""
#建高塔
mc.setBlock(x, y, z, 206)
mc.setBlock(x, y+1, z, 206)
mc.setBlock(x, y+2, z, 206)
mc.setBlock(x, y+3, z, 206)
mc.setBlock(x, y+4, z, 206)
mc.setBlock(x, y+5, z, 206)
mc.setBlock(x, y+6, z, 206)
mc.setBlock(x, y+7, z, 206)
mc.setBlock(x, y+8, z, 206)
mc.setBlock(x, y+9 , z, 206)
"""

"""
#放置九宮格方塊
mc.setBlock(x, y-1, z, 46)
mc.setBlock(x+1, y-1, z, 46)
mc.setBlock(x+2, y-1, z, 46)
mc.setBlock(x+2, y-1, z-1, 46)
mc.setBlock(x+2, y-1, z-2, 46)
mc.setBlock(x+1, y-1, z-2, 46)
mc.setBlock(x, y-1, z-2, 46)
mc.setBlock(x, y-1, z-1, 46)
"""

"""
#放置大範圍長方形方塊
mc.setBlocks(x+1, y-1, z+1, x-1, y-1, z-1, 11)
"""
