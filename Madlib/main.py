#Spacing
print ""
print ""


#Assigning input to variables with series of questions
nick_name = raw_input("Give us your nick name:  ")
weapon = raw_input("Name a deadly weapon of choice:  ")
faction = raw_input("Name your faction:  ")
homeland = raw_input("What is the name of your homeland:  ")
minute1 = int(raw_input("Enter a number 1-5:  "))
minute2 = int(raw_input("Enter a number 1-3:  "))
born = int(raw_input("What year were you born:  "))
odd_or_even = raw_input("Pick 'odd' or 'even':  ")
rock_or_rap = raw_input("Which do you like better? 'rock' or 'rap':  ")


#Creating array and assigned to the allies variable
allies = ["Bohemoths" , "Grunts" , "Redshirts" , "Scallywags"]


#Declaring dictionary
artists = dict()

#Diciontary assigning rap to PDiddy and rock to Rage Against The Machine
artists = {"rap":"PDiddy", "rock":"Rage Against The Machine"}


#Print Statements
print ""
print "*-*-*-*-*-*-*-*- YEAR 2943 - BATTLE OF THE ROBOTS *-*-*-*-*-*-*-*- "
print ""

#This string displays the nickname and faction
print nick_name + ", we are all counting on you as the leader of the " + faction
print " to save the world from the grips of the menacing robots."

#Displays weapon of choice
print "I pray that you have brought your trusty " + weapon + " with you."
print ""
print "The robots are spreading through the universe at a rapid pace and "

#Displays users homeland
print "will soon take over your beloved " + homeland + ". You only have "

#Take the two random number and multiply to give player amount of minutes
print "approximately " + str(minute1*minute2 ) + " minutes to save your people."
print ""

#This takes the value of the year you were born and the current year of the story
print "Seeming as you are " + str(2943-born) + " years old, you must use "
print "your wisdom against the new generation of deadly robot machines."


#If Statements

#If player picks odd, index 0 and 2 will be used from the allies array
if odd_or_even == str("odd"): 
	picked_allies = allies[0] + " and " + allies[2]
	print "Today you will fight with your allies " + picked_allies + "."
	print ""

#If player picks anything other than odd, index 1 and 3 will be used from the allies array
else:
	picked_allies = allies[1] + " and " + allies[3]
	print "Today you will fight with your allies " + picked_allies + "."
	print ""

#If player picks rap, the string will be printed
if rock_or_rap == str("rap"):
	print "As your soaring through the galaxy straight for the robot hive, "
	print artists["rap"] + " begins to play on the radio."

#Else if player picks rock, string will be printed
elif rock_or_rap == str("rock"):
	print "As your soaring through the galaxy straight for the robot hive, "
	print artists["rock"] + " begins to play on the radio."	

#If neither rock or rap are picked, the following string will be printed	
else:
	print "You concentrate in silence while approaching the colony."


print ""
print "WARNING YOU HAVE ARRIVED AT THE ENEMY STRONGHLOD"

#How many times the player will fire
fire_amount = int(raw_input("How many times do you wish to fire?  "))

#How much damage is caused by each fire
fire_damage= int(raw_input("How much damage do your rockets do? '1-20'  "))
raw_input("Press ENTER to begin firing!!!")
print ""

#A while loop to loop the amount of times the player chose to fire
i = 0
while i<fire_amount:
	print "-8-8-8-8-8-8-PEW-8-8-8-8-8-8-"
	i = i+1

#Defining a function for the calculation of total damage caused by rockets
def damageCaused():
	total_damage = fire_amount * fire_damage
	return total_damage

#Assigning the function to a variable
dmg = damageCaused();

print ""

#Printing a string to show how many robots were destroyed
print "You have destroyed " + str(dmg*1000) + " robots."
print ""
print "By destroying enough robots......."
print "YOU HAVE SAVED THE EARTH!!!!!!"
print ""















