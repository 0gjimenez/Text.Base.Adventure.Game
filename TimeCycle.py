time = 0 
day = True 
temp = normal
light = bright

#loop for each turn

If time  > 6 or time < 18:
    day = True
    temp = normal
    light = bright

If time  < 6 or time > 18:
    day = False
    temp = cold
    light = dark
