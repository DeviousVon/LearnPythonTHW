#  A variable with four string assignments from an array.
formatter = "%r %r %r %r"

#  Print the variable formatter with it's four array defined strings as 1 2 3 4
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
#  This one is interesting, should print a bunch of %r's as strings 16 of em
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
