Cell = 1
Hall2 = 0
Patroll = 0
Hall1 = 0
Hall3 = 0
CBlock = 0
HallO = 0
yard = 0


items = ['knife', 'spoon', 'fork', 'shovel', 'drugs', 'hammer', 'bleach', 'screwdriver', 'keys', 'tazer', 'letter', 'loosetie', 'showerhead']
inventory = []
def invento(a):
    inventory.append(a)


r=1
o=1
q=3
while Cell == 1:
    if o == 1:
        print "You awaken from your bed on a cold and stormy night to find that your cell door has been mysteriously left open."
        print "You wonder if this is a trap or if this is your lucky day."
        print "It is up to you to take advantage of this situation and ESCAPE."
        o = 0
    if r == 1:
        moov = raw_input("what do you do?")
        
    if ("inspect cell") in moov:
        print "In the corner of your cell you see a toilet next to your bed with a work desk."
        moov = ""
    if ("inspect" and "toilet") in moov:
        print "if you had a screwdriver,you might be able to remove the toilet."
    if ("inspect" and  "desk") in moov:
        print "on the desk you see a note."
        q=4
    if q==4 and ("read" and "note") in moov:
        print "Today is your lucky day. You have one chance to escape. Make it COUNT!"
        print "You have two options. You can either escape through the sewer system or brute force your way out."
        print "Best of luck, see you on the outside"
        print "Your friend,"
        print "The DEVS"
    if ("move" and "outside") in moov:
        print "You move outside your cell"
        Cell = 0
        Hall2 = 1







t = 0
p = 1
while Hall2 == 1:
  u = 1
  if p == 1:
    print "Standing in front of your cell, you see a cell block in front of you, a hall to your left and right, and your cell behind you."
    p = 0
  if u == 1:
    dohall = raw_input("what do you do?")
    u = 0
  if ("move" and "left") in dohall:
    print "You move to the left hall"
    Hall2 = 0
    Hall1 = 1
  if ("move" and "right") in dohall:
    print "You move the hall to your right"
    Hall2 = 0
    Hall3 = 1
  if ("move" and "forward") in dohall:
    print "You move into the cell block in front of you"
    Hall2 = 0
    CellB1 = 1
  if ("move" and "backwards" or "back") in dohall:
    print "You move back into your cell"
    Hall2 = 0
    Cell = 1
  if ("inspect" and "hall" or "room") in dohall:
    print "You see a small tile slightly raised compared to the rest of the floor."
  if ("inspect" and "tile" or "small tile") in dohall:
    t = 1
    print "You lift a small tile off the floor revealing a small satchel of a slurry of all drugs"
  if t == 1 and ("take satchel") in dohall:
    print "You take the small satchel of drugs"
    invento("drugs")
    t = 8

    

while Hall1 == 1:
    y = 1
    print "You enter the hall, to your left is a cell block, to your right are the showers"
    if y == 1:
        move = raw_input("What do you do?")
        y = 0
    if "move" and "left" in move:
        print "You move into the cell block"
        C_Block = 1
        Hall1 = 0
    if "move" and "left" in move:
        print "you move into the showers, don't drop the soap..."
        Shower = 1
        Hall1 = 0
    if "move" and "left" in move:
        print "you move back into the hall outside your cell"
        Hall2 = 1
        Hall1 = 0
        
while Hall3 == 1:
    print "you enter a long hall, to your left and right are two other halls, directly in front of you is the door to the yard"
    if me == 1:
        mo = raw_input("What do you do?")
        me = 0
    if "move" and "left" in mo:
        Hall3 = 0
        Hall4 = 1
    if "move" and "right" in mo:
        Hall3 = 0
        HallO = 1 
    
 
j = 1 
while HallO == 1:
    print "You enter a hall, to your right is the canteent, to your left is the kitchen"
    if j ==1:
        muuv = raw_input("What do you do")
        j = 0
    if ("move" and "left") in muuv:
        print "you move into the kitchen"
        HallO = 0
        kitchen = 1
    if ("move" and "right") in muuv:
        print "You move into the canteen"
        HallO = 0
        canteen = 1
        
ugh_killme = 1
while canteen == 1:
    if ugh_killme == 1:
        buehler = raw_input("What do you do?")
        ugh_killme = 0
    if ("move" and "outside") in buehler:
        print "You move out into the hall, to your right is the canteent, to your left is the kitchen"
        HallO = 1
        canteen = 0
        
        


wee = 1
while yard == 1:
    print "along the fence of the yard you sight an opening the fence, freedom"
    if wee == 1:
        ack = raw_input("What do you do?")
        wee = 0
    if ("move" and "back") in ack:
        print "You move back into the hall,to your front is the yard, to your left and right are halls, behind you is another hallway to your cell"
        yard = 0
        Hall3 = 1
    if ("move" and "opening"):
        print "you win your freedom, you have won the game!!"
        yard = 0

        
hodor = 1
while shower == 1:
    if hodor ==1:
        knute = raw_input("What do you do?")
        hodor = 0
    if ("move" and "outside") in knute:
        print "you move outside, to your left is the shower, and to your right is the canteen"
        shower = 0
        HallO = 1      
 
  
        
        
        
