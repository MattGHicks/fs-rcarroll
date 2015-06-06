print ""
print ""

#Input Variables

nick_name = raw_input("Give us your nick name:  ")
weapon = raw_input("Name a deadly weapon of choice:  ")
faction = raw_input("Name your faction:  ")
homeland = raw_input("What is the name of your homeland:  ")
minute1 = int(raw_input("Enter a number 1-5:  "))
minute2 = int(raw_input("Enter a number 1-3:  "))
born = int(raw_input("What year were you born:  "))
odd_or_even = raw_input("Pick 'odd' or 'even':  ")
rock_or_rap = raw_input("Which do you like better? 'rock' or 'rap':  ")

#Array

allies = ["Bohemoths" , "Grunts" , "Redshirts" , "Scallywags"]

#Dictionary

artists = dict()
artists = {"rap":"PDiddy", "rock":"Rage Against The Machine"}


#Function


#Print Statements

print ""
print "*-*-*-*-*-*-*-*- YEAR 2943 - BATTLE OF THE ROBOTS *-*-*-*-*-*-*-*- "
print ""
print nick_name + ", we are all counting on you as the leader of the " + faction
print " to save the world from the grips of the menacing robots."
print "I pray that you have brought your trusty " + weapon + " with you."
print ""
print "The robots are spreading through the universe at a rapid pace and "
print "will soon take over your beloved " + homeland + ". You only have "
print "approximately " + str(minute1*minute2 ) + " minutes."
print ""
print "Seeming as you are " + str(2943-born) + " years old, you must use "
print "your wisdom against the new generation of deadly robot machines."

#If Statements

if odd_or_even == str("odd"): 
	picked_allies = allies[0] + " and " + allies[2]
	print "Today you will fight with your allies " + picked_allies + "."
	print ""

else:
	picked_allies = allies[1] + " and " + allies[3]
	print "Today you will fight with your allies " + picked_allies + "."
	print ""

if rock_or_rap == str("rap"):
	print "As your soaring through the galaxy straight for the robot hive, "
	print artists["rap"] + " begins to play on the radio."

elif rock_or_rap == str("rock"):
	print "As your soaring through the galaxy straight for the robot hive, "
	print artists["rock"] + " begins to play on the radio."	
else:
	print "You concentrate in silence while approaching the colony."



#Loop

print ""
print "WARNING YOU HAVE ARRIVED AT THE ENEMY STRONGHLOD"
fire_amount = int(raw_input("How many times do you wish to fire?  "))
fire_damage= int(raw_input("How much damage do your rockets do? '1-20'  "))
raw_input("Press ENTER to begin firing!!!")

i = 0
while i<fire_amount:
	print "-8-8-8-8-8-8-PEW-8-8-8-8-8-8-"
	i = i+1

def damageCaused():
	total_damage = fire_amount * fire_damage
	return total_damage

dmg = damageCaused();

print str(dmg)













