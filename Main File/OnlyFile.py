Cell = 1
Hall2 = 0
Patroll = 0
Hall1 = 0
Hall3 = 0
CBlock = 0
HallO = 0


items = ['knife', 'spoon', 'fork', 'shovel', 'drugs', 'hammer', 'bleach', 'screwdriver', 'keys', 'tazer', 'letter', 'loosetie', 'showerhead']
inventory = []
def invento(a):
    inventory.append(a)

r=1
while Cell == 1:
    print "You awaken from your bed on a cold and stormy night to find that your cell door has been mysteriously left open."
    print "You wonder if this is a trap or if this is your lucky day."
    print "It is up to you to take advantage of this situation and ESCAPE."
    if r == 1:
        moov = raw_input("what do you do?")
        r = 0
    if ("move" and "outside" and "cell") or ("move" and "in" and "cell") in moov:
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
    print "You lift a small tile off the floor revealing a small satchel of a slurry of all drugs"
    t = 1
  if (t == 1 and "take" and "satchel of drugs" or "satchel" or "drugs") in dohall:
    print "you take the small satchel of drugs"
    invento("drugs")

while Hall1 == 1:
    y = 1
    print "You enter the hall, to your left is a cell block, to your right are the showers"
    if y == 1:
        move = raw_input("What do you do?")
        y = 0
    if "move" and "left" in move:
        print "You move into the cell block"
        CBlock = 1
        Hall1 = 0
    if ("move" and "left") in move:
        print "you move into the showers, don't drop the soap..."
        print "You see a perfectly ordinary room of showers"
        Shower = 1
        Hall1 = 0
    if ("move" and "left") in move:
        print "you move back into the hall outside your cell"
        Hall2 = 1
        Hall1 = 0
    
while Hall3 == 1:
    print "you enter a long hall, to your left and right are two other halls, directly in front of you is the door to the yard"
    if me == 1:
        mo = raw_input("What do you do?")
        me = 0
    if ("move" and "left") in move:
        Hall3 = 0
        Hall4 = 1
    if ("move" and "right") in move:
        Hall3 = 0
        HallO = 1 

while HallO == 1:
    print 'You enter a hall, to your right is the canteent, to your left is the kitchen"
    if j ==1:
        muuv = raw_input("What do you do")
        j = 0
    if ("move" and "left") in muuv:
        print "you move into the kitchen"
        HallO = 0
        kitchen = 1
    if ("move" and "right") in muuv:
        print "You move into the canteen"
        
hodor = 1
while shower == 1:
    if hodor ==1
        knute = raw_input("What do you do?")
        hodor = 0
    if ("move" and "outside") in knute:
        print "you move outside, to your left is the shower, and to your right is the canteen"
        shower = 0
        HallO = 1
    
 
  
        
        
        
