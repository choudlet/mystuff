filename = raw_input("What is the file you want to run?")

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

