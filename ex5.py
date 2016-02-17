name = 'Zed A. Shaw'
age = 35  # totally a lie
height = 74  # inches
weight = 180  # pounds lbs
eyes = 'Blue'
teeth = 'White'  # Doubtful
hair = 'Brown'  # and falling out...rapidly
inches_to_cm = 2.54
pounds_to_kilo = 2.2
height_in_cm = height * inches_to_cm
weight_in_kg = weight * pounds_to_kilo

print "Let's talk about %s" % name
print "He's %d inches, or %d centimeters tall." % (height, height_in_cm)
print "He's %d pounds, or %d kilograms heavy." % (weight, weight_in_kg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee" % teeth

#  this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
