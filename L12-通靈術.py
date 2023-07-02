def on_call_monster():  #10
    loops.pause(1000)
    
    r = randint(0, 2)  #10

    if r == 0:  #20
        for i in range(-10,10,2):
            for j in range(-10,10,2):  #20
                mobs.execute(mobs.entities_by_type(ARROW_PROJECTILE_MOB),pos(i,0,j),"summon zombie ~ ~ ~")  #10

    elif r == 1:
        mobs.execute(mobs.entities_by_type(ARROW_PROJECTILE_MOB),pos(0,10,0),"/summon wither skeleton ~ ~ ~")  #10

    else:
        mobs.execute(mobs.entities_by_type(ARROW_PROJECTILE_MOB),pos(0,10,0),"/summon ender_dragon")  #10
    
    mobs.kill(mobs.entities_by_type(ARROW_PROJECTILE_MOB))  #5



player.on_arrow_shot(on_call_monster)  #15