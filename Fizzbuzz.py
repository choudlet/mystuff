print "Fizzbuzz Counting up to 100!"
n = 0
while n < 100:
	n = n + 1
	print n
	if n % 3 == 0:
		print "Fizz"
	if n % 5 == 0:
		print "buzz"
	if n % 3 == 0 and n % 5 == 0:
		print "Fizzbuzz"