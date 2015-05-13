import random

questions = {
	"strong" : "Do ye like yer drinks strong?",
	"salty" : "Do ye like it with a salty tang?",
	"bitter" : "Are you a lubber who likes it bitter?",
	"sweet" : "Would ye like a bit of sweetness with yer poison",
	"fruity" : "are ye one for a fruity finish?"
}

ingredients = {
	"strong" : ["glug of rum", "slug of whisky", "splash of gin"],
	"salty" : ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
	"bitter" : ["shake of bitters", "splash of tonic", "twist of lemon peel"],
	"sweet" : ["sugar cube", "spoonful of honey:", "splash of cola"],
	"fruity" : ["slice of orange", "dash of cassis", "cherry on top"]
}


adjectives = [
	"Magic",
	"Pristine",
	"Crisp",
	"Dangerous",
	"Powerful",
	"Little",
	]

nouns = [
	"Toddy",
	"Gimlet",
	"Freshie",
	"Eddy",
	"Hound-dog",
	]
	
def askq():
	preference = []
	for adj, question in questions.items():
		print question
		if raw_input() in ['yes', 'y', 'ye']:
			preference.append(adj)
		print ""
	return preference
	
def makedrink(preference):
	drink = []
	for adj in preference:
		drink.append(random.choice(ingredients[adj]))
	return drink
	
		
if __name__ == '__main__':
	consumption = 0
	drinking = True
	while drinking:
		preference = askq()
		drink = makedrink(preference)
		print "Your drink is made of"
		for ingred in drink:
			print ingred
		print "And is called the %s %s" % (
		random.choice(adjectives), random.choice(nouns))
		consumption +=1
		drinking = raw_input("Do you want another drink? ") in ['yes', 'y', 'ye']
			
	
	print "Congrats! You drank %s drinks!" % (consumption)	
	
			
		