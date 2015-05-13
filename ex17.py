from sys import argv
from os.path import exists
script, in_file, out_file = argv

print "Copying from %s to %s" % (in_file, out_file)

indata = open(in_file).read

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)

print "Ready, hit RETURN to continue. CTRL-C to abort."
raw_input()

with open(argv[1]) as in_file, open(argv[2], 'w') as out_file:
    out_file.write(in_file.read())

print "Alright, done!"

out_file.close()
to_file.close()