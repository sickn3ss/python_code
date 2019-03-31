# Convert a string to a C char array for position independent C code. 

import sys
if len(sys.argv) < 2: 
	print "[>] Usage: " + sys.argv[0] + " <string>"
	print "[>] Example: " + sys.argv[0] + " convertme"
	sys.exit()

orig_string = sys.argv[1]
end_string = ""

for char in orig_string: 
	end_string+= "'" + char + "'" + ", "

print "\nPAY ATTENTION TO WHITESPACES WHEN COPYING FROM CMD.EXE\n"
print "\nchar string[] = { " + end_string[:-1] + ", 0 }"