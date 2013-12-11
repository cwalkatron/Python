name 	= "Tyler Fazakerley"
age 	= 36 # not a lie
height 	= 77 # inches
weight 	= 168 # lbs
eyes 	= "Brown"
teeth 	= 'White'
hair 	= 'Brown'

#imperial to metric converters
centi 	= 2.54 #multiply inches and "centi" to get centimeters
kilo 	= .453 #multiply points to "kilo" to get kilograms


print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "His height in centimeters is %d." % (height * centi)
print "His weight in kilograms is %d." % (weight * kilo)

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)