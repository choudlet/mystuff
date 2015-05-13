from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file." 

target.write('%r\n%r\n%r' % (line1, line2, line3))


target.close()

print "Now do you want to see the results?"

finalprint = open(filename, 'r')

yes = set(['yes', 'y', 'ye'])
no = set(['no', 'n'])

choice = raw_input().lower()

if choice in yes:
	for line in finalprint:
		print line
elif choice in no:
	print "Ok Whatever!"

	
print "And finally, we close it."

finalprint.close()


