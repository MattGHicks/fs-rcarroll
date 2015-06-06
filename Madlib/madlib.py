#Input Variables
print ""
print ""
nick_name = raw_input("Give us your nick name:  ")
weapon = raw_input("Name a deadly weapon of choice:  ")
faction = raw_input("Name your faction:  ")
homeland = raw_input("What is the name of your homeland:  ")
minute1 = int(raw_input("Enter a number 1-5:  "))
minute2 = int(raw_input("Enter a number 1-3:  "))
born = raw_input("What year were you born")

#Declared Variables


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
print "approximately " + str(minute1+minute2 ) + " minutes."
print ""
print "Seeming as you are " + str(2943-born) + " years old, you must use "
print "your wisdom against the new generation of deadly robot machines."