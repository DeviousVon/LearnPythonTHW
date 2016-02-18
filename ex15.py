#  Imports the argv (argument variable) from the sys module
from sys import argv

#  Executes the script ex15.py with the argument supplied in commandline for second file
script, filename = argv

#  imports the contents of the file passed as an argument into the txt variable.
txt = open(filename)

#  prints a message about what filename you passed as an argument
print "Here's your file %r:" % filename
#  prints the content of the txt variable, which is the contents assigned from your file
print txt.read()

#  Just a print line
print "Type the filename again:"
#  Assigns variable file_again with the input from the user
file_again = raw_input("> ")

#  assigns the content of the filename typed in from raw_input to the variable txt_again
txt_again = open(file_again)

#  prints the variable txt_again
print txt_again.read()