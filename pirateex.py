import random, os

questions = {
    "strong": "Do ye like yer drinks strong? ",
    "salty": "Do ye like it with a salty tang? ",
    "bitter": "Are ye a lubber who likes it bitter? ",
    "sweet": "Would ye like a bit of sweetness with yer poison? ",
    "fruity": "Are ye one for a fruity finish? "
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

adjectives = [
    "ugly",
    "fulsome",
    "contumacious",
    "attrocious",
    "tenacious",
    "arcadian"
]

nouns = [
    "potato",
    "nibblet",
    "locomotive",
    "kazoo",
    "gelatin",
    "hippopotamus",
    "hooligan",
    "leprechaun",
    "donkey"
]

customers = {}

inventory = {}

def asking():
    '''This function asks the user each question in the questions dictionary'''
    preferences = {}
    print ""
    print ""
    print "Answer yes by entering 'y' or 'yes', all other answers will count as No"
    print ""
    for x,y in questions.items():
        answer = raw_input(y).lower()
        if answer == 'y' or answer == 'yes':
            final = True
            preferences[x] = final
        else:
            final = False
            preferences[x] = final
    return preferences

def mixing(preferences):
    '''This function looks at all the answers from asking() and mixes the drink'''
    drink = []
    for a, b in preferences.items():
        if b == True:
            drink.append(random.choice(ingredients[a]))
    print "\nYour drink contains the following ingredients:"
    for x in drink:
        print x
    return drink

def name_drink():
    '''This function chooses random words from the noun and adjectives lists'''
    for x in adjectives:
        adj = random.choice(adjectives)
    for y in nouns:
        noun = random.choice(nouns)
    name_of_drink = str(adj) + " " + str(noun)
    print "\nThis drink will now be known as: the " + name_of_drink

def another_round(name_customer,preferences):
    '''This function allows the user to order additional drinks by prompting for y/n and rerunning other functions'''
    response = True
    while response:
        attention = raw_input("\nHey, " + name_customer + ", Press enter when you want another drink or tab out!")
        response = raw_input("\nSo do you want another drink? (y/n) ").lower()
        if response == 'y' or response == 'yes':
            drink = mixing(preferences)
            name_drink()
            pass
        else:
            print "\nYou entered No or an incorrect response!"
            print "You've likely had enough anyways! I'm tabbing you out!"
            print "Your cab is waiting outside! See you next time!"
            print "ARGGGGGGG!\n"
            response = False

def person():
    '''This function prompts the user for their first name to store later'''    
    customer = raw_input("\nWhat's yer first name by the way? " ).lower()
    return customer

def build_inventory(products):
    '''Builds the initial inventory from the ingredients dictionary. 10 servings of each product'''
    inventory2 = {}
    for x, y in products.items():
        for product in y:
            inventory2[product] = 10
    return inventory2






'''
def update_inventory(x,y):
    Subtracks the just used ingredients from the inventory
    for ingredient in x:
        inventory[ingredient] = 
'''






def main():
    '''This is the main function that calls all the functions to bartend!'''
    os.system('clear') # clears the screen
    inventory = build_inventory(ingredients) # builds the inventory from the ingredients dictionary and sets a quantity of 10 servings for each product
    print "\nARRG! Welcome to the Pirate Bar! I'm the bartender, matey! I'm going to ask you some questions so I can make you a drink.\n"
    name_customer = person() # runs the person function which prompts the user for their first name
    preferences = asking() #runs the asking function and sets their answers to a variable called preferences
    customers[name_customer] = preferences # adds the persons name and preferences to a dictionary
    name_drink() # runs the name_drink() function and randomly generates a name for the drink
    drink = mixing(preferences) # passes the preferences to the mixing function and assigns the results to variable called drink
    #update_inventory(drink,inventory)
    another_round(name_customer,preferences) # this function asks the user if they would like another drink and uses the preferences from before


if __name__ == '__main__':
    main()