class Command (object): 
    def init_ (self, astring, afunction): 
        self.helper = astring 
        self.funct = afunction 

""'"move is not defined because map has not been created ""'"

up = Command ("Moves the character up", move (up, 1)) 
down = Command ("Moves  the character down", move (down, 1)) 
left = Command (''Moves the character left", move (left, 1))
right = Command ("Moves the character right", move (right, 1)) 

commanddict = {up:true, down:true, left:true, right:true}

def help(x): 
    print (x.helper) 

help(up)

